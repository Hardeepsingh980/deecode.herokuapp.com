def main_code(in_):
  def codes(l):
    d = []
    for code in l:
      if code == "A":
        d.append("2")
      elif code == "B":
        d.append("22")
      elif code == "C":
       d.append ("222")
      elif code == "D":
       d.append ("3")
      elif code == "E":
       d.append ("33")    
      elif code == "F":
        d.append("333")    
      elif code == "G":
        d.append("4")     
      elif code == "H":
         d.append("44")    
      elif code == "I":
        d.append("444")     
      elif code == "J":
        d.append("5")     
      elif code == "K":
        d.append("55")    
      elif code == "L":
        d.append("555")      
      elif code == "M":
        d.append("6")
      elif code == "N":
        d.append("66")      
      elif code == "O":
        d.append("666")    
      elif code == "P":
         d.append("7")      
      elif code == "Q":
       d.append ("77")      
      elif code == "R":
        d.append("777")      
      elif code == "S":
        d.append("7777")     
      elif code == "T":
        d.append("8")      
      elif code == "U":
        d.append("88")      
      elif code == "V":
        d.append("888")      
      elif code == "W":
        d.append("9")      
      elif code == "X":
         d.append("99")           
      elif code == "Y":
        d.append("999")
      elif code == "Z":
        d.append("9999")
      elif code == " ":
         d.append("0,")
   # ans = ''.join(d)
    return d

  input = in_
  l1 = []

  for i in input:
     l1.append(i.upper())
     
  l1.append(" ")   

  l2 = codes(l1)
  l3 = []
  for i in l2:
     if l2[-1] == i:
        l3.append(i)
        
     else:
        l3.append(i + ",")
        
  ans = ''.join(l3)

  return ans


  


      
