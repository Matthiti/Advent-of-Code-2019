## PART 1 ##
MIN_BOUND = 158126
MAX_BOUND = 624574


def password_possibilities() -> int:
	result = 0
	number = MIN_BOUND
	while number < MAX_BOUND:
		if is_increasing(number) and has_double(number):
			result += 1
		number += 1
	return result


def is_increasing(number: int) -> bool:
	string = str(number)
	for i in range(len(string) - 1):
		if string[i] > string[i + 1]:
			return False
	return True


def has_double(number: int) -> bool:
	string = str(number)
	return len(set(string)) < len(string)


#if __name__ == '__main__':
#	print(password_possibilities())


## PART 2 ##
def adjacent_digits_not_part_of_larger_group(number: int) -> bool:
	result = False
	string = str(number)
	previous = string[0]
	part_of_larger_group = False
	for i in range(1, len(string)):
		if previous == string[i]:
			if result or part_of_larger_group:
				result = False
				part_of_larger_group = True
			else:
				result = True
				part_of_larger_group = False
		elif result and not part_of_larger_group:
			return True
		else:
			part_of_larger_group = False
			result = False
		previous = string[i]
	return result and not part_of_larger_group


def new_password_possibilites() -> int:
	result = 0
	number = MIN_BOUND
	while number < MAX_BOUND:
		if is_increasing(number) and has_double(
				number) and adjacent_digits_not_part_of_larger_group(number):
			result += 1
		number += 1
	return result


if __name__ == '__main__':
	print(new_password_possibilites())

