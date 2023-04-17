from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestUrls(APITestCase):

    def test_post_video(self):
        url = reverse('video')
        data = {'id': 7, 'title': 'new', 'uploaded_date': '2023-01-11', 'views': 0, 'likes': 0, 'dislike': 0,
                'playlist': None}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
