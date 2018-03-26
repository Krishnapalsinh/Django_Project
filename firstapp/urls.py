from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('displayForm/', views.displayForm, name="disp_form"),
    path('Details/', views.showDetails, name="form_details"),
]
