import matplotlib
matplotlib.rcParams = matplotlib.rc_params_from_file('../../matplotlibrc')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import decomposition
from scipy import linalg as la

from solutions import kmeans



iris = load_iris()
X = iris.data
# pre-process
Y = X - X.mean(axis=0)
# get SVD
U,S,VT = la.svd(Y,full_matrices=False)
# project onto the first two principal components
Yhat = U[:,:2].dot(np.diag(S[:2]))
p1, p2 = Yhat[:,0], Yhat[:,1]

def iris_pca():
    plt.scatter(p1,p2, marker='.', color='blue')
    plt.ylim([-4,5])
    plt.xlim([-4,4])
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.savefig('iris_pca.pdf')
    plt.clf()
    
def iris_means():
    means1 = np.array([[ 0.07285021,  1.34415468],
                      [ 1.46512994,  0.60248906],
                      [-1.39915695, -1.97941598]])
    means2 = np.array([[-2.18408621,  2.2533815 ],
                       [-0.84276589, -2.57842716],
                       [ 1.06821566,  1.59168296]])
    
    means,labs,i = kmeans(Yhat,3,init=means1)
    
    setosa = iris.target==0
    versicolor = iris.target==1
    virginica = iris.target==2
    p1, p2 = Yhat[:,0], Yhat[:,1]
    mrkr = []
    for flower, m,n in zip([setosa,versicolor,virginica],['*','.','^'],['Setosa','Versicolor','Virginica']):
        mr = plt.scatter([],[],color='k',marker=m,label=n)
        mrkr.append(mr)
        for i,c in enumerate(['cyan','red','green']):
            msk = np.where(labs[flower]==i)[0]
            if msk.any():
                plt.scatter(p1[flower][msk],p2[flower][msk], marker=m, color=c)
    mrkr.append(plt.scatter(means[:,0],means[:,1],marker='+',s=100,linewidths=2,label="Means"))
    plt.legend(handles=mrkr, loc=2)
    plt.ylim([-4,5])
    plt.xlim([-4,4])
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.savefig("iris_means_1.pdf")
    
    means,labs,i = kmeans(Yhat,3,init=means2)
    
    setosa = iris.target==0
    versicolor = iris.target==1
    virginica = iris.target==2
    p1, p2 = Yhat[:,0], Yhat[:,1]
    mrkr = []
    for flower, m,n in zip([setosa,versicolor,virginica],['*','.','^'],['Setosa','Versicolor','Virginica']):
        mr = plt.scatter([],[],color='k',marker=m,label=n)
        mrkr.append(mr)
        for i,c in enumerate(['cyan','red','green']):
            msk = np.where(labs[flower]==i)[0]
            if msk.any():
                plt.scatter(p1[flower][msk],p2[flower][msk], marker=m, color=c)
    mrkr.append(plt.scatter(means[:,0],means[:,1],marker='+',s=100,linewidths=2,label="Means"))
    plt.legend(handles=mrkr, loc=2)
    plt.ylim([-4,5])
    plt.xlim([-4,4])
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.savefig("iris_means_2.pdf")

if __name__ == "__main__":
    iris_means()
