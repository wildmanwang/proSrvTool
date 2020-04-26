from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, "toolsPrivate/test.html", {"title": "测试"})