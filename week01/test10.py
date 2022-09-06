wr=input('Enter secret code : ')
myList = [chr(chNum) for chNum in list(range(ord('a'),ord('z')+1))]

def bon(wr):
    for an in range(0, len(wr)):  
        count = 1  
        for bn in range(an+1, len(wr)):  
            if wr[an] == wr[bn] and wr[an] != ' ':  
                count = count + 1  
                wr = wr[:bn] + '0' + wr[bn+1:]  
        if count > 1 and wr[an] != '0':
            if  wr[an] in myList:
                if count%2==0:
                    result=((myList.index(wr[an])+1)*count)*2
                    
                else:
                    result=((myList.index(wr[an])+1)*(count+1))

                print(result)
     
   
bon(wr)        
        


