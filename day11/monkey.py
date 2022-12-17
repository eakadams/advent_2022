# code for tacking monkeys

# read in monkeys
def read_monkeys(input):
    with open(input, 'r', encoding="utf-8") as f:
        monkeys = f.read()
    return monkeys.split("\n\n")


# take an object based approach to monkeys
class Monkey(object):
    """Monkey class
    In addition to defining with input,
    want methods for inspecting / testing / tossing / receiving
    """
    def __init__(self, monkeyinfo):
        input_lines = monkeyinfo.split('\n')
        #print(input_lines)
        item_line = input_lines[1]
        self.items = [int(x.strip()) for x in item_line.split(":")[1].split(',')]
        operation_line = input_lines[2].split(' ')
        self.operand1 = operation_line[5]
        self.operator = operation_line[6]
        self.operand2 = operation_line[7]
        test_line = input_lines[3].split(' ')
        self.test_divisor = int(test_line[-1])
        true_line = input_lines[4].split(' ')
        self.true_toss = int(true_line[-1])
        false_line = input_lines[5].split(' ')
        self.false_toss = int(false_line[-1])
        self.held_item = None
        self.n_inspect = 0

    def inspect(self):
        """monkey inspects first item"""
        try:
            # get item
            self.held_item = self.items.pop(0)
            # print(f"Original worry is {self.held_item}")
            # inspect and increase worry
            if self.operand2 == 'old':
                if self.operator == '+':
                    self.held_item = self.held_item + self.held_item
                else:
                    self.held_item = self.held_item * self.held_item
            else:
                if self.operator == '+':
                    self.held_item = self.held_item + int(self.operand2)
                else:
                    self.held_item = self.held_item * int(self.operand2)
            # print(f"After inspection worry is {self.held_item}")
            # print(f"Relief reduces worry to {self.held_item}")
            self.n_inspect += 1
        except:
            print("Monkey has no items to inspect")

    def worry_redux(self, part, lcm = None):
        if part == 'part1':
            self.held_item = self.held_item // 3
        if part == 'part2':
            # used reddit to help me figure out how to do this
            # don't need worry value at all, so just don't want it to
            # affect monkey behavior, hence lcm (or rough appox, doesn't matter)
            self.held_item = self.held_item % lcm

    def toss(self):
        """ Get index of monkey to toss to"""
        if (self.held_item % self.test_divisor) == 0:
            toss_monkey = self.true_toss
        else:
            toss_monkey = self.false_toss
        return toss_monkey, self.held_item

    def catch(self, new_item):
        """ Catch a new_item with given worry value"""
        self.items.append(new_item)


def part1(input, nrounds):
    split_monkeys = read_monkeys(input)
    monkey_list = []
    for monkey in split_monkeys:
        monkey_list.append(Monkey(monkey))
        # do this as list comprehension?
    for round in range(nrounds):
        for monkey in monkey_list:
            for _ in range(len(monkey.items)):
                monkey.inspect()
                monkey.worry_redux('part1')
                toss_monkey, toss_item = monkey.toss()
                # print(toss_monkey, toss_item)
                monkey_list[toss_monkey].catch(toss_item)
    for monkey in monkey_list:
        print(monkey.items)
    ninspect_list = []
    for i, monkey in enumerate(monkey_list):
        print(f"Monkey {i} inspected items {monkey.n_inspect} times")
        ninspect_list.append(monkey.n_inspect)
    ninspect_list.sort()
    print(ninspect_list[-1]*ninspect_list[-2])

part1('test_monkeys.txt',20)
part1('monkeys.txt',20)

def part2(input, nrounds):
    split_monkeys = read_monkeys(input)
    monkey_list = []
    for monkey in split_monkeys:
        monkey_list.append(Monkey(monkey))
        # do this as list comprehension?
    divisor_vals = [m.test_divisor for m in monkey_list]
    lcm = 1
    for val in divisor_vals:
        lcm *= val
    for round in range(nrounds):
        for monkey in monkey_list:
            for _ in range(len(monkey.items)):
                monkey.inspect()
                monkey.worry_redux('part2', lcm)
                toss_monkey, toss_item = monkey.toss()
                # print(toss_monkey, toss_item)
                monkey_list[toss_monkey].catch(toss_item)
        if round % 500 == 0:
            print(f"Starting round {round}")
    for monkey in monkey_list:
        print(monkey.items)
    ninspect_list = []
    for i, monkey in enumerate(monkey_list):
        print(f"Monkey {i} inspected items {monkey.n_inspect} times")
        ninspect_list.append(monkey.n_inspect)
    ninspect_list.sort()
    print(ninspect_list[-1]*ninspect_list[-2])

part2('test_monkeys.txt',10000)
part2('monkeys.txt',10000)