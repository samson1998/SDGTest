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



  outputData['impact']['infectionsByRequestedTime'] = round(outputData['impact']['currentlyInfected'] * (2 ** (data['timeToElapse']/3)), 2)
  outputData['severeImpact']['infectionsByRequestedTime'] = round(outputData['severeImpact']['currentlyInfected'] * (2 ** (data['timeToElapse']/3)), 2)
  outputData['impact']['severeCasesByRequestedTime'] = round(outputData['impact']['infectionsByRequestedTime'] * (15/100), 2)
  outputData['severeImpact']['severeCasesByRequestedTime'] = round(outputData['impact']['infectionsByRequestedTime'] * (15/100), 2)
  outputData['impact']['hospitalBedsByRequestedTime'] = outputData['data']['totalHospitalBeds'] - outputData['impact']['severeCasesByRequestedTime'] 
  outputData['severeImpact']['hospitalBedsByRequestedTime'] = outputData['data']['totalHospitalBeds'] - outputData['severeImpact']['severeCasesByRequestedTime']
  outputData['impact']['casesForICUByRequestedTime'] = round(outputData['impact']['infectionsByRequestedTime'] * (5/100), 2)
  outputData['severeImpact']['casesForICUByRequestedTime'] = round(outputData['severeImpact']['infectionsByRequestedTime'] * (5/100), 2)
  outputData['impact']['casesForVentilatorsByRequestedTime'] = round(outputData['impact']['infectionsByRequestedTime'] * (2/100), 2)
  outputData['severeImpact']['casesForVentilatorsByRequestedTime'] = round(outputData['severeImpact']['infectionsByRequestedTime'] * (2/100), 2)


  return outputData


estimator(data)