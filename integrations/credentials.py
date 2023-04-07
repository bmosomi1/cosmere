import json

import requests
from requests.auth import HTTPBasicAuth


class Miwama():
    CONSUMER_KEY = "QsQL9odAOLFScbay5WdORIqXMC9UhAIU"
    CONSUMER_PASSWORD = "KvrqNpZvl38XdGXa"
    PASS_KEY = "9758377c9ec4d2fdf8479ce1cee77eb6d421db518997cd3db3664a2b69a868f7"


def mpesa_access_token(consumer_key, consumer_secret):
    api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL,
                     auth=HTTPBasicAuth(consumer_key, consumer_secret))
    print(r.status_code)
    print("GOT HERE")
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    print(mpesa_access_token)
    return validated_mpesa_access_token


class GreenNote():
    CONSUMER_KEY = "VHcVxg0WqnjeKynXnYVjMRXmVH0wdP0K"
    CONSUMER_PASSWORD = "cnY55jGpqZQenmir"
    PASS_KEY = ""


class Parklands():
    CONSUMER_KEY = "Cw9vRzVZFGjfJYdWScmGEUdnEqGQQAlc"
    CONSUMER_PASSWORD = "IaEzpQYei8f7FHQ4"
    PASS_KEY = ""


class Parklands2:
    CONSUMER_KEY = "tN3ZSyPQR24n9Ne1FtUkkbM5ym3ATGUX"
    CONSUMER_PASSWORD = "1AfN304CYOrIGAGo"
    PASS_KEY = ""


class Boresha:
    CONSUMER_KEY = "w4jsRHQHuxRMxp23LGO5LONoyILrSCbj"
    CONSUMER_PASSWORD = "TJlQEPlGLT16havp"
    PASS_KEY = ""


class RealBoutique1:
    shortcode = 4016345
    pass_key = "817b1bd0672cc549a72412d0476539490c7510e55f78187793e92d7e8390e911"
    CONSUMER_KEY = "2UGMygbHOf3Dgpqnk8DnIMNF5GAC5AG8"
    CONSUMER_PASSWORD = "9StiqIrDMusjMyQr"


class RealBoutique2:
    pass_key = "dc783e3b176c7aecbbbcf1aac355ba46fafb014b32de5b01eca4d1ce829529ca"
    CONSUMER_KEY = "pVzd3LWo3mmsLdpjWjJZ5rXzTP2llwTm"
    CONSUMER_PASSWORD = "e7bdZbLMhHTyAMNf"


class RealBoutique3:
    shortcode = 461923
    pass_key = "80cdd2a0db39909b3b16e32eb4b6f10518392770f64c2fc071228e0f9057ce14"
    CONSUMER_KEY = "dOALndjDkSikpQApuV7jerPjj34QcOo2"
    CONSUMER_PASSWORD = "CqKFK8MuhxAD7apy"


class Roberms:
    pass_key = "46db27d1ecc173abb0a863c3e3de801c967c4dc1ef314106f35141fc0133a28f"
    CONSUMER_KEY = "ywcRjacgNeCGoCPxk3lBUrzJZJwbwz0Q"
    CONSUMER_PASSWORD = "TvCUt9PxSfDInBv8"


class Perezu:
    pass_key = "33806bc0b01de91a827b3d1c3903f336a688616b8319719ff5a032e37cf921ca"
    CONSUMER_KEY = "t5wO7NvIPd78fOfCnqwfXjRYz5Ga5qOK"
    CONSUMER_PASSWORD = "jcMiDbIgL08OhGWe"


class Perezu2:
    pass_key = ""
    CONSUMER_KEY = "B4mslWXLy20wCnBWLh1FUjpHkAWtfpZ0"
    CONSUMER_PASSWORD = "LHggW8WEh7CqEI7f"


class Nope:
    pass_key = ""
    CONSUMER_KEY = "sy2QSgdfn1B3bWmJIANKNLRsviDm5hOh"
    CONSUMER_PASSWORD = "UXdTXMuTYE5Qm4EY"


class CleanShiftCredentials:
    pass_key = "a3182d6a983643e88898e9cf004cb4a41d99a138b23ab8df3609d2ccb994f2c0"
    CONSUMER_KEY = "gA8UgUGKGjerdj1G3ZSfAhOkURuJvMYs"
    CONSUMER_PASSWORD = "Md99dnCTkfnB20GL"


class GreenNote2Credentials:
    pass_key = ""
    CONSUMER_KEY = "gDSAofGGpA1Qzf8Koq5Nlrqbznhc8BmX"
    CONSUMER_PASSWORD = "UlzVgvdNjNtHP7G1"


class OlemaxCredentials:
    pass_key = ""
    CONSUMER_KEY = "4Enn3bDsRjQ9w9HkF98JHPowyAvh0l75"
    CONSUMER_PASSWORD = "bg2SkviggNCOmSWw"


class AquaNovaCredentials:
    pass_key = ""
    CONSUMER_KEY = "OdxFqwXRqZKbsH9R8Bf5KbPP6ugWBufg"
    CONSUMER_PASSWORD = "mrsKX3k45GcXrF0C"