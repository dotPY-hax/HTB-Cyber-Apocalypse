channels_to_segment = {1:5, 3:10, 7:9, 2:7, 5:6, 4:4,0:2,6:1}
gnd = [8, 3]



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
	

