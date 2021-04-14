"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views # 생성한 앱 articles 폴더 안의 views.py 파일
# urls.py는 집배원 -> 127.0.0.1:8000/articles/로 접속하면, views.py의 index 함수가 실행됨

urlpatterns = [
    path('index/', views.index), #
    path('admin/', admin.site.urls),
]
