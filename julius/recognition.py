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
    while os.path.exists('/app/recognize.lock'):
        time.sleep(1)

    os.system('touch /app/recognize.lock')
    
    p = subprocess.Popen(
        ["/app/julius/julius-start.sh"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    ) # julius起動スクリプトを実行

    p.stdin.write(voice)

    time.sleep(10)

    # pid = str(p.stdout.read().decode('utf-8')) # juliusのプロセスIDを取得
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port)) #サーバーモードで起動したjuliusに接続

    data = '' # dataの初期化

    while True:
        tmp = str(client.recv(chunkSize).decode('utf-8')) #dataが空のときjuliusからdataに入れる
        data += tmp

        # print(data) # 認識した言葉を表示して確認
        if '</RECOGOUT>\n.' in data: 
            print(data)

            word = None

            root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
            for whypo in root.findall('./SHYPO/WHYPO'):
                word = whypo.get('WORD')# juliusで認識したWORDをwordに入れる

            break

    p.kill()
    # subprocess.call(["kill " + pid], shell=True)# juliusのプロセスを終了する。
    client.close()

    os.system('rm /app/recognize.lock')

    return word

# 参考文献
#  https://qiita.com/fishkiller/items/c6c5c4dcd9bb8184e484
