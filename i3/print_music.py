from subprocess import check_output

status = check_output(['rhythmbox-client','--print-playing'], universal_newlines=True)

print status.split("-")[1].strip()

