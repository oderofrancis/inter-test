from email import message
from multiprocessing import context
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import MessageSerializer

# Create your views here.

class MessageView(APIView):
    def get(self,request):
        message = Message.objects.all()

        serializer = MessageSerializer(message,many=True)

        context = {
            "message":serializer.data
        }
        return Response(context)

def post(self, request):
    message = request.data.get('message')

    # create message from the above data

    serializer = MessageSerializer(data=message)
    if serializer.is_valid(raise_exception=True):
        message_saved = serializer.save()
    return Response({"Succes": "Message '{}' created successfully ".format(message)})