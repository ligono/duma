from django.db import models

#from django.utils.encoding import smart_unicode
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from jobCategories import models as jobcat_models
from model_utils.models import StatusModel
from model_utils.managers import QueryManager
from model_utils import Choices
from django.core.mail import send_mail

# Create your models here.

class Job(models.Model):
    job_title = models.CharField(max_length=256, null=False, blank=False)
    job_description = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(2000)])
    key_requirements = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(512)])
    key_responsibilities = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(512)])
    qualifications = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(512)])
    location = models.CharField(max_length=256, null=False, blank=False)
    category = models.ForeignKey(jobcat_models.JobCategory)
    company = models.ForeignKey(User)
    terms = models.CharField(max_length=256, null=True, blank=True)
        
    def __str__(self):
        return self.job_title
    
class InterestedJob(StatusModel):
    STATUS = Choices('yes', 'no')
    job = models.ForeignKey(Job)
    user = models.ForeignKey(User)
    
    objects = models.Manager()
    public = QueryManager(STATUS=True).order_by('status_changed')
    #InterestedJob.objects.get(STATUS__iexact='yes')
    #def __str__(self):
    #    return self.job
    
a = InterestedJob()
a.status = InterestedJob.STATUS.yes

a.save

InterestedJob.yes.all()

#class Report()
    
    

    
    
    
    

