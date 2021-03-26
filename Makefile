# vim: set noet:
all: help
help:
	@echo 'Avalable targets:'
	@echo ' [*] help'
	@echo ' [*] install'
	@echo ' [*] uninstall'
install: *.py
	install -Cdvm755 ~/.local/lib/python3.8/site-packages/stack-calc
	install -Cv *.py ~/.local/lib/python3.8/site-packages/stack-calc
	install -Cdvm777 ~/.local/bin
	ln -svf ~/.local/lib/python3.8/site-packages/stack-calc/app.py ~/.local/bin/stack-calc
uninstall:
	rm -rfv ~/.local/lib/python3.8/site-packages/stack-calc
	rm -rfv ~/.local/bin/stack-calc
