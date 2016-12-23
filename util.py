def s2c(conn, text):
	conn.send((text + "\n").encode("utf-8"))

def rfc(conn):
	return conn.recv(1024).decode("utf-8")[:-2]

