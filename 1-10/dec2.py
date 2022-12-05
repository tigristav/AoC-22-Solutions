
def go1():
    result = 0
    with open('dec2input.txt') as f:
        for line in f:
            tokens = line.split(" ")
            them = tokens[0]
            me = tokens[1].strip()
            
            if (them == 'A' and me == 'Y') or (them == 'B' and me == 'Z') or (them == 'C' and me == 'X'):
                result += 6
            elif (them == 'A' and me == 'X') or (them == 'B' and me == 'Y') or (them == 'C' and me == 'Z'):
                result += 3 
            elif (them == 'A' and me == 'Z') or (them == 'B' and me == 'X') or (them == 'C' and me == 'Y'):
                result += 0 
                
            if me == 'X':
                result += 1
            elif me == 'Y':
                result += 2
            elif me == 'Z':
                result += 3
                
    print(result)

def go2():
    result = 0
    with open('dec2input.txt') as f:
        for line in f:
            tokens = line.split(" ")
            them = tokens[0]
            me = tokens[1].strip()
             
            if (me == "Z" and them == "A") or (me == "Y" and them == "B") or (me == "X" and them == "C"): #paper
                result += 2
            elif (me == "Z" and them == "C") or (me == "Y" and them == "A") or (me == "X" and them == "B"): #rock
                result += 1 
            elif (me == "Z" and them == "B") or (me == "Y" and them == "C") or (me == "X" and them == "A"): #scissor
                result += 3 
            
                
            if me == 'X':
                result += 0
            elif me == 'Y':
                result += 3
            elif me == 'Z':
                result += 6
                
    print(result)


if __name__ == '__main__':
#    go1()
#    go2()
    pass