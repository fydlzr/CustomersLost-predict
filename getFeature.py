__author__ = 'haha'
import random
import toNpy
length = 30

def lastNdaysZero(data):
    length = len(data)
    count = 0
    for i in range(1, length+1):
        if data[length - i] == '0':
            count += 1
        else:
            break
    #print(data, count)
    return count

def daysSum(data, Ndays):
    length = len(data)
    res = sum(int(t) for t in data[length-Ndays:length])
    return res

def daysSumFromXToY(data, X, Y):
    res = sum(int(t) for t in data[X: Y])
    return res

def deleteAbnormalPoint(features, label):
    if label == '1':#active
        if features[-1] > 25:#last 25 days' activities are zeros
            return True
    else:#non-active
        if features[-2] > 30:#last week has more than 30 activities
            return True

    return False


def getFeatures(infile, outfile, trainOrTest):
    fin = open(infile, 'r')
    fout = open(outfile, 'w')
    pos = 0
    neg = 0


    for line in fin:
        features = []
        data = line.strip().split()[:-1]
        label = line.strip()[-1]

        #
        # for i in range(2,30,7):
        #     # print(i)
        #     features.append(daysSumFromXToY(data, i, i+7))

        for i in range(28,0,-7):
            # print(i)
            features.append(daysSum(data, i))

        features.append(lastNdaysZero(data))

        if trainOrTest == 'train' and deleteAbnormalPoint(features, label): continue

        if label == '1':
            # r = random.random()
            # if r<0.8 and trainOrTest =='train' : continue
            pos+=1
        else:
            neg+=1

        # if trainOrTest == 'train':
        #     if label == '0' and features[0] < 100:
        #         for j in range(1):
        #             neg+=1
        #             fout.write('\t'.join(str(t) for t in features)+'\t'+ label + '\n')
        fout.write('\t'.join(str(t) for t in features)+'\t'+ label + '\n')
    fout.close()
    fin.close()
    print('pos:neg= %d:%d' %(pos, neg))

if __name__ == '__main__':
    filename = '5'
    getFeatures('data\\dataSet_Train.txt', 'data\\'+filename+'Train.txt', 'train')
    toNpy.Npy.saveNpy('data\\'+filename+'Train.txt')
    #
    getFeatures('data\\dataSet_Test.txt', 'data\\'+filename+'Test.txt', 'test')
    toNpy.Npy.saveNpy('data\\'+filename+'Test.txt')