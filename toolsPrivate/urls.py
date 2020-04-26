from django.urls import re_path
from toolsPrivate import views

urlpatterns = [
    re_path('test$', views.test),
]
