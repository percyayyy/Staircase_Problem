stairs = int(input())

primes = [1]
count = []

for i in range(2, stairs + 1):
    checkPrime = 0
    for j in range(2, i):
        if (i % j) == 0:
            checkPrime += 1
    if checkPrime == 0:
        primes.append(i)

for i in range(stairs + 1):
    count.append(0)

count[0] = 1

for i in range(1, stairs + 1):
    accumulate = 0
    for j in range(len(primes)):
        if i - primes[j] >= 0:
            accumulate += count[i - primes[j]]
    count[i] = accumulate

print(count[stairs])
