import socket
import subprocess

ip = "159.65.81.51"
port = 31010




sock = socket.socket()


def establish_connection():
	sock.connect((ip, port))
	print(sock.recv(1024))
	sock.send(b"2\n")

def get_quest():
	quest = sock.recv(1024)
	quest = quest.split(b"\n")
	start = 7
	line = quest[start]
	times = []
	while b"Person" in line:
		print(line)
		n = line.split()[4].decode()
		times.append(n)
		start += 1
		line = quest[start]

	command = f"{len(times)}\n2\n{' '.join(times)}\n".encode()
	return command, times

def run_solver(command):
	solver = subprocess.Popen(["runhaskell", "TorchSolver.hs"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	solver_output = solver.communicate(command)
	solver_output  = solver_output [0].split(b"\n")
	return solver_output

def parse_solver_output(solver_output, times):
	start = 5
	end = -4
	solution = solver_output[start:end]
	solution = [i.split()[0] for i in solution]
	solution = [eval(i) for i in solution]
	
	print(solution)
	print(times)

	translated_solution = []
	for path in solution:
		new_path = []
		for i in path:
			new_path.append(times.index(str(i))+1)
		translated_solution.append(str(new_path))
	translated_solution = ",".join(translated_solution)
	print(translated_solution)
	return translated_solution
	
def send_back_to_challenge(translated_solution):
	sock.send(translated_solution.encode())
	sock.send(b"\n")
	result = sock.recv(1024)
	print(result)
	return result

def solve():
	establish_connection()
	command_for_solver, times = get_quest()
	solver_output = run_solver(command_for_solver)
	solution = parse_solver_output(solver_output, times)
	result = send_back_to_challenge(solution)
	if b"HTB{" in result:
		print("WINNER WINNER CHICKEN NUGGIE DINNER")
solve()
