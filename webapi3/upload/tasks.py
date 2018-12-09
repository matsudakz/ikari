# -*- coding: utf-8 -*-
from poster.encode import multipart_encode, MultipartParam
from poster.streaminghttp import register_openers
import urllib2
import json
import time
import subprocess

MAX_RANGE=255
SLEEP_TIME=1
EMPATH_URL="https://api.webempath.net/v2/analyzeWav"

# 解析メソッド
def max_func(n):
    return n[1]

def voice_rgb(file_path, apikey):
    time.sleep(SLEEP_TIME)
    register_openers()
    items = [MultipartParam('apikey', apikey),
             MultipartParam.from_file('wav', file_path)]
    datagen, headers = multipart_encode(items)
    request = urllib2.Request(EMPATH_URL, datagen, headers)
    readObject = urllib2.urlopen(request)  # type: object

    if readObject.getcode() != 200:
        print("HTTP status %d" % (readObject.getcode()))

    response = json.load(readObject)
    print(response)

    if response['error'] != 0:
        print("analyze error %d" % (response['error']))
        return

    list=[('anger', response['anger']),('joy', response['joy']),('sorrow', response['sorrow']),('calm', response['calm'])]
    max_num=max(list, key=max_func)
    if max_num[0] == 'calm':
        rgb=int('ffffff', 16)
    else:
        red=(response['anger']+response['energy']/2)*(MAX_RANGE//50)
        green=(response['joy']+response['energy']/2)*(MAX_RANGE//50)
        blue=(response['sorrow']+response['energy']/2)*(MAX_RANGE//50)
        rgb=(red<<16)+(green<<8)+blue

    print("rgb=", rgb)

    while True:
        if subprocess.check_call(["gatttool","-b","24:0A:C4:07:84:3E","--char-write-req","-a","0x002a","-n", format(rgb, 'x')]) == 0:
            break

def voice(file_path, apikey):
    time.sleep(SLEEP_TIME)
    register_openers()
    items = [MultipartParam('apikey', apikey),
             MultipartParam.from_file('wav', file_path)]
    datagen, headers = multipart_encode(items)
    request = urllib2.Request(EMPATH_URL, datagen, headers)
    readObject = urllib2.urlopen(request)  # type: object

    if readObject.getcode() != 200:
        print("HTTP status %d" % (readObject.getcode()))

    response = json.load(readObject)
    print(response)

    if response['error'] != 0:
        print("analyze error %d" % (response['error']))
        return

    anger_num=response['anger']*(MAX_RANGE//50)
    print(anger_num)
    print(format(anger_num, 'x'))
    while True:
        if subprocess.check_call(["gatttool","-b","24:0A:C4:07:84:3E","--char-write-req","-a","0x002a","-n", format(anger_num, 'x')]) == 0:
            break
