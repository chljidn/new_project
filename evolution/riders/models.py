from django.db import models
from authentication.models import User

class rider(models.Model):
    rider_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, db_column="user")
    # address