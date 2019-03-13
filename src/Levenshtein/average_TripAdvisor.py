import numpy as np

f_name = "DataSets/tripadvisor_review.txt"

data = np.loadtxt(f_name, dtype="float32", delimiter=" ")

avg = np.reshape(np.around(np.mean(data, axis=0), decimals=2), (1,10))
print(avg)
print(avg.shape)

np.savetxt("DataSets/tripadvisor_review_avg.txt", avg, fmt="%0.2f", delimiter=" ")