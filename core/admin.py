from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin): 
    #ImportExportModelAdmin allows for importation of external csv file to populate db within model structure
    pass