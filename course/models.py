from django.db.models import (
    Model,
    CharField,
    ManyToManyField,
    DateTimeField
)

class Course(Model):
    title = CharField(
        null=False,
        blank=False,
        max_length=250,
        unique=True
    )

    students = ManyToManyField(
        'student.Student',
        related_name='students'
    )

    created_at = DateTimeField(
        auto_now_add=True
    )

    updated_at = DateTimeField(
        auto_now=True
    )

    class Meta:
        app_label = 'course'
        db_table = 'courses'
        ordering = ['title']

    def __str__(self):
        return self.title