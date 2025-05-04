from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.list_of_ads, name='list_of_ads'),    
    path('<int:id>/', views.ads_detail, name='detail'),
]