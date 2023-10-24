import requests, time

discord_webhook = input("Webhook URL: ")

message = input("Message to send: ")

while True:
    payload = {"content": message}

    response = requests.post(discord_webhook, json=payload)

    if response.status_code == 204:
        print("Message succesfully sent to discord webhook")

    time.sleep(0.375) # you can change this to whatever you want
