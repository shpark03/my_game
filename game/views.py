from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

import json
import os

def save(request):
        id = request.GET.get('data')
        fout = open('game/positions.json','w+')
        fout.write(id)
        fout.close()
        return HttpResponse("Saved to game/position.json")


def index(request):
        return render(request, "game/make_it_rain_object_save.html", {})

def json_response(request):
        try:
              res = open('game/positions.json').read()
              return HttpResponse(res)
        except os.error:
              return HttpResponseNotFound
