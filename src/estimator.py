def convertToDays(period_type, timeToElapse):
  if period_type == 'days':
    return timeToElapse

  elif period_type == 'weeks':
    return timeToElapse * 7

  elif period_type == 'months':
    return timeToElapse * 30

  else:
    return 'Incorrect input'





period_type = input('Enter ')
timeToElapse = int(input('Enter the number of days'))
reportedCases = int(input('Enter the number of reported cases'))
population = int(input('Population'))
totalHospitalBeds = int(input('Hospital beds'))
currentlyInfected = 0
infectionsByRequestedTime = 0
name = input('Enter a country name')
avgAge = int(input('Enter an age'))
avgDailyIncomeInUSD =  int(input('Enter an integer'))
avgDailyIncomePopulation =  int(input('Enter an integer'))

data = {

    'data' : {
      'region':{
        'name' : name,
        'avgAge' : avgAge,
        'avgDailyIncomeInUSD' : avgDailyIncomeInUSD,
        'avgDailyIncomePopulation' : avgDailyIncomePopulation
      },
      'period_type' : period_type,
      'timeToElapse' : convertToDays(period_type, timeToElapse),
      'reportedCases' : reportedCases,
      'population' : population,
      'totalHospitalBeds' : totalHospitalBeds
    },

    'impact' : {
      'currentlyInfected' : reportedCases * 10,
    },

    'severeImpact' : {
      'currentlyInfected' : reportedCases * 50,
    }

  }



data['impact']['infectionsByRequestedTime'] = data['impact']['currentlyInfected'] * (2 ** (timeToElapse/3))
data['severeImpact']['infectionsByRequestedTime'] = data['severeImpact']['currentlyInfected'] * (2 ** (timeToElapse/3))
data['impact']['severeCasesByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (15/100)
data['severeImpact']['severeCasesByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (15/100)
data['impact']['hospitalBedsByRequestedTime'] = data['impact']['severeCasesByRequestedTime'] - data['data']['totalHospitalBeds']
data['severeImpact']['hospitalBedsByRequestedTime'] = data['severeImpact']['severeCasesByRequestedTime'] - data['data']['totalHospitalBeds']
data['impact']['casesForICUByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (5/100)
data['severeImpact']['casesForICUByRequestedTime'] = data['severeImpact']['infectionsByRequestedTime'] * (5/100)
data['impact']['casesForVentilatorsByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (2/100)
data['severeImpact']['casesForVentilatorsByRequestedTime'] = data['severeImpact']['infectionsByRequestedTime'] * (2/100)




# print(data)

def estimator(data):
  
  return data


print(estimator(data))