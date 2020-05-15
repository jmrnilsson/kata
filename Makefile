SHELL=bash

.PHONY: 1, 2, 3, 4, 5, 6, 7, master

0:
	@ git checkout 5f85ba5cda820ecdf91e9cb992107239ba83a359
1:
	@ git checkout 285440d7b7451bc5f8e9c4ef0754eb793c5b827a
2:
	@ git checkout 285440d7b7451bc5f8e9c4ef0754eb793c5b827a
3:
	@ git checkout 1a639d1a9dfe3e9dd035c195767065ad9b487f3f
4:
	@ git checkout c66c4f7e9992b8c800dd42796b82f334ba56e5a0
5:
	@ git checkout ade1f7301b8967ec8359e5c9f047af1feada22e6
6:
	@ git checkout e078ebd7c40395924445d973b4f628426d53e0dc
7:
	@ git checkout d936715e2609c7d9b47aff86da8cc044a9e2a8cb

master:
	@ git checkout master
