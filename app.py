from flask import Flask
import requests

f = Flask(__name__)

@f.route("/")
def hello():
    try:
        requests.get('https://www.google.ru/', proxies={"http": '<прокси:порт>'})
    except requests.exceptions.ConnectionError:
        return 'Вы забанены'
    else:
        return 'Я смогла кое как выгрузить веб сайт на сервер ,конечно не идеально, но спустя долгое врем я сделала это. Мне не описать всю боль и тяжесть свою, но я так рада, что у меня получилось!'

if __name__ == "__main__":
    f.run()

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.ngrok.io']