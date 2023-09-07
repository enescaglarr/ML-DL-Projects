# Salary Calculation using Machine Learning

Welcome to the "Salary Calculation using Machine Learning" project! In this repository, we have developed a machine learning model that calculates employee salaries based on their experience levels. Many companies have non-linear salary structures, making it challenging to determine salaries accurately. To address this issue, we have employed the Polynomial Linear Regression algorithm to create a model capable of handling such complexities.

## Prerequisites

Before using the provided code, make sure you have the following prerequisites installed on your system:

1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Libraries:** This project uses the following Python libraries:
   - pandas
   - matplotlib
   - scikit-learn (for Polynomial Linear Regression)

   You can install these libraries using pip:

   ```bash
   pip install pandas matplotlib scikit-learn
   ```

3. **Dataset:** Download the dataset "salaries_dataset.csv" and place it in the same directory as the code. The dataset should contain columns for employee experience levels and their corresponding salaries.

## Code Overview

The Python code provided in this repository performs the following steps:

1. Import the necessary libraries, including pandas for data manipulation, matplotlib for data visualization, and scikit-learn for machine learning tasks.

2. Load the dataset "salaries_dataset.csv" into a pandas DataFrame for data analysis.

3. Visualize the data by creating a scatter plot of experience levels against salaries.

4. Perform Polynomial Linear Regression. We use the PolynomialFeatures class from scikit-learn to transform the input feature 'experience_level' into polynomial features, allowing us to capture non-linear relationships.

5. Fit the Polynomial Linear Regression model to the transformed data.

6. Make predictions using the trained model.

7. Visualize the results by plotting the polynomial regression curve alongside the original data points.

8. You can experiment with different degrees of polynomials by adjusting the `degree` parameter in the `PolynomialFeatures` class to potentially improve model performance.

9. Finally, you can use the model to predict salaries for employees with specific experience levels.

## Usage

To use this code for salary calculation:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/salary-calculation.git
   ```

2. Download the "salaries_dataset.csv" dataset and place it in the same directory as the code.

3. Open the Jupyter Notebook or Python environment of your choice.

4. Run the provided code to train the Polynomial Linear Regression model, visualize the results, and make salary predictions.

Feel free to experiment with different degrees of polynomials to improve the accuracy of salary predictions.

Enjoy calculating salaries accurately using machine learning!
