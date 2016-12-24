def s2c(conn, text):
	conn.send((text + "\n").encode("utf-8"))

def rfc(conn):
	return conn.recv(1024).decode("utf-8")[:-2]

def menu_option(options, conn):
	for i, option in enumerate(options):
		s2c(conn, "%d. %s" % (i, option))
	s2c(conn, "Type in a number or option: ")
	choice = rfc(conn)
	try:
		choice = options[int(choice)]
	except:
		pass
	return choice
