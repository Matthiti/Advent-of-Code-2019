import math

## PART 1 ##

input = """14 LQGXD, 6 TDLQ => 9 VGLV
1 WBQF, 2 JZKMJ => 5 TRSK
5 MGHZ, 5 ZLDQF => 8 HMVG
1 JWQH, 1 QFBC, 2 ZXVNM => 8 JFJZH
8 QTPX, 8 LDLWS => 6 NVZPS
2 QPWF, 1 PRWSM => 5 WHWF
1 QPWF, 8 LDLWS => 5 LZBQ
127 ORE => 1 MDPJB
4 WHWF => 4 KQHW
1 QBCKX, 3 TMTH => 4 WLFTZ
15 NPMPT, 4 TMTH => 6 QFBC
12 MDPJB => 9 PRWSM
5 QXHFH, 3 LCDVR, 24 MWFP, 1 MSFV, 1 BPDJL, 3 LQGXD, 2 DVGW => 2 KCPSH
6 FPZXN, 1 FQSK, 3 TMTH => 1 FBHW
25 PRWSM => 1 MGHZ
6 XWKXC, 5 TMTH, 1 PZTGX => 6 NTQZ
3 BPDJL, 3 DJWCL, 2 JZKMJ => 7 MWFP
5 JFJZH => 3 DJWCL
22 WRNJ, 12 TRSK => 5 TBGJC
3 HKWP => 1 PDRN
3 JWQH => 5 JZKMJ
4 WBQF => 2 BJNS
1 GNBQ => 9 FQSK
8 HMVG, 1 HQHD => 5 NJFNC
7 QBCKX, 1 FQSK => 9 NDCQ
3 XWKXC, 7 QFBC, 3 GPFRS, 2 LPQZ, 2 LQGXD, 20 LZKM, 1 QRTH => 8 TDTKT
1 QTPX => 3 LPQZ
2 QGVQC, 14 LDLWS => 1 NPMPT
1 QRTH, 7 BPDJL => 7 XWKXC
9 WLFTZ, 8 TDLQ => 6 GKPK
4 GNBQ => 3 QXHFH
3 TBGJC, 1 LPQZ => 3 DVGW
3 NDCQ, 1 KGZT => 7 FPZXN
36 WLFTZ, 1 KCPSH, 1 GKPK, 1 TDTKT, 3 CSPFK, 27 JZKMJ, 5 VGLV, 39 XWKXC => 1 FUEL
115 ORE => 7 QGVQC
21 NTQZ, 11 HQHD, 33 JFJZH, 3 NJFNC, 3 MSFV, 1 TRSK, 7 WRNJ => 9 CSPFK
3 DVGW => 4 TDLQ
5 FPZXN => 6 WRNJ
10 TSDLM, 17 XDKP, 3 PDRN => 2 HQHD
1 PCWS => 3 PZTGX
2 QXHFH => 5 JWQH
17 KQHW => 2 WBQF
139 ORE => 5 LDLWS
3 TSDLM => 9 KGZT
16 NPMPT => 3 QTPX
3 DVGW, 5 KVFMS, 3 WLFTZ => 6 GPFRS
1 PZTGX, 2 LCDVR, 13 TBGJC => 6 LZKM
5 ZXVNM, 2 QXHFH => 4 MSFV
4 XDKP, 7 FBHW, 2 PCWS => 3 LCDVR
3 TRSK => 7 KVFMS
10 LDLWS => 9 TMTH
2 TBGJC => 6 LQGXD
2 TRSK => 6 ZXVNM
4 KQHW, 1 NVZPS => 8 ZLDQF
2 LZBQ => 4 QBCKX
7 QBCKX => 6 TSDLM
152 ORE => 3 QPWF
2 TSDLM, 8 WHWF => 3 HKWP
19 FQSK => 8 QRTH
19 QTPX => 3 GNBQ
4 PDRN, 12 HKWP, 4 PCWS => 3 XDKP
6 LZBQ, 19 BJNS => 5 BPDJL
5 HKWP, 6 NVZPS => 3 PCWS"""


class Chemical(object):
	def __init__(self, name: str, amount: int):
		self.name = name
		self.amount = amount
		
	def __str__(self) -> str:
		return "%d %s" % (self.amount, self.name)
		
	def __repr__(self) -> str:
		return str(self)
		
	def __eq__(self, other: 'Chemical') -> bool:
		return self.name == other.name and self.amount == other.amount
		
	def __hash__(self) -> int:
		return hash((self.name, self.amount))


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


def ore_to_produce_chemical(chemical: (str, int), reactions: [Reaction], stack: {str: int}) -> int:
	if chemical.name == 'ORE':
		return chemical.amount

	# chemical = 6C, x = needed amount
	# r = 3A + 4B -> 5C
	# r.out_chemical.amount = 5
	r = find_out_reaction(chemical, reactions)
	
	multiplier = math.ceil(chemical.amount / r.out_chemical.amount)
			
	diff = r.out_chemical.amount * multiplier - chemical.amount
	if diff > 0:
		if chemical.name in stack:
			stack[chemical.name] += diff
		else:
			stack[chemical.name] = diff

	total = 0
	for i in r.in_chemicals:
		amount_needed = i.amount * multiplier
		if i.name in stack:
			if stack[i.name] >= amount_needed:
				stack[i.name] -= amount_needed
				continue
			else:
				amount_needed -= stack[i.name]
				stack[i.name] = 0
		total += ore_to_produce_chemical(Chemical(i.name, amount_needed), reactions, stack)
	return total


def find_out_reaction(chemical: (str, int), reactions: [Reaction]) -> Reaction:
	for r in reactions:
		if chemical.name == r.out_chemical.name:
			return r
	return None  # Should never occur


## PART 2 ##
# Done by adjusting and trying fuel_amount #
def main_2(input: str = input) -> int:
	reactions = parse_input(input)
	fuel_amount = 1120408
	return ore_to_produce_chemical(Chemical("FUEL", fuel_amount), reactions, {})
