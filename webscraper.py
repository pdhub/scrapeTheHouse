from bs4 import BeautifulSoup
import requests
import json
url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=100)
content = BeautifulSoup(response.content, "html.parser")
tweetArr = []
for tweet in content.findAll('div', attrs={"class":"tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class":"author"}).text.encode('utf-8')
    }
    tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)
