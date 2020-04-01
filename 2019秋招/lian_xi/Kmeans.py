
import numpy as np

def kmeans(k,data):
    m, n = data.shape
    classAss=np.mat(np.zeros((m,2)))
    # 1.随机选择k个样本点作为聚类中心
    centers=np.mat(np.zeros((k,n)))
    for j in range(n):
        minj=min(data[:,j])
        rangej=float(max(data[:,j])-minj)
        centers[:,j]=minj+rangej*np.random.rand(k,1)
    classChanged=True

    while classChanged:
        classChanged=False
        for i in range(m):
            minDist=float("inf")
            minIndex=-1
            for j in range(k):
                distij=(centers[j,:]-data[i,:])**2
                if distij<minDist:
                    minDist=distij
                    minIndex=j
            if classAss[i,0]!=minIndex:
                classChanged=True
            classAss[i,:]=minIndex,minDist

        for center in range(k):
            pts=data[np.nonzero(classAss[:,0].A==center)[0]]
            centers[center,:]=np.mean(pts,axis=0)
    return  centers,classAss


def kmeans(k,data):
    m,n=data.shape
    classAss=np.mat(np.zeros(m,2))#第一列保存类别，第二列保存最小距离
    #1.随机选择聚类中心
    centers=np.mat(np.zeros((k,n)))
    for j in range(n):
        minj=min(data[:,j])
        rangej=max(data[:,j])-min(data[:,j])
        centers[:,j]=minj+np.random.rand(k,1)*rangej

    classChanged=True
    while classChanged:
        classChanged=False
        for i in range(m):
            minIndex=-1
            minDist=np.inf
            for j in range(k):
                disij=(data[i,:]-centers[j,:])**2
                if minDist>disij:
                    minDist=disij
                    minIndex=j
            if classAss[i,0]!=minIndex:
                classChanged=True
            classAss[i,:]=minIndex,minDist

        for center in centers:
            pts=data[np.nonzeros(classAss[:,0].A==center)[0]]
            centers[center,:]=np.mean(pts,axis=0)
    return classAss,centers

def knn(k,data,x):
    data_x=data[:-1]
    data_y=data[-1]
    data_size=data.shape[0]
    diff=np.tile(x,(data_size,1))
    sd=(diff-data_x)**2
    dis=sd.sum(axis=1)
    sdis=dis**0.5
    sorted_indices=sdis.argsort()
    class_count={}
    for i in range(k):
        vote_label=data_y[sorted_indices[i]]
        class_count[vote_label]=class_count.get(vote_label,0)+1
    class_count=sorted(class_count.items(),key=lambda x:x[1])

    return class_count

def kmeans(k,data):
    m,n=data.shape
    classAss=np.mat(np.zeros(m,2))
    centers=np.mat(np.zeros((k,n)))
    for j in range(n):
        minj=min(data[:,j])
        rangej=max(data[:,j])-minj
        centers[:,j]=minj+rangej*np.random.rand(k,1)

    classChanged=True
    while classChanged:
        classChanged=False
        for i in range(m):
            minIndex=-1
            minDis=np.inf
            for j in range(k):
                disij=(centers[j,:]-data[i,:])**2
                if minDis>disij:
                    minDis=disij
                    minIndex=j
            if classAss[i,0]!=minIndex:
                classChanged=True
            classAss[i,:]=minIndex,minDis

        for c in range(k):
            pts=data[np.nonzeros(classAss[:,0].A==c)[0]]
            centers[c,:]=np.mean(pts,axis=0)
    return classAss,centers
