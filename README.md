# Pothole Detector using IBM Watson's Visual Recognition API

The pothole detector is built in Python with Flask as its web framework. It uses IBM Watson’s visual recognition API for detecting the potholes on the road. It basically takes any place on the Google Maps and takes its Street View images for analysis. It then passes that image to the API where we built a visual recognition model using potholes and no-potholes road images. That classifier model is just fed with those two types of images and it then analyses the given image based on that and predicts a score on how close it falls towards a certain category.

**Live Application:** http://pothole-detector-ibm.herokuapp.com/ <br>
**Dataset used:**
https://drive.google.com/open?id=0B7Zefvy_mkNwMUtfcnFhX3BOeUk

### Test Locations:
**Latitude** : 41.750791337697564
<br> **Longitude** : -87.59532922991751
 <br> **Pitch** : -45
  <br> **Heading** : 0 <br>
  
**Latitude** : 41.9209159784344
<br> **Longitude** : -87.72681716571067
 <br> **Pitch** : -60
  <br> **Heading** : 0 <br>
  
**Latitude** : 41.89729779454106
<br> **Longitude** : -87.72506334574346
 <br> **Pitch** : -50
  <br> **Heading** : 270 <br>
  
**Latitude** : 41.864516820382946
<br> **Longitude** : -87.70325089784822
 <br> **Pitch** : -45
  <br> **Heading** : 90 <br>
  
**Latitude** : 41.9033282
<br> **Longitude** : -87.66741033
 <br> **Pitch** : -20
  <br> **Heading** : 60 <br>
  
**Latitude** : 41.9033282
<br> **Longitude** : -87.66741033
 <br> **Pitch** : -40
  <br> **Heading** : 0 <br>
  
**Latitude** : 41.9032983
<br> **Longitude** : -87.66770433
 <br> **Pitch** : -40
  <br> **Heading** : 0 <br>
  
**Latitude** : 41.9047656
<br> **Longitude** : -87.64302023
 <br> **Pitch** : -30
  <br> **Heading** : 90 <br>
  
**Latitude** : 41.9044623
<br> **Longitude** : -87.64195363
 <br> **Pitch** : -30
  <br> **Heading** : 150 <br>
  
**Latitude** : 41.9689247
<br> **Longitude** : -87.7490793
 <br> **Pitch** : -45
  <br> **Heading** : 90 <br>
  
**Latitude** : 41.9689217
<br> **Longitude** : -87.74920323
 <br> **Pitch** : -45
  <br> **Heading** : 0 <br>
  
