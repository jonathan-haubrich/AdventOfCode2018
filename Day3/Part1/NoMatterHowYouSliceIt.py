class Square:
    def __init__(self, side_len):
        self.side_len = side_len
        self.surface = [['.' for _ in range(self.side_len)] for _ in range(self.side_len)]

    def extend(self, required_len):
        if required_len <= self.side_len:
            return
        added_side_len = required_len - self.side_len
        self.surface.extend([list('.' * self.side_len) for _ in range(added_side_len)])
        for row in self.surface:
            row.extend('.' * added_side_len)
        self.side_len = required_len

    def __iadd__(self, pattern):
        req_side_len = max(pattern.req_width, pattern.req_height)
        if req_side_len > self.side_len:
            self.extend(req_side_len)
        for w in range(pattern.width):
            for h in range(pattern.height):
                y = h + pattern.t_offset
                x = w + pattern.l_offset
                if self.surface[y][x] == '.':
                    self.surface[y][x] = '0'
                self.surface[y][x] = str(int(self.surface[y][x]) + 1)
        return self

    def __str__(self):
        s = '\n'.join([''.join(r) for r in self.surface])
        return s

class Pattern:
    def __init__(self, desc_str):
        self.desc_str = desc_str
        self.parse_desc_str()

    def parse_desc_str(self):
        self.pattern_id, square_info = self.desc_str.split('@')
        offsets, dimensions = square_info.split(':')
        self.l_offset, self.t_offset = map(int, offsets.split(','))
        self.width, self.height = map(int, dimensions.split('x'))
        self.req_width = self.l_offset + self.width
        self.req_height = self.t_offset + self.height

    def __str__(self):
        s = []
        h_pad = '.' * self.req_width
        w_pad = '.' * self.l_offset
        for _ in range(self.t_offset):
            s.append(h_pad)
        for i in range(self.height):
            s.append("{}{}{}".format(w_pad, '#' * self.width, w_pad))
        for _ in range(self.t_offset):
            s.append(h_pad)
        return '\n'.join(s)

def main():
    desc_strs = open('input.txt').readlines()

    square = Square(0)
    for ds in desc_strs:
        pattern = Pattern(ds)
        square += pattern

    square_area_overlap = 0
    for row in square.surface:
        for pixel in row:
            if pixel == '.':
                continue
            i = int(pixel)
            if i > 1:
                square_area_overlap += 1

    print(f"Overlapping square area: {square_area_overlap}")

if __name__ == '__main__':
    main()