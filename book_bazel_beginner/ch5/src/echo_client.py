import sys
import socket
import json


print("=== Spinning up the Echo Client in Python... ===")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as so:
        so.connect(("localhost", 1234))
        print("Waiting on input from the user...")

        input_string = input()
        if input_string:
            obj = {"message": input_string, "value": 3.145}

            data = json.dumps(obj).encode("utf-8")
            so.sendall(data)

            recv = so.recv(1024)
            print(f"Received by Python: {recv.decode('utf-8')}")

except Exception as err:
    print("Error: {0}".format(err))
    sys.exit(1)
