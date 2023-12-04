# Import necessary modules
from flask import Flask, jsonify, request
import json

# Create Flask app
app = Flask(__name__)

# Read tweet data from the JSON file
with open('100tweets.json', 'r') as file:
    tweet_data = json.load(file)

# 2. Hello World endpoint
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!"

# 3. Get all tweets endpoint
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    return jsonify(tweet_data)

# 4. Filter tweets by a query parameter
@app.route('/tweets/filter', methods=['GET'])
def filter_tweets():
    query_param = request.args.get('query')
    filtered_tweets = [tweet for tweet in tweet_data if query_param.lower() in tweet['text'].lower()]
    return jsonify(filtered_tweets)

# 5. Get a specific tweet by ID
@app.route('/tweet/<int:tweet_id>', methods=['GET'])
def get_tweet_by_id(tweet_id):
    try:
        tweet = next(tweet for tweet in tweet_data if tweet['id'] == tweet_id)
        return jsonify(tweet)
    except StopIteration:
        return jsonify({'error': 'Tweet not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# 6. Handle errors with Try/Except

# 7. Run the app
if __name__ == '__main__':
    app.run(debug=True)

# Sample curl requests:
# 1. curl http://localhost:5000/
# 2. curl http://localhost:5000/tweets
# 3. curl http://localhost:5000/tweets/filter?query=some_keyword
# 4. curl http://localhost:5000/tweet/1
