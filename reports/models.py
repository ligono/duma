from django.db import models

from model_utils.managers import QueryManager
from jobs.models import Job
from employee_info.models import EmployeeInfo
from jobs.models import InterestedJob
from django.core.mail import send_mail

# Create your models here.

class ReportLab(models.Model):
    
    InterestedJob.objects
    #<django.db.models.manager.Manager object at ...>
    InterestedJob.objects.filter(status__iexact = 'yes')


