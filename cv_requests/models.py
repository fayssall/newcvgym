from django.db import models
import uuid

class CVRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=50)  # E.g., 'Internship', 'Graduate', 'Job Improvement'
    email = models.EmailField()  # To send the CV to the user
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
