import pandas
from multiprocessing import Pool
import datetime
import numpy


elements = 10000000
# testlist = list(range(elements))
string_list = ["Apples", "Bananas", "Carrots"]

word_list = []
import random
for number in range(elements):
    random_number = random.randint(0,len(string_list)-1)
    word_list.append(string_list[random_number])


def testfunction(something):
    if something == "Apples":
        dosomething = something + " are red or green."
    elif something == "Bananas":
        dosomething = something + " are yellow."
    else:
        dosomething = something + " are orange."

    return dosomething


if __name__ == "__main__":

    start2 = datetime.datetime.now()
    result2 = list(map(testfunction, word_list))
    diff2 = datetime.datetime.now() - start2
    print("TIME TAKEN WITHOUT POOL :: " + str(diff2))
