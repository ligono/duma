from jobs.models import Job
from django.contrib import admin

# Register your models here.

from .models import Job

class JobAdmin(admin.ModelAdmin):
    class Meta:
        model = Job
        
    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change): 
        if formset.model == Job:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()
        
admin.site.register(Job, JobAdmin)

from .models import InterestedJob

class InterestedJobAdmin(admin.ModelAdmin):
    class Meta:
        model = InterestedJob
        
    
admin.site.register(InterestedJob, InterestedJobAdmin)
