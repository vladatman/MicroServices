import sys
import requests
import getopt
import json

welcome_message = '''
    Microservice help

    -h           print help message and exit
    -m/--method  [GET, POST] method for testing
    -t/--text    text of message to insert for POST method
'''


def get_messages():
    responce = requests.get("http://127.0.0.1:1111/")
    return responce.json()["message"]


def post_message(message: str = "default"):
    header = {
        "Content-Type": "application/json"
    }
    body = json.dumps({"message": message})
    return requests.post("http://127.0.0.1:1111/", headers=header, data=body).json()["status"]


def main(argv):
    method = None
    message = "default message"
    result = ""

    try:
        options, arguments = getopt.getopt(argv, "hm:t:", ['help', 'method=', 'text='])
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
            case _:
                print(f"Unknown option {option}. please, check instruction:")
                print(welcome_message)
                sys.exit(1)

    if method == "GET":
        reply = get_messages()
    elif method == "POST":
        if message is None:
            reply = post_message()
        else:
            reply = post_message(message)

    print(f"Return:\n{reply}")


if __name__ == '__main__':
    main(sys.argv[1:])
