import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Api key", 
    "Secret key") #Api keys and secret key
auth.set_access_token("access token", 
    "Secret key") #access tokern and secret key

api = tweepy.API(auth)

def seeAuthentication():
	try:
	    api.verify_credentials()
	    print("Authentication OK")
	except:
	    print("Error during authentication")

seeAuthentication()
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

def seeTweets():
	timeline = api.home_timeline()
	for tweet in timeline[:2]:
	    print(f"{tweet.user.name} said {tweet.text}")
#seeTweets()
def postTweets():
	api.update_status("Test tweet from Tweepy Python")

#postTweets()
def searchUser():
	user = api.get_user("MikezGarcia")
	print("User details:")
	print(user.name)
	print(user.description)
	print(user.location)

	print("Last 20 Followers:")
	for follower in user.followers():
	    print(follower.name)
#searchUser()
def toFollow():
	api.create_friendship("realpython")
#toFollow()
def updateProfile():
	api.update_profile(description="I like Python")
	api.update_profile(name="CoderMan17")
#updateProfile()
def toLikeTweetsfromHomepage():
	tweets = api.home_timeline(count=1)
	tweet = tweets[0]
	print(f"Liking tweet {tweet.id} of {tweet.author.name}")
	api.create_favorite(tweet.id)
#toLikeTweetsfromHomepage()

def toShowBlocklist():
	for block in api.blocks():
		print(block.name)

def toSeeTweetswithKeyword():
	for tweet in api.search(q="Python", lang="en", rpp=10):
	    print(f"{tweet.user.name}:{tweet.text}")
#toSeeTweetswithKeyword()

def toSeeTrends():
	trends_result = api.trends_place(1) #Here 1 means worldwide Trend you can check trend list of all county by checking below function
	for trend in trends_result[0]["trends"]:
		print(trend["name"])


#toSeeTrends()
def tocheckYourCountry():
	county_list = api.trends_available()
	print(county_list)	
#tocheckYourCountry()



'''Suppose you want to fetch every tweet in which you are mentioned, and then mark each tweet as Liked and follow its author. You can do that like this:'''
def toFollowUserwhoMentionyou():
	tweets = api.mentions_timeline()
	for tweet in tweets:
		tweet.favorite()
		tweet.user.follow()
    	
#toFollowUserwhoMentionyou()

def toTakeTweetswithHashtag():
	for tweet in tweepy.Cursor(api.search, q='#CoderMan17', rpp=500).items():
		#if not tweet.user.following:
		#	tweet.user.follow()
		tweet.favorite()
		tweet.retweet()
		api.update_status(f"Thanks for the tweet @{tweet.user.screen_name}",tweet.id_str)
		print(tweet.id_str)
#toTakeTweetswithHashtag()

def deleteTweetsofTimeLIne():
	user = api.get_user("CoderMan17")
	tweets= api.user_timeline(id=user.id, include_rts=True)
	for tweet in tweets :
		api.destroy_status(tweet.id_str)
deleteTweetsofTimeLIne()	
