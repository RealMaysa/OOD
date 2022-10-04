'''
จงเขียนฟังก์ชั่นสำหรับการเรียงค่าใน List ของจำนวนเต็มโดยจะเรียงค่าจากมากไปน้อย

****ห้ามใช้ for/while และฟังก์ชั่นอื่นๆในการวนลูป ให้ใช้ recursion ในการเขียนเท่านั้น****
'''
def reverseSort(list) :
    result = []

    def sort(list) :
        if list :
            maximum = max(list)
            result.append(list.pop(list.index(maximum)))
            sort(list)
        else :
            return

    sort(list)

    return result

def toInt(i,list) :
    if i < len(list) :
        list[i] = int(list[i])
        toInt(i+1,list)
    
    return list

input = (input("Enter your List : ").split(","))

print("List after Sorted : " + str(reverseSort(toInt(0,input))))