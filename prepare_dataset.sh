#!/bin/bash

BASE_DIR="images/top"
OUTPUT_DIR="data/top"
TEST_PERCENT=30

image_dirs=$(ls $BASE_DIR)
#Create train and test folders
rm -rf $OUTPUT_DIR
mkdir -p $OUTPUT_DIR/train
mkdir -p $OUTPUT_DIR/test
for image_dir in $image_dirs; do
    echo "============================================================================================"
    echo "============================== Checking $image_dir ... ====================================="
    echo "============================================================================================"
    labels=$(ls $BASE_DIR/$image_dir | grep json)
    for label in $labels; do
        filename=$(basename -- "$label")
        extension="${filename##*.}"
        filename="${filename%.*}"
        if [ -f "$BASE_DIR/$image_dir/$filename.json" ] && [ -f "$BASE_DIR/$image_dir/$filename.jpg" ]; then
            random=$((1 + RANDOM % 100))
            if (($random <= $TEST_PERCENT)); then
                echo "Copying $filename to test..."
                cp "$BASE_DIR/$image_dir/$filename.json" "$OUTPUT_DIR/test"
                cp "$BASE_DIR/$image_dir/$filename.jpg" "$OUTPUT_DIR/test"
            else
                echo "Copying $filename to train..."
                cp "$BASE_DIR/$image_dir/$filename.json" "$OUTPUT_DIR/train"
                cp "$BASE_DIR/$image_dir/$filename.jpg" "$OUTPUT_DIR/train"
            fi
        else
            echo "$filename pair doesn't exist"
        fi
    done
    echo "============================================================================================"
    echo "==============================              Done              =============================="
    echo "============================================================================================"
done
python3 labelme2coco.py "$OUTPUT_DIR/train" --output "$OUTPUT_DIR/train/trainval.json"
python3 labelme2coco.py "$OUTPUT_DIR/test" --output "$OUTPUT_DIR/test/trainval.json"
find "$OUTPUT_DIR" -type f -name '*.json' ! -name "trainval.json" -delete
rm data.tar.gz
tar -zcvf data.tar.gz data
