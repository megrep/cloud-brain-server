import json

import key

from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from ibm_watson import SpeechToTextV1


jp = 'ja-JP_BroadbandModel'
URL = 'https://stream.watsonplatform.net/speech-to-text/api'

authenticator = IAMAuthenticator(key.APIKEY)

audio_file = open("test.ogg", "rb")

stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(URL)
result = stt.recognize(audio = audio_file, content_type="audio/ogg",timestamps = False, model=jp)
result = result.get_result()

msg = result['results'][0]['alternatives'][0]['transcript']
print(msg)
print (json.dumps(result, indent=2, ensure_ascii=False))

