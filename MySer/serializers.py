# 此文件用来存放序列化器

from rest_framework import serializers  # 序列化器都存放在这里

from MySer.models import *

#class StudentSer(serializers.Serializer): # 自定义的序列化器要求继承于serializers.Serializer
class StudentSer(serializers.ModelSerializer):

    '''
    里面写的是每一个需要序列化/发序列化的字段
    跟定义模型基本一致
    '''

    # name = serializers.CharField(label='姓名', max_length=20) # 字段长度最好与model里面定义的一致
    # age = serializers.IntegerField()
    # score = serializers.IntegerField()

    class Meta():
        model = Student
        #fields = ['name','age','score']
        # all左右两边是两个下划线
        fields = '__all__'



