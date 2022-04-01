from snscrape.modules import twitter
import csv
import os
import datetime
from dataclasses import dataclass
from tqdm import tqdm

@dataclass(frozen=True, order=True)
class Tweet:
    id: int
    content: str
    username: str
    display_name: str
    user_bio: str
    user_statuses_count: str
    date: str
    url: str

def get_users(query, max_users=10):
    '''
    USAGE:
    users = get_users('AI Alignment', max_tweets=100)

    Returns: List of usernames (each username is str)
    '''
    users = set()
    for tweet in twitter.TwitterSearchScraper(query).get_items():
        if len(users) < max_users:
            users.add(tweet.user.username)
        else:
            break
    return list(users)

def get_tweets(user, max_tweets_per_user=10):
    '''
    USAGE:
    tweets = get_tweets('username', max_tweets=100)
    for tweet in tweets:
        print(tweet.id, tweet.display_name, tweet.user_bio, tweet.user_statuses_count, tweet.date, tweet.url)
    '''
    user_tweets = []
    for i, tweet in enumerate(twitter.TwitterUserScraper(user).get_items()):
        if i < max_tweets_per_user:
            tweet = Tweet(id=tweet.id,
                        content=tweet.content,
                        username=tweet.user.username,
                        display_name=tweet.user.displayname,
                        user_bio=tweet.user.description,
                        user_statuses_count=tweet.user.statusesCount,
                        date=tweet.date,
                        url=tweet.url)
            user_tweets.append(tweet)
        else:
            break
    return user_tweets

def get_tweets_by_users(users, max_tweets_per_user=10):
    tweets = []
    for user in tqdm(users):
        user_tweets = get_tweets(user, max_tweets_per_user=max_tweets_per_user)
        tweets.extend(user_tweets)
    return tweets

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H-%M-%S")

def writetocsv(filename, values, header=None):
    if not os.path.exists(filename):
        header_added = False
    else:
        header_added = True

    if header == None:
        header = (len(values) * [''])
    if values == None:
        raise ValueError("You might have forgotten to specify what to write in rows or the values are None.")
    with open(filename, mode='a') as csv_writer:
        csv_writer = csv.writer(csv_writer, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if not header_added:
            csv_writer.writerow(header)
        csv_writer.writerow(values)

#Sample Usage:
'''
query = 'AI Alignment'

max_users = 100
max_tweets_per_user = 100
users = get_users(query, max_users=max_users)
tweets = get_tweets_by_users(users, max_tweets_per_user=max_tweets_per_user)
current_time = get_current_time()
for tweet in tweets:
    writetocsv(f'Tweet data - query={query} max_users={max_users} max_tweets_per_user={max_tweets_per_user} date={current_time}.csv',
    [tweet.id, tweet.username, tweet.content, tweet.user_bio, tweet.display_name, tweet.user_statuses_count, tweet.date, tweet.url],
    header=['id', 'username', 'tweet', 'user bio', 'display name', 'user statuses count', 'date', 'url'])
'''
