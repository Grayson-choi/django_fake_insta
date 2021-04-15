from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index) # 빈스트링을 넣게되면 프로젝트의 urls의 articles가 index페이지로 간다.
]
