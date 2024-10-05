from elasticsearch import Elasticsearch
from django.conf import settings
from .models import Course

class CourseSearch:
    def __init__(self):
        # Initialize Elasticsearch client
        self.es = Elasticsearch([settings.ELASTICSEARCH_HOST])

    def search_courses(self, query):
        # Search courses in Elasticsearch
        response = self.es.search(
            index='courses',
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["title", "description"],  # Fields to search
                    }
                }
            }
        )
        return response['hits']['hits']

    def index_courses(self):
        # Index all courses in Elasticsearch
        courses = Course.objects.all()
        for course in courses:
            self.es.index(
                index='courses',
                id=course.id,
                body={
                    "title": course.title,
                    "description": course.description,
                }
            )

    def delete_course(self, course_id):
        # Delete a course from the Elasticsearch index
        self.es.delete(index='courses', id=course_id)
