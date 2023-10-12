#Object to JSON  and JSOn to Dictionary Validation

from rest_framework import serializers
from crud.models import Classroom, Student, StudentProfile

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
    #over riding get_fields for classroom serializer
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")

        if request and request.method == "GET":
            fields['classroom'] = ClassroomModelSerializer()  #Convert the object of the class to JSON ##
        return fields

class StudentProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")

        if request and request.method == "GET":
            fields['student'] = StudentModelSerializer()
        return fields
