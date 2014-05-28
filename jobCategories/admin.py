from django.contrib import admin

# Register your models here.
from .models import JobCategory

class JobCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = JobCategory
        
admin.site.register(JobCategory, JobCategoryAdmin)
