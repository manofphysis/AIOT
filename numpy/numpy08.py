import numpy as np
scores = np.array([[99, 93, 60], [98, 82, 93],[93, 65, 81], [78, 82, 81]])
print(scores.sum())
print(scores.sum(axis=0))  # Sum along columns
print(scores.sum(axis=1))  # Sum along rows 
print(scores.mean())
print(scores.mean(axis=0))  # Mean along columns
print(scores.mean(axis=1))  # Mean along rows
print(scores.std())
print(scores.std(axis=0))  # Standard deviation along columns   
print(scores.std(axis=1))  # Standard deviation along rows
print(scores.var())
print(scores.var(axis=0))  # Variance along columns
print(scores.var(axis=1))  # Variance along rows
print(scores.max())
print(scores.max(axis=0))  # Maximum along columns          
print(scores.max(axis=1))  # Maximum along rows
print(scores.min())
print(scores.min(axis=0))  # Minimum along columns          
print(scores.min(axis=1))  # Minimum along rows
