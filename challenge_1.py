def multiplesOf3and5(number):
    content = []
    for i in range(1, number):
        if i%3 == 0 or i%5 == 0:
            content.append(i)
    return sum(content)

assert multiplesOf3and5(1000) == 233168
assert multiplesOf3and5(49) == 543
assert multiplesOf3and5(19564) == 89301183
assert multiplesOf3and5(8456) == 16687353