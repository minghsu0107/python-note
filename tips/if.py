def bmi(kg, m):
  return kg / (m * m)
def check(kg, m):
  b = bmi(kg, m)
  msg = None
  if b < 18.5: msg = "thin"
  elif bmk < 25: msg = "ok"
  else: msg = "careful"

  print(msg)

def check2(kg, m):
  b = bmi(kg, m)
  msg = "thin" if b < 18.5 else "ok" if b < 25 else "careful"
  print(msg)

def check3(kg, m):
  b = bmi(kg, m)
  msg = "thin" if b < 18.5 else (
    "ok" if b < 25 else "careful")
  print(msg)