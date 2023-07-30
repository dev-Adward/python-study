from django.shortcuts import render
from main.models import Member
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MemberSerializer

class MemberAPI(APIView):
    def post(self, request):
        queryset = Member.objects.all()
        print(queryset)
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)