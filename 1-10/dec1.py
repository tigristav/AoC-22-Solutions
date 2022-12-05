

def go():
    total = []
    result = 0
    with open("dec1input.txt") as f:
        for line in f:
            if line.strip():
                result += int(line)
            else:
                total.append(result)
                result = 0
    total.sort()
    print(total)


if __name__ == "__main__":
    go()
