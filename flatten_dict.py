# Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
def flatten_dict(data):

	res = {}

	for k in data:
		if isinstance(data[k], dict):
			x = flatten_dict(data[k])
			z = {k+'.'+c : x[c] for c in x}

			for key in z:
				res[key] = z
			else:
				res[k] = data[k]

	return res

flatten_dict({a:4, c:6})