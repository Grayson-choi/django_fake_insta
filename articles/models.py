from django.db import models

# Create your models here.
class Article(models.Model): # 상속
    # id(프라이머리 키)는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10) # CharField는 max_length 인자가 필수다. -> 클래스 변수(DB의 필드이다.)
    content = models.TextField() # 클래스 변수 (DB의 필드이다.)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
