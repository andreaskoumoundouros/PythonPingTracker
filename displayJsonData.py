import json
import os
import pandas as pd
from argparse import ArgumentParser
import matplotlib.pyplot as plt

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('-f', '--file',required=True, help='Log file to read data from')
	args = parser.parse_args()

	if args.file:
		if os.path.exists(args.file):
			timingData = json.load(open(args.file, "r"))
			for key in timingData:
				df = pd.DataFrame(timingData[key])
				df.plot(title=key,x="timeSent", y="pingTime")
				plt.show()
		else:
			print(f"\"{args.file}\" does not exist")