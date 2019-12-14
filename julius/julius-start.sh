#!/bin/sh

KIT_PATH=/app/julius/ssr-kit-v4.5

# julius -C $KIT_PATH/main.jconf -dnnconf $KIT_PATH/main.dnnconf -input stdin -module > /app/julius/julius.log &
julius -C $KIT_PATH/main.jconf -dnnconf $KIT_PATH/main.dnnconf -input stdin -module > /app/julius/julius.log -smpFreq 44100
# echo $! #プロセスIDを出力
# sleep 2 #2秒間スリープ

# 参考文献:
#  https://qiita.com/fishkiller/items/c6c5c4dcd9bb8184e484
