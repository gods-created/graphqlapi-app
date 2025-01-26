from django.test import TestCase
from graphene.test import Client
from graphqlapi.schema import schema

class Tests(TestCase):
    def setUp(self):
        self.client = Client(schema=schema)

    def test__graphene_mutation_create_course(self):
        response = self.client.execute(
            """
                mutation CreateCourse {
                    createCourse(title: "Test Course Title #1") {
                        course {
                            id,
                            title,
                            createdAt
                        }
                    }
                }
            """
        )

        self.assertIn('data', response)

        data = response.get('data')
        
        self.assertIn('createCourse', data)

    def test__graphene_mutation_add_student_to_course(self):
        response = self.client.execute(
            """
                mutation AddStudentToCourse {
                    addStudentToCourse(courseId: 100, studentId: 10) {
                        course {
                            id
                            title
                            createdAt
                            updatedAt
                            students {
                                id,
                                email,
                                fullname
                            }
                        }
                    }
                }

            """
        )

        self.assertIn('errors', response)

        errors = response.get('errors', [])
        message = errors[0].get('message', '')

        self.assertEqual(message, 'A student with so ID is not exist')

    def tearDown(self):
        del self.client