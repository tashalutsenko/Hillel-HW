n = int(input('Enter number: '))

counter = 0
i = 1
sum = 0
while counter < n:
    counter += 1
    if counter % 3 == 0:
        continue
    i = counter**3
    sum += i
print(f"Total sum: {sum} ")

sum = 0
for i in range(1, n+1):
    if not i % 3 == 0:
        i **= 3
        sum += i
print(f"Total sum: {sum} ")