from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('displayForm/', views.displayForm, name="disp_form"),
    path('ins_data/', views.ins_data, name="ins_data"),
    path('details/', views.show_data, name="show_details"),
    path('operations/', views.perform_operations, name="operations"),
    path('update/', views.update_record, name="update"),
]
