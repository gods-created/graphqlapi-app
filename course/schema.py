from graphene import ObjectType, Mutation, Field, List, Int, String
from graphene_django import DjangoObjectType
from .models import Course
from student.models import Student
from typing import Optional

def validate_title(title: str) -> Optional[str]:
    if len(title) > 250:
        return 'The \'title\' field can to have max. 250 characters'
    
    if Course.objects.filter(title=title).exists():
        return 'A course with so title is already exist'
    
    return None

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = '__all__'

    studnets = List('student.schema.StudentType')

    def resolve_students(self, info):
        return self.students.all()
    
class CreateCourse(Mutation):
    class Arguments:
        title = String(required=True)

    course = Field(CourseType)

    def mutate(self, info, title):
        try:
            if (response := validate_title(title)) is not None:
                raise AttributeError(
                    response
                )
            
            course = Course.objects.create(title=title)
            return CreateCourse(course=course)
        
        except AttributeError as e:
            raise Exception(str(e))
        
class AddStudentToCourse(Mutation):
    class Arguments:
        student_id = Int(required=True)
        course_id = Int(required=True)

    course = Field(CourseType)

    def mutate(self, info, student_id, course_id):
        try:
            if (student := Student.objects.filter(pk=student_id).first()) is None:
                raise AttributeError(
                    'A student with so ID is not exist'
                )

            if (course := Course.objects.filter(pk=course_id).first()) is None:
                raise AttributeError(
                    'A course with so ID is not exist'
                )
            
            course.students.add(student)
            return AddStudentToCourse(course=course)

        except AttributeError as e:
            raise Exception(str(e)) 
        
class Mutation(ObjectType):
    create_course = CreateCourse.Field()
    add_student_to_course = AddStudentToCourse.Field()

class Query(ObjectType):
    courses = List(CourseType)
    course = Field(CourseType, id=Int(required=True))

    def resolve_courses(self, info):
        return Course.objects.all()
    
    def resolve_course(self, info, id):
        return Course.objects.prefetch_related('students').filter(pk=id).first()