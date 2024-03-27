from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from django.contrib.auth.models import User


 

# class AccountAPIView(APIView):
#     def get(self, request):
#         accounts_mobile_phones = UserAccount.objects.all().values('mobile_phone')
#         return Response (list(accounts_mobile_phones))
    
#     def post(self, request):
#         print(request.data)
#         return Response('test')

