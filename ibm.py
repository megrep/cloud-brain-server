import json
import sys
import wave
import struct


import key

from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from ibm_watson import SpeechToTextV1


jp = 'ja-JP_BroadbandModel'
URL = 'https://stream.watsonplatform.net/speech-to-text/api'

authenticator = IAMAuthenticator(key.APIKEY)

stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(URL)


def bin2wav(filedata, filename, channels=1, sampwidth=2, framerate=44100, nframe=0, comptype='NONE', compname='not compressed'):
    w = wave.Wave_write(filename)
    p = (channels, sampwidth, framerate, nframe, comptype, compname)

    w.setparams(p)
    w.writeframes(filedata)
    w.close()


def recognize(binary):
    # result = []
    # for b in list(binary):
    #     result.append(b / 32768)
    # binary = bytes(result)

    nframe = len(binary) // 2
    #struct.unpack_from(">I4sIIBB", binary, 8)
    
    binary = list(binary)

    for i in range(nframe):
        binary[i*2], binary[i*2+1] = binary[i*2+1], binary[i*2]

    binary = bytes(binary)
    #with open('tmp.wav', "wb") as f:
    #    f.write(binary)

    # nframe = len(binary)
    bin2wav(filedata=binary, filename="tmp.wav", nframe=nframe)

    with open("tmp.wav", "rb") as f:
        result = stt.recognize(
            audio=f, content_type="audio/wav", timestamps=False, model=jp)

    result = result.get_result()

    try:
        msg = result['results'][0]['alternatives'][0]['transcript']
        print(msg, file=sys.stderr)
        return msg
    except:
        return None
