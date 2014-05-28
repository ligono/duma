from django.db import models

#from django.utils.encoding import smart_unicode
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.

class EmployerInfo(models.Model):
    company_name = models.CharField(max_length=256, null=False, blank=False)
    address = models.CharField(max_length=256, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    head_office = models.CharField(max_length=256, null=False, blank=False)
    attached_user = models.ForeignKey(User)
    description = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(700)])
        
    def __str__(self):
        return self.company_name
    