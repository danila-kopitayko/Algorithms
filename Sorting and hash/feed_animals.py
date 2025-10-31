import random

def solution(animals,food):
    animals = sorted(animals)
    food = sorted(food)
    count = 0
    print(f'animals={animals}')
    print(f'food={food}')
    for i in range(len(food)):
        if food[i]>=animals[count]:
            count+=1
        if count==len(animals):
            return count
    return count

def main():
    n = random.randint(1,10)
    f = random.randint(1,10)
    animals = []
    food = []
    for i in range(n):
        animals.append(random.randint(1,10))
    for i in range(f):
        food.append(random.randint(1,10))
    #print(animals,food)
    print(solution(animals,food))

    return 0

main()

