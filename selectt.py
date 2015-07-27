# -*- coding: utf-8 -*-
def hasZhouQi(sts):
    count = 0
    for i in range(1,15):
        if sts[i] == sts[30+i]:
            count +=1
            if count>6:
                return True
    return False
    

if __name__=='__main__':
    n = 100000
    fin = open('data\\tmueractive.txt', encoding='utf-8')
    fout = open('data\\tt'+str(n)+'.txt','w')
    c = 0
    for line in fin:
        c+=1
        if c%100000==0:
            print(c)
        '''if c<6100000:
            continue'''
        summ = 0
        sts = line.strip().split()
        if(len(sts)!=92):
            continue
        for i in range(1,len(sts)):
            summ += int(sts[i])
        if '''summ >= 0''' and summ < 1000 and not hasZhouQi(sts):
            fout.write(line)
    fout.close()
    fin.close()
