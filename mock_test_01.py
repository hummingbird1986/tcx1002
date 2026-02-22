def f(s):
   
    if s == '':
        return ''
    first_ele=s[0]
    
  
    if first_ele.lower() in ['a', 'e', 'i', 'o', 'u']:
           type = "V"
    elif first_ele.isalpha():
           type = "C"
    else:
           type = "-"
           
    return type + f(s[1:])

print(f('e2cbi'))