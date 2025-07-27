from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Candidate', 'Candidate'),
        ('Employer', 'Employer'),
    ]


    phone = models.CharField(max_length=15, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default='Candidate', null=True)

    def __str__(self):
        return self.username

class PendingAccount(models.Model):
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Candidate', 'Candidate'),
        ('Employer', 'Employer'),
    ]
    PENDING_STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    username = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE, null=True)

    painted_status = models.CharField(max_length=10, choices=PENDING_STATUS, null=True)

    def __str__(self):
        return self.username