# Advanced Customer Segmentation using Machine Learning

Welcome to the "Advanced Customer Segmentation using Machine Learning" project repository! This project leverages a cutting-edge segmentation library developed by the Massachusetts Institute of Technology (MIT). While earlier customer segmentation projects might have relied on simpler K-Means clustering, the complexity of real-world customer data demands a more sophisticated approach. In this project, we utilize a special unsupervised learning algorithm to segment a group of 2,000 customers into distinct groups, employing the latest artificial intelligence algorithms.

## Prerequisites

Before using the provided code, make sure you have the following prerequisites installed on your system:

1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Libraries:** This project uses various Python libraries for data manipulation, visualization, and machine learning. Install the necessary libraries using pip:

   ```bash
   pip install pandas numpy matplotlib kmodes
   ```

3. **Dataset:** Download the dataset "segmentation-data.csv" and place it in the same directory as the code. The dataset contains complex customer data, including both numerical and categorical features.

## Code Overview

The Python code provided in this repository performs the following steps:

1. Imports necessary libraries, including pandas for data handling, numpy for numerical operations, and kmodes for customer segmentation.

2. Reads the "segmentation-data.csv" dataset containing customer data, including both numerical and categorical features.

3. Checks for missing values in the dataset.

4. Preprocesses the data by scaling the 'Age' and 'Income' columns using Min-Max scaling to make them suitable for clustering.

5. Performs customer segmentation using the KPrototypes algorithm, designed to handle both numerical and categorical data.

6. Assigns cluster labels to the customers.

7. Visualizes the customer clusters in a scatter plot, using 'Age' and 'Income' as the axes. Different clusters are represented by various colors.

## Usage

To use this code for advanced customer segmentation:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/customer-segmentation.git
   ```

2. Download the "segmentation-data.csv" dataset and place it in the same directory as the code.

3. Open the Jupyter Notebook or Python environment of your choice.

4. Run the provided code to perform customer segmentation based on complex data, visualize the results, and gain insights into your customer base.

5. Customize the code and experiment with different parameters to refine the segmentation process further.

This project demonstrates how modern machine learning algorithms can be used to segment customers effectively, providing valuable insights for businesses. Whether you are a data scientist, analyst, or business professional, this repository offers a powerful tool for understanding customer behavior.

If you have any questions or encounter issues, please don't hesitate to [create an issue](https://github.com/your-username/customer-segmentation/issues) in this repository.

Explore the world of advanced customer segmentation using the latest artificial intelligence algorithms!
