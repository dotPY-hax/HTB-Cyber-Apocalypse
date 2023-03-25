#  Janken
> As you approach an ancient tomb, you're met with a wise guru who guards its entrance. In order to proceed, he challenges you to a game of Janken, a variation of rock paper scissors with a unique twist. But there's a catch: you must win 100 rounds in a row to pass. Fail to do so, and you'll be denied entry.

Before looking at the supplied binary (which was to find the intended way of abusing strstr) fuzzing suggested that the socket didnt have any rate limiting and picking the correct answer 1 out of 3 for 100 times didnt look that bad ```¯\_(ツ)_/¯```


```python
import socket

IP = "167.71.143.44"
PORT = 32226

fuck = ""

win = 0
lose = 0
while "HTB{" not in fuck:
	s = socket.socket()
	s.connect((IP, PORT))
	print(s.recv(1024).decode())
	s.send(b"1\n")
	print(s.recv(1024).decode())
	for i in range(100):
		s.send(b"rock\n")
		fuck = s.recv(1024).decode()
		print(fuck)
		if "[-] You lost the game.." in fuck:
			lose += 1
			break
		win += 1
		
print(f"rounds won: {win}")
print(f"rounds lost: {lose}")

```

![image](https://user-images.githubusercontent.com/67259802/227714984-8db55db1-8021-4120-9e10-d9db3671bc13.png)

![image](https://user-images.githubusercontent.com/67259802/227709569-26b57935-8138-445c-9e60-e58d6588bd88.png)
