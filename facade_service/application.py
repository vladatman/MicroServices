from flask import Flask, jsonify, request
import requests
from bson import ObjectId
from random import choice

application = Flask(__name__)

logging_service_url = ["http://logging_service_1:7001/",
                       "http://logging_service_2:7001/",
                       "http://logging_service_3:7001/"]
messages_service_url = "http://messages_service:7002/"


@application.route('/', methods=['POST'])
def log():
    log_message = request.json['message']
    message = {str(ObjectId()): log_message}
    log_response = None
    output = dict()
    logg_service = None

    with requests.Session() as session:
        mes_response = session.post(messages_service_url, json=message)

    while not log_response:
        logg_service = choice(logging_service_url)

        try:
            with requests.Session() as session:
                log_response = session.post(logg_service, json=message)
        except Exception as e:
            print(f"Unable to connect to {logg_service}, reason = {e.__class__.__name__} : {e}")
            continue

    output['logger'] = logg_service
    output['logger_response'] = log_response.json()
    output['message-service-response'] = mes_response.json()

    return jsonify(output)

@application.route('/', methods=['GET'])
def get_messages():
    reply = dict()
    output = dict()
    logg_service = None
    log_response = None

    with requests.Session() as session:
        mes_response = session.get(messages_service_url)

    while not log_response:
        logg_service = choice(logging_service_url)

        try:
            with requests.Session() as session:
                log_response = session.get(logg_service)
        except Exception as e:
            print(f"Unable to connect to {logg_service}, reason = {e.__class__.__name__} : {e}")
            continue

    reply['messages_service_response'] = mes_response.json()
    reply['logging_service_response'] = log_response.json()

    output['logger'] = logg_service
    output['get-response'] = reply

    return jsonify(output)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=7000)
