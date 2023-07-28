from django.shortcuts import render


# 장고가 url을 연결하는 방식
def main(request):
    print(request)  
    # 요청이 들어오면 templates안에 main안에 main.html파일을 선택하겠다.
    return render(request, "main/main.html")
