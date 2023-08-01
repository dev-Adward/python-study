from django.shortcuts import render
from main.models import Member
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MemberSerializer
from django.core.paginator import Paginator
import openai


#  OpenAI의 ChatGPT API 사용 카드 등록 안해서 안됨
# # 발급받은 API 키 설정
# OPENAI_API_KEY = "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"
# # openai API 키 인증
# openai.api_key = OPENAI_API_KEY
# model = "gpt-3.5-turbo"
# messages = []
#
# competition = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=messages,
# )
#
# chat_response = competition.choices[0].message.content
# print(chat_response)




class MemberAPI(APIView):
    def post(self, request):
        queryset = Member.objects.all()

        # 장고에서 특정 데이터를 조회하는 메소드 사용
        querysetFilter = Member.objects.filter(id=1)
        # 장고가 가져온 객체의 특정 프로퍼티를 가져오는 방법
        print(querysetFilter.values('name'))
        print(querysetFilter.values_list('name'))
        # ajax로 데이터를 보냈을때 장고에서 데이터를 받는 방법
        # 메서드를 POST로 설정해놓으면 함수이름이 POST여도 request.POST로 받아야만한다.
        page = request.POST.get('page')
        print(page, "페이지")
        count = queryset.count()  # queryset의 개수를 구함
        serializer = MemberSerializer(queryset, many=True)
        response_data = {
            'count': count,
            'data': serializer.data,
            # 'chat': chat_response,
        }
        return Response(response_data)

def goRest(request):
    return render(request, "rest.html")