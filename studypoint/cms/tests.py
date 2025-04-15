from django.test import TestCase
from .models import *

# Create your tests here.
# model test case

class FirstTestCase(TestCase):
    def setUp(self):
        print("Setting up the test case...")

    def test_topic(self):
        topics = ["Math", "Science", "History"]
        for topic in topics:
            obj = Topics.objects.create(
                name=topic,
                description=f"This is a description for {topic}."
            )
            self.assertEqual(topic, obj.name)

        objs = Topics.objects.all()
        self.assertEqual(objs.count(), 3)