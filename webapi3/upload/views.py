# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.http import HttpResponse
from upload.models import FileNameModel
import os
import threading
from tasks import voice

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'
TARGET_FILE = ''


def form(request):
    if request.method != 'POST':
        return render(request, 'upload/form.html')

    apikey = request.POST['api-key']
    upload_file = request.FILES['file']
    path = os.path.join(UPLOADE_DIR, upload_file.name)
    destination = open(path, 'wb')

    for chunk in upload_file.chunks():
        destination.write(chunk)

    # 結果をDBに保存
    insert_data = FileNameModel(file_name=upload_file.name)
    insert_data.save()

    # ファイルアップロード後、Empathにファイルを送信し、結果を受け取る
    print("upload done.")
    t = threading.Thread(target=voice, args=(path, apikey, ))
    t.start()

    return HttpResponse(status=200)
