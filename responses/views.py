import openai
import time
import os
from rest_framework import generics, status
from rest_framework.response import Response as APIResponse
from .models import Response
from .serializers import ResponseSerializer

class ResponseListCreateView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    def post(self, request, *args, **kwargs):
        prompt = request.data.get("prompt")
        model_used = request.data.get("model_used", "gpt-3.5-turbo")

        if not prompt:
            return APIResponse({"error": "Prompt is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Load the OpenAI API key securely
        api_key = os.getenv("OPENAI_API_KEY")
        print(api_key)
        if not api_key:
            return APIResponse({"error": "Missing OpenAI API key."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            start_time = time.time()
            openai.api_key = api_key

            # Call the OpenAI GPT Model API
            response = openai.ChatCompletion.create(
                model=model_used,
                messages=[{"role": "user", "content": prompt}]
            )
            response_text = response['choices'][0]['message']['content']
            processing_time = round(time.time() - start_time, 2)

            # Save the response to the database
            response_instance = Response.objects.create(
                prompt=prompt,
                response_text=response_text,
                model_used=model_used,
                status="completed",
                processing_time=processing_time
            )
            serializer = self.get_serializer(response_instance)
            return APIResponse(serializer.data, status=status.HTTP_201_CREATED)

        except openai.error.AuthenticationError:
            return APIResponse({"error": "Invalid OpenAI API key."}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return APIResponse({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResponseDetailView(generics.RetrieveAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
