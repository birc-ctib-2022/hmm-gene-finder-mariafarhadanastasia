from math import sqrt

ann="CCCNNNNNNRRRRRRRRRR"
#data="AACTGATATATATATGCC"


def find_state(ann, k):
    states_3=[]
    states_7=[]
    if k==3:
        for i in range(0,len(ann)):
            if ann[i]=="C":
                states_3.append(0)
            if ann[i]=="N":
                states_3.append(1)
            if ann[i]=="R":
                states_3.append(2)
        return states_3
    if k==7:
        for i in range(0,len(ann)):
            if ann[i]=="C" and ann[i-1]!="C":
                states_7.append(0)
            if ann[i]=="C" and ann[i-1]=="C":
                num=(states_7[i-1]+1)%3
                states_7.append(num)
            if ann[i]=="N":
                states_7.append(3)
            if ann[i]=="R" and ann[i-1]!="R":
                states_7.append(4)
            if ann[i]=="R" and ann[i-1]=="R":
                num=((states_7[i-1]+3)%3)+4
                states_7.append(num)
        return states_7


find_state(ann,3)
find_state(ann,7)

