import re
def isPhishing(url):
    risk=0
    reason=[]
    
    #check ip address in URL
    if re.match(r"https?://\d+\.\d+\.\d+\.\d+",url):
        risk+=2
        reason.append("URL contains IP address")

#check @ symbol
if '@' in url:
    risk+=1
    reason.append("URL contains @ symbol")
    
    # check for Long URL
    if len(url)>75:
        risk+=1
        reason.append("URL is too long")
        
        #check for suspicious word
        suspicious=["login","verify","secure","account","update"]
        for word in suspicious:
            if word in url.lower():
                risk+=1
                reason.append(f"contains suspicious word:{word}")
            
        if risk==0:
            reason.append("Looks safe")
            return False,risk,reason
        else:
            return True,risk,reason 

#Testing
url=input("Enter URL to check:")
result,risk,reasons=isPhishing(url)
print(f"\nRisk Score:{risk}")
print(f"isPhishing?:{result}")
print(f"Reasons:{reasons}")