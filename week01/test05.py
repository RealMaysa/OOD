ip=list(map(int,input('Enter All Bid : ').split()))
ip.sort(reverse=True)
if len(ip)==1:
    print("not enough bidder")

elif ip[0] == ip[1]:
    print("error : have more than one highest bid")
else:
    print("winner bid is %d need to pay %d"% (ip[0],ip[1]))
