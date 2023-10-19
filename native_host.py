import sys
import json

def send_response(response):
    sys.stdout.write(json.dumps(response))
    sys.stdout.flush()


while True:
    try:
        message_length = sys.stdin.read(4)
        if not message_length:
            break
        message_length = int(message_length)
        message = sys.stdin.read(message_length)

        url = json.loads(message)['url']

        #processing will b done here

        response = {"status" : "URL processed successfully " }
        send_response(response)

    except Exception as e: 
        response = {"error": str(e)}
        send_response(response)