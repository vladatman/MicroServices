import hazelcast.client
from flask import Flask, jsonify, request
from hazelcast.client import HazelcastClient
import os

application = Flask(__name__)

hazelcast_node_address = os.environ.get('HAZELCAST_NODE_ADDRESS')
client = HazelcastClient(cluster_members=[hazelcast_node_address])
messages = client.get_map('messages').blocking()


@application.route('/', methods=['POST'])
def log():
    message = request.json
    try:
        for i in message.keys():
            messages.put(i, message[i])
            print(message[i])
    except Exception as e:
        return jsonify({'status': 'fail', "message": e})

    return jsonify({'status': 'success'})


@application.route('/', methods=['GET'])
def get_messages():
    reply = list()
    for id_, text in messages.entry_set():
        reply.append({id_: text})
    return jsonify(reply)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=7001)