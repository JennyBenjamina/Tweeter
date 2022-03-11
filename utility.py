import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import os 


def to_df(tweets):
    '''
    this function turns text of tweets into a dataframe
    Args:
        a list of tweets
    Returns:
        df a dataframe
    '''
    df = pd.DataFrame({
    "tweets": range(1, len(tweets)+1), 
    "text": tweets
    })
    return df

def to_countdf(df):
    '''
    this function adds a count vectorizer to the dataframe and finds the important words
    Args:
        a dataframe
    Returns:
        a dataframe with count vectorizer
    '''
    vec = CountVectorizer(stop_words="english", min_df=0.1) 
    counts = vec.fit_transform(df['text'])
    count_df = pd.DataFrame(counts.toarray(), columns = vec.get_feature_names())
    
    if 'https' in count_df.columns.values.tolist():
        count_df.drop(columns='https', axis=1, inplace=True)
        print('dropped')

    return count_df

def to_csv(dat=[], col=[]):
    '''
    this turns objects to a csv file
    Args:
        dat: list of data
        col: column names
    Returns:
        a csv file
    '''
    current_dir = os.getcwd()
    if len(dat) != len(col):
        col.append('Id')
    try:
        df = pd.DataFrame(dat, columns=col)
    except: 
        print('Data and columns must be valid!')
    return df.to_csv(current_dir + r'\homeTweets.csv')#the r is 'raw'. file path