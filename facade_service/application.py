from flask import Flask, jsonify, request
import requests
from bson import ObjectId

application = Flask(__name__)

logging_service_url =   "http://logging_service:7001/"
messages_service_url =  "http://messages_service:7002/"

@application.route('/', methods=['POST'])
def log():
    log_message = request.json['message']
    requests.post(logging_service_url, json={str(ObjectId()): log_message})
    return jsonify({'status': 'success'})

@application.route('/', methods=['GET'])
def get_messages():
    message_response = requests.get(messages_service_url)
    log_response = requests.get(logging_service_url)
    reply = list()
    reply.append(message_response.json()['message'])
    reply.append(', ')
    reply.append(log_response.json()['message'])
    response = ''.join(reply)
    return jsonify({"message": response})


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=7000)