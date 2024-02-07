import os
from django.conf import settings
from .models import CVRequest

def generate_cv(cv_request_id):
    cv_request = get_object_or_404(CVRequest, id=cv_request_id)

    # Define the filename for the CV using the request ID to ensure uniqueness
    cv_filename = f"CV_{cv_request_id}.txt"
    cv_filepath = os.path.join(settings.MEDIA_ROOT, cv_filename)

    # Generate the CV content
    cv_content = [
        f"Full Name: {cv_request.full_name}",
        f"Email: {cv_request.email}",
        f"Phone Number: {cv_request.phone_number}",
        f"Address: {cv_request.address}",
        f"Education History: {cv_request.education_history}",
        f"Work Experience: {cv_request.work_experience}",
        f"Skills: {cv_request.skills}",
        f"Certifications: {cv_request.certifications}",
        f"Languages: {cv_request.languages}",
    ]
    cv_text = "\n".join(cv_content)

    # Write the CV content to a text file
    with open(cv_filepath, 'w') as cv_file:
        cv_file.write(cv_text)

    # Return the path to the generated CV file
    return cv_filepath
