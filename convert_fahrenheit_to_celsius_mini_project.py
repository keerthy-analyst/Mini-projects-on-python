# -*- coding: utf-8 -*-
"""Convert Fahrenheit to Celsius mini project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XIbXL6UrqHiE54fJngLQ5-Kpbe5B-NJV
"""

''' Note: we have to convert the temperature because celsius and fahrenheit has 
different starting points 0 degree celsius is 32 degree Fahrenheit

    problem and solutions: so just convert fahrenheit to celsius we just need to subtract 32 from fahrenheit
    sometimes the size of units is also different, celsius divides the temperature range between freezing point and boilng point of water is 100 degrees. 
    while fahrenheit divides the range between 180 degree
  
  so i will also multiply the value by 5/9 to convert 180 degree fahrenheit to 100 degree celsius'''

def convert(s):
  f = float (s)
  c = (f-32)*5/9
  return c

print(convert(91))

