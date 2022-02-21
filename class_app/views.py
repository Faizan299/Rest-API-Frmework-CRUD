from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)


class getStudent(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    def get(self, request, pk, format = None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

   
class Student1(GenericAPIView):
    def get(self,request,format=None):
        stu = Student.objects.all()
        serial = StudentSerializer(stu, many=True)
        return Response(serial.data)


class Student2(GenericAPIView):
    serializer_class = StudentSerializer
    def post(self,request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({     'payload' : serializer.data,
                              'message' : 'Data Created Successfully'})

class Student3(GenericAPIView):
    serializer_class = StudentSerializer
    def put(self, request, pk = None , format = None):
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
        return Response({'message' : 'Data Updated Successfully'})

class Student4(GenericAPIView):
    serializer_class = StudentSerializer
    def delete(self , request, pk = None , format = None):
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'message' : 'Delete Data Succesfully'})
