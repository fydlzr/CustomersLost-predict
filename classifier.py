# -*- coding: utf-8 -*-
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve, roc_curve, auc
from sklearn.metrics import classification_report
import sys
import time
from getData import getData
import toNpy
from loadFile import *
from getResult import *


def fitModels(training_data, training_labels, test_data, test_labels):
    print('=========fitModels========:')

    # print('RandomForestClassifier:')
    # clf =RandomForestClassifier(n_estimators=100)
    # clf.fit(training_data, training_labels)  # 训练模型
    # getReport(clf, test_data, test_labels)
    # print('='*50)

    # print('GradientBoostingClassifier: ')
    # gbdt = GradientBoostingClassifier()
    # gbdt.fit(training_data, training_labels)
    # getReport(gbdt, test_data, test_labels)
    # print('='*50)

    # print('MultinomialNB: ')
    # clf =MultinomialNB()
    # clf.fit(training_data, training_labels)  # 训练模型
    # getReport(clf, test_data, test_labels)
    # print('='*50)
    #
    # print('GaussianNB: ')
    # clf =GaussianNB()
    # clf.fit(training_data, training_labels)  # 训练模型
    # getReport(clf, test_data, test_labels)
    # print('='*50)

    print('LogisticRegression: ')
    lr =LogisticRegressionCV()
    lr.fit(training_data, training_labels)  # 训练模型
    print(lr)
    getReport(lr, test_data, test_labels)
    print('='*50)

    print('LinearSVC: ')
    linSVC =LinearSVC()
    linSVC.fit(training_data, training_labels)  # 训练模型
    predict_labels = linSVC.predict(test_data)  # 预测训练集
    getPRF(predict_labels, test_labels)
    print('='*50)
    
    # print('svm: ')
    # clf =svm.SVC()
    # clf.fit(training_data, training_labels)  # 训练模型
    # getReport(clf, test_data, test_labels)
    # print('='*50)

    # print('DecisionTreeClassifier: ')
    # clf =tree.DecisionTreeClassifier()
    # clf.fit(training_data, training_labels)  # 训练模型
    # getReport(clf, test_data, test_labels)
    # print('='*50)

    return lr, linSVC




if __name__ =='__main__':
    # if len(sys.argv)>1:
    #     print('======Classifier======')
    #     filename = sys.argv[1]
    #     dataFile = getData(30,30,filename)
    #     print(dataFile)
    #     toNpy.saveNpy(dataFile)
    sys.stdout.write('Example: python classifier.py filename')
    print('='*50)
    # filename = 'data\\dataSet.txt'
    filename = '5'
    training_data, training_labels, test_data, test_labels = loadFile('data\\'+filename+'Train.txt', 'data\\'+filename+'Test.txt')
    # training_data, training_labels, test_data, test_labels = loadFileBasedTime(filename)
    # training_data, training_labels, test_data, test_labels = loadFile(filename)
    lr, linSVC = fitModels(training_data, training_labels, test_data, test_labels)







