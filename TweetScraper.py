import tweepy
import re
import nltk
import pandas as pd
nltk.download('stopwords')
from nltk.corpus import stopwords
from matplotlib import pyplot as plt

class TweetScraper():
    '''
    A simple class that scrapes through Twitter
    '''
    
    ######################################################################
    #attempt authentication
    api_key = ''
    api_key_secret = ''
    access_token = ''
    access_token_secret = ''
    
    try:
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
    except:
        print('Error in authentication')
        
    ######################################################################
    
    def __init__ (self):
        self.api = TweetScraper.api

    def get_tweets(self, *args):
        '''
        this function grabs tweets from the inputted keywords
        Args:
            *args keywords to search through Twitter
        Returns:
            Tweets object that can ...
        '''
        try:
            tweets = self.api.search_tweets(args, count=100, lang='en', result_type="popular") #result_type can also be mixed or recent
            text = [tweet.text for tweet in tweets]
        except:
            print('Must be a valid entry')
            return

        return text
    
    
    def get_my_tweets(self):
        '''
        this function searches through my home twitter feed
        Returns:
            a tuple of dat and columns of time, user, and tweets
        '''
        home_tweets = self.api.home_timeline()

        columns = ['Time', 'User', 'Tweet']
        dat = [] #stores data
        id = 1

        for tweet in home_tweets:
            dat.append([tweet.created_at, tweet.user.screen_name, tweet.text, id ])
            id+=1
        
        return dat, columns
    

            
    def top_words(self, user, count = 100):
        '''
        find the top words used by this user
        Args:
            user: username aka screenname
            count: the max number of tweets
        Returns: 
            df dataframe
        '''
        stop = stopwords.words('english')
        stop_words = stop + [x.capitalize() for x in stop]

        tweets = []

        try:
            search = self.api.user_timeline(screen_name = user, count = 100, include_rts = True)
        except:
            print('User does not exist')
            return None
        
        
        for i in range(100):
            tweets.append(search[i].text)
        lines = list()
        for line in tweets:    
            words = line.split()
            for w in words: 
                lines.append(w)

        lines = [re.sub(r'[^A-Za-z0-9]+|http\S+|RT', '', x) for x in lines] #using regex 
        finalLines = []
        for word in lines:
            if word not in stop_words and word != '':
                finalLines.append(word)

        df = pd.DataFrame({'Words': finalLines }) #creates dataframe
        df = df['Words'].value_counts()
        df = df[:20]

        return df

    def to_graph(self, df):
        '''
        this function turns a dataframe to a graph
        Args:
            df: dataframe to turn to a graph
        '''
        try:
            fig, ax = plt.subplots(1,1, figsize=(10,5))
            ax = df.plot.barh(df.values, df.index, alpha=0.8)
            ax.set(title = 'Top Words Overall', ylabel = 'Word from Tweet', xlabel = 'Count of Words')
            plt.show()
        except:
            print('Must have columns values and index in dataframe')
            return
        return ax 


