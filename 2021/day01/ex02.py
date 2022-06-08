def main():
    with open('input.txt') as input:
        lines = input.readlines()
        depths = [int(l) for l in lines]

    increments = 0
    record = depths[0:2]
    for depth in depths[3:]:
        a = sum(record)
        # Update record ("slide the sum")
        record.pop(0)
        record.append(depth)
        b = sum(record)
        if a > b:
            increments += 1
    print(increments)

if __name__ == '__main__':
    main()
