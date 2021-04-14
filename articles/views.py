from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
# view는 중간 관리자, urls.py의 요청에 맞게 해당 view를 실행시키면 여기에서 DB등을 처리하고 최종적으로 사용자에게 무언가를 보여준다.
def index(request): # 첫 번째 request
    return render(request, "index.html") # render의 첫번째 인자도 반드시 request 여야함, 2 번째는 templates 위치, 3 번째는 데이터를 담아 보내는데 이건 나중에 다룬다 언급

def introduce(request):
    return render(request, "introduce.html")

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Woong'
    }
    context = {
        'foods': foods,
        'info': info,
    } # django 공식 문서에서 권장하는 대로 context를 사용(다른걸 사용해도 동작은 함)
    return render(request, "greeting.html", context)

def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'pick':pick,
    } # django 공식 문서에서 권장하는 대로 context를 사용한다는 것 다시 한번 강조
    return render(request, 'dinner.html', context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now() # 오늘에 대한 날짜/시각 정보
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)