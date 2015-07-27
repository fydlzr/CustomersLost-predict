# -*- coding: utf-8 -*-
import sys

def getData(preNday = 30, nextNday = 30, infile = 'data\\filtedData', outfile = 'data\\dataSet', max = 170000):
    print('getData: %d %d %d' %(preNday, nextNday, max))
    start = 1
    fin = open(infile+'.txt')
    fout = open(outfile+'.txt', 'w')
    fout2 = open('sums.txt','w')
    c = 0
    sumsOfLabel0 = {}
    for line in fin:
        if c%1000==0:
            print(c)
        c+=1
        sts = line.strip().split()
        
        for offset in range(start, start+31, 30):
            features = sts[offset:offset+preNday]
            nextsum = sum(int(t) for t in sts[offset+preNday:offset+preNday+nextNday])
            sums = sum(int(t) for t in features)
            label = ('1' if nextsum>0 else '0')
            if label == '0':
                if sums in sumsOfLabel0:
                    sumsOfLabel0[sums] +=1
                else:
                    sumsOfLabel0[sums] = 1
            fout.write('\t'.join(s for s in features)+'\t'+ label +'\n')
            fout2.write(str(sums) + '\t' + label +'\n')
        if c>max:
            break
    fout.close()
    fout2.close()
    fin.close()
    print('='*50)
    print(sorted(sumsOfLabel0.items(), key=lambda d:d[0], reverse = True ))
    return outfile

def SplitTrainTestBasedTime(preNday = 30, nextNday = 30, infile = 'filtedData', outfile = 'dataSet', max = 170000):
    print('getData: %d %d %d' %(preNday, nextNday, max))
    start = 1
    fin = open(infile+'.txt')
    foutTrain = open(outfile+'_Train.txt', 'w')
    foutTest = open(outfile+'_Test.txt', 'w')
    # fout2 = open('sums.txt','w')
    c = 0
    sumsOfLabel0 = {}
    for line in fin:
        if c%10000==0:
            print(c)
        c+=1
        sts = line.strip().split()

        for offset in range(start, start+31, 30):
            #print(offset)
            features = sts[offset:offset+preNday]
            nextsum = sum(int(t) for t in sts[offset+preNday:offset+preNday+nextNday])
            sums = sum(int(t) for t in features)
            label = ('1' if nextsum > 0 else '0')
            # if label == '0':
            #     if sums in sumsOfLabel0:
            #         sumsOfLabel0[sums] += 1
            #     else:
            #         sumsOfLabel0[sums] = 1
            if offset == start:#Train
                foutTrain.write('\t'.join(s for s in features)+'\t'+ label +'\n')
            else:#Test
                foutTest.write('\t'.join(s for s in features)+'\t'+ label +'\n')
            #fout2.write(str(sums) + '\t' + label +'\n')
        if c>max:
            break
    foutTrain.close()
    foutTest.close()
    # fout2.close()
    fin.close()
    print('='*50)
    print(sorted(sumsOfLabel0.items(), key=lambda d:d[0], reverse = True ))
    return outfile

if __name__=='__main__':
    if len(sys.argv)>4:
        preNday = int(sys.argv[1])
        nextNday = int(sys.argv[2])
        infile = sys.argv[3]
        outfile = sys.argv[4]
        getData(preNday, nextNday, infile, outfile)
    else:
        sys.stdout.write('Example: python getTrain.py preNday nextNday infile outfile\n')
        getData(30,30,'data\\'+'filtedData', 'data\\'+'dataSet')
        SplitTrainTestBasedTime(30,30,'data\\'+'filtedData', 'data\\'+'dataSet')