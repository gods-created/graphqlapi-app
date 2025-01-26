from django.db.models import Manager, Q

class StudentManager(Manager):
    def with_fullname(self):
        return list(
            self.filter(~Q(fullname__exact='')).order_by('id')
        )