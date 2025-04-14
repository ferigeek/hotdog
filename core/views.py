from django.shortcuts import render
from rest_framework import generics
from .models import Course, FieldOfStudy
from .serializers import CourseSerializer, FieldOfStudySerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class FieldOfStudyListView(generics.ListAPIView):
    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer