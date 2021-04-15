from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index), # 아무것도 안 넣으면 127.0.0.1:8000/pages/ 를 의미한다. 
    path('introduce/', views.introduce, name='introduce'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('template_language/', views.template_language, name='template_language'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
