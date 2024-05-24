from django.contrib import admin

# Register your models here.
from . models import employer_registration
from . models import employee_registration
from . models import job
from . models import acknowledgement


class employeradmin(admin.ModelAdmin):
    list_display = ('username','phone','age','gender','location','email','image','password')

class employeeadmin(admin.ModelAdmin):
    list_display = ('workername','phone','age','gender','occupation','location','email','image','password')

class jobadmin(admin.ModelAdmin):
    list_display = ('username','workername','job_description','job_location','job_date','job_review')

class acknowledgementadmin(admin.ModelAdmin):
    list_display = ('username','workername','wphone','ackmesg')

admin.site.register(employer_registration, employeradmin)

admin.site.register(employee_registration, employeeadmin)

admin.site.register(job, jobadmin)

admin.site.register(acknowledgement, acknowledgementadmin)

