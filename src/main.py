import requests


def main(url_to_short: str, api: str):
    _url = "https://api.apilayer.com/short_url/hash"

    payload = f"{url_to_short}".encode("utf-8")
    headers = {
        "apikey": api
    }

    response = requests.request("POST", _url, headers=headers, data=payload)

    return response


if __name__ == '__main__':
    url = input("Enter Your URL: ")
    res = main(url, "Enter Your API Here")
    if res.ok:
        print("Short URL: {}".format(res.json().get('short_url')))
    elif res.status_code == 429:
        print("You have exceeded your daily. Go to https://apilayer.com/subscriptions to upgrade your account")
    else:
        print(res.json().get('message'))