from django.db import models
from django.contrib.auth.models import User

class Sekolah(models.Model):
    npsn = models.CharField(max_length=30)
    name_school = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    logo_school = models.CharField(max_length=2000)
    school_level = models.CharField(max_length=60)
    status_school = models.CharField(max_length=60)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name_school





