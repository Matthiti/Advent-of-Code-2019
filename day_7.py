## PART 1 ##
import sys
import itertools
from threading import Thread
from queue import Queue

import intcode

program = [
	3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 30, 55, 80, 101, 118, 199, 280, 361,
	442, 99999, 3, 9, 101, 4, 9, 9, 4, 9, 99, 3, 9, 101, 4, 9, 9, 1002, 9, 4, 9,
	101, 4, 9, 9, 1002, 9, 5, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 101, 5, 9, 9,
	1002, 9, 2, 9, 101, 3, 9, 9, 102, 4, 9, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 102,
	2, 9, 9, 101, 5, 9, 9, 102, 3, 9, 9, 101, 3, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 2,
	9, 102, 4, 9, 9, 1001, 9, 3, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9,
	102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
	1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3,
	9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99,
	3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9,
	3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4,
	9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9,
	4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1,
	9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102,
	2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102,
	2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9,
	1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3,
	9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3,
	9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3,
	9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4,
	9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9,
	4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2,
	9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99
]

settings = [0, 1, 2, 3, 4]


def find_max_thruster_signal() -> int:
	global program
	possibilities = itertools.permutations(settings)
	max = 0
	for p in possibilities:
		next_input = 0
		for setting in p:
			#program_copy = program.copy()
			#res = Intcode.run(program, [setting, next_input])
			machine = intcode.Machine(program.copy(), [setting, next_input])
			res = machine.run()
			next_input = res[0]
		if next_input > max:
			max = next_input
	return max
	
	
## PART 2 ##
settings_2 = [5, 6, 7, 8, 9]

def find_max_thruster_signal_with_feedback() -> int:
	possibilities = itertools.permutations(settings_2)
	max = 0
	for p in possibilities:
		next_input = 0
		amplifiers = []
		
		# queues[0] for comm between A and B
		# queues[1] for comm between B and C
		# queues[2] for comm between C and D
		# queues[3] for comm between D and E
		# queues[4] for comm between E and A
		queues = [Queue() for _ in settings_2]
		
		# Start machines
		for i in range(len(p)):
			user_input = [p[i]] # p[i] is the used setting
			if i == 0:
				user_input.append(0)
			machine = intcode.Machine(program.copy(), user_input, queues[i-1], queues[i])
			t = Thread(target = machine.run)
			t.start()
			amplifiers.append(t)
		
		for a in amplifiers:
			a.join()	
		res = queues[-1].get()
		if res > max:
			max = res
	return max
	
#if __name__ == '__main__':
	#last_printed_value()
