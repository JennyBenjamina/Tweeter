import tweepy

class TweetScraper():
    '''
    A simple class that scrapes through Twitter
    '''
    
    ######################################################################
    #attempt authentication
    api_key = '5akGm05U5UZ8mI3xsuTmdVJ6u'
    api_key_secret = 'AZybqHegDHRUJSOPBmcFkSvjud2t5yEtXGNpNwgwCpONRL4CkQ'
    access_token = '81393427-P7MwmV4O8tKFfjnaXQvByx89XB5ptRD3aNvhWMlmz'
    access_token_secret = 'IGSsYoPlY9DkBrMKEvM3yHHt7rmbfslNE6Z4SsoXZS7Sa'
    
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
        tweets = self.api.search_tweets(args, count=100, lang='en', result_type="popular") #result_type can also be mixed or recent
        
        return tweets
    
    def find_users_tweets(self, sname='elonmusk'):
        user_tweets = self.api.user_timeline(screen_name=sname)
        print(user_tweets[0].user.__dict__.keys())
        # print(user_tweets[0].user.name)
        # print(user_tweets[0].created_at)
        
        for i, tweet in enumerate(user_tweets):
            # print(tweet.text)
            print(i, tweet.created_at)
        return 'hello'
    
    def get_my_tweets(self):
        home_tweets = self.api.home_timeline()

        columns = ['Time', 'User', 'Tweet']
        dat = [] #stores data
        id = 1

        for tweet in home_tweets:
            dat.append([tweet.created_at, tweet.user.screen_name, tweet.text, id ])
            id+=1

        
        print(home_tweets[0].__dict__.keys()) #this is a trick to see what's going on. Lists can be converted to dictionary 
        
        return dat, columns
    
    def find_users(self, user='noble'):
        users = self.api.search_users(user)
        print(users[0].__dict__.keys())
        # for user in users:
        #     print(user.name, '|', user.screen_name)
        #     print(user.created_at)
        #     print('User verified:', user.verified)
        #     print('----------------')
        return users[0]
            
        
    def search_tweets(self, arg='puppy'):
        t = tweepy.Cursor(self.api.search_tweets, q=arg, lang='en', result_type='popular').items(500)
        t = [x.text for x in t]
        return t
            

