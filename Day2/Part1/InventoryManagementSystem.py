from collections import Counter
def main():
    box_ids = open("input.txt").readlines()

    totals = {}
    for bi in box_ids:
        counter = Counter(list(bi.strip()))
        counts = set(counter.values())
        for c in counts:
            try:
                totals[c] += 1
            except:
                totals[c] = 1

    checksum = totals[2] * totals[3]

    print(f"Checksum: {checksum}")

if __name__ == '__main__':
    main()