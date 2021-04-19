
import numpy as np
import random
import json
class person():
    def __init__(self):
        self.b=False
        self.sick =False
        self.i =False
        self.day=0
        if(self.sick):
            self.setSickTime()
    def canSick(self):
        if not self.sick or not self.i:
            return True
        return False
    def setSickTime(self):
        self.day=1
    def tick(self):
        if self.sick :
            if self.day==1:
                if random.random()<=.1:
                    self.sick=False
                    if random.random()<=.9:
                        self.i=True
            if self.day==2:
                if random.random()<=.3:
                    self.sick=False
                    if random.random()<=.9:
                        self.i=True
            if self.day==3:
                if random.random()<=.6:
                    self.sick=False
                    if random.random()<=.9:
                        self.i=True
            if self.day==4:
                if random.random()<=.9:
                    self.sick=False
                    if random.random()<=.9:
                        self.i=True
            if self.day>=5:
                self.sick=False
                if random.random()<=.9:
                        self.i=True
            self.day+=1
        
        
    def getSick(self):
        if not self.i and not self.sick:
            self.sick=True
            self.b=True
            self.setSickTime()
            return True
        return False
    def __str__(self):
        return str(self.sick)+"  "+str(self.i)+ "   "+str(self.day)

def save(array,day):
    array2 = [[ ["*"  for col in range(500)] for col in range(500)] for row in range(20)]
    for i in range(len(array)):
        for j in range(500):
            for k in range(500):
                temp=""
                if array[i][j][k].b:
                    temp+="1"
                else:
                    temp+="0"
                if array[i][j][k].i:
                    temp+="1"
                else:
                    temp+="0"
                if array[i][j][k].sick:
                    temp+="1"
                else:
                    temp+="0"
                temp+=str(array[i][j][k].day)
                
                array2[i][j][k]=temp
                # array2[i][j][k] = json.loads(json.dumps(array[i][j][k].__dict__))
                if j==0 and i==0 and k ==0:
                    print(type(array2[i][j][k]))
    out_file = open("day"+str(day)+".json", "w")
  
    json.dump(array2, out_file, indent = 6)


def sim(array):
    day =0
    print("starting day: "+str(day))
    sicktoday=25
    floor={-1:1}
    
    while sicktoday>0:
        sicktoday=0
        if day %10==0 or day ==0:
            print("day: "+str(day))
            save(array,day) 
        day+=1
        for i in range(len(array)):
            print("floor: "+str(i))
            for j in range(500):
                for k in range(500):
                    if array[i][j][k].sick:
                        
                        for q in range(8):
                            if (q%2==1 and random.random()<.2) or (q%2==0 and random.random()<.1):
                                if q==1 and k<499:
                                    if array[i][j][k+1].getSick():
                                        sicktoday+=1
                                if q==2  and j<499 and k<499:
                                    if array[i][j+1][k+1].getSick():
                                        sicktoday+=1
                                if q==3  and k>1:
                                    if array[i][j][k-1].getSick():
                                        sicktoday+=1
                                if q==4  and j>1 and k>1:
                                    if array[i][j-1][k-1].getSick():
                                        sicktoday+=1
                                if q==5  and j<499:
                                    if array[i][j+1][k].getSick():
                                        sicktoday+=1
                                if q==6 and k>1 and j<499:
                                    if array[i][j+1][k-1].getSick():
                                        sicktoday+=1
                                if q==7 and j>1:
                                    if array[i][j-1][k].getSick():
                                        sicktoday+=1
                                if q==8 and j>1 and k<499:
                                    if array[i][j-1][k+1].getSick():
                                        sicktoday+=1
                    else:
                        if j<125 and random.random()<.0005*floor[i-1]:
                            if array[i][j][k].getSick():
                                sicktoday+=1
                        elif j<250 and random.random()<(.0005/2)*floor[i-1]:
                            if array[i][j][k].getSick():
                                sicktoday+=1
                        elif j<375 and random.random()<(.0005/4)*floor[i-1]:
                            if array[i][j][k].getSick():
                                sicktoday+=1
                        elif random.random()<(.0005/8)*floor[i-1]:
                            if array[i][j][k].getSick():
                                sicktoday+=1
            sicknum=0
            for a in range(500):
                for b in range(500):
                    if array[i][a][b].sick:
                        sicknum+=1
                        array[i][a][b].tick()
            print("sicknum: "+str(sicknum))
            if sicknum<3000:
                floor[i]=1
            elif sicknum<5000:
                floor[i]=2
            elif sicknum<70000:
                floor[i]=3
            elif sicknum<50000:
                floor[i]=4
        print(floor)
        print(sicktoday)
        print(day)



                



array = [[ [person() for col in range(500)] for col in range(500)] for row in range(20)]
for i in range(25):
    print("day0 sick: "+str(i))
    array[round(random.random()*19)][round(random.random()*499)][round(random.random()*499)].getSick()
sim(array)
