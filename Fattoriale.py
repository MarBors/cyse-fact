
var = 5

def fattoriale(n):
    if(n > 1):
        return fattoriale(n-1) * n
    else:
        return 1
    
print(fattoriale(var))