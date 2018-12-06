import datetime

DATETIME_FMT_STR = "[%Y-%m-%d %H:%M" # We split on the ]

class Event:
    def __init__(self, log_entry):
        self.log_entry = log_entry
        self.parse_entry()

    def parse_entry(self):
        time, self.details = map(str.strip, self.log_entry.split(']'))
        self.time = datetime.datetime.strptime(time, DATETIME_FMT_STR)

    def __str__(self):
        formatted_time = datetime.datetime.strftime(self.time, DATETIME_FMT_STR)
        return "{}] {}".format(formatted_time, self.details)

    def __repr__(self):
        return str(self)

class Guard:
    def __init__(self, guard_num):
        self.guard_num = guard_num
        self.shifts = []

    def add_shift(self, shift):
        self.shifts.append(shift)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"Guard({self.guard_num})"

class Shift:
    def __init__(self, start):
        self.start = start
        self.minutes_awake = 0
        self.minutes_asleep = 0
        self.calculate_shift_end()

    def calculate_shift_end(self):
        # shift end is always 00:59 of same day
        end = self.start.replace(hour=0, minute=59)
        if end < self.start:
            end += datetime.timedelta(days=1)
        self.minutes_awake = (end - self.start).seconds // 60
        self.shift_end = end

    def update(self, status, time):
        duration = (self.shift_end - time).seconds // 60
        if status == 'falls asleep':
            self.minutes_awake -= duration
            self.minutes_asleep += duration
        elif status == 'wakes up':
            self.minutes_asleep -= duration
            self.minutes_awake += duration

    def __str__(self):
        return f"Start: {datetime.datetime.strftime(self.start, DATETIME_FMT_STR)}]\tMinutes awake: {self.minutes_awake}\tMinutes asleep: {self.minutes_asleep}"

def main():
    log_entries = open('input.txt').readlines()

    events = []
    for entry in log_entries:
        events.append(Event(entry))

    events.sort(key=lambda x: x.time)
    with open("input_sorted.txt", "w") as fp:
        for event in events:
            fp.write(str(event) + '\n')

    guards = {}
    shift = None
    guard = None
    # Some assumptions:
    # Guard always starts shift awake
    # There is only 1 guard per shift
    # Strict formatting of event puts guard # at index 1 after split(' ')
    for event in events:
        if 'begins shift' in event.details:
            shift = Shift(event.time)
            guard_num = event.details.split()[1]
            guard = guards.get(guard_num, Guard(guard_num))
            guards[guard_num] = guard
            guard.add_shift(shift)
        else:
            guard.shifts[-1].update(event.details, event.time)

    for guard in guards:
        print(f"Guard: {guards[guard]}")
        print("Shifts:")
        for shift in guards[guard].shifts:
            print(f"\t{shift}")    

if __name__ == '__main__':
    main()