from django.db import models

#from django.utils.encoding import smart_unicode
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from jobCategories import models as jobcat_models

# Create your models here.

class Cvitae(models.Model):
    cv_title = models.CharField(max_length=256, null=False, blank=False)  
    address = models.CharField(max_length=256, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    education_one = models.CharField(max_length=512, null=False, blank=False)
    education_two = models.CharField(max_length=512, null=False, blank=False)
    education_three = models.CharField(max_length=512, null=True, blank=True)
    education_four = models.CharField(max_length=512, null=True, blank=True)
    experience = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(1000)])
    skills = models.ManyToManyField(jobcat_models.JobCategory)
    full_name = models.ForeignKey(User)
    
    def __str__(self):
        return self.cv_title
    
