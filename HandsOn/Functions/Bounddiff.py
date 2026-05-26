def odd():
    oddTotal = 0
    for i in range(1, 1001):
        if i % 2 != 0:
            oddTotal += i
    return oddTotal

def even():
    evenTotal = 0
    for i in range(1, 1001):
        if i % 2 == 0:
            evenTotal += i
    return evenTotal

oddsum = odd()
evensum = even()
diff = abs(evensum - oddsum)

print("The sum of odd numbers from 1 to 1000 is:", oddsum)
print("The sum of even numbers from 1 to 1000 is:", evensum)
print("The absolute difference between the two sums is:", diff)