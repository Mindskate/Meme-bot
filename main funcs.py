import json 
import requests


TOKEN = "Concealed" #you may request for it if you are interested in the project
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    update_js = get_json_from_url(url)
    return update_js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = (num_updates - 1)
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)
