from rest_framework import serializers
from .models import TaskMaster

class TaskMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMaster
        fields = "__all__"