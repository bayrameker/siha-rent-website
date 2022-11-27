from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexPage,name='index_page'),
    path('about/',views.AboutPage,name='about_page')
]
