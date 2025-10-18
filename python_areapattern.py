
    
def Areat():
    while True:
        area = int(input("enter area for ur square :"))
        if area == 0:
            break
        
        art = int(area**0.5)
        count= 0
        count1=0
        dad=[]
        while count < art:
            count=count+1
            dad.append(' * ')
            pro = "".join(dad)
        
        while count1<art:
            count1=count1+1
            print(pro)
            if count1==art:
                break
        
def pattert():
    
    exceptcount = 0
    while True:
        try:
            w = int(input(" enter ur width: "))
            h = int(input(" enter ur height: "))
            
            if w or h == 000:
                break
            
            count= 0
            count2= 0 
            dad = []
            while count<w:
                count=count+1
                dad.append(' * ')
                pro = "".join(dad)
            print(pro)
            while count2<h:
                count2=count2+1
                print(pro)
        except:
            exceptcount=exceptcount+1
            print(" X Try again X")
            print(" Your reamining chances are :",10-exceptcount)
            if exceptcount>10:
                break
                print(pro)
                

while True:
    print(" For areaprinting press 'ART' for patternpritning prss 'PTR'")
    a = input(" Would u like areaprinting or patternprinting ?:")
    
    if a == 'ART':
        Areat()
        
    if a == 'PTR':
        pattert()
        
    if a == 'exit':
        break
            
            
    