from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import ComicGroupMessage,Comments

class TestComments(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.comment = Comments.objects.create(
            sender='Reetish',
            body='fkldsjafads',
            user_id = 'fdsafsadfasdfas'
        )

    def test_comment_API_Response(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code,200)
