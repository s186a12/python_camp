x = input()
y = input()

try: 
  sum = float(x)+float(y) 
  print(sum)
except ValueError:
  print("輸入的資料型態錯誤...")

#當int與float相加時，int會轉換為float
