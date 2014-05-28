from django.db import models

#from django.utils.encoding import smart_unicode
from django.core.validators import MaxLengthValidator

# Create your models here.
class JobCategory(models.Model):
    category_name = models.CharField(max_length=256, null=False, blank=False)
    cat_description = models.TextField(validators=[MaxLengthValidator(512)])
    
    def __str__(self):
        return self.category_name
