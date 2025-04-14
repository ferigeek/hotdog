from django.urls import path, include
from .views import CourseListView, FieldOfStudyListView


urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('fields-of-study/', FieldOfStudyListView.as_view(), name='field-of-study-list'),
]