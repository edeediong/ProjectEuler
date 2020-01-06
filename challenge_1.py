def multiples_of_3_and_5(number):
    content = []
    for i in range(1, number):
        if i%3 == 0 or i%5 == 0:
            content.append(i)
    return sum(content)

assert multiples_of_3_and_5(1000) == 233168
assert multiples_of_3_and_5(49) == 543
assert multiples_of_3_and_5(19564) == 89301183
assert multiples_of_3_and_5(8456) == 16687353
