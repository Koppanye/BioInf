from utils import hamming

with open("hamm_test_2", "r") as f:
    s = f.readline().strip()
    t = f.readline().strip()
    print(hamming(s,t))
