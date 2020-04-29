from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os


def imgExt(objs):
    rtn = {
        "result": True,
        "data": None,
        "msg": None
    }
    try:
        if "imgBack" in objs:
            filename = objs.pop("imgBack")[1:]
        else:
            raise Exception("请选择背景图片")
        img = Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), filename))
        if len(objs) == 0:
            raise Exception("请选择需要合并的图片或者文字")
        for item in objs:
            posX = int(float(objs[item]["beginX"][:-2]))
            posY = int(float(objs[item]["beginY"][:-2]))
            if objs[item]["type"] == "img":
                fileExt = objs[item]["file"][1:]
                fileWidth = int(objs[item]["width"][:-2])
                fileRotate = int(objs[item]["rotate"])
                img = imgCImg(img, fileExt, posX, posY, fileWidth, fileRotate)
            elif objs[item]["type"] == "text":
                sText = objs[item]["text"]
                fontFamily = objs[item]["fontFamily"]
                fontSize = int(objs[item]["fontSize"][:-2])
                fontWeight = int(objs[item]["fontWeight"])
                fontColor = objs[item]["fontColor"]
                img = imgCText(img, sText, fontFamily, fontSize, fontWeight, fontColor, posX, posY)
            else:
                pass
        iPos = filename.find(".")
        if iPos > 0:
            if iPos > 34:
                iPos = 34
            fileSave = filename[:iPos]
        else:
            fileSave = filename
        fileSave += datetime.strftime(datetime.now(), "%d%H%M%S") + ".PNG"
        img.save(os.path.join(os.path.dirname(os.path.dirname(__file__)), fileSave))
        rtn["data"] = fileSave
    except Exception as e:
        rtn["result"] = False
        rtn["msg"] = str(e)

    return rtn


def imgCImg(img, fileExt, beginX, beginY, fileWidth, fileRotate=0):
    imgExt = Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), fileExt))
    if fileWidth > 0 and fileWidth != imgExt.size[0]:
        newHeight = fileWidth * imgExt.size[1] // imgExt.size[0]
        imgExt = imgExt.resize((fileWidth, newHeight))
    if fileRotate != 0:
        imgExt = imgExt.rotate(-fileRotate)

    img.paste(imgExt, (beginX, beginY))

    return img


def imgCText(img, sText, fontFamily, fontSize, fontWeight, fontColor, beginX, beginY):
    """
    文字合并到图片
    :param img:
    :param sText: 文本内容
    :param fontFamily: 字体， 例如：宋体
    :param fontSize: 字体大小，例如：24
    :param fontWeight: 粗体：700；常规：400
    :param fontColor: 颜色，例如：#FF0000
    :param beginX: x坐标
    :param beginY: y坐标
    :return:
    """
    image_draw = ImageDraw.Draw(img)
    sFont = "static\\rs\\"
    if fontFamily == "宋体":
        sFont += "simsun.ttc"
    elif fontFamily == "楷体":
        sFont += "simkai.ttf"
    elif fontFamily == "黑体":
        sFont += "simhei.ttf"
    elif fontFamily == "华文细黑":
        sFont += "STXIHEI.TTF"
    elif fontFamily == "仿宋":
        sFont += "simfang.ttf"
    else:
        sFont += "simfang.ttf"
    font=ImageFont.truetype(sFont, fontSize)
    image_draw.text((beginX, beginY), sText, font=font, fill=fontColor)

    return img
