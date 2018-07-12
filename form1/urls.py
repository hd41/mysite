from django.urls import path

from . import views

urlpatterns = [
    # ex: /form/
    path('', views.index, name='index'),
    # ex: /form/formq
    path('formq/', views.get_name, name='form'),
    path('thanks/', views.thanks, name='thanks'),
]
