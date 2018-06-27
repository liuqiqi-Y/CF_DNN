#import scipy.sparse as sp
import pandas as pd
import numpy as np
import random
#from sklearn.model_selection import train_test_split
#users_Name=['user_id','gender','age','work','zip']
ratings_Name=['user_id','movies_id','ratings','timeStamp']
#movie_Name=['movie_id','title','calss']
#users=pd.read_table('users.dat',sep='::',header=None,names=users_Name,engine='python')
ratings=pd.read_table('u.data',sep='\t',header=None,names=ratings_Name,engine='python')
#movies=pd.read_table('movies.dat',sep='::',header=None,names=movie_Name,engine='python')
#print('评分表记录数：',len(ratings))
#print('**********用户表前五条记录**********')
#print(users.head(5))
#print('**********评分表前五条记录**********')
#print(ratings[:6])
#print('********电影表前五条记录************')
#print(movies.head(5))
#x=np.array(ratings)
#print(x)

#trainRatings,testRatings = train_test_split(ratings,test_size=0.2)

trainRatingsPivot = pd.pivot_table(ratings[['user_id','movies_id','ratings']],columns=['movies_id'],index=['user_id'],values='ratings',fill_value=0)
#moviesMap = dict(enumerate(list(trainRatingsPivot.columns)))
#usersMap = dict(enumerate(list(trainRatingsPivot.index)))
ratingValues = trainRatingsPivot.values.tolist()

trainRatingsPivot1 = pd.pivot_table(ratings[['user_id','movies_id','ratings']],columns=['user_id'],index=['movies_id'],values='ratings',fill_value=0)
#usersMap1 = dict(enumerate(list(trainRatingsPivot1.columns)))
#moviesMap1 = dict(enumerate(list(trainRatingsPivot1.index)))
ratingValues1 = trainRatingsPivot1.values.tolist()


def vectorized_result(m):
	e=np.zeros((5,1))
	e[m-1]=1
	return(e)
def load_data():
	train_data=[]
	train_data_s=[]
	for i in ratingValues:
		k=-1
		for j in i:
			k+=1
			if j!=0:
				tem=np.reshape(i+ratingValues1[k],(2625,1))
				train_data.append(tem)
				train_data_s.append(vectorized_result(j))
	data=list(zip(train_data,train_data_s))
	random.shuffle(data)
	traindata=data[:90000]
	testdata=data[90000:]
	return(traindata,testdata)
if __name__ == '__main__':
	td,ted=load_data()
	print(td[9])
