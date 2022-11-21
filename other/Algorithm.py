import secrets
from sqlite3 import Time
import time


#バブルソートっぽいやつ
time1 = time.time()
for q in range(0,1000):
    sample = [secrets.randbelow(100) for i in range(0,100)]
    k = 101
    while True:
        sum = 0
        k -= 1
        for i in range(1,k):
            if sample[i-1] > sample[i]:
                a = sample[i-1]
                sample[i-1] = sample[i]
                sample[i] = a
                sum += 1

        if sum == 0:
            break

average1 = (time.time() - time1) / 1000



#選択ソート
time2 = time.time()
for q in range(0,1000):
    sample = [secrets.randbelow(1000) for i in range(0,1000)]

    f = 100
    while f > 0:
        max = 0
        for i in range(0,f):
            max = i if sample[max] < sample[i] else max
        a = sample[max]
        sample[max] = sample[i]
        sample[i] = a
        f -= 1

average2 = (time.time()-time2)/1000


#挿入ソート
time3 = time.time()
for q in range(0,1000):
    sample = [secrets.randbelow(1000) for i in range(0,1000)]
    for i in range(1,100):
        for j in range(i-1,-1,-1):
            if sample[j] <= sample[i]:
                sample.insert(j+1,sample[i])
                sample.pop(i+1)
                break
            elif sample[i] < sample[0]:
                sample.insert(0,sample[i])
                sample.pop(i+1)
                break
average3 = (time.time() - time3)/2

print(f"bubble:{average1} select:{average2} insert:{average3}")