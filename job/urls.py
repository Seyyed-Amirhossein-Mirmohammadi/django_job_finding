from django.urls import path

from . import views


urlpatterns = [
    path('', views.choose, name = "choose"),
    path('form/', views.form, name = "form"),
    path('jobs/', views.result, name = "result" )
]