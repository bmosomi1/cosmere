import json

import requests
from requests.auth import HTTPBasicAuth


class Gathu():
    CONSUMER_KEY = "qcFUeKnloh80PyVxl4tgYgPGrOI3dT4J"
    CONSUMER_PASSWORD = "7kyiwuxcRdBdGoLl"
    PASS_KEY = ""


class Chrisbe():
    CONSUMER_KEY = "VteH7lhs9DKZziGQufAZzACKkzZeGM78"
    CONSUMER_PASSWORD = "YRDstTtH2Yly4ZW4"
    PASS_KEY = "748127c7fc3bb0db576e892b515dd552cf944061b881b0f1e47a6da77ba042b6"


class Experiential():
    CONSUMER_KEY = "IScFKREI8Q6QeV5NqGLCV1DdfQ2dzOFh"
    CONSUMER_PASSWORD = "Pq961kdZO78kFHEI"
    PASS_KEY = "7291001a49caa067a4cdfa916b9e0961e4ba225bcb6e8b81a117d605188dd4bd"


class Clemode():
    CONSUMER_KEY = "A7PpxkVogKCzKHhitYODZxKpzUkDwQZG"
    CONSUMER_PASSWORD = "c3EVkKxQtxZLGxGL"
    PASS_KEY = "0c8f7e5dead2236b13a51fb376d88b881c05420cdf1f76cb87493bbc0e40a0b0"


class Dimples():
    CONSUMER_KEY = "if0N9HijcA3nA9MhMk8Y8x3RWBEPsG1c"
    CONSUMER_PASSWORD = "rtbRjIEi3xsaGY7v"
    PASS_KEY = "d4d8b158d7d832e039f3815ee60aee3ec4cbcbc6efec008af4740098d6f10120"


class Miwama():
    CONSUMER_KEY = "QsQL9odAOLFScbay5WdORIqXMC9UhAIU"
    CONSUMER_PASSWORD = "KvrqNpZvl38XdGXa"
    PASS_KEY = ""


def mpesa_access_token(consumer_key, consumer_secret):
    api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL,
                     auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return validated_mpesa_access_token

