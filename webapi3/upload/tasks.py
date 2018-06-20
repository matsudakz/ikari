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
    if response["error"] > 0:
        print(response["error"])
