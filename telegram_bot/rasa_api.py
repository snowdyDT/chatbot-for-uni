import requests

url = f'http://0.0.0.0:5005'


def send_text_to_model(text: str):
    payload = {
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


if __name__ == "__main__":
    t = "Привет"
    result = send_text_to_model(text=t)
    print(result)
