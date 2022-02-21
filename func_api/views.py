from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student_data
from .serializers import StudentSerializer

@api_view(['GET', 'POST' , 'PUT' , 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        id = request.data.get('id')
        if id is not None:
            stu = Student_data.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)


        stu = Student_data.objects.all()
        serial = StudentSerializer(stu, many=True)
        return Response(serial.data)


# @api_view(['POST'])
# def post_data(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Created'})

# @api_view(['PUT'])
# def update_data(request):
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student_data.objects.get(pk=id)
        serializer = StudentSerializer(stu, data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Data Updated Successfully '})

# @api_view(['DELETE'])
# def delete_data(request):
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student_data.objects.get(pk=id)
        stu.delete()
        # serializer = StudentSerializer(stu, data= request.data)
        # if serializer.is_valid():
        #     serializer.save()
        return Response({'message' : 'Delete Data Succesfully'})
            



