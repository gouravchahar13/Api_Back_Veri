from django.shortcuts import HttpResponse
from django.http import JsonResponse,HttpResponseBadRequest
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json,os

def get(request):
    data=list(User.objects.all()[:10])
    if not data:
        return JsonResponse({"message": "empty"})
    user_list = serializers.serialize('json', data)
    data=json.dumps(user_list)
    return JsonResponse(data, safe=False)
    
@csrf_exempt
def search(request,id):
    id=int(id)
    users = User.objects.filter(govt_id=id)
    if not users.exists():
        return JsonResponse({"message": "empty"},status=404)
    else:
        user_list = serializers.serialize('json', users)
        return JsonResponse(user_list, safe=False)