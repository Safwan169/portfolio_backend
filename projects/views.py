# from django.shortcuts import render
from .serializers import ProjectSerializer
from projects.models import Project
from rest_framework import viewsets

class ProjectListViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

