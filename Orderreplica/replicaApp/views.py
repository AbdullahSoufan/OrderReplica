import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class bookList(APIView) :
    def put(self, request, id):
        books_with_specific_topic = requests.get('http://127.0.0.1:8003/info/'+str(id)+'/', params=request.GET, timeout=5)
        data = books_with_specific_topic.text

        jsondata = json.loads(data)

        quantity = jsondata[0]['quantity']
        if quantity > 0:
            requests.put('http://127.0.0.1:8003/decrease/' + str(id) + '/', timeout=5)
            return HttpResponse('The book has been purchased successfully')
        else:
            return HttpResponse('There are no books left')
