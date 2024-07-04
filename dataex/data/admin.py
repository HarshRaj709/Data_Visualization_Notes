from django.contrib import admin
from .models import Languages,Username

# Register your models here.
@admin.register(Languages)
class AdminLanguages(admin.ModelAdmin):
    list_display = [field.name for field in Languages._meta.fields]

@admin.register(Username)
class AdminUsername(admin.ModelAdmin):
    list_display = [field.name for field in Username._meta.fields]