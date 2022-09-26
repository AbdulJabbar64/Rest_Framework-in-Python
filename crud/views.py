import io
from django import views
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(views.View):
    def get(self, request, *args, **kwargs):
        data1 = request.body
        stream = io.BytesIO(data1)
        parser = JSONParser().parse(stream)
        id = parser.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_rander = JSONRenderer().render(serializer.data)
            return HttpResponse(json_rander, content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_rander = JSONRenderer().render(serializer.data)
        return HttpResponse(json_rander, content_type="application/json")
    
    def post(self, request, *args, **kwargs):
        data1 = request.body
        stream = io.BytesIO(data1)
        parser = JSONParser().parse(stream)
        serializer = StudentSerializer(data=parser)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"Data Created!!"}
            json_rander = JSONRenderer().render(msg)
            return HttpResponse(json_rander, content_type="application/json")
        json_rander = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_rander, content_type="application/json")
    
    def put(self, request, *args, **kwargs):
        data1 = request.body
        stream = io.BytesIO(data1)
        parser = JSONParser().parse(stream)
        id = parser.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=parser, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"Data Updated!!"}
            json_rander = JSONRenderer().render(msg)
            return HttpResponse(json_rander, content_type="application/json")
        json_rander = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_rander, content_type="application/json")
    
    def delete(self, request, *args, **kwargs):
        data1 = request.body
        stream = io.BytesIO(data1)
        parser = JSONParser().parse(stream)
        id = parser.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        msg = {"msg":"Data Deleted!!"}
        json_rander = JSONRenderer().render(msg)
        return HttpResponse(json_rander, content_type="application/json")

def get_all(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_rander = JSONRenderer().render(serializer.data)
    return HttpResponse(json_rander, content_type="application/json")

# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         data1 = request.body
#         stream = io.BytesIO(data1)
#         parser = JSONParser().parse(stream)
#         id = parser.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_rander = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_rander, content_type="application/json")
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_rander = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_rander, content_type="application/json")

#     elif request.method == 'POST':
#         data1 = request.body
#         stream = io.BytesIO(data1)
#         parser = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=parser)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {"msg":"Data Created!!"}
#             json_rander = JSONRenderer().render(msg)
#             return HttpResponse(json_rander, content_type="application/json")
#         json_rander = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_rander, content_type="application/json")
    
#     elif request.method == 'PUT':
#         data1 = request.body
#         stream = io.BytesIO(data1)
#         parser = JSONParser().parse(stream)
#         id = parser.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=parser, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {"msg":"Data Updated!!"}
#             json_rander = JSONRenderer().render(msg)
#             return HttpResponse(json_rander, content_type="application/json")
#         json_rander = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_rander, content_type="application/json")
    
#     elif request.method == 'DELETE':
#         data1 = request.body
#         stream = io.BytesIO(data1)
#         parser = JSONParser().parse(stream)
#         id = parser.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         msg = {"msg":"Data Deleted!!"}
#         json_rander = JSONRenderer().render(msg)
#         return HttpResponse(json_rander, content_type="application/json")