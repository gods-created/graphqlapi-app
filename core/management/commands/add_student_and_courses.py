from django.core.management import BaseCommand
from student.models import Student
from course.models import Course
from services import generate_random_string

class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help=''
        )

    def __execute(self, course):
        fullname = generate_random_string(10)
        email = generate_random_string(15) + '@gmail.com'

        student, created = Student.objects.get_or_create(
            fullname=fullname,
            email=email
        )

        if not created:
            return self.__execute(course)
        
        student.courses.add(course)
        return student

    def handle(self, *args, **options):
        count = options.get('count', 10)
        course, _ = Course.objects.get_or_create(
            title=generate_random_string(25)
        )

        for _ in range(count):
            student = self.__execute(course)
            course.students.add(student)

        return 'Success'