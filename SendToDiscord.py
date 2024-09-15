import requests
import json

def send_discord_message(webhook_url, message):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'content': message,
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

    if response.status_code == 204:
        print('Message sent successfully.')
    else:
        print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')

def main():
    webhook_url = input('Webhook URL: ')
    print("Made by Star")
    while True:
        message = input('Type to send (or press 2 to exit.): ')
        
        if message.lower() == 'exit':
            print('Exiting the message sender.')
            break

        send_discord_message(webhook_url, message)

if __name__ == '__main__':
    main()
