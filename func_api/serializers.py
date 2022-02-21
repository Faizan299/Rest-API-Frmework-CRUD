from rest_framework import serializers
from .models import Student_data

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_data
        fields = "__all__"