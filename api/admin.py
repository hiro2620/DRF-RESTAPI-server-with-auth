from django.contrib import admin
from .models import Schedule

# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    model = Schedule
    list_display = ['owner', 'id', 'date', 'time', 'content', 'created_at', 'updated_at', 'is_done']