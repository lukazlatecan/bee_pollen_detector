<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="logo.png" alt="Project logo"></a>
</p>

<h3 align="center">Bee Pollen Detector</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/lukazlatecan/bee_pollen_detector/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/lukazlatecan/bee_pollen_detector/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [Data](#data)
- [Getting Started](#getting_started)
- [Train](#train)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## ℹ️ About <a name = "about"></a>

This project is a part of my master thesis named "Detecting Pollen On Bees With Convolutional Neural Networks". It is mentored by prof. dr. Patricio Bulić.

## 🧐 Data <a name = "data"></a>

All of the intermediate data is available over Google Drive to download. If you have any additional questions regarding data, please contact the author.

### Videos

All of the videos are available on this link: [Videos](https://drive.google.com/drive/folders/1Er3fSRfcOANaKn3t1CKMZWZrcVKtosyC?usp=sharing)

### Images

Images were extracted from the videos using `convert_video_to_images.py` script. Anotations of bees with and without pollen was done with the help of [LabelMe](https://github.com/wkentaro/labelme). Anotations were divided in two classes: `bee` and `pollenbee`.
All of the images with anotation files are available on this link: [Images & Anotations](https://drive.google.com/drive/folders/1CsjobFd0q0M5ljBsELvHJ3u47sCDbzLO?usp=sharing)
NOTE: Image name is consisted of the video name and frame number in the video. (i.e. `GOPR1599_432.jpg`)

### Train & Test dataset

To divide all of the images with anotations into training and testing dataset, I used `prepare_dataset.sh`, which divides dataset into two parts. With the help of prepared the script `labelme2coco.py` I was able to export COCO-format dataset for instance segmentation. Dataset with all the needed files is avilable on this link: [Dataset](https://drive.google.com/drive/folders/1C25sg-YSQFxg4GQJejOFcCqhIYzTOHXH?usp=sharing)
There is also a .tar.gz file available to downlod [here](https://drive.google.com/file/d/1hoHTa1VWoIOD_zpdSP8H0eKSbTvXksqK/view?usp=sharing)

### Neural network

Result of this project is a neural network that detects bees with and without pollen on the image.
To see details on how to train the neural network, check [Google Collab](https://colab.research.google.com/drive/13W2IGGL1Mwt43lsGWSuFLmGI5XHLiRsD?usp=sharing)

## 🏁 Getting Started <a name = "getting_started"></a>

In order to train and test the data I used [Google Collab](https://colab.research.google.com/). You can find my notebook [here](https://colab.research.google.com/drive/13trSURrUEV7lz4fnWbV1wYFCru0fOWuZ) These notebook will get you through whole process, from installing requirements, preparing the dataset, training neural network and finally running bee pollen detection on some sample video.

## 🔧 Running the tests <a train = "train"></a>

You can see how to train the dataset [here](https://colab.research.google.com/drive/13trSURrUEV7lz4fnWbV1wYFCru0fOWuZ#scrollTo=wlqXIXXhW8dA)

## 🎈 Usage <a name="usage"></a>

You can see how to try out bee pollen detection [here](https://colab.research.google.com/drive/13trSURrUEV7lz4fnWbV1wYFCru0fOWuZ#scrollTo=oKBbjnLw5GGG&line=1&uniqifier=1)

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org) - Scripts & Core
- [Detectron2](https://github.com/facebookresearch/detectron2) - Neural network

## ✍️ Authors <a name = "authors"></a>

- [Luka Zlatečan](https://www.linkedin.com/in/luka-zlatecan/)
- [prof. dr. Patricio Bulić](https://fri.uni-lj.si/sl/o-fakulteti/osebje/patricio-bulic)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- [Janko Božič](https://www.bf.uni-lj.si/sl/o-fakulteti/zaposleni/278/bozic-janko) - special thanks go to Professor Božič, who made it possible to film the bees
