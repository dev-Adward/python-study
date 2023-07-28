from django.shortcuts import render
from . import models
import json


# 장고가 url을 연결하는 방식, 컨트롤러와 매우 유사함
def main(request):
    
    jsonArray = []
    member = models.Member.objects.get(pk=1)
    member_json = json.dumps(member.to_json())
    # json.dumps(member.to_json)
    
    # for element in models.Member.objects.all():
    #     print(element)
        # jsonObject = json.dumps(element)
        # jsonArray.append(jsonObject)
    
    # 요청이 들어오면 templates안에 main안에 main.html파일을 선택하겠다.
    return render(request, "main/main.html", {"member":member_json})

