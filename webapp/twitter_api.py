from flask import Flask, request, jsonify
import twint
import json

app = Flask(__name__)

@app.route('/q')
def func_query():
    search_text = request.args.get('search_text')
    tweets_list = []
    c = twint.Config()
    c.Search = search_text
    c.Hide_output = True
    c.Store_object = True
    c.Store_object_tweets_list = tweets_list
    twint.run.Search(c)

    tweets_dict = dict()
    for tweet in tweets_list:
        tweet_dict = {'username':tweet.username, 'tweet':tweet.tweet, 'replies_count':tweet.replies_count, 'link':tweet.link, 'mentions':tweet.mentions}
        tweets_dict.update({tweet.id : tweet_dict})
    
    return jsonify(tweets_dict)

if __name__ == '__main__':
    app.run()
