from django.db.models import Count
from django.shortcuts import render
from randomapp.models import UserData
from randomapp.serializer import UserDataSerializer
from rest_framework import generics 
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def index(request):
    users = UserData.objects.values('worker_id').annotate(num_values=Count('first_name')).order_by('-num_values')
    data_dict = {'user_list': get_work}
    return render(request, 'index.html', context=data_dict)

class UserDataListCreate(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
