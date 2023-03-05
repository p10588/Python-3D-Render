import GUIManager

gui = GUIManager.GUI()

def _initalize():
	gui.initalizeMainWindow()

def _update():
	pass
	#gui.updateMainWindow()

def main():
	_initalize()

	while(True):
		_update()

main()
