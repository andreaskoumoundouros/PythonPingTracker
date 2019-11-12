import subprocess
import time
import re
import json
from datetime import datetime
from argparse import ArgumentParser

logFile = "log.json"
ipAddress = "104.160.131.3"

if __name__ == '__main__':
	start_time = time.time()

	parser = ArgumentParser()
	parser.add_argument('-H', '--host', help='Alternate host to ping')
	parser.add_argument('-f', '--file', help='Log output file')
	args = parser.parse_args()

	if args.host:
		ipAddress = args.host

	process = subprocess.Popen(['ping', ipAddress, '-t'], stdout=subprocess.PIPE)
	
	jsonKey = datetime.now().strftime("%d/%m/%y|%H:%M:%S")

	if args.file:
		try:
			if open(args.file, "x"):
				timingData = {jsonKey:{"timeSent":[], "pingTime":[]}}
		except Exception as e:
			timingData = json.load(open(args.file, "r"))
			timingData[jsonKey] = {"timeSent":[], "pingTime":[]}	

	try:
		while not process.poll():
			time.sleep(0.1)
			line = (process.stdout.readline()).decode('utf-8')
			print(line)
			if "time" in line and args.file:
				try:
					pingTime = re.split("ms",(re.split("time=", line, 1))[1])[0]
				except Exception as e:
					pingTime = 0
				timingData[jsonKey]["timeSent"].append((time.time() - start_time))
				timingData[jsonKey]["pingTime"].append(int(pingTime))

	except KeyboardInterrupt:
		if args.file:			
			with open(args.file, "w") as myfile:
				myfile.write(json.dumps(timingData))
			print(f"Saved ping logs to \"{args.file}\"")
		raise SystemExit