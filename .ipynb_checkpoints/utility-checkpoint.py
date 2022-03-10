import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer 

def text_extractor(tweets):
    '''
    this function filters out the text (tweets) 
    returns:
        a list of texts of tweets
    '''
    return [t.text for t in tweets]

def to_single_line(tweets):
    '''
    this function turns tweets into a single line by removing new line characters and joining them.
    Args:
        tweets
    returns:
        joined strings in a list
    '''
    splits = [str(tweet) for tweet in tweets]
    splits = [tweet.split('\n') for tweet in splits]
    joined = [''.join(split) for split in splits]
    
    return joined


def to_df(tweets):
    df = pd.DataFrame({
    "tweets": range(1, len(tweets)+1), 
    "text": tweets
    })
    return df

def count(df):
    vec = CountVectorizer(stop_words="english") 
    counts = vec.fit_transform(df['text'])
    counts = counts.toarray()
    return counts