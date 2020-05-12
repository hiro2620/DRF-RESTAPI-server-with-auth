import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

class Schedule(models.Model):

    class Meta:
        db_table   = 'schedule'
        ordering   = ['-date', 'time']

    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date       = models.DateField(verbose_name='date')
    time       = models.TimeField(verbose_name='time')
    content    = models.TextField(verbose_name='content')
    is_done    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner      = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + str(self.content)
