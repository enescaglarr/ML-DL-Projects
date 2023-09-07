# House Price Prediction using Machine Learning

This repository contains a Python project for predicting house prices using the Multiple Linear Regression algorithm from scikit-learn (sklearn). The project is a simple example of how machine learning can be used to make predictions based on input features. Below, you'll find information on how to use this project and what you need to get started.

## Prerequisites

Before running the code, you'll need the following:

1. Python: You should have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Required Libraries: This project uses pandas for data manipulation and scikit-learn for machine learning tasks. You can install these libraries using pip:

   ```bash
   pip install pandas scikit-learn
   ```

3. Dataset: You should download the dataset "housepricesdataset.csv" and place it in the same directory as the code. The dataset should be in CSV format, with columns for features (e.g., area, room count, building age) and the target variable (price).

## Code Overview

The Python code provided in this repository performs the following steps:

1. Import necessary libraries, including pandas for data handling and scikit-learn for machine learning.

2. Load the dataset "housepricesdataset.csv" into a pandas DataFrame for data analysis.

3. Create a Linear Regression model using scikit-learn.

4. Fit the model to the dataset, using the 'area,' 'roomcount,' and 'buildingage' columns as input features and the 'price' column as the target variable.

5. Make predictions using the trained model based on specific input values.

6. Display the coefficients and intercept of the linear regression model.

7. Provide a manual calculation example of predicting house prices using the formula `price = intercept + area + room count - building age`.

## Usage

To use this code for house price prediction:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   ```

2. Download the "housepricesdataset.csv" dataset and place it in the same directory as the code.

3. Open the Jupyter Notebook or Python environment of your choice.

4. Run the provided code to train the model and make predictions. You can modify the input values to predict house prices for different scenarios.

Remember that this is a simplified example, and in practice, you may want to use more extensive datasets and advanced techniques for accurate house price predictions.

If you have any questions or encounter issues, feel free to [create an issue](https://github.com/your-username/house-price-prediction/issues) in this repository.

Enjoy predicting house prices using machine learning!
