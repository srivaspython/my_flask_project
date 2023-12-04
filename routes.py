# routes.py
from flask import jsonify, request

def configure_routes(app):
    tweet_data = [
        {"id": 1, "text": "Tweet 1"},
        {"id": 2, "text": "Tweet 2"},
        # ... other tweets
    ]

    @app.route('/', methods=['GET'])
    def hello_world():
        return "Hello World!"

    @app.route('/tweets', methods=['GET'])
    def get_all_tweets():
        return jsonify(tweet_data)

    @app.route('/tweets/filter', methods=['GET'])
    def filter_tweets():
        query_param = request.args.get('query')
        if query_param:
            filtered_tweets = [tweet for tweet in tweet_data if query_param.lower() in tweet['text'].lower()]
            return jsonify(filtered_tweets)
        else:
            return jsonify({"error": "Missing query parameter"}), 400

    @app.route('/tweet/<int:tweet_id>', methods=['GET'])
    def get_tweet_by_id(tweet_id):
        try:
            tweet = next(tweet for tweet in tweet_data if tweet['id'] == tweet_id)
            return jsonify(tweet)
        except StopIteration:
            return jsonify({'error': 'Tweet not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/tweets', methods=['POST'])
    def create_tweet():
        try:
            data = request.get_json()
            if 'text' in data:
                new_tweet = {"id": len(tweet_data) + 1, "text": data['text']}
                tweet_data.append(new_tweet)
                return jsonify(new_tweet), 201  # 201 Created status code
            else:
                return jsonify({"error": "Missing 'text' in request body"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400
