from django.shortcuts import render

# Create your views here.
# view는 중간 관리자, urls.py의 요청에 맞게 해당 view를 실행시키면 여기에서 DB등을 처리하고 최종적으로 사용자에게 무언가를 보여준다.
def index(request): # 첫 번째 request
    return render(request, "index.html") # render의 첫번째 인자도 반드시 request 여야함, 2 번째는 templates 위치, 3 번째는 데이터를 담아 보내는데 이건 나중에 다룬다 언급