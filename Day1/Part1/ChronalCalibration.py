
def main():
    freq_changes = open("input.txt").readlines()

    result = 0
    for fc in freq_changes:
        result += int(fc.strip())

    print(f"Resulting frequency: {result}")

if __name__ == '__main__':
    main()