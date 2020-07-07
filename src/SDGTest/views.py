from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from simplexml import dumps
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.reverse import reverse
from .estimator import *
from django.db import connection
from rest_framework_tracking.models import APIRequestLog
from .Renderer import PlainTextRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_xml.renderers import XMLRenderer



# Create your views here.


class API_Root(APIView):
    ''' List of all endpoints'''
    def get(self,request, format=None):
        # read_to_file()
        return Response({
            'on-covid-19':reverse('Covid-19 Estimator',request=request, format=format),
            'json':reverse('Covid-19 Estimator JSON', request=request, format=format),
            'xml':reverse('Covid-19 Estimator XML', request=request, format=format),
            
        })
# def load_and_dump_json(request.data){
#     data = json.dumps(request.data)
#     d
# }      

class EstimateView(LoggingMixin,APIView):
    def post(self, request, format=None):
        data = json.dumps(request.data)
        datas = json.loads(data)
        return Response(estimator(datas))

    
class EstimateViewJSON(LoggingMixin, APIView):
    def post(self, request, format=None):
        data = json.dumps(request.data)
        datas = json.loads(data)
        return Response(estimator(datas))

class EstimateViewXML(LoggingMixin, APIView):
    renderer_classes = [XMLRenderer]

    def post(self, request, format=None):
        data = json.dumps(request.data)
        datas = json.loads(data)
        return Response(estimator(datas))

# class EstimateViewXML(LoggingMixin, APIView):
#     def post(self, request, format=None):
#         data = json.dumps(request.data)
#         datas = json.loads(data)
#         res = dumps({'response': estimator(datas)})
#         return Response(res)

# https://docs.google.com/forms/d/e/1FAIpQLSeO48xMfAcdQZRRQVhlBzyRbeXah3hkkbsfIaScYgIDfapkqQ/viewanalytics

# class APILogs(APIView):
#   renderer_classes = [PlainTextRenderer]
#   def get(self, request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT method, path, status_code, response_ms FROM rest_framework_tracking_apirequestlog")
#         row = cursor.fetchall()
#         f = open('log.txt', 'w')
#         for i in row:
#           z = "{} \t\t {} \t\t  {} \t\t {}ms \n".format(i[0], i[1], i[2], i[3])
#           f.write(z)
#         f.close()

#     f = open('log.txt', 'r')
#     test_string = [i.strip() for i in f]
#     test_strings = [i.replace('\t', '') for i in test_string]
    
#     return Response(str(test_strings))

class APILogs(LoggingMixin, APIView):
    renderer_classes = [PlainTextRenderer]

    def get(self, request, format=None):
        logs = [f"{log.method}\t\t{log.path}\t\t{log.status_code}\t\t{int(str(log.response_ms)[0:2])}ms\n" for log in APIRequestLog.objects.all()]
        logs = ''.join(logs)
        return Response(logs)


