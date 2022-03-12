### jennybenjamina.github.io
GitHub Pages

# Pic 16A Tweeter (Project Name)
## Authors 
**JennyBenjamina**,
**Jamie1130**

## Short Description
* Our project scrapes tweets from Twitter and turns it into a dataframe, a graph, or a csv file.

## Instructions on how to install packages
1. Install necessary packages using `conda create --name NEWENV --file requirements.txt`

## demo file
**main.ipynb** uses most of the methods and class
1. Run cells in the main.ipynb file

### Dataframe from top_words used method
![image](https://user-images.githubusercontent.com/97067692/158002653-936845f7-e691-43b4-9c8f-8043b7c1a01f.png)

### Graph of top_words used
![image](https://user-images.githubusercontent.com/97067692/158002675-03faed20-2155-490e-bc9e-3894adce637b.png)

1. main.ipynb is the main file to run the class and functions.
2. top_words method takes the tweets from the user inputted and finds the top 20 most important words.
3. get_tweets methodd finds tweets related to the keyword(s) given.
4. get_my_tweets method grabs all the tweets from my homepage twitter.
5. to_graph method creates a graph with the dataframe given.

* api key and token is necessary to run these programs. 
* They are attainable here: https://developer.twitter.com/en
