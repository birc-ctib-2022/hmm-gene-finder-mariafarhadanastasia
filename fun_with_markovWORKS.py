from math import sqrt

ann="CCCNNNNNNRRRRRRRRRR"
#data="AACTGATATATATATGCC"


def find_state(ann):
    states=[]
    for i in range(0,len(ann)):
        if ann[i]=="C" and ann[i-1]!="C":
            states.append(0)
        if ann[i]=="C" and ann[i-1]=="C":
            num=(states[i-1]+1)%3
            states.append(num)
        if ann[i]=="N":
            states.append(3)
        if ann[i]=="R" and ann[i-1]!="R":
            states.append(4)
        if ann[i]=="R" and ann[i-1]=="R":
            num=((states[i-1]+3)%3)+4
            states.append(num)
    return states


find_state(ann)

