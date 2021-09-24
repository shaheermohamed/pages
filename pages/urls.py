from django.urls import path
from .views import HomePageView,Contactpageview

urlpatterns = [
    path('home/', HomePageView.as_view(), name='Home'),
    path('about/',Contactpageview.as_view(), name='about'),
]
