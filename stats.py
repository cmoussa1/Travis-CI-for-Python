def compute_avg(scores):
    """
    Computes average of a list of numbers.

    :param scores: The list of numbers.
    :return: An average of the list of numbers.
    """
	total = 0
	for score in scores:
		total = total + score

	avg = float(total) / len(scores)
	print("The average is " + str(avg))
	return avg 

def compute_min(scores):
    """
    Returns minimum score.

    :param scores: The list of numbers.
    :return: The minimum.
    """
	return min(scores)

def compute_max(scores):
    """
    Returns maximum score.

    :param scores: The list of numbers.
    :return: The maximum.
    """
	return max(scores)