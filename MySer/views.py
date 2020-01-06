from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from MySer.models import *
from MySer.serializers import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class StudentGenAPIView(GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSer

    def get(self, request):
        ser = self.get_serializer(self.get_queryset(), many=True)
        #ser = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=ser.data,)


class StudentVS(viewsets.ModelViewSet):
    pass

class StudentAPIView(APIView):
    '''
    处理用户的get请求
    '''
    def get(self, request):
        '''
        处理业务
        跟数据进行交互
        '''
        stus = Student.objects.all()
        ser = StudentSer(stus, many=True)
        return Response(data=ser.data,)

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    def list(self, request, *args, **kwargs):
        print("hahah")
        rst = super(StudentViewSet, self).list(*args, **kwargs)
        return rst
