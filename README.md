# Capstone: Image Classification
--------

## Executive Summary

New York City is one of the most visited, expensive, and cultured cities in the world. I have created a weekend guide that allows users to visit NYC on a budget. We will explore a model that uses image recognition to classify 10 popular landmarks and measure accuracy between train and validation datasets. I collected 1,810 images from Yelp and Google and separated each landmark into their own folder. Some difficulties included finding a uniform amount of photos between landmarks and training the model on images with little to no noise (ie. people, nature, other buidlings). I found that by best model that utilized EfficientNETB0 was able to ignore the noise in the images when classifying. After this, I developed an app that provides users with the history and some additional recommendations to do in the area by landmark when they upload an image. 

## Data Collection

Folder Name | Targeted Landmark | Number of Photos
-------------------|------------------ |------------------ 
911Memorial | 9/11 Memorial | 175
BrooklynBridge| Brooklyn Bridge | 233
EmpireStateBuilding | Empire State Building | 236
Clock| Grand Central Terminal | 223
MetropolitanMuseum | Metropolitan Museum | 110
PepsiCola| The Gantry Plaza State Park | 239
RooseveltIsland | Roosevelt Island | 70
Gold| Rockefeller Center| 144
StatueofLiberty| Statue of Liberty | 193
Vessel| Hudson Yards | 186

## Data Exploration

To gain a deeper understanding of how feature detection and matching occur, I utilized ORB from the OpenCV lab in a function to explore feature detection. Oriented FAST and rotated BRIEF (ORB) is a feature detector that adds an orientation component and multiscale features to FAST and efficient computation, analysis of variance and correlation of oriented BRIEF features; it also decorrelates BRIEF features under rotational invariance. If you want to learn more about the basis of FAST and BRIEF and how ORB has transformed it be more efficient and accurate, click [here](https://medium.com/@deepanshut041/introduction-to-orb-oriented-fast-and-rotated-brief-4220e8ec40cf). I created a second function that takes two image paths, number of features, and number of matches. This finds the key features between two images and connects or matches common key features between with the Brute Force Matcher. If you want to learn more about Brute Force Matcher. It takes one descriptor from an image and matches to all the descriptors of a second image. It then takes a second descriptor of the original image and matches to all the descriptor of the second image until if reaches the amount of features denoted. To learn more about feature detection and matching, click [here](https://blog.francium.tech/feature-detection-and-matching-with-opencv-5fd2394a590).

## Data Modeling 

The fourth model had the least amount of layers, obtained a validation accuracy score of about 96%, and accurately classified my sample image of the Empire State building. This incorporated EfficientNETB0 and was able to outperform all other models. The benefit of EfficientNETB0 is that it uniformly scales each neural network dimension (width, depth and resolution). 

## Future Development 

In the future, I recommend utilizing more landmarks and cities and creating a more interactive and seamless app that incorporates the details of the landmarks within the map and the history and recommendations are embedded in the app. 
