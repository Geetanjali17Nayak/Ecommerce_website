from django.db import models
import uuid # unique identification no. act as a primary key



class basemodel(models.Model):
    uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at= models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:  # this create meta information and abstract class helps in inheritance
        abstract=True
