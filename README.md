---
license: cc0-1.0
task_categories:
  - image-segmentation
language:
- en
tags:
  - clouds
  - sentinel-2
  - image-segmentation
  - deep-learning
  - remote-sensing
pretty_name: CloudSEN12Plus
---
# CloudSEN12Plus

***``A global dataset for semantic understanding of cloud and cloud shadow in Sentinel-2``***

<img src='cloudsen12.gif' alt='drawing' width='20%'/>
CloudSEN12+ is a significant extension of the CloudSEN12 dataset, which doubles the number of expert-reviewed labels, making it, by a large margin, the largest cloud detection dataset to date for Sentinel-2. All labels from the previous version have been curated and refined, enhancing the dataset's trustworthiness. This new release is licensed under CC0, which puts it in the public domain and allows anyone to use, modify, and distribute it without permission or attribution.

##Data Folder order:

 The CloudSEN12+ dataset is organized into `train`, `val`, and `test` splits. The images have been padded from 509x509 to 512x512 and 2000x2000 to 2048x2048 to ensure that the patches are divisible by 32. The padding is filled with zeros in the left and bottom sides of the image. For those who prefer traditional storage formats, GeoTIFF files are available in our [ScienceDataBank](https://www.scidb.cn/en/detail?dataSetId=2036f4657b094edfbb099053d6024b08&version=V1) repository.

<center>
<img src='https://cdn-uploads.huggingface.co/production/uploads/6402474cfa1acad600659e92/9UA4U3WObVeq7BAcf37-C.png' alt='drawing' width='50%'/>
</center>
*CloudSEN12+ spatial coverage. The terms p509 and p2000 denote the patch size 509 × 509 and 2000 × 2000, respectively. `high`, `scribble`, and `nolabel` refer to the types of expert-labeled annotations*


**ML-STAC Snippet**
```python
import mlstac
dataset = mlstac.load('...')
```

**Sensor: Sentinel2 - MSI**

**ML-STAC Task: image-segmentation**

**Data raw repository:  [https://cloudsen12.github.io/](https://cloudsen12.github.io/)**

**Dataset discussion:  [https://huggingface.co/datasets/isp-uv-es/CloudSEN12Plus/discussions](https://huggingface.co/datasets/isp-uv-es/CloudSEN12Plus/discussions)**

**Split_strategy:  stratified**

**Paper:  [https://www.sciencedirect.com/science/article/pii/S2352340924008163](https://www.sciencedirect.com/science/article/pii/S2352340924008163)**
## Data Providers

|Name|Role|URL|
| :---: | :---: | :---: |
|Image & Signal Processing|['host']|https://isp.uv.es/|
|ESA|['producer']|https://www.esa.int/|

## Curators

|Name|Organization|URL|
| :---: | :---: | :---: |
|Cesar Aybar|Image & Signal Processing|http://csaybar.github.io/|

## Labels

|Name|Value|
| :---: | :---: |
|clear|0|
|thick-cloud|1|
|thin-cloud|2|
|cloud-shadow|3|

## Dimensions

### dimensions

|Axis|Name|Description|
| :---: | :---: | :---: |
|0|C|Spectral bands|
|1|H|Height|
|2|W|Width|

## Spectral Bands

|Name|Common Name|Description|Center Wavelength|Full Width Half Max|Index|
| :---: | :---: | :---: | :---: | :---: | :---: |
|B01|coastal aerosol|Band 1 - Coastal aerosol - 60m|443.5|17.0|0|
|B02|blue|Band 2 - Blue - 10m|496.5|53.0|1|
|B03|green|Band 3 - Green - 10m|560.0|34.0|2|
|B04|red|Band 4 - Red - 10m|664.5|29.0|3|
|B05|red edge 1|Band 5 - Vegetation red edge 1 - 20m|704.5|13.0|4|
|B06|red edge 2|Band 6 - Vegetation red edge 2 - 20m|740.5|13.0|5|
|B07|red edge 3|Band 7 - Vegetation red edge 3 - 20m|783.0|18.0|6|
|B08|NIR|Band 8 - Near infrared - 10m|840.0|114.0|7|
|B8A|red edge 4|Band 8A - Vegetation red edge 4 - 20m|864.5|19.0|8|
|B09|water vapor|Band 9 - Water vapor - 60m|945.0|18.0|9|
|B10|cirrus|Band 10 - Cirrus - 60m|1375.5|31.0|10|
|B11|SWIR 1|Band 11 - Shortwave infrared 1 - 20m|1613.5|89.0|11|
|B12|SWIR 2|Band 12 - Shortwave infrared 2 - 20m|2199.5|173.0|12|
