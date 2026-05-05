from django.shortcuts import render
from .models import tecnologies
from  rest_framework import viewsets
from .serializer import tecnologiesSerializer

class ProjectListViewSet(viewsets.ModelViewSet):
    queryset = tecnologies.objects.all()
    serializer_class = tecnologiesSerializer
