# code for parsing signal

with open('signal.txt', 'r', encoding="utf-8") as f:
    signal = f.readline()

test1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test3 = 'nppdvjthqldpwncqszvftbrmjlhg'
test4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def find_start(signal):
    """Find start of signal"""
    for i in range(len(signal)-4):
        start_packet = signal[i:i+4]
        # check if start packet is all unique
        unique_packet = set(start_packet)
        if len(unique_packet) == 4:
            break
    print(f'The start packet is {start_packet} and it arrives complete with the {i+4}th character')

find_start(test1)
find_start(test2)
find_start(test3)
find_start(test4)
find_start(test5)
find_start(signal)

def find_start_message(signal):
    """Find start of message"""
    for i in range(len(signal)-14):
        start_packet = signal[i:i+14]
        # check if start packet is all unique
        unique_packet = set(start_packet)
        if len(unique_packet) == 14:
            break
    print(f'The start message marrke is {start_packet} and it arrives complete with the {i+14}th character')

find_start_message(test1)
find_start_message(test2)
find_start_message(test3)
find_start_message(test4)
find_start_message(test5)
find_start_message(signal)