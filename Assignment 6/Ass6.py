#Task 1
numbers = []

while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    numbers.append(int(entry))

numbers.sort(reverse=True)
print("Top 5 numbers:", numbers[:5])

#Task 2
numbers = []

while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    numbers.append(int(entry))

numbers.sort(reverse=True)
print("Top 5 numbers:", numbers[:5])

#Task 3
names = set()

while True:
    name = input("Enter a name (empty to quit): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("Names entered:")
for n in names:
    print(n)

#Task 4
def word_frequency(text):
    freq = {}
    for word in text.split():
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq

sample = "This is a test. This test is simple."
print(word_frequency(sample))

#Task 5
def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]

original = [1, 2, 3, 4, 5, 6]
filtered = remove_odds(original)

print("Original:", original)
print("Without odds:", filtered)

#Task 6
import random

N = int(input("How many random points? "))
inside = 0

for _ in range(N):
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside += 1

pi_approx = 4 * inside / N
print("Approximation of pi:", pi_approx)
