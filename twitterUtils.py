import re
import config
excluded = config.excluded

def tweetCleaner(tweet):
	tweet = tweet.replace(';',' ').replace(',',' ')\
			.replace('"','').replace('\'','')\
			.replace(':','').replace('“','')\
			.replace('”','').replace('¿','')\
			.replace('?','').replace('...','')
	tweet = re.sub('[áàâäÁÀÂÄ]', 'a', tweet)
	tweet = re.sub('[éèêëÉÈÊË]', 'e', tweet)
	tweet = re.sub('[íìîïÍÌÎÏ]', 'i', tweet)
	tweet = re.sub('[óòôöÓÒÔÖ]', 'o', tweet)
	tweet = re.sub('[úùûüÚÙÛÜ]', 'u', tweet)
	return tweet

def tweetWords(tweet,length):
	tweet = tweetCleaner(tweet)
	wordsDirty = tweet.lower().split()
	words = []
	for word in wordsDirty:
		if (re.search("\W", word) is None and len(word) >= length and word not in excluded):
			words.append(word)
	return words