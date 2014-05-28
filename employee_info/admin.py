from employee_info.models import EmployeeInfo
from django.contrib import admin

# Register your models here.

from .models import EmployeeInfo

class EmployeeInfoAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeInfo
        
    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change): 
        if formset.model == EmployeeInfo:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()
        
admin.site.register(EmployeeInfo, EmployeeInfoAdmin)

