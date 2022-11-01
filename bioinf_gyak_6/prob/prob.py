from utils import rand_from_gc
import math

with open("prob_test_2", "r") as f:
    s = f.readline().strip()
    gcs = list(f.readline().split(" "))
    print(s)
    print(gcs)
    probs = [math.log(rand_from_gc(s, float(gcs[i])), 10) for i in range(len(gcs))]
    print(*probs)
