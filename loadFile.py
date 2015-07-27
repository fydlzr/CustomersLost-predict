__author__ = 'haha'
from sklearn.cross_validation import train_test_split
import numpy as np

def loadFile(filename):
    if filename.find('.txt')!=-1: filename = filename.split('.txt')[0]
    print('=========loadFile========:'+ filename)
    training_x = np.load(filename+"train_data.npy")
    print(training_x.shape)
    training_y = np.load(filename+"train_target.npy")
    print(training_y.shape)
    test_x = np.load(filename+"test_data.npy")
    print(test_x.shape)
    test_y = np.load(filename+"test_target.npy")
    print(test_y.shape)
    return training_x, training_y, test_x, test_y

def loadFileBasedTime(filename):
    if filename.find('.txt')!=-1: filename = filename.split('.txt')[0]
    print('=========loadFileBasedTime========:'+ filename)
    training_x = np.load(filename+"_Train_data.npy")
    print(training_x.shape)
    training_y = np.load(filename+"_Train_target.npy")
    print(training_y.shape)
    test_x = np.load(filename+"_Test_data.npy")
    print(test_x.shape)
    test_y = np.load(filename+"_Test_target.npy")
    print(test_y.shape)
    return training_x, training_y, test_x, test_y

def loadFileSplit(filename):
    if filename.find('.txt')!=-1: filename = filename.split('.txt')[0]
    print('=========loadFileSplit========:'+ filename)
    data = np.load(filename+"_data.npy")
    print(data.shape)
    labels = np.load(filename+"_target.npy")
    print(labels.shape)
    training_x, test_x, training_y, test_y\
        = train_test_split(data, labels, test_size = 0.2)
    return training_x, training_y, test_x, test_y

def loadFile(trainFile, testFile):
    if trainFile.find('.txt')!=-1: trainFile = trainFile.split('.txt')[0]
    if testFile.find('.txt')!=-1: testFile = testFile.split('.txt')[0]
    print('=========loadFile(trainFile, testFile)========:'+ trainFile+':'+ testFile)
    training_x = np.load(trainFile+"_data.npy")
    print(training_x.shape)
    training_y = np.load(trainFile+"_target.npy")
    print(training_y.shape)
    test_x = np.load(testFile+"_data.npy")
    print(test_x.shape)
    test_y = np.load(testFile+"_target.npy")
    print(test_y.shape)
    return training_x, training_y, test_x, test_y