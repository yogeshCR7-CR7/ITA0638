# FIND-S Algorithm

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# number of attributes
n = len(data[0]) - 1

# initialize most specific hypothesis
hypothesis = ['0'] * n

for sample in data:
    if sample[-1] == 'Yes':   # consider only positive examples
        for i in range(n):
            if hypothesis[i] == '0':
                hypothesis[i] = sample[i]
            elif hypothesis[i] != sample[i]:
                hypothesis[i] = '?'

print("Most specific hypothesis is:")
print(hypothesis)
