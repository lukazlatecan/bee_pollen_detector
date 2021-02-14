#!/usr/bin/env python3

import sys
import os
import shutil
import argparse
import cv2
import logging
from setup_logger import logger


"""
    Global variables
"""
script_name = "Convert video to images"

"""
    Functions
"""


def parse_args() -> argparse.Namespace:
    """
        Parse arguments
        return: The parsed arguments
    """
    parser = argparse.ArgumentParser(description=script_name)
    parser.add_argument(
        "-i", "--input", help="input video file", required=True)
    parser.add_argument(
        "-o", "--output", help="output image folder", required=True)
    parser.add_argument("-v", "--verbose", help="increase verbosity level",
                        type=int, choices=range(0, 5), default=0)
    parser.add_argument(
        "-p", "--period", help="period to take image in miliseconds; default is 1000", type=int, default=1000)
    parser.add_argument("-r", "--resize", help="resize factor in percents; possible values are from 0 to 100; default is 100",
                        type=int, default=100, choices=range(0, 101, 10))
    return parser.parse_args()


def extract_images(input_video, output_folder, period, resize_factor):
    logger.info("Extracting images from " + input_video + " on every " +
                str(period) + " miliseconds. Saving to " + output_folder)
    count = 0
    video_capture = cv2.VideoCapture(input_video)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps
    logger.info("FPS of video: " + str(fps))
    logger.info("Total frames of video: " + str(frame_count))
    logger.info("Duration of video: " + str(duration))
    count = 0
    while video_capture.isOpened():
        success, image = video_capture.read()
        if (int(video_capture.get(cv2.CAP_PROP_POS_FRAMES)) > (frame_count-1)):
            video_capture.release()
            logger.info("Done extracting frames")
            logger.info("Saved " + str(count) + " images in total")
            break
        if(int(video_capture.get(cv2.CAP_PROP_POS_FRAMES) - 1) % round(period * fps / 1000) == 0 and success):
            new_image_path = os.path.join(output_folder, input_video.split(
                "/")[-1].split(".")[0] + "_" + str(int(video_capture.get(cv2.CAP_PROP_POS_FRAMES) - 1)) + ".jpg")
            logger.debug("Saving new image " + new_image_path + " from frame " +
                         str(int(video_capture.get(cv2.CAP_PROP_POS_FRAMES) - 1)))
            if(resize_factor < 100):
                logger.debug("Resizing on " + str(resize_factor) +
                             "\% of original size before saving")
                width = int(image.shape[1] * resize_factor / 100)
                height = int(image.shape[0] * resize_factor / 100)
                dim = (width, height)
                image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite(new_image_path, image)
            count = count + 1


"""
    Main entry point
"""
# Parse arguments
args = parse_args()

if args.verbose:
    logger.warning("Verbosity level set to: " + str(args.verbose))
    if(args.verbose == 0):
        level_name = 'CRITICAL'
    elif(args.verbose == 1):
        level_name = 'ERROR'
    elif(args.verbose == 2):
        level_name = 'WARNING'
    elif(args.verbose == 3):
        level_name = 'INFO'
    elif(args.verbose == 4):
        level_name = 'DEBUG'
    level = logging.getLevelName(level_name)
    logger.setLevel(level)

input_video = args.input
output_folder = args.output
period = args.period
resize_factor = args.resize

if(not os.path.exists(input_video)):
    logger.critical("Video file " + input_video + " does not exist!")
    sys.exit(1)

if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

os.makedirs(output_folder)

extract_images(input_video, output_folder, period, resize_factor)
