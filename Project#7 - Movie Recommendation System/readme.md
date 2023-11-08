# Building a Movie Recommendation System

Welcome to the "Building a Movie Recommendation System" project repository! In this project, we'll create a software that recommends five different movies to a user based on their preferences and the likes of other users. You've probably seen a similar system on platforms like Netflix, where it suggests movies that may interest you. We'll be using the IMDB movie dataset to achieve this. Let's dive into the code and see how it works.

## Prerequisites

Before using the provided code, make sure you have the following prerequisites installed on your system:

1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Libraries:** This project uses various Python libraries for data manipulation and recommendation system development. Install the necessary libraries using pip:

   ```bash
   pip install pandas
   ```

3. **Dataset:** Download the dataset files "u.data" and "u.item" from the Kaggle link provided in the code. These files contain information about user reviews and movie details, respectively.

## Code Overview

The Python code provided in this repository builds a movie recommendation system. Here's a summary of the steps:

1. Import the necessary libraries, such as pandas, to handle data.

2. Read the "u.data" dataset, which contains information about user reviews.

3. Import the "u.item" file, which contains details about movies.

4. Merge the user reviews and movie details based on the movie's item ID.

5. Create a pivot table-like structure where each row represents a user (indexed by user ID) and movie titles in the columns, with rating values in the table.

6. Calculate the correlation of user ratings with the movie "Star Wars (1977)."

7. Create a DataFrame of movie correlations and remove records with NaN values.

8. Sort the movie correlations to recommend movies similar to "Star Wars (1977)."

9. Filter out movies with fewer than 100 votes to improve recommendation quality.

10. Join the "rating_count" column to the correlation DataFrame to account for the number of votes received by each movie.

11. Display the final movie recommendations for "Star Wars (1977)."

## Usage

To use this code to build a movie recommendation system:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/enescaglarr/movie-recommendation-system.git
   ```

2. Download the "u.data" and "u.item" dataset files and place them in the same directory as the code. You can obtain the dataset from the Kaggle link provided in the code comments.

3. Open the Jupyter Notebook or Python environment of your choice.

4. Run the provided code to build the movie recommendation system.

5. Customize the code, experiment with different movies, or use your own datasets for movie recommendations.

This project showcases the creation of a simple movie recommendation system using user ratings and movie correlations. Whether you are a data scientist, movie enthusiast, or just curious about recommendation systems, this repository offers a practical introduction to the field.


Enjoy building your own movie recommendation system and discovering new movies you may like!
