def convertToDays(period_type, timeToElapse):
  if period_type == 'days':
    return timeToElapse

  elif period_type == 'weeks':
    return timeToElapse * 7

  elif period_type == 'months':
    return timeToElapse * 30

  else:
    return 'Incorrect input'



# data = {
# 'region': {
#     'name': "Africa",
#     'avgAge': 19.7,
#     'avgDailyIncomeInUSD': 5,
#     'avgDailyIncomePopulation': 0.71
#     },
#   'periodType': "days",
#   'timeToElapse': 58,
#   'reportedCases': 674,
#   'population': 66622705,
#   'totalHospitalBeds': 1380614
# }

def estimator(data):
  
  data['timeToElapse'] = convertToDays(data['periodType'], data['timeToElapse'])

  outputData = {
    'data': data,
    'impact' : {
      'currentlyInfected' : data['reportedCases'] * 10,
    },

    'severeImpact' : {
      'currentlyInfected' : data['reportedCases'] * 50,
    }

  }



  outputData['impact']['infectionsByRequestedTime'] = outputData['impact']['currentlyInfected'] * int((2 ** (data['timeToElapse']/3)))
  outputData['severeImpact']['infectionsByRequestedTime'] = outputData['severeImpact']['currentlyInfected'] * int((2 ** (data['timeToElapse']/3)))
  outputData['impact']['severeCasesByRequestedTime'] = round(outputData['impact']['infectionsByRequestedTime'] * (15/100), 2)
  outputData['severeImpact']['severeCasesByRequestedTime'] = round(outputData['severeImpact']['infectionsByRequestedTime'] * (15/100), 2)
  outputData['impact']['hospitalBedsByRequestedTime'] = int((outputData['data']['totalHospitalBeds'] * 0.35) - outputData['impact']['severeCasesByRequestedTime'])
  outputData['severeImpact']['hospitalBedsByRequestedTime'] = int((outputData['data']['totalHospitalBeds'] * 0.35) - outputData['severeImpact']['severeCasesByRequestedTime'])
  outputData['impact']['casesForICUByRequestedTime'] = int(round(outputData['impact']['infectionsByRequestedTime'] * (5/100), 2))
  outputData['severeImpact']['casesForICUByRequestedTime'] = int(round(outputData['severeImpact']['infectionsByRequestedTime'] * (5/100), 2))
  outputData['impact']['casesForVentilatorsByRequestedTime'] = int(round(outputData['impact']['infectionsByRequestedTime'] * (2/100), 2))
  outputData['severeImpact']['casesForVentilatorsByRequestedTime'] = int(round(outputData['severeImpact']['infectionsByRequestedTime'] * (2/100), 2))
  outputData['impact']['dollarsInFlight'] = int((outputData['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])
  outputData['severeImpact']['dollarsInFlight'] = int((outputData['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])
    

  return outputData


# print(estimator(data))