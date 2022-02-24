# ex3 - prompt user for hrs and rate per hour to compute gross pay

try:
  hrlyRate = float(input('Please tell me your hourly rate:\n'))
  print('Your hourly rate is:', hrlyRate)
  
  # above can be improved with string formatting
  extraPay = 0
  hrsWorked = float(input('Please tell me the # of hours worked\n'))
  if hrsWorked > 40:
      extraHrs = hrsWorked - 40
      extraPay = extraHrs * hrlyRate * 1.5
      hrsWorked = 40 #reset
  
  grossPay = round((hrlyRate * hrsWorked)+extraPay, 2)
  
  print('You have earned:', grossPay)

except:
    print("Please make sure you are entering numbers :)")
