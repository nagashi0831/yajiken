from django.urls import path
from . import views

app_name = 'yajisanpo' #アプリ名
urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
]
