from subprocess import check_output

status = check_output(['free','-m'], universal_newlines=True).strip().splitlines()

no=status[1].strip("Mem:").strip().split(" ")[1:]
for i in no:
    if i=='':
        continue
    no=i
    break

print "%.1fG" % (float(no)/1000)
