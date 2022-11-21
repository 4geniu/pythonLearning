import secrets

sample = [secrets.randbelow(500) for q in range(0,500)]
print(sample)
for i in range(1,500):
    for j in range(i-1,-1,-1):
        if sample[j] <= sample[i]:
            print(f"{sample[j]}<{sample[i]}<{sample[j+1]}")
            sample.insert(j+1,sample[i])
            sample.pop(i+1)
            break
        elif sample[i] < sample[0]:
            sample.insert(0,sample[i])
            sample.pop(i+1)
            break

print(sample)