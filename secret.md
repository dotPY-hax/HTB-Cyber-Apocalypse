#  Secret Code
> To gain access to the tomb containing the relic, you must find a way to open the door. While scanning the surrounding area for any unusual signals, you come across a device that appears to be a fusion of various alien technologies. However, the device is broken into two pieces and you are unable to see the secret code displayed on it. The device is transmitting a new character every second and you must decipher the transmitted signals in order to retrieve the code and gain entry to the tomb.

We get some Gerber files and a Salae file. 

## Board
We look into the Gerber files and find a board with only a 7 Segment display and some channels routed to the different pins.

![image](https://user-images.githubusercontent.com/67259802/227711393-ee954079-f6ea-401d-a62c-ac17169b5aa4.png)

![image](https://user-images.githubusercontent.com/67259802/227711471-ba353a53-2e63-45d5-bfd6-6894d03034e9.png)

After highlighting all the nets we get a channel to pin mapping on the 7 segment display. 
``` 
channels_to_segment = {1:5, 3:10, 7:9, 2:7, 5:6, 4:4,0:2,6:1}
gnd = [8, 3]
```

Now we google for a smd common cathode 7 segment diplay with gnd pins on 3 and 8 and find that a lot of them seem to be the same so we pull up the first datasheet on mouser.
![image](https://user-images.githubusercontent.com/67259802/227711718-ba758b64-c178-4683-a222-e0b1f78d5882.png)



Now we have a pin to segment mapping (which is also a channel to segment mapping)

```segments = {1:e, 2:d, 4:c, 5:"P", 6:b, 7:a, 9:f, 10:g}```

## Channels
To get the channels we open the .sal file in Logic and export the data to .csv! Fortunately channel 1 is always on so we can use it as clock!

![image](https://user-images.githubusercontent.com/67259802/227711965-95082ac8-bdaf-442d-aa5e-b8ebed78310d.png)

Now all we have to do is open the csv in python and massage the data a little bit.
```python
with open("digital.csv") as f:
	data = f.readlines()
data = [i.strip() for i in data[1:]]
data = [i.split(",")[1:] for i in data]
data = [i for i in data if i[1]=='1']

```
## Human readability
Now that we have all the data we need we need to make it human readable which is the point of using 7 segment diplays in the first place.

```python
empty = "   "
left = "*  "
right = "  *"
full = "***"
a = [full, empty,  empty, empty, empty]
b = [right, right,right, empty, empty]
c = [empty, empty, right,right,right]
d = [empty,empty,empty,empty, full]
e = [empty,empty,left,left,left]
f = [left,left,left,empty,empty]
g = [empty,empty,full, empty,empty]


segments = {1:e, 2:d, 4:c, 5:"P", 6:b, 7:a, 9:f, 10:g}




def draw(list_of_segments):
	buffer = [[" "," "," "], [" "," "," "],[" "," "," "],[" "," "," "],[" "," "," "]]
	for segment in list_of_segments:
		if segment == "P":
			continue
		for l,line in enumerate(buffer):
			for c, char in enumerate(line):
				if segment[l][c] == "*":
					buffer[l][c] = "*"
	for line in buffer:
		print("".join(line))
	print("")
	

def decode(list_of_channels):
	_segments = []
	for i, channel in enumerate(list_of_channels):
		if channel == "1":
			s = segments[channels_to_segment[i]]
			_segments.append(s)


	draw(_segments)
	return _segments
  ```
  
Now we only need to add some simple drawing logic and we get a human readable output.
We could now write a dictionary to map segments to nibbles or we just copy them by hand.

![image](https://user-images.githubusercontent.com/67259802/227712669-d386eefd-d665-4ee4-aa27-62c92b6b474a.png)

The full code is [here](https://github.com/dotPY-hax/HTB-Cyber-Apocalypse/blob/main/secret_extract.py) and [there](https://github.com/dotPY-hax/HTB-Cyber-Apocalypse/blob/main/secret_seven.py)


python3 extract.py
