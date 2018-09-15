# -*- coding: utf-8 -*-
from poster.encode import multipart_encode, MultipartParam
from poster.streaminghttp import register_openers
import urllib2
import json
import time


# 解析メソッド
def voice(file_path, apikey):
    time.sleep(5)
    url = "https://api.webempath.net/v2/analyzeWav"
    register_openers()
    items = [MultipartParam('apikey', apikey),
             MultipartParam.from_file('wav', file_path)]
    datagen, headers = multipart_encode(items)
    request = urllib2.Request(url, datagen, headers)
    readObject = urllib2.urlopen(request)  # type: object

    if readObject.getcode() != 200:
        print("HTTP status %d" % (readObject.getcode()))

    response = json.load(readObject)
    print(response)
    anger_num=response['anger']*(255//50)
    print(anger_num)
    print(hex(anger_num))
    while True:
        if subprocess.check_call(["gatttool","-b","24:0A:C4:07:84:3E","--char-write-req","-a","0x002a","-n", hex(anger_num)]) == 0:
            break

    print(response)
    if response["error"] > 0:
        print(response["error"])
