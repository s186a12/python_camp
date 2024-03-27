def check_input(p_input):
    try:
      num = int(p_input)
      if (num<1):
          print(p_input+'是一個不合法的輸入，無法運算...') 
      else:
          return num
    except ValueError:
      print(p_input+'是一個不合法的輸入，無法運算...')   

str_input = input('請輸入正整數...')

num = check_input(str_input)
      
if num is not None:       
      x = 1         
      for i in range(1,num+1):          
          x = x*i      
      print(x)
