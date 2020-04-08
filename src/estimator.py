def convertToDays(period_type, timeToElapse):
  if period_type == 'days':
    return timeToElapse

  elif period_type == 'weeks':
    return timeToElapse * 7

  elif period_type == 'months':
    return timeToElapse * 30

  else:
    return 'Incorrect input'



inputData = {
'region': {
    'name': "Africa",
    'avgAge': 19.7,
    'avgDailyIncomeInUSD': 5,
    'avgDailyIncomePopulation': 0.71
    },
  'periodType': "days",
  'timeToElapse': 58,
  'reportedCases': 674,
  'population': 66622705,
  'totalHospitalBeds': 1380614
}

inputData['timeToElapse'] = convertToDays(inputData['periodType'], inputData['timeToElapse'])

data = {
    'data': inputData,
    'impact' : {
      'currentlyInfected' : inputData['reportedCases'] * 10,
    },

    'severeImpact' : {
      'currentlyInfected' : inputData['reportedCases'] * 50,
    }

  }



data['impact']['infectionsByRequestedTime'] = round(data['impact']['currentlyInfected'] * (2 ** (inputData['timeToElapse']/3)), 2)
data['severeImpact']['infectionsByRequestedTime'] = round(data['severeImpact']['currentlyInfected'] * (2 ** (inputData['timeToElapse']/3)), 2)
data['impact']['severeCasesByRequestedTime'] = round(data['impact']['infectionsByRequestedTime'] * (15/100), 2)
data['severeImpact']['severeCasesByRequestedTime'] = round(data['impact']['infectionsByRequestedTime'] * (15/100), 2)
data['impact']['hospitalBedsByRequestedTime'] = data['data']['totalHospitalBeds'] - data['impact']['severeCasesByRequestedTime'] 
data['severeImpact']['hospitalBedsByRequestedTime'] = data['data']['totalHospitalBeds'] - data['severeImpact']['severeCasesByRequestedTime']
data['impact']['casesForICUByRequestedTime'] = round(data['impact']['infectionsByRequestedTime'] * (5/100), 2)
data['severeImpact']['casesForICUByRequestedTime'] = round(data['severeImpact']['infectionsByRequestedTime'] * (5/100), 2)
data['impact']['casesForVentilatorsByRequestedTime'] = round(data['impact']['infectionsByRequestedTime'] * (2/100), 2)
data['severeImpact']['casesForVentilatorsByRequestedTime'] = round(data['severeImpact']['infectionsByRequestedTime'] * (2/100), 2)




# print(data)

def estimator(inputData):
  
  return data


print(estimator(data))