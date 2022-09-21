from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import*
from rest_framework.response import Response
from .data import Data
# # Create your views here.
@api_view(['GET'])
def getPlans(request):
    data = Data()
    print(data)
    for d in data :
        new_plan = Plans.objects.create(plans = d)
    plans = Plans.objects.all()
    print(new_plan)
    print(plans)
    serializer = PlanSerializer(plans,many = True)
    return Response(serializer.data)