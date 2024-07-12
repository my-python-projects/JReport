import json
from services.rabbitmq import receive_messages

def send_email(message):
    username = message['username']
    email = message['email']
    print(f"Sending email to {username} at {email}")


if __name__ == '__main__':
    receive_messages('user_registered', send_email)
