import tweepy

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
    

# tweetie = api.search_tweets('golf', lang='en', result_type="popular")

# print(tweetie[0].text)

# for status in tweepy.Cursor(api.user_timeline).items(100):
    # print('print ', status)
    
# t = tweepy.Cursor(api.user_timeline).items(100)
# t = list(t)
# print(t[0].__dict__.keys())

#################################################################################

# t = tweepy.Cursor(api.search_tweets, q='puppy', lang='en', result_type='popular').items(100)

# t = [x.text for x in t]
# for x in t:
#     print(x)

#################################################
# t = tweepy.Cursor(api.user_timeline,  
#               screen_name="elonmusk",
#               count=500).items()
# t = [x.text for x in t]
# for x in t:
#     print(x)
    
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

    
'''
The get_place_trends() method of the API class in Tweepy module is used to fetch 
the top 50 trending topics for a specific location. 
'''

# WOEID of New York
# woeid = 2459115
#api.trends_available()
# woeid=1
# trends_result = api.get_place_trends(id=woeid, exclude="hashtags")
# for trend in trends_result[0]["trends"]:
#     print(trend["name"])