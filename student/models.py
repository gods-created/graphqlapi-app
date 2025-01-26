from django.db.models import (
    Model,
    EmailField,
    CharField,
    ManyToManyField,
    DateTimeField
)

from .manager import StudentManager

class Student(Model):
    email = EmailField(
        null=False,
        blank=False,
        unique=True,
        max_length=150
    )

    fullname = CharField(
        null=False,
        blank=True,
        default='',
        max_length=150
    )

    courses = ManyToManyField(
        'course.Course',
        related_name='courses'
    )

    created_at = DateTimeField(
        auto_now_add=True
    )

    objects = StudentManager()

    class Meta:
        app_label = 'student'
        db_table = 'students'
        ordering = ['email', 'created_at']

    def __str__(self):
        return self.email