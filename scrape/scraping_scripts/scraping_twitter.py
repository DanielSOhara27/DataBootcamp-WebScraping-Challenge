# Dependencies
from bs4 import BeautifulSoup
import requests

# URLs of page to be scraped
twitter_url = 'https://twitter.com/marswxreport?lang=en'

def doScrape():
    response_twitter = requests.get(twitter_url)

    #Mars weather tweet variable
    mars_weather = ''

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_tweet = BeautifulSoup(response_twitter.text, 'html.parser')

    # Looking for the div (a parent container) with class content
    results = soup_tweet.find_all('div', class_='content')

    # Inside the parent Div you look for the p tag
    result = results[0].find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    for x in result:
        mars_weather = x
        break

    #mars_weather = mars_weather[:(len(mars_weather) - len("n\nWelcome to the Mars Weather team "))]
    return mars_weather

