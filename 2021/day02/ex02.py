def main():
    aim = 0
    depth = 0
    horizontal = 0
    with open('input.txt') as input:
        for line in input:
            direction, x = line.split()
            x = int(x)
            match direction:
                case 'down': 
                    aim += x
                case 'up': 
                    aim -= x
                case 'forward': 
                    horizontal += x
                    depth += aim * x
        print(horizontal * depth)

if __name__ == '__main__':
    main()
