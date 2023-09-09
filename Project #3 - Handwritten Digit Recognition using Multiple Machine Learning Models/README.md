# Handwritten Digit Recognition using Multiple Machine Learning Models

Welcome to the "Handwritten Digit Recognition using Multiple Machine Learning Models" project! In this repository, we have developed a software solution that can recognize and interpret handwritten digits in photographs. This project demonstrates the power of combining multiple machine learning models to tackle complex problems. By implementing this solution, you'll gain insights into how artificial intelligence (AI) can be applied to solve real-world problems, such as recognizing handwritten text.

## Prerequisites

Before using the provided code, make sure you have the following prerequisites installed on your system:

1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Libraries:** This project uses various Python libraries for data manipulation, visualization, and machine learning. Install the necessary libraries using pip:

   ```bash
   pip install pandas matplotlib scikit-learn
   ```

3. **MNIST Dataset:** The code uses the MNIST784 dataset, which contains grayscale images of hand-drawn digits (0-9). The training set comprises 60,000 images, and the test set contains 10,000 images for evaluation. The dataset will be automatically downloaded using the code.

## Code Overview

The Python code provided in this repository performs the following steps:

1. Imports necessary libraries, including pandas for data handling, matplotlib for data visualization, scikit-learn for machine learning, and more.

2. Downloads the MNIST784 dataset, which consists of grayscale images of hand-drawn digits.

3. Displays an example image from the dataset to provide insight into the data.

4. Splits the dataset into training and testing sets, with a 1/7 and 6/7 ratio, respectively.

5. Standardizes the data using the StandardScaler to prepare it for Principal Component Analysis (PCA).

6. Applies PCA to reduce the dimensionality of the dataset while preserving 95% of the variance.

7. Trains a Logistic Regression model using the transformed data.

8. Demonstrates the model's ability to predict a digit from a test image.

9. Displays the test image alongside the predicted result.

10. Calculates the accuracy of the model on the test dataset.

## Usage

To use this code for handwritten digit recognition:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/enescaglarr/ML-DL-Projects.git
   ```

2. Open the Jupyter Notebook or Python environment of your choice.

3. Run the provided code to download the dataset, preprocess it, train the model, and make predictions on test images.

4. Experiment with different test images or customize the code to suit your requirements.

Feel free to explore different aspects of the code and dataset to gain a better understanding of machine learning for image recognition.

If you have any questions or encounter issues, please don't hesitate to issue in this repository.

Enjoy exploring handwritten digit recognition using multiple machine learning models!
