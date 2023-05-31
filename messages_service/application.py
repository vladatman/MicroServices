from flask import Flask, jsonify

application = Flask(__name__)


@application.route('/', methods=['GET'])
def get_messages():
    return jsonify({'message': 'Default message'})


@application.route('/', methods=['POST'])
def post_messages():
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=7002)
