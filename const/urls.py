from django.urls import path

from const.views import ConstTest

url = [
    path('g', ConstTest.index)
]
urlpatterns = url
