from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CVRequest
from .utils import generate_cv  # Assuming there's a utility function for CV generation
from django.http import FileResponse, HttpResponse
from django.conf import settings
from django.views.generic import TemplateView
import os


def home(request):
    return render(request, 'index.html')





class CVDownloadAPIView(APIView):
    def get(self, request, cv_request_id, *args, **kwargs):
        # Retrieve the CVRequest object based on the provided id
        cv_request = get_object_or_404(CVRequest, id=cv_request_id)
        
        # Construct the file path using the id
        cv_filename = f"CV_{cv_request_id}.txt"
        cv_filepath = os.path.join(settings.MEDIA_ROOT, cv_filename)

        # Check if the file exists
        if not os.path.exists(cv_filepath):
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)

        # Open the file and send it as a response
        response = FileResponse(open(cv_filepath, 'rb'))
        return response


class CVRequestAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract the necessary data from the request
        category = request.data.get('category')
        email = request.data.get('email')
        full_name = request.data.get('full_name')
        phone_number = request.data.get('phone_number')
        address = request.data.get('address')
        education_history = request.data.get('education_history')
        work_experience = request.data.get('work_experience')
        skills = request.data.get('skills')
        certifications = request.data.get('certifications')
        languages = request.data.get('languages')

        # Check if category is one of the allowed options
        if category not in ['Internship', 'Graduate', 'Job Improvement']:
            return Response(
                {"error": "Invalid category provided."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new CVRequest object with the received data
        cv_request = CVRequest.objects.create(
            category=category,
            email=email,
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            education_history=education_history,
            work_experience=work_experience,
            skills=skills,
            certifications=certifications,
            languages=languages
        )

        # Call the CV generation function
        generated_cv = generate_cv(cv_request.id)  # This function should handle CV generation

        # Assuming the function returns the generated CV's file path or similar identifier
        return Response({
            'request_id': cv_request.id,
            'generated_cv': generated_cv
        }, status=status.HTTP_201_CREATED)

# Create your views here.
