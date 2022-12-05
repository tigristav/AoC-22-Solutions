
STACKS = {
    1: ['G', 'T', 'R', 'W'],
    2: ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'],
    3: ['C', 'L', 'T', 'S', 'G', 'M'],
    4: ['J', 'H', 'D', 'M', 'W', 'R', 'F'],
    5: ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'],
    6: ['P', 'J', 'D', 'N', 'F', 'M', 'S'],
    7: ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'],
    8: ['R', 'T', 'B'],
    9: ['H', 'N', 'W', 'L', 'C'],
}

def del1():
    global STACKS
    with open('dec5input.txt') as file:
        for line in file:
            numbers = line.split()[1::2]
            numbers = [int(x) for x in numbers]
            fromStack = STACKS.get(numbers[1])
            toStack = STACKS.get(numbers[2])
            for x in reversed(fromStack[-numbers[0]::]):
                toStack.append(x)
            del fromStack[-numbers[0]::]
    
    print(f'{STACKS.get(1)[-1]} {STACKS.get(2)[-1]} {STACKS.get(3)[-1]} {STACKS.get(4)[-1]} {STACKS.get(5)[-1]} {STACKS.get(6)[-1]} {STACKS.get(7)[-1]} {STACKS.get(8)[-1]} {STACKS.get(9)[-1]}')
            
def del2():
    global STACKS
    with open('dec5input.txt') as file:
        for line in file:
            numbers = line.split()[1::2]
            numbers = [int(x) for x in numbers]
            fromStack = STACKS.get(numbers[1])
            toStack = STACKS.get(numbers[2])
            if numbers[0] == 1:    
                for x in reversed(fromStack[-numbers[0]::]):
                    toStack.append(x)
            else:
                for x in fromStack[-numbers[0]::]:
                    toStack.append(x)
            del fromStack[-numbers[0]::]
    
    print(f'{STACKS.get(1)[-1]} {STACKS.get(2)[-1]} {STACKS.get(3)[-1]} {STACKS.get(4)[-1]} {STACKS.get(5)[-1]} {STACKS.get(6)[-1]} {STACKS.get(7)[-1]} {STACKS.get(8)[-1]} {STACKS.get(9)[-1]}')



if __name__ == '__main__':
#    del1()
    del2()