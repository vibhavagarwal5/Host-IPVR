# Pothole Detector using IBM Watson's Visual Recognition API

The pothole detector is built in Python with Flask as its web framework. It uses IBM Watson’s visual recognition API for detecting the potholes on the road. It basically takes any place on the Google Maps and takes its Street View images for analysis. It then passes that image to the API where we built a visual recognition model using potholes and no-potholes road images. That classifier model is just fed with those two types of images and it then analyses the given image based on that and predicts a score on how close it falls towards a certain category.

**Live Application:** http://pothole-detector-ibm.herokuapp.com/ <br>
**Dataset used:**
https://drive.google.com/open?id=0B7Zefvy_mkNwMUtfcnFhX3BOeUk

### Test Locations:
• **Latitude** : 41.750791337697564, **Longitude** : -87.59532922991751, **Pitch** : -45, **Heading** : 0 <br>
• **Latitude** : 41.9209159784344, **Longitude** : -87.72681716571067, **Pitch** : -60, **Heading** : 0 <br>
• **Latitude** : 41.89729779454106, **Longitude** : -87.72506334574346, **Pitch** : -50, **Heading** : 270 <br>
• **Latitude** : 41.864516820382946, **Longitude** : -87.70325089784822, **Pitch** : -45, **Heading** : 90 <br>
• **Latitude** : 41.9033282, **Longitude** : -87.66741033, **Pitch** : -20, **Heading** : 60 <br>
• **Latitude** : 41.9033282, **Longitude** : -87.66741033, **Pitch** : -40, **Heading** : 0 <br>
• **Latitude** : 41.9032983, **Longitude** : -87.66770433, **Pitch** : -40, **Heading** : 0 <br>
• **Latitude** : 41.9047656, **Longitude** : -87.64302023, **Pitch** : -30, **Heading** : 90 <br>
• **Latitude** : 41.9044623, **Longitude** : -87.64195363, **Pitch** : -30, **Heading** : 150 <br>
• **Latitude** : 41.9689247, **Longitude** : -87.7490793, **Pitch** : -45, **Heading** : 90 <br>
• **Latitude** : 41.9689217, **Longitude** : -87.74920323, **Pitch** : -45, **Heading** : 0 <br>
