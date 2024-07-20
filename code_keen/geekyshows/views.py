from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.http import JsonResponse
from rest_framework.response import Response
from .Serializers import StudentSerilizers

from rest_framework.parsers import JSONParser
# Create your views here.
@api_view(['GET'])
@csrf_exempt
def student_list(request,id):
    if request.method == 'GET':
        students = Student.objects.get(id=id)
        serializer = StudentSerilizers(students, partial=True)
        return JsonResponse({"data":serializer.data})
@api_view(['POST'])
@csrf_exempt
def student_post(request):
    if request.method=='POST':
        data=request.data
        name=data.get('name')
        img=data.get('img')
        print(name,img,'-------------------------------')
        data  = {
        "name":name,
        "img": img                               # Note: Adjust this based on your model requirements
    }
        serializer=StudentSerilizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"success":'..................'})
@api_view(['PUT'])
def student_put(request,id):
    if request.method=='PUT':
        name=request.data.get('name')
        img=request.data.get('img')
        new_id=Student.objects.get(id=id)
        data  = {
        "name": name,
        "img": img  # Note: Adjust this based on your model requirements
    }
        serializer=StudentSerilizers(new_id,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"success":'..................'})
