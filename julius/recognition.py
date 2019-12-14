import socket
import xml.etree.ElementTree as ET
import os
import subprocess
import time
import sys

host = '127.0.0.1' #localhost
port = 10500   #juliusサーバーモードのポート
chunkSize = 1024

def recognize(voice):
    with open('tmp.dat', 'wb') as f:
        f.write(voice)

    p = subprocess.Popen(
        ["/app/julius/julius-start.sh"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    ) # julius起動スクリプトを実行

    time.sleep(3)

    p.stdin.write(voice)

    time.sleep(3)

    # pid = str(p.stdout.read().decode('utf-8')) # juliusのプロセスIDを取得
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port)) #サーバーモードで起動したjuliusに接続

    data = '' # dataの初期化

    word = None

    while True:
        tmp = str(client.recv(chunkSize).decode('utf-8')) #dataが空のときjuliusからdataに入れる
        print(tmp, file=sys.stderr)
        if len(tmp) == 0:
            break

        data += tmp

        # print(data) # 認識した言葉を表示して確認
        if '</RECOGOUT>\n.' in data: 
            print(data)

            root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
            for whypo in root.findall('./SHYPO/WHYPO'):
                word = whypo.get('WORD')# juliusで認識したWORDをwordに入れる

            break

    p.kill()
    # subprocess.call(["kill " + pid], shell=True)# juliusのプロセスを終了する。
    client.close()

    return word

# 参考文献
#  https://qiita.com/fishkiller/items/c6c5c4dcd9bb8184e484
