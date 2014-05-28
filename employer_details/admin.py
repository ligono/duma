from employer_details.models import EmployerInfo
from django.contrib import admin

# Register your models here.

from .models import EmployerInfo

class EmployerInfoAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployerInfo
        
    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change): 
        if formset.model == Employer:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()
            
admin.site.register(EmployerInfo, EmployerInfoAdmin)
