
import numpy as np

def knn(k,x,data):
    data_size=data.shape[0]
    data_x=data[:-1]
    data_y=data[-1]
    diffMat=np.tile(x,(data_size,1))#生成多个x
    sd=(diffMat-data_x)**2
    dis=sd.sum(axis=1)#按行求和
    sdis=dis**0.5
    sorted_dis=sdis.argsort()#返回升序索引
    class_count={}
    for i in range(k):
        vote_label=data_y[sorted_dis[i]]
        class_count[vote_label]=class_count.get(vote_label)+1
    sorted_label=sorted(class_count.items(),key=lambda x:x[1])
    return sorted_label[0][0]

def knn(x,k,data):
    data_x=data[:-1]
    data_y=data[-1]
    data_size=data.shape[0]
    diff=np.tile(x,(data_size,1))
    sd=(diff-data_x)**2
    dis=sd.sum(axis=1)#按行求和
    sdis=dis**0.5
    sorted_indices=sdis.argsort()#升序索引
    class_count={}
    for i in range(k):
        vote_label=data_y[sorted_indices[i]]
        class_count[vote_label]=class_count.get(vote_label,0)+1
    class_count=sorted(class_count.items(),key=lambda x:x[1])
    return class_count[0][0]