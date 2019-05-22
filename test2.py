import datetime

while True:
	bd = input("Geben Sie ihr Geburtstag ein : ").split(".")
	if len(bd) == 1:
		bd=bd[0].split()
	elif len(bd) == 3:
		break

d = datetime.datetime.now()-datetime.datetime(int(bd[2]),int(bd[1]),int(bd[0]))
print(f"Sie sind {d.days} Tage alt!")


