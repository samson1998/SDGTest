from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from simplexml import dumps
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.reverse import reverse



# Create your views here.



def estimator(data):

  periodtype = data['periodType']
  time_to_elapse = data['timeToElapse']
  reported_cases = data['reportedCases']
  hospital_beds = data['totalHospitalBeds']
  income = data['region']['avgDailyIncomeInUSD']
  income_population = data['region']['avgDailyIncomePopulation']

  impact_cases = reported_cases * 10
  severe_cases = reported_cases * 50
  available_beds = 0.35 * hospital_beds


  #calculate the number of days
  def number_of_days(periodtype, time_to_elapse):
    if periodtype == 'days':
      days = time_to_elapse
    elif periodtype == 'weeks':
      days = time_to_elapse * 7
    elif periodtype == 'months':
      days = time_to_elapse * 30
    return days

  #infections by requested time, where case = currentlyInfected
  def infected_till_date(case):
    days = number_of_days(periodtype, time_to_elapse) // 3
    return case * (2 ** days)

  def severe_by_req_time(case):
    return 0.15 * infected_till_date(case)

  def hospital_bedsby_time(case):
    return int(available_beds - severe_by_req_time(case))

  def money_lost(case):
    inf = infected_till_date(case)
    days = number_of_days(periodtype, time_to_elapse)
    return int((inf * income_population * income) / days)
    # return round(inf * income_population * income * days, 2)



  result = {
    "data":data,
    "impact": {
      "currentlyInfected": impact_cases,
      "infectionsByRequestedTime": infected_till_date(impact_cases),
      "severeCasesByRequestedTime": int(severe_by_req_time(impact_cases)),
      "hospitalBedsByRequestedTime": hospital_bedsby_time(impact_cases),
      "casesForICUByRequestedTime": int(0.05 * infected_till_date(impact_cases)),
      "casesForVentilatorsByRequestedTime":int(0.02 * infected_till_date(impact_cases)),
      "dollarsInFlight": money_lost(impact_cases)
    },
    "severeImpact": {
      "currentlyInfected": severe_cases,
      "infectionsByRequestedTime": infected_till_date(severe_cases),
      "severeCasesByRequestedTime": int(severe_by_req_time(severe_cases)),
      "hospitalBedsByRequestedTime": hospital_bedsby_time(severe_cases),
      "casesForICUByRequestedTime": int(0.05 * infected_till_date(severe_cases)),
      "casesForVentilatorsByRequestedTime": int(0.02 * infected_till_date(severe_cases)),
      "dollarsInFlight": money_lost(severe_cases)
    }
  }

  return result

class API_Root(APIView):
    ''' List of all endpoints'''
    def get(self,request, format=None):
        return Response({
            'on-covid-19':reverse('Covid-19 Estimator',request=request, format=format),
            'json':reverse('Covid-19 Estimator JSON', request=request, format=format),
            'xml':reverse('Covid-19 Estimator XML', request=request, format=format),
            
        })


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
    def post(self, request, format=None):
        data = json.dumps(request.data)
        datas = json.loads(data)
        res = dumps({'response': estimator(datas)})
        return Response(res)


     


    
   


    

     
    
