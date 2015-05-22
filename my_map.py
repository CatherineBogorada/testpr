import sys
for line in sys.stdn:
	for token in line.strip().split():
		print(token + "\t1")

