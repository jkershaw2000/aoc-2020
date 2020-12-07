import string
from timeit import default_timer as timer

def get_input():
    with open("./day6/6.in","r") as f:
        return f.read().split("\n\n")

def p1():
    res = []
    data = [group.replace("\n","") for group in get_input()]
    for group in data:
        res.append(len(set(group)))
    return sum(res)

def p2():
    res = []
    ques = set(string.ascii_lowercase)
    data  = [group.split("\n")for group in get_input()]
    for group in data:
        for line in group:
            ques &= set(line) # removes questions that werent answered yes. 
        res.append(len(ques))
        ques = set(string.ascii_lowercase)
    return sum(res)


print("Day 6: Custom Customs")

p1start = timer()
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2()
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")