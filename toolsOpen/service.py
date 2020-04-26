from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


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
        img = Image.open(filename)
        if len(objs) == 0:
            raise Exception("请选择需要合并的图片或者文字")
        for item in objs:
            posX = int(objs[item]["beginX"][:-2])
            posY = int(objs[item]["beginY"][:-2])
            if objs[item]["type"] == "img":
                fileExt = objs[item]["file"][1:]
                img = imgCImg(img, fileExt, posX, posY)
            elif objs[item]["type"] == "text":
                sText = objs[item]["text"]
                fontSize = int(objs[item]["fontSize"][:-2])
                fontColor = objs[item]["fontColor"]
                img = imgCText(img, sText, fontSize, fontColor, posX, posY)
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
        img.save(fileSave)
        rtn["data"] = fileSave
    except Exception as e:
        rtn["result"] = False
        rtn["msg"] = str(e)

    return rtn


def imgCImg(img, fileExt, beginX, beginY):
    imgExt = Image.open(fileExt)
    img.paste(imgExt, (beginX, beginY))

    return img


def imgCText(img, sText, fontSize, fontColor, beginX, beginY):
    image_draw = ImageDraw.Draw(img)
    font=ImageFont.truetype(r"static\rs\simfang.ttf", fontSize)
    image_draw.text((beginX, beginY), sText, font=font, fill=fontColor)

    return img
