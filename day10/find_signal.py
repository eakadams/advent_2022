# code for finding signal

with open('test_signal.txt', 'r', encoding="utf-8") as f:
    test_signal = f.read()

with open('signal.txt', 'r', encoding="utf-8") as f:
    signal = f.read()

signal_list = signal.split("\n")
test_signal_list = test_signal.split("\n")
small_test_list = ['noop', 'addx 3', 'addx -5']

def get_signal(signal_list, ncycle):
    """Get signal for a given cycle"""
    # starting conditions
    X = 1
    cycle = 1
    wait = True
    move_index = 0
    for _ in range(ncycle - 1):
        instr = signal_list[move_index]
        if instr == 'noop':
            move_index += 1
        else:
            if wait:
                # on first execution of command
                # set next to be last
                wait = False
            else:
                # reset wait
                wait = True
                signal_change = int(instr.split()[1])
                X += signal_change
                move_index += 1
        cycle += 1
    return X


#print((f"For test signal cycle 20 is {get_signal(test_signal_list, 20)}"
#       f' cycle 60 is {get_signal(test_signal_list, 60)}, '
#       f' cycle 100 is {get_signal(test_signal_list, 100)}, '
#       f' cycle 140 is {get_signal(test_signal_list, 140)}, '
#       f' cycle 180 is {get_signal(test_signal_list, 180)}, '
#       f'cycle 220 is {get_signal(test_signal_list, 220)}'))

cycle_list = [20, 60, 100, 140, 180, 220]

def get_sum_strength(signal_list, cycle_list):
    """Get sum of strengths"""
    sum_strength = 0
    for cycle in cycle_list:
        # print(cycle)
        strength = cycle * get_signal(signal_list, cycle)
        sum_strength += strength

    print(f'The total signal strength is {sum_strength}')


get_sum_strength(test_signal_list, cycle_list)
get_sum_strength(signal_list, cycle_list)


def get_message(signal_list):
    """Get message"""
    # starting conditions
    X = 1
    wait = True
    move_index = 0
    ncycle = 240
    #ncycle = 10
    message = ''
    message_bold = ''
    pix = 0
    for cycle in range(1, ncycle+1):
        if abs(X - pix % 40) <= 1:
            message += '#'
            message_bold += '\N{FULL BLOCK}'
        else:
            message += '.'
            message_bold += ' '
        #print(cycle, X, pix % 40, message[-1])
        instr = signal_list[move_index]
        if instr == 'noop':
            move_index += 1
        else:
            if wait:
                # on first execution of command
                # set next to be last
                wait = False
            else:
                # reset wait
                wait = True
                signal_change = int(instr.split()[1])
                X += signal_change
                move_index += 1
        pix += 1
    print(message[0:40])
    print(message[40:80])
    print(message[80:120])
    print(message[120:160])
    print(message[160:200])
    print(message[200:240])
    for line in range(6):
        print(message_bold[line*40:(line+1)*40])
    return message


get_message(test_signal_list)
get_message(signal_list)