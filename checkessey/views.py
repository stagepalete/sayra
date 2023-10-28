from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import openai

# Create your views here.
class CheckEssey(APIView):
    def post(self, request):
        openai.api_key = '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'
        user_input_text = request.data.get('user_input_text', '')

        # Define messages for the OpenAI API
        messages = []
        system_msg = 'Imagine that you are a writing IELTS examiner. Candidate\'s writing is in triple asterisks (e.g. ***text***).'
        messages.append({"role": "system", "content": system_msg})
        messages.append({"role": "user", "content": user_input_text})

        # Call the OpenAI API to get the response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )

        # Extract the reply from the API response
        reply = response["choices"][0]["message"]["content"]

        # Add triple asterisks to the reply
        reply = f"{reply}"

        # Prepare the response to send back to the user
        response_data = {"response": reply}
        return Response(response_data, status=status.HTTP_200_OK)
