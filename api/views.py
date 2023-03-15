from django.shortcuts import render
from .serializers import SchoolSerializer,StudentSerializer,NestedStudentSerializer
from .models import School,Student
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics,status
from rest_framework.response import Response
from django.db.utils import IntegrityError


# Create your views here.

# class SchoolList(generics.ListCreateAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

# class StudentList(generics.ListCreateAPIView):
#     queryset = School.objects.all()
#     serializer_class = StudentSerializer

#     def create(self, request, *args, **kwargs):
#         school_id = request.data.get('school_id')

#         if school_id:
#             try:
#                 school = School.objects.get(pk=school_id)
#                 num_students = Student.objects.filter(school_id=school_id).count()
#                 if num_students >= school.maximum:
#                     return Response({'error': 'School has reached its maximum number of students.'}, status=status.HTTP_400_BAD_REQUEST)
#             except School.DoesNotExist:
#                 return Response({'error': 'School does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.validated_data['school'] = school 
#         try:
#             self.perform_create(serializer)
#         except IntegrityError as e:
#             return Response({'error': 'Duplicate entry for student ID in this school.'}, status=status.HTTP_400_BAD_REQUEST)  

# class SchoolDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
    

# class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentsInSchool(generics.ListCreateAPIView):
#     serializer_class = StudentSerializer

#     def get_queryset(self):
#         return Student.objects.filter(school_id=self.kwargs["school_pk"])

#Nested Routers
class SchoolVeiwSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(ModelViewSet):
    serializer_class = NestedStudentSerializer

    def get_queryset(self):
        return  Student.objects.filter(school_id=self.kwargs["school_pk"])
    
    def get_serializer_context(self):
        return {"school_id": self.kwargs["school_pk"]}
    
