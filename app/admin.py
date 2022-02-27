from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class authorize(admin.ModelAdmin):
    labels=('name','element','conselation','havetodo','completed')