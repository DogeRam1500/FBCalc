#!/usr/bin/python
from datetime import date
import math
def inputNumber(message):
    while True:
        try:
            userInput=int(input(message))
        except ValueError:
            print('Please enter a whole number.')
        else:
            return userInput
def inputFloat(message):
    while True:
        try:
            userInput=float(input(message))
        except ValueError:
            print('Please enter a number.')
        else:
            return userInput
def inputString(message):
    userInput=input(message).casefold()
    while userInput not in ['yes','y','no','n']:
        print("That was not a valid option, please enter 'yes' or 'no'")
        userInput=input(message).casefold()
    else:
        return userInput
today=date.today()
number=inputNumber('How many locations do you need scores for? ')
bonuses=inputString('Do you want scores with multiplier bonuses? ')
#store points
location=[]
max_temp=[]
min_temp=[]
wind_gust=[]
precip=[]
bonus_days=[]
dd_points=[]
wind_points=[]
precip_points=[]
raw_score=[]
multiplier=[]
point_total=[]
#input data
for i in range(0,number):
    location.append(input('Please enter location ''{}'': '.format(i+1)))
    max_temp.append(round(inputFloat('Max temp: '),0))
    min_temp.append(round(inputFloat('Min temp: '),0))
    wind_gust.append(round(inputFloat('Max wind gust: '),0))
    if 5<=today.month<=9:
        precip.append(round(inputFloat('Rainfall: '),2))
    else:
        precip.append(round(inputFloat('Snowfall: '),1))
    if bonuses=='yes' or bonuses=='y':
        bonus_days.append(inputNumber('How many days out is the pick? '))
    wind_points.append(int(wind_gust[i]))
    avtemp=(max_temp[i]+min_temp[i])/2
    if 5<=today.month<=9:
        if avtemp>=65:
            dd_points.append(int(math.trunc(avtemp-65)))
        else:
            dd_points.append(0)
        precip_points.append(int(100*precip[i]))
    else:
        if avtemp<=65:
            dd_points.append(int(math.floor(65-avtemp)))
        else:
            dd_points.append(0)
        precip_points.append(int(10*precip[i]))
    raw_score.append(dd_points[i]+wind_points[i]+precip_points[i])
    if bonuses=='yes' or bonuses=='y':
        if raw_score[i]>=100:
            if bonus_days[i]==2:
                multiplier.append(1.2)
            elif bonus_days[i]==3:
                multiplier.append(1.3)
            elif bonus_days[i]==4:
                multiplier.append(1.4)
            elif bonus_days[i]>=5:
                multiplier.append(1.5)
        else:
            multiplier.append(1)
        point_total.append(raw_score[i]*multiplier[i])
    if 5<=today.month<=9:
        print('\n''Summer Mode')
    else:
        print('\n''Winter Mode')
    print('Score for ''{}''\n''DD Points: ''{}''\n''Wind Points: ''{}''\n''Precip Points: ''{}'.format(location[i],dd_points[i],wind_points[i],precip_points[i]))
    if bonuses=='yes' or bonuses=='y':
        print('Raw Score: ''{}''\n''Multiplier: ''{}''\n''Total Score: ''{}'.format(raw_score[i],multiplier[i],point_total[i]))
    else:
        print('Total Score: ''{}'.format(raw_score[i]))
