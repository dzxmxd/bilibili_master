import numpy as np
#import random
with open('./bilibili.txt', 'r+',encoding='utf-8') as f:
    lst=[]
    for line in f.readlines():
        lst.append(line.split(','))

mom_ = [int(i[4]) for i in lst[0:50:]]

view = []
reply = []
favorite = []
coin = []
share = []
like = []
time = []
for i in lst[0:50]:
    view.append(float(i[2].strip("万"))*10000)
    reply.append(int(i[8]))
    favorite.append(int(i[9]))
    coin.append(int(i[10]))
    share.append(int(i[11]))
    like.append(int(i[12]))
    #time.append(random.randint(1,50))
    #print(random.randint(1,50))
son_ = [view,reply,favorite,coin,share,like]

mom_ = np.array(mom_)
son_ = np.array(son_)

son_ = son_.T / son_.mean(axis=1)
mom_ = mom_/mom_.mean()

for i in range(son_.shape[1]):
    son_[:,i] = abs(son_[:,i]-mom_.T)

Mmin = son_.min()
Mmax = son_.max()

cors = (Mmin + 0.5*Mmax)/(son_+0.5*Mmax)
print(cors)

Mmean = cors.mean(axis = 0)
print('    播放       评论        收藏        投币        分享       点赞')
print(Mmean)
