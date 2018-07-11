def compute_avg(scores):
	total = 0
	for score in scores:
		total = total + score

	avg = float(total) / len(scores)
	print("The average is " + str(avg))
	return avg 

def compute_min(scores):
	return min(scores)

def compute_max(scores):
	return max(scores)