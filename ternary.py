states = ["0","1","2"]#Available values

def F000(x): #To zero
    x = "0"
    return x
def F001(x): #Inversion
    x = str(x)
    if x == states[2] or x == states[1]:
        print (x)      
        return "0"
    else:
        return "1"
    
def FT2N13203(x,y): #OR
    x = str(x)
    y = str(y)
    if x == states[2] and y == states[2]:
        return "2"
        """
          if x == states[1] and y == states [2] or x == states[2] and y == states[1]:
        return "0"
        if x == states [0] and y == states [2] or x == states [2] and y == states[0]:
            return "0"
        """ 
    if x == states[1] and y == states [1]:
        return "1"
    else:
        return "0"
def FT2N8038(x,y): #AND
    x = str(x)
    y = str(y)
    if x == states[1] and y == states [1] or x==states[2] and y==states[2]:
        return "1"
    if x == states[2] and y == states [1] or x == states [1] or y == states[2]:
        return "2"
    else:
        return "0"
    
