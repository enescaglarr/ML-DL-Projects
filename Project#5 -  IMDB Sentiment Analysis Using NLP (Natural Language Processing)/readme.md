# IMDB Sentiment Analysis Using NLP (Natural Language Processing)

Welcome to the "IMDB Sentiment Analysis Using NLP" project repository! In this project, we'll develop sentiment analysis software utilizing Natural Language Processing (NLP) techniques. The dataset used in this study is obtained from Kaggle, a platform owned by Google. Our artificial intelligence software will automatically extract positive or negative sentiments from English IMDB movie reviews in this dataset. This project provides a practical and hands-on way to learn NLP concepts without getting lost in theoretical details.

## Prerequisites

Before using the provided code, make sure you have the following prerequisites installed on your system:

1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Libraries:** This project uses various Python libraries for data manipulation, text processing, and machine learning. Install the necessary libraries using pip:

   ```bash
   pip install numpy pandas matplotlib scikit-learn beautifulsoup4 nltk
   ```

3. **Dataset:** Download the dataset "labeledTrainData.tsv" and place it in the same directory as the code. The dataset contains labeled IMDB movie reviews, which will be used for sentiment analysis.

## Code Overview

The Python code provided in this repository performs the following steps:

1. Imports necessary libraries, including pandas for data handling, beautifulsoup4 for HTML tag removal, re for text preprocessing, and scikit-learn for machine learning.

2. Reads the "labeledTrainData.tsv" dataset containing IMDB movie reviews and their corresponding sentiments.

3. Preprocesses the reviews by removing HTML tags, special characters, and numbers.

4. Converts all text to lowercase and removes common English stopwords.

5. Creates a function to preprocess multiple reviews simultaneously.

6. Splits the dataset into training and testing sets.

7. Uses the CountVectorizer to convert text data into numerical form suitable for machine learning.

8. Trains a Random Forest Classifier on the training data.

9. Predicts sentiments on the test data and calculates accuracy using ROC AUC score.

## Usage

To use this code for IMDB sentiment analysis:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/enescaglarr/imdb-sentiment-analysis.git
   ```

2. Download the "labeledTrainData.tsv" dataset and place it in the same directory as the code.

3. Open the Jupyter Notebook or Python environment of your choice.

4. Run the provided code to preprocess the data, train the sentiment analysis model, and evaluate its accuracy.

5. Customize the code, experiment with different parameters, or use your own dataset for sentiment analysis.

This project demonstrates the power of NLP and machine learning in automatically classifying sentiments in textual data. Whether you are a data scientist, aspiring NLP enthusiast, or simply interested in sentiment analysis, this repository offers a practical introduction to the field.


Explore the world of IMDB sentiment analysis using NLP and enhance your understanding of text classification!
