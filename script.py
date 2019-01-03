#!/usr/bin/python3
"""
Simple armagetron snake script, MIT licensed

Copyright 2018 Glen Harpring

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
# This script will only work in +ap. Sorry!

# user config
growtime = 3 #time between growth
growby = 5 #how much to grow
# end user config

import random, math
players = []; getnamebyteam = {}; colorname = {}
length = 0
while True:
	event = input('')
	split = event.split(" ")
	if split[0] == "ROUND_COMMENCING" or split[0] == "GAME_END":
		players = []; getnamebyteam = {}
		print("START_NEW_MATCH")
	if split[0] == "NEW_ROUND":
		length = 0
	if split[0] == "PLAYER_COLORED_NAME":
		colorname[split[1]] = ' '.join(split[2:])
	if split[0] == "ONLINE_PLAYER":
		try:
			getnamebyteam[split[9]] = split[1]
		except IndexError:
			pass
	if split[0] == "CYCLE_CREATED":
		print("SPAWN_ZONE fortress "+(split[6].replace("\\","\\\\"))+" "+split[2]+" "+split[3]+" 10 0")
		players.append(split[1])
	if split[0] == "CYCLE_DESTROYED":
		players.remove(split[1])
	if split[0] == "BASEZONE_CONQUERED":
		try:
			player = getnamebyteam[split[1]]
			print("ADMIN_KILL_MESSAGE 0\nKILL "+player+"\nADMIN_KILL_MESSAGE 1")
			print("CONSOLE_MESSAGE "+colorname[player]+"0xRESETT was killed for letting their zone collapse.")
		except LookupError:
			pass
	if split[0] == "GAME_TIME":
		if math.floor(float(split[1])/growtime)*growtime == float(split[1]):
			length += growby
			print("CYCLE_WALLS_LENGTH "+str(length))
			for player in players:
				print("ADD_SCORE_PLAYER "+player+" 1")
