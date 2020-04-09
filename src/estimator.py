# def convertToDays(period_type, timeToElapse):
#   if period_type == 'days':
#     return timeToElapse

#   elif period_type == 'weeks':
#     return timeToElapse * 7

#   elif period_type == 'months':
#     return timeToElapse * 30

#   else:
#     return timeToElapse



# # data = {
# # 'region': {
# #     'name': "Africa",
# #     'avgAge': 19.7,
# #     'avgDailyIncomeInUSD': 5,
# #     'avgDailyIncomePopulation': 0.71
# #     },
# #   'periodType': "days",
# #   'timeToElapse': 58,
# #   'reportedCases': 674,
# #   'population': 66622705,
# #   'totalHospitalBeds': 1380614
# # }

# def estimator(data):
  
#   data['timeToElapse'] = convertToDays(data['periodType'], data['timeToElapse'])

#   outputData = {
#     'data': data,
#     'impact' : {
#       'currentlyInfected' : data['reportedCases'] * 10,
#     },

#     'severeImpact' : {
#       'currentlyInfected' : data['reportedCases'] * 50,
#     }

#   }


#   days = 2 ** int((data['timeToElapse']/3))
#   beds = int(outputData['data']['totalHospitalBeds'] * 0.35)
#   outputData['impact']['infectionsByRequestedTime'] = outputData['impact']['currentlyInfected'] * days
#   outputData['severeImpact']['infectionsByRequestedTime'] = outputData['severeImpact']['currentlyInfected'] * days
#   outputData['impact']['severeCasesByRequestedTime'] = outputData['impact']['infectionsByRequestedTime'] * 0.15
#   outputData['severeImpact']['severeCasesByRequestedTime'] = outputData['severeImpact']['infectionsByRequestedTime'] * 0.15
#   outputData['impact']['hospitalBedsByRequestedTime'] =  beds - outputData['impact']['severeCasesByRequestedTime']
#   outputData['severeImpact']['hospitalBedsByRequestedTime'] = beds - outputData['severeImpact']['severeCasesByRequestedTime']
#   outputData['impact']['casesForICUByRequestedTime'] = int(round(outputData['impact']['infectionsByRequestedTime'] * (5/100), 2))
#   outputData['severeImpact']['casesForICUByRequestedTime'] = int(round(outputData['severeImpact']['infectionsByRequestedTime'] * (5/100), 2))
#   outputData['impact']['casesForVentilatorsByRequestedTime'] = int(round(outputData['impact']['infectionsByRequestedTime'] * (2/100), 2))
#   outputData['severeImpact']['casesForVentilatorsByRequestedTime'] = int(round(outputData['severeImpact']['infectionsByRequestedTime'] * (2/100), 2))
#   outputData['impact']['dollarsInFlight'] = int((outputData['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])
#   outputData['severeImpact']['dollarsInFlight'] = int((outputData['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])
    

#   return outputData


# # print(estimator(data))

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
    return round(inf * income_population * income * days, 2)



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

#test
tt = {
    "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 4,
        "avgDailyIncomePopulation": 0.73
    },
    "periodType": "days",
    "timeToElapse": 38,
    "reportedCases": 2747,
    "population": 92931687,
    "totalHospitalBeds": 678874
}

print(estimator(tt))