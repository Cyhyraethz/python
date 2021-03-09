height, weight = 0, 0

while not height:
  try:
    height = float(input('Height (centimeters): '))
  except:
    print('Error. Invalid height.')

while not weight:
  try:
    weight = float(input('Weight (kilograms): '))
  except:
    print('Error. Invalid weight.')

bmi = round(weight / height / height * 10000, 1)

if bmi < 18.5:
  range = 'underweight'
elif bmi >= 18.5 and bmi <= 24.9:
  range = 'healthy weight'
elif bmi >= 25 and bmi <= 29.9:
  range = 'overweight'
else:
  range = 'obese'

print('Your BMI is {}, which puts you in the {} range.'.format(bmi, range))