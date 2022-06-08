def main():
    depth = 0
    horizontal = 0
    with open('input.txt') as input:
        for line in input:
            direction, x = line.split()
            x = int(x)
            match direction:
                case 'forward': horizontal += x
                case 'down': depth += x
                case 'up': depth -= x
        print(horizontal * depth)

if __name__ == '__main__':
    main()
