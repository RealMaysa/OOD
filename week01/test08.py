from operator import mod


print("*** Mod Position ***")

arr,s=input('Enter Input : ').split(",")
s=int(s)
def mod_position(arr, s):
    result=[]
    for i in range(0,len(arr)):
        if (i+1)%s==0:
            result.append(arr[i])
        else:
            pass
    return result

print(mod_position(arr, s))
       