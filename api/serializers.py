#Object to JSON  and JSOn to Dictionary Validation

from rest_framework import serializers
from crud.models import Classroom, Student

class ClassroomSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)

class ClassroomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id","name"] #returns only value that is in the list. or validate only the data of the given list.

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"