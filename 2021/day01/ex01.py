def main():
    with open('input.txt') as input:
        lines = input.readlines()
        depths = [int(l) for l in lines]

    increments = 0
    prev_depth = depths[0]
    for depth in depths[1:]:
        if depth > prev_depth:
            increments += 1
        prev_depth = depth
    print(increments)

if __name__ == '__main__':
    main()
