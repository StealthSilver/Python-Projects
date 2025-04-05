# Maximum score

scores = [12,3,4,5,6,7,8,56,4,32,21,1]

print(max(scores))

max =0

for score in scores:
    if score >= max:
        max = score 

print(max)
