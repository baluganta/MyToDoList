from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class CreateView(generics.CreateAPIView):   #Create
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateView(generics.UpdateAPIView):   #Update
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class ListView(generics.ListAPIView):   #Read
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteView(generics.DestroyAPIView):  #Delete
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DetailView(generics.RetrieveAPIView): #Details
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


