from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="assessment"),
    path("result/", views.result, name="result"),
    path("result/?uuid=<uuid>/", views.result, name="result"),
    path("delete/", views.delete_assessment, name="delete_assessment"),
    path('delete/?uuid=<uuid>/', views.delete_assessment, name='delete_assessment'),
]
