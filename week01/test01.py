
print('*** Converting hh.mm.ss to seconds ***')
h,m,s = input('Enter hh mm ss : ').split()

h = int (h)
m = int (m)
s = int (s)

def f(h,m,s):
    if h<0:
        print("hh(%s)" % str(h)+" is invalid!")
    elif m>=60 or m<0:
        print("mm(%s)" % str(m)+" is invalid!")
    elif s>=60 or s<0:
        print("ss(%s)"% str(s)+" is invalid!")
    else:
        sec=h*3600+m*60+s
        sec='{:,}'.format(sec)
        print("%02d:%02d:%02d = %s seconds" % (h,m,s,sec))


f(h,m,s)

