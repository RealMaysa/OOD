arr=list(map(int,input('Enter Your List : ').split()))
if len(arr)<3:
        print("Array Input Length Must More Than 2")
else:
         
    def findTriplets(arr, n):
            result=[]
            found = False
            same =  False
            arr.sort()
  
            for i in range(0, n-1):
      
        
                l = i + 1
                r = n - 1
                x = arr[i]
                while (l < r):
          
                    if (x + arr[l] + arr[r] == 5 and same == False):
            
                            if [x, arr[l], arr[r]] not in result:    
                                result.append([x, arr[l], arr[r]])
                                l+=1
                                r-=1
                                found = True
                            else:
                                same=True
                            
                                    
                    elif (x + arr[l] + arr[r] < 5):
                        l+=1
  

                    else:
                        r-=1
          
            if (found == False):
                    print(" No Triplet Found")

            return result
    print(findTriplets(arr, len(arr)))



        
