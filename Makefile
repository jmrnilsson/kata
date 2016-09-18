SHELL=bash

.PHONY: 1, master

1:
	@ git checkout b735ca61b60e28e06b32f19740481b67b41f645c

2:
	@ git checkout a8a33376b9289a4437eac5424e5627b11f75c8c3

3: 2

4:
	@ git checkout d0133baa7926e202bb6cc0beba0b672983585eda

master:
	@ git checkout master
