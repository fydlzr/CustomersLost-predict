n = 10000
span = 1
filename = '90+.txt'
fin = open(filename)
fout = open(filename+'_'+str(span)+'.txt','w')
c = 0
for line in fin:
    c+=1
    print(str(c)+'='*20) 
    ss = line.strip().split()
    timeSpan = 0
    summ = 0;
    sums = []
    for i in range(1,91):
        timeSpan += 1
        if span !=1 and (timeSpan%span ==0 or i==90):
            #print(summ)
            sums.append(summ)
            
            timeSpan = 0
            summ = 0
        elif span == 1:
            sums.append(int(ss[i]))
        else:
            summ += int(ss[i])
    fout.write('\t'.join(str(t) for t in sums)+'\n')
fout.close()
        
