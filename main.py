import sys
import requests
import getopt
import json
from pprint import pprint

welcome_message = '''
    Microservice help

    -h           print help message and exit
    -m/--method  [GET, POST] method for testing
    -t/--text    text of message to insert for POST method
    -n/--number  number of POST requests
'''


def get_messages() -> dict:
    response = requests.get("http://127.0.0.1:7000/")
    return response.json()


def post_message(message: str = "default", counter: int = 1) -> list:
    header = {
        "Content-Type": "application/json"
    }

    reply = list()
    iterator = 0

    for i in range(counter):
        text = f"{message}_{str(iterator)}"
        body = json.dumps({"message": text})
        response = requests.post("http://127.0.0.1:7000/", headers=header, data=body)
        reply.append(response.json())
        iterator += 1

    return reply


def main(argv):
    method = None
    message = "default message"
    counter = 1
    result = ""

    try:
        options, arguments = getopt.getopt(argv, "hm:t:n:", ['help', 'method=', 'text=', 'number='])
    except getopt.GetoptError as e:
        print(f"Argument Error: {e}")
        sys.exit(1)

    for option, argument in options:
        match option:
            case "-h" | "--help":
                print(welcome_message)
                sys.exit(0)
            case "-m" | "--method":
                method = argument.upper()
            case "-t" | "--text":
                message = argument
            case "-n" | "--number":
                count = int(argument)
            case _:
                print(f"Unknown option {option}. please, check instruction:")
                print(welcome_message)
                sys.exit(1)
    reply = ""
    if method == "GET" or method is None:
        reply = get_messages()
    elif method == "POST":
        if message is None:
            reply = post_message(counter=counter)
        else:
            reply = post_message(message, counter=counter)

    print(f"Return:\n")
    pprint(reply)

    sys.exit(0)



if __name__ == '__main__':
    main(sys.argv[1:])
