from rest_framework import serializers
from .models import School,Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','student_ID','first_Name','last_Name']

class SchoolSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True,read_only=True)
    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = School
        fields = ['ID','school_Name','maximum','students']

class NestedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','student_ID','first_Name','last_Name']

    def create(self, validated_data):
        school_id = self.context["school_id"]
        return Student.objects.create(school_id = school_id, **validated_data)
        