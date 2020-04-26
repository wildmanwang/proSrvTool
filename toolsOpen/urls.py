from django.urls import re_path
from toolsOpen import views

urlpatterns = [
    re_path('appImg$', views.appImg),
    re_path('appImg-upload-back$', views.appImgUploadBack, name="imgBack"),
    re_path('appImg-upload-front$', views.appImgUploadFront, name="imgFront"),
    re_path('appImg-Comp$', views.appImgComp, name="imgComp"),
]
