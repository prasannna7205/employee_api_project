from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.viewsets import ViewSet
from rest_framework.pagination import PageNumberPagination
from  rest_framework import status
from rest_framework.generics import ListAPIView

# Create your views here.


class pagination1(PageNumberPagination):
    page_size = 5

class getemployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeecurAapi(ViewSet):
    def addpost(self,request):
        payload = request.data
        esiri = EmployeeSerializer(data = payload)
        if esiri.is_valid():
            esiri.save()
        return Response(esiri.data,status=status.HTTP_201_CREATED)
    
    def getemployeebyid(self,request,id):
        qs = Employee.objects.get(id = id)
        esiri = EmployeeSerializer(qs)
        return Response(esiri.data,status=status.HTTP_200_OK)
    
    def updateemployee(self,request):
        data1 = request.data
        qs = Employee.objects.get(id=data1['id'])
        esiri  = EmployeeSerializer(qs,data=data1)
        if esiri.is_valid():
            esiri.save()
        return Response(esiri.data,status=status.HTTP_201_CREATED)
    
    def deleteemployee(self,request,id):
        try:
            qs = Employee.objects.get(id = id)
            qs.delete()
            return Response('deleted',status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response('id doesnot exist',status=status.HTTP_200_OK)


    def validateemployee(self,request):
        data1 = request.data
        if data1['age']<60 and data1['gender'] in ['M','F','T']:
            esiri = EmployeeSerializer(data=data1)
            if esiri.is_valid():
                esiri.save()
            return Response(esiri.data,status=status.HTTP_200_OK)
        else:
            return Response({"msg":"employee age cannot be morethan 60 an gender sh"})

    

