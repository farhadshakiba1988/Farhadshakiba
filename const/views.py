from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from const.const import Const


class ConstTest:
    @staticmethod
    def index(request):
        return JsonResponse(Const.get(request.GET['k']), safe=False)
