import re,datetime,time,math

def rule1(data,points):
    if (isinstance(data['retailer'],str) and re.match("^\\S+",data['retailer'])):

        retailer = data['retailer']      
        res = len([ele for ele in retailer if ele.isalnum()])
        points += res
      
        return points 

    else:
        return "400: The receipt is invalid"

def rule2_and_rule3(data,points):

    if (isinstance(data['total'],str) and re.match("^\\d+\\.\\d{2}$",data['total'])):

        total = data['total']
        total = float(total)

        s,t = divmod((total),1)
        if(t==0):
            points += 50

        if((total) % 0.25==0):
            points += 25
        
        return points
    
    else:
        return "400: The receipt is invalid"

def rule4_and_rule5(data,points):

    if (isinstance(data['items'],list) and len(data['items'])>=1):

        items = data['items']
        
        for ele in items:
        
            description = ele['shortDescription'].strip()

            if(isinstance(description,str) and re.match("^\\S+",description) and isinstance(ele['price'],str) and re.match("^\\d+\\.\\d{2}$",ele['price'])):
                
                if(len(description)%3==0):
                    price = ele['price']
                    result = math.ceil(float(price)*0.2)
                    points += result

            else:
                return "400: The receipt is invalid"
        
        if len(items)%2==0:
            points += (5*len(items)/2)
        else:
            comp = (len(items)-1)/2
            points += (5*comp)

        return points

    else:
        return "400: The receipt is invalid"


def rule6(data,points):

    if(isinstance(data['purchaseDate'],str)):
        try:
            datetime.datetime.strptime(data['purchaseDate'], '%Y-%m-%d')
            purchase_date = data['purchaseDate']
            year,month,day = purchase_date.split("-")
        
            day = int(day)

            if(day%2 !=0):
                points += 6

        except ValueError:
            return "400: The receipt is invalid"
    else:
        return "400: The receipt is invalid"
    return points

def rule7(data,points):
    
    if(isinstance(data['purchaseTime'],str)):

        try:
            time.strptime(data['purchaseTime'],'%H:%M')
            purchase_time = data['purchaseTime']
            hour,minute = purchase_time.split(":")
            
            if(int(hour)==14 and int(minute)>0):
                points += 10

            elif (int(hour)>14 and int(hour)<16):
                points += 10
                
        except ValueError:
            return "400: The receipt is invalid"

    else:
        return "400: The receipt is invalid"
    
    return points