def main_code(in_):
  def codes(l):
    d = []
    for code in l:
      if code == "2":
        d.append("A")
      elif code == "22":
        d.append("B")
      elif code == "222":
       d.append ("C")
      elif code == "3":
       d.append ("D")
      elif code == "33":
       d.append ("E")    
      elif code == "333":
        d.append("F")    
      elif code == "4":
        d.append("G")     
      elif code == "44":
         d.append("H")    
      elif code == "444":
        d.append("I")     
      elif code == "5":
        d.append("J")     
      elif code == "55":
        d.append("K")    
      elif code == "555":
        d.append("L")      
      elif code == "6":
        d.append("M")
      elif code == "66":
        d.append("N")      
      elif code == "666":
        d.append("O")    
      elif code == "7":
         d.append("P")      
      elif code == "77":
       d.append ("Q")      
      elif code == "777":
        d.append("R")      
      elif code == "7777":
        d.append("S")     
      elif code == "8":
        d.append("T")      
      elif code == "88":
        d.append("U")      
      elif code == "888":
        d.append("V")      
      elif code == "9":
        d.append("W")      
      elif code == "99":
         d.append("X")           
      elif code == "999":
        d.append("Y")
      elif code == "9999":
        d.append("Z")
      elif code == "0":
         d.append(" ")
    ans = ''.join(d)
    return ans
    
  name = in_.split(",")
  l1 = []
  for i in name:
    l1.append(i)
         
  return codes(l1)

