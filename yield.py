# https://realpython.com/introduction-to-python-generators/


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


get = infinite_sequence()
print(get)

print(next(get))
print(next(get))
print(next(get))
print(next(get))


def infinite_sequence2():
    num = 0
    while True:
        return num
        num += 1


print("infinite_sequence2", infinite_sequence2())
