from django.shortcuts import render, HttpResponse
import os, json

# Create your views here.

def appImg(request):
    return render(request, "toolsOpen/appImgComp.html", {"title": "App图片合成"})


def appImgUploadBack(request):
    rtn = {
        "result": False,
        "data": None,
        "msg": None
    }
    myfile = request.FILES.get("uploadB")
    filename = myfile.name
    filename = os.path.join(r"static\upload", filename)
    with open(filename, "wb") as f:
        for item in myfile.chunks():
            f.write(item)
    rtn["result"] = True
    rtn["data"] = "\\" + filename
    rep = HttpResponse(json.dumps(rtn))
    rep["X-Frame-Options"] = "SAMEORIGIN"  # 允许在Frame框架中显示
    return rep


def appImgUploadFront(request):
    rtn = {
        "result": False,
        "data": None,
        "msg": None
    }
    if request.method == "POST":
        myfile = request.FILES.get("uploadF")
        filename = myfile.name
        filename = os.path.join(r"static\upload", filename)
        with open(filename, "wb") as f:
            for item in myfile.chunks():
                f.write(item)
        rtn["result"] = True
        rtn["data"] = "\\" + filename
        rep = HttpResponse(json.dumps(rtn))
        rep["X-Frame-Options"] = "SAMEORIGIN"  # 允许在Frame框架中显示
        return rep


def appImgComp(request):
    rtn = {
        "result": False,
        "data": None,
        "msg": None
    }
    if request.method == "POST":
        try:
            dataComp = json.loads(request.POST.get("dataComp", None))
            from toolsOpen.service import imgExt
            rtn = imgExt(dataComp)
            if rtn["result"]:
                rtn["data"] = "\\" + rtn["data"]
        except Exception as e:
            rtn["msg"] = str(e)
        rep = HttpResponse(json.dumps(rtn))
        return rep
