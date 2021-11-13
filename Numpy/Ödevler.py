import numpy as np
soru1 = np.array([10,15,30,45,60])
soru2 = np.arange(5,15)
soru3 = np.arange(50,100,5)
soru4 = np.zeros(10,dtype=np.int)
soru5 = np.ones(10,dtype=np.int)
soru6 = np.linspace(0,100,5,dtype=np.int)
soru7 = np.random.randint(10,30,5)
soru8 = np.random.randn(10)
soru9 = np.random.randint(10,50,(3,5))
soru10row = np.sum(soru9,axis=0)
soru10column = np.sum(soru9,axis=1)
soru11max = soru9.max()
soru11min = soru9.min()
soru11mean = soru9.mean()
soru12 = soru9.argmax()
soru13 = np.arange(10,20)[:3]
soru14 = np.arange(10,20)[::-1]
soru15 = np.arange(10,20).reshape(2,5)[0]
soru16 = np.arange(10,20).reshape(2,5)[1][3]
soru17 = np.arange(10,20).reshape(2,5)**2
soru18ilk = np.random.randint(-50,50,10)
soru18son = soru18ilk % 2 == 0
soru19 = np.arange(7,42,2)
soru20 = np.random.randint(1,10,(4,4))
soru21 = np.linspace(0.1,1,10)
soru22 = np.arange(0,25).reshape(5,5)[1:3,2:4]
print(soru22)
