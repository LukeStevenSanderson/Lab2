#
def createmenue(optionlist):
    tmp=''
    ct=0
    for item in optionlist:
        tmp+=str(ct)+'.'+item +'\n'
        ct+=1
    return tmp
