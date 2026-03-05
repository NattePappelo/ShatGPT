
def shatAPI(x):
	if "!" in x:
		return "ÅHÅ"

	elif "?" in x:
		return "Jå"

	elif "." in x:
		return "Jaha"

	else:
		return "HÖH?"


if __name__ == "__main__":

	print("\n\nVälkommen till ShatGPT 0.1.1 alfa \n\n")

	while 1:
		print("\n   "+ shatAPI(input(":  ")) +"\n")