from django.test import TestCase
from unittest.mock import patch
from .models import Student
from graphene.test import Client
from graphqlapi.schema import schema

class Tests(TestCase):
    @patch('student.models.Student.objects.with_fullname')
    def test__with_fullname(self, mock_object):
        return_value = []
        mock_object.return_value = return_value

        response = Student.objects.with_fullname()

        self.assertEqual(response, return_value)

    def test__graphql_query(self):
        client = Client(schema=schema)
        response = client.execute(
            """
                query Students {
                    students {
                        id
                        email
                        fullname
                        createdAt
                    }
                }
            """
        )

        self.assertIn('data', response)