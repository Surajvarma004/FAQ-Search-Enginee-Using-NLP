import pandas as pd
from utils import question_search
from config import *

df = pd.read_csv(DATA)

q = "how do i make bomb"

df["embd"] = df["embd"].apply(lambda x: eval(x))

res = question_search(q, df, conf=0.50)

print("Similar questions found...")
for i in res:
    print(i)
