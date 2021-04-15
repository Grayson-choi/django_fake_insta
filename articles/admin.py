from django.contrib import admin
from .models import Article # 명시적 상대경로 표현 / model 경로도 동작하지만 이렇게 불러오는게 관용적

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at',) # 관리자 사이트에서 해당 컬럼의 내용을 정렬해서 보여준다.

# Register your models here.
admin.site.register(Article, ArticleAdmin) # admin site에 register(등록-Article 모델)합니다. 처럼 문장으로 외울 수 있도록 설명