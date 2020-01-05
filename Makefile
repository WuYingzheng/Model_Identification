.PHONY: all clean

all:
	pyrcc5 -o csb_rc.py                   csb.qrc
	pyuic5 -o GuiLib/ui_mainwindow.py     GuiLib/MainWindow.ui
	pyuic5 -o GuiLib/ui_about_author.py   GuiLib/AboutAuthor.ui
	pyuic5 -o GuiLib/ui_signal_gen.py     GuiLib/SignalGen.ui
	pyuic5 -o GuiLib/ui_signal_sample.py  GuiLib/SignalSample.ui

test-clean:
	rm -f  csb.qrc
	rm -f  GuiLib/MainWindow.ui
	rm -f  GuiLib/AboutAuthor.ui
	rm -f  GuiLib/SignalGen.ui
	rm -f  GuiLib/SignalSample.ui