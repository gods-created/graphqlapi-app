from graphene import ObjectType, Mutation, Field, List, Int, String
from graphene_django import DjangoObjectType
from .models import Student

class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = '__all__'

    courses = List('course.schema.CourseType')

    def resolve_courses(self, info):
        return self.courses.all()

class Query(ObjectType):
    students = List(StudentType)
    student = Field(StudentType, id=Int(required=True))

    def resolve_students(self, info):
        return Student.objects.all()
    
    def resolve_student(self, info, id):
        return Student.objects.prefetch_related('courses').filter(pk=id).first()