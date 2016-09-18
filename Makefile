SHELL=bash

.PHONY: 1, master

1:
	@ git checkout b735ca61b60e28e06b32f19740481b67b41f645c

2:
	@ git checkout a8a33376b9289a4437eac5424e5627b11f75c8c3

3: 2

3_1:
	@ git checkout 714b877d8264b4405b875015337ba43c88ed4fbf

master:
	@ git checkout master
