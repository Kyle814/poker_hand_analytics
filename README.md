# Poker Hand Prediction Project
This project is focused on predicting poker hands using machine learning models. We utilize convolutional neural networks (CNN) and random forests to predict poker hands based on a given set of cards. The dataset used for training and testing this model is obtained from the UCI Machine Learning Repository.

## Dataset Credits
The dataset used in this project is credited to the following source:

Title: Poker Hand
Authors: Robert Cattral and Franz Oppacher
Year: 2007
Source: UCI Machine Learning Repository
Dataset Link: Poker Hand Dataset
The dataset provides two CSV files:

poker-hand-training.data: Training data.
poker-hand-testing.data: Testing data.
poker-hand.names

## Usage
Downloading the Data
Before running the project, you need to download the dataset. To do this, simply run the provided Python script obtain_poker_data.py. The script will automatically fetch the dataset and save it as poker-hand-training.data and poker-hand-testing.data . After rename these files by adding .csv to them. This turns them into csv files.


Copy code into terminal and run
python obtain_poker_data.py
Setting Up the Environment
Make sure you have the required dependencies by installing them with pip using the provided requirements.txt file.

Copy code into terminal and run
pip install -r requirements.txt
Running the Models
The project includes two machine learning models: a Convolutional Neural Network (CNN) and a Random Forest.

To train and evaluate the CNN model, use the Jupyter Notebook provided in the project folder.
To train and evaluate the Random Forest model, use the Jupyter Notebook provided in the project folder.
Running the Jupyter Notebook


Note
Please note that this project is intended for educational and demonstration purposes. The accuracy of the models and their predictive power may vary. The dataset credits belong to the original authors mentioned above.

Obtained the poker+hand.zip from
Cattral,Robert and Oppacher,Franz. (2007). Poker Hand. UCI Machine Learning Repository. https://doi.org/10.24432/C5KW38.
Giving access to poker-hand-testing.csv, poker-hand-training.csv, 