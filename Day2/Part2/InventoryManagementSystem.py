
def main():
    box_ids = open("input.txt").readlines()

    differences = 0
    for box_id in box_ids:
        box_id_len = len(box_id)
        for comp_box_id in box_ids:
            if box_id_len != len(comp_box_id):
                continue

            differences = 0
            for i in range(box_id_len):
                if box_id[i] != comp_box_id[i]:
                    differences += 1

            if differences == 1:
                for i in range(box_id_len):
                    if box_id[i] == comp_box_id[i]:
                        print(box_id[i], end='')
                print()
                break
        if differences == 1:
            break            

if __name__ == '__main__':
    main()