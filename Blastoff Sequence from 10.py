import time

for i in range(10, 0, -1) :
    if i <= 3:
        print(f'{i}...')
        time.sleep(1)
        continue
    print(i)
    time.sleep(1)
print('Blastoff!')