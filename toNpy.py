# -*- coding: utf-8 -*-
import scipy as sp
import numpy as np
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
import sys

class Npy(object):
    def __init__(self, filename):
        self.filename = filename
    @staticmethod
    def saveNpy(filename):
        print("============saveNpy============:"+filename)
        if filename.find('.txt')!=-1: filename = filename.split('.txt')[0]
        f = open(filename+'.txt', 'r')
        data = np.loadtxt(f)

        x = data[:,:-1]
        y = data[:,-1]
        sp.save(filename+'_data.npy', x.data)
        sp.save(filename+'_target.npy', y.data)


        # x_train, x_test, y_train, y_test\
        #     = train_test_split(x, y, test_size = 0.5)
        #
        # sp.save(filename+'Train_data.npy', x_train.data)
        # sp.save(filename+'Train_target.npy', y_train.data)
        # sp.save(filename+'Test_data.npy', x_test.data)
        # sp.save(filename+'Test_target.npy', y_test.data)


    @staticmethod
    def splitTrainTestBasedTime(filename):
        print("============splitTrainTestBasedTime============:"+filename)
        if filename.find('.txt')!=-1: filename = filename.split('.txt')[0]
        trainName = filename+'_Train'
        f = open(trainName+'.txt', 'r')

        data = np.loadtxt(f)
        x = data[:, :-1]
        y = data[:, -1]
        sp.save(trainName+'_data.npy', x.data)
        sp.save(trainName+'_target.npy', y.data)
        f.close()

        testName = filename+'_Test'
        f = open(testName+'.txt', 'r')
        data = np.loadtxt(f)
        x = data[:, :-1]
        y = data[:, -1]
        sp.save(testName+'_data.npy', x.data)
        sp.save(testName+'_target.npy', y.data)


if __name__ == '__main__':
    if len(sys.argv)>1:
        filename = sys.argv[1].split('.')[0]
    else:
        filename = 'data\\dataSet'
    filename = 'data\\4Train'
    # filename = 'data\\4Test'
    Npy.saveNpy(filename)
    #Npy.splitTrainTestBasedTime(filename)
