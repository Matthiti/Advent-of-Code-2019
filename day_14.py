## PART 1 ##
'''
input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
'''

input = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

'''
input = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""
'''


class Chemical(object):
	def __init__(self, name: str, amount: int):
		self.name = name
		self.amount = amount
		
	def __str__(self) -> str:
		return "%d %s" % (self.amount, self.name)
		
	def __repr__(self) -> str:
		return str(self)
		
	def __eq__(self, other: 'Chemical') -> bool:
		return self.name == other.name
		
	def __hash__(self) -> int:
		return hash(self.name)


class Reaction(object):
	def __init__(self, in_chemicals: [Chemical], out_chemical: Chemical):
		self.in_chemicals = in_chemicals
		self.out_chemical = out_chemical

	def __str__(self) -> str:
		return ''.join([str(i) + ', ' for i in self.in_chemicals]) + "=> " + str(self.out_chemical)

	def __repr__(self) -> str:
		return str(self)


def parse_input(input: str) -> [Reaction]:
	res = []
	reactions = input.split('\n')
	for r in reactions:
		reaction = r.split('=>')
		ins = reaction[0].split(',')
		in_chemicals = []
		for i in ins:
			s = i.strip().split(' ')
			in_chemicals.append(Chemical(s[1], int(s[0])))

		o = reaction[1].strip().split(' ')
		out_chemical = Chemical(o[1], int(o[0]))
		res.append(Reaction(in_chemicals, out_chemical))
	return res


def main(input: str=input) -> int:
	reactions = parse_input(input)
	return ore_to_produce_chemical(Chemical("FUEL", 1), reactions, {})


def ore_to_produce_chemical(chemical: (str, int), reactions: [Reaction], stack: {Chemical: int}) -> int:
	print(stack)
	if chemical.name == 'ORE':
		return chemical.amount

	# chemical = 6C, x = needed amount
	# r = 3A + 4B -> 5C
	# r.out_chemical.amount = 5
	r = find_out_reaction(chemical, reactions)
	
	multiplier = 1
	while chemical.amount > r.out_chemical.amount * multiplier:
		multiplier += 1
			
	diff = r.out_chemical.amount * multiplier - chemical.amount
	if diff > 0:
		if chemical in stack:
			stack[chemical] += diff
		else:
			stack[chemical] = diff

	total = 0
	for i in r.in_chemicals:
		amount_needed = i.amount * multiplier
		if i in stack:
			if stack[i] >= amount_needed:
				stack[i] -= amount_needed
				continue
			else:
				amount_needed -= stack[i]
				stack[i] = 0
		i.amount = amount_needed
		total += ore_to_produce_chemical(i, reactions, stack)
	return total


def find_out_reaction(chemical: (str, int), reactions: [Reaction]) -> Reaction:
	for r in reactions:
		if chemical.name == r.out_chemical.name:
			return r
	return None  # Should never occur

