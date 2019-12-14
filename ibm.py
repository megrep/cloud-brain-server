import json

import key

from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from ibm_watson import SpeechToTextV1


jp = 'ja-JP_BroadbandModel'
URL = 'https://stream.watsonplatform.net/speech-to-text/api'

authenticator = IAMAuthenticator(key.APIKEY)

stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(URL)


def recognize(binary):
    with open('tmp.wav', 'rb+') as f:
        f.write(binary)

    with open("test.wav", "rb") as f:
        result = stt.recognize(audio=audio_file, content_type="audio/wav", timestamps=False, model=jp)
    
    result = result.get_result()

    try:
        msg = result['results'][0]['alternatives'][0]['transcript']
        return msg
    except:
        return None

