from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer): 

    class Meta:

        model = Schedule
        fields = '__all__'
        extra_kwargs = {
            'created_at': {
                'read_only': True
            },
            'updated_at': {
                'read_only': True
            },
            'owner': {
                'write_only': True
            },
        }