from flask import Flask, request, jsonify, abort
import json

def create_app():
    app = Flask(__name__)

    # Load tweet data from the file
    with open("100tweets.json", "r") as file:
        tweets = json.load(file)

    @app.route('/')
    def hello_world():
        return 'Hello World.'

    @app.route('/tweets', methods=['GET'])
    def get_all_tweets():
        try:
            # Example: /tweets?filter_param=value
            filter_param = request.args.get('filter_param')
            
            if filter_param:
                filtered_tweets = [tweet for tweet in tweets if tweet.get('filter_field') == filter_param]
                return jsonify(filtered_tweets)
            else:
                return jsonify(tweets)

        except Exception as e:
            return str(e), 500

    @app.route('/tweets', methods=['POST'])
    def create_tweet():
        try:
            data = request.get_json()
            if 'text' not in data:
                abort(400, description="Incomplete request: 'text' field is required.")

            new_tweet = {
                'id': len(tweets) + 1,
                'text': data['text']
            }

            tweets.append(new_tweet)

            return jsonify(new_tweet), 201  # 201 Created status code for successful creation
        except Exception as e:
            return str(e), 400  # 400 Bad Request status code for unsuccessful request

    @app.route('/tweet/<int:tweet_id>', methods=['GET'])
    def get_tweet_by_id(tweet_id):
        try:
            tweet = next((tweet for tweet in tweets if tweet['id'] == tweet_id), None)
            if tweet:
                return jsonify(tweet)
            else:
                abort(404, description="Tweet not found")
        except Exception as e:
            return str(e), 400

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
