#Ken Su Opt 3
#Detection system


print("start")
print("System inactive")
system_active = False
system_alert = False
bell = False
a = int(input("Press one to turn on the system"))
if a == 1:
    system_active = True
else:
    system_active = False
while (system_active == True) and (system_alert == False):
    b = int(input("Sir, press one to intrude, enter PIN to turn it off:"))
    if b == 20000223:
        system_active = False
    if b == 1:
        system_alert = True
if system_active == False:
    print("You have turned off the system")
while system_alert == True:
    c = int(input("Enter PIN to turn it off, or bell will ring"))
    if c == 20000223:
        system_active = False
        system_alert = False
    else:
        bell = True
        system_alert = False
if system_active == False:
        print("You have turned off the system")
while bell == True:
    print("Bell is going to ring")
    d = int(input("Your last chance to enter PIN:"))
    if d == 20000223:
        system_active = False
        bell = False
        if system_active == False:
            print("end of game")
            
        
        
        
        
   
