from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('displayForm/', views.displayForm, name="disp_form"),
    path('ins_data/', views.ins_data, name="ins_data"),
    path('Details/', views.show_data, name="show_details"),
    path('operations/', views.perform_operations, name="operations"),

]
