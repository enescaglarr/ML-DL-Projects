
# San Francisco Crime Geographical Clustering using Machine Learning

Welcome to the "San Francisco Crime Geographical Clustering using Machine Learning" project repository! In this project, we will explore geographic clustering using geolocation information (latitude and longitude) from a dataset provided by the San Francisco Police Department (SFPD). This dataset contains information about crimes committed in the city of San Francisco between 2003 and 2015. Our project will cover several key steps, including determining the optimal number of clusters, displaying geographic coordinates on a Python-based map, and exporting the map to an HTML file.

## Prerequisites

Before using the provided code, make sure you have the following prerequisites installed on your system:

1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Libraries:** This project uses various Python libraries for data manipulation, geographic mapping, and machine learning. Install the necessary libraries using pip:

   ```bash
   pip install pandas scikit-learn matplotlib plotly
   ```

3. **Dataset:** Download the dataset "train.csv" and place it in the same directory as the code. This dataset contains information about crimes, including their geographical coordinates.

## Code Overview

The Python code provided in this repository performs the following steps:

1. Imports necessary libraries, including scikit-learn for machine learning, pandas for data handling, and plotly for geographic mapping.

2. Reads the "train.csv" dataset, which contains information about crimes in San Francisco.

3. Preprocesses the data by removing unnecessary columns and cleaning the date information.

4. Scales the geographical coordinates (latitude and longitude) to prepare them for clustering.

5. Determines the optimal number of clusters using the Elbow method.

6. Applies K-Means clustering to group crimes into clusters based on their geographical coordinates.

7. Displays the clustering results on a geographic map using Plotly.

8. Exports the map to an HTML file for easy sharing and visualization.

## Usage

To use this code for San Francisco crime geographical clustering:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/enescaglarr/sf-crime-geographical-clustering.git
   ```

2. Download the "train.csv" dataset and place it in the same directory as the code.

3. Open the Jupyter Notebook or Python environment of your choice.

4. Run the provided code to preprocess the data, perform geographical clustering, and visualize the results on a map.

5. Customize the code, experiment with different clustering parameters, or use your own dataset for geographical clustering.

This project showcases the application of machine learning to geographical data, providing valuable insights into the distribution of crimes in San Francisco. Whether you are a data scientist, geospatial analyst, or just curious about geographic clustering, this repository offers a practical introduction to the field.

Explore San Francisco crime geographical clustering using machine learning and enhance your understanding of geospatial data analysis!
