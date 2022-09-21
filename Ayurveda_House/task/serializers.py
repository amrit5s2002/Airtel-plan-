from rest_framework.serializers import ModelSerializer
from .models import *

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'