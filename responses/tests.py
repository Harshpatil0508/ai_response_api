from rest_framework.test import APITestCase
from rest_framework import status
from .models import Response

class ResponseAPITest(APITestCase):
    def test_create_response(self):
        data = {"prompt": "Describe a sunset", "model_used": "gpt-3.5-turbo"}
        response = self.client.post("/api/responses/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("response_text", response.data)

    def test_list_responses(self):
        Response.objects.create(prompt="Test prompt", response_text="Test response",
                                 model_used="test-model", status="completed", processing_time=0.5)
        response = self.client.get("/api/responses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)