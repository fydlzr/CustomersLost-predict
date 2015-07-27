__author__ = 'haha'
# -*- coding: utf-8 -*-

from sklearn.metrics import precision_recall_curve, roc_curve, auc, precision_recall_fscore_support
from sklearn.metrics import classification_report
import time


#准确率与召回率
def getReport(clf, test_data, test_labels):
    time1 = time.time()
    answer = clf.predict_proba(test_data)[:,1]
    time2 = time.time()
    print('PredictTime: %f' % (time2-time1))
    precision, recall, thresholds = precision_recall_curve(test_labels, answer)
    report = answer > 0.5
    print(classification_report(test_labels, report, target_names = ['neg', 'pos'],digits = 6))

def getPRF(predict_labels, test_labels):
    # tp = 0
    # tn = 0
    # fp = 0
    # fn = 0
    # for i in range(len(predict_labels)):
    #     if predict_labels[i]== test_labels[i]==1: tp +=1
    #     if predict_labels[i]== test_labels[i]==0: tn +=1
    # print(tp, tn)

    p,r,f,s = precision_recall_fscore_support(test_labels, predict_labels, average=None)
    print(p,r,f,s)
    return p,r,f,s
