from . import views
from django.urls import path




urlpatterns = [

    # path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects')
    ]
