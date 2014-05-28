from django.contrib import admin

# Register your models here.

from .models import ReportLab

class ReportLabAdmin(admin.ModelAdmin):
    class Meta:
        model = ReportLab
        
admin.site.register(ReportLab, ReportLabAdmin)

