
def main():
    freq_changes = open("input.txt").readlines()

    result = current_freq = 0
    reached = {}
    while True:
        result += int(freq_changes[current_freq % len(freq_changes)].strip())
        if reached.get(result):
            break
        reached[result] = current_freq
        current_freq += 1

    print(f"Freq reached twice: {result}")

if __name__ == '__main__':
    main()