# -*- coding: utf-8 -*-

import gi
import os
import zlib
import traceback
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from controller import ControllerModelPycFile


builder = Gtk.Builder()
app_path = os.path.dirname(os.path.abspath(__file__))
__all__ = ["App"]

class App(ControllerModelPycFile):

	def __init__(self, *args, **kwargs):
		super(App, self).__init__(*args, **kwargs)
		self.start_ui()
		self.renderer_model(self.search_file())

	def start_ui(self):
		self.code_file = None
		self.path_file = builder.get_object("file")
		self.entry_description = builder.get_object("entry_description")
		self.gr_file = builder.get_object("gr_file")
		self.modelFiles = builder.get_object("modelFiles")
		self.file_chooser = builder.get_object("file_chooser")
		self.dialog_window = builder.get_object("dialog_window")
		self.main_window = builder.get_object("main_window")
		self.main_window.show_all()

	# On destroy GtkWindow
	def on_bt_exit_clicked(self, *args):
		Gtk.main_quit()

	# On GtkButton Clicked
	def on_bt_open_view_file_clicked(self, *args):
		try:
			archive = self.search_file_id(int(self.code_file))
			path = os.path.join(os.path.join(os.path.sep, "tmp", archive["file_name"]))
			with open(path, "wb") as file:
				file.write(zlib.decompress(archive["file"]))
			subprocess.call(["xdg-open", path])

		except Exception as ex:
			traceback.print_exc()

	# On GtkButton Clicked
	def on_bt_add_file_clicked(self, *args):
		try:
			archive = self.path_file.get_filename()
			bytecode = zlib.compress(open(archive, "rb").read(), 9)
			name = os.path.basename(archive)
			description = self.entry_description.get_text()
			self.save_file(bytecode, name, description)
			self.renderer_model(self.search_file())
		except Exception as ex:
			traceback.print_exc()

	# On GtkButton Clicked
	def on_bt_remove_file_clicked(self, *args):
		try:
			if self.code_file:
				self.delete_file(int(self.code_file))
				self.renderer_model(self.search_file())
				self.show_dialog(self.dialog_window, "Success!", ("File deleted!"))
		except Exception as ex:
			traceback.print_exc()

	# On GtkTreeView Cursor Changed
	def on_gr_file_cursor_changed(self, *args):
		try:
			self.code_file = self.select_code(args[0].get_selection())
		except Exception as ex:
			traceback.print_exc()

	# Rederer Model
	def renderer_model(self, model):
		self.modelFiles.clear()
		if model:
			for file in model:
				self.modelFiles.append(file)

	# Return value column `#` selected in GtkTreeView
	def select_code(self, selection):
		model, treeiter = selection.get_selected()
		if treeiter is not None:
			return model[treeiter][0]

	# Show Message Dialog
	def show_dialog(self, component, title, text, icon=None):
		component.props.text = (title)
		component.props.secondary_text = (text)
		component.props.icon_name = (icon)
		component.props.modal
		component.show_all()
		component.run()
		component.hide()

if __name__ == "__main__":
	builder.add_from_file(os.path.join(app_path, "templates", "interface.ui"))
	builder.connect_signals(App())
	Gtk.main()
