from rest_framework import serializers
from .models import Student

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("name","password")