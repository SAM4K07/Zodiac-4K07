
for i in range(3):
    
    while True:
        while True:
            try:
                h = int(input("enter ur dimesion for star: "))
                break
            except:
                print("please enter a nunmber ")
        #the value of a varable can be changed,when we write count = 0 its not permenant, we are just giving it some initial value,when the loops below run and are completed h value is stored in them 
        
        count= 0
        space=0
        count2=0
        dad= []
        spc = []
        
        while space<h: #in this peice of code we are creating a list and adding spaces in it [       ]
            space= space+1 # in a triangle spaces should decrese after each line,but to decrease them we should have a list full of empty space sot that in next while loop we can remove those spaces and print them before our stars 
            spc.append(' ') #and number of spaces in a list should be equal to the number given by the user and this loop should be first because we are in the second while loop we are removing spaces, but to remove space we should have a list of spaces 
            # when the list has spaces that it is supposed to have , 
        
        
        while count<h:#this loop process will run until the count value is equal to h. in this loop value of count variabel
            count=count+1    #increases form 1 to 2 to 3 and so on until it is equal to h(h is a number given by the user)
            dad.append(' * ')   #everytime the value of count increases a star is added in lists called dad 
            spc.remove(' ')
            ppc= "".join(spc)
            pro= "".join(dad)  #pro variable is taking list and concacnating the strings in it
            print(ppc,pro)          #then we are printing the concacnated words which are in variable called pro 
                                  #once this loop has ran h times it break
        #previous while loop broke when count value reached h value 
        #this is the interesting part our list spc which we created to store space is now empty and our list dad is full, to print the bottom half of the triangle we need to remove stars from our dad list and add spaces in our spc list and then just print them together side by side 
        
        while count2 < h:
            count2=count2+1
            #we need to add space in spc list,them we need to remove stars form dad and print them each time 
            spc.append(' ')
            dad.remove(' * ')
            ppc= "".join(spc)
            pro= "".join(dad)
            print(ppc,pro)
        # once the count2 has reached value equal to h it breaks 
        break
print("processed has stopped ")       
            
        
     