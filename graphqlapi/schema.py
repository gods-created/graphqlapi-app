from graphene import ObjectType, Schema
from student.schema import Query as StudentQuery
from course.schema import (
    Query as CourseQuery,
    Mutation as CourseMutation
)

class Query(StudentQuery, CourseQuery, ObjectType):
    pass

class Mutation(CourseMutation, ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)