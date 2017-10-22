from django.http import JsonResponse
from django.shortcuts import render
from yk import yk_login
from login import login
import requests
import json
import subprocess
# Create your views here.

def index(request):
    return render(request,"index.html")

def _login(request):
    uid = request.GET.get("uid")
    pwd = request.GET.get("pwd")
    if yk_login():
        command = "svm-scale testfile"
        out = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        command = "svm-predict testfile.scale *.modle outputfile"
        out = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

        context = {"a": "男", "b": "16-25","c": "本科","d": "教育","e": "金牛座","f": "30w","g": "未婚","h": "0-30min","i": "否","j": "是","k": "否","l": "否","m": "是","n": "否","o": "是","p": "是","q": "否","r": "否","s": "是","t": "否","u": "是","v": "是","w": "是","x": "是","y": "美国","z": "科幻","aa": "动作","ab": "教育","ac": "国防","ad": "股票",}
        return render(request, "result.html", context=context)
    else:
        render(request, "index.html")
