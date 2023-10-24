#PyPaIDE main file
#Lang python
#By Imm0rtall
#imports and test case for import
try:
    import sys
    import json
    import os
    import subprocess
    import save_for_ui
    from PyQt5 import QtWidgets
    from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QTextEdit, QVBoxLayout, QFileDialog, QListView, QHBoxLayout, QShortcut, QAction, QMainWindow
    from PyQt5.QtGui import QFont, QFontDatabase, QColor, QSyntaxHighlighter, QTextCharFormat, QIcon, QKeyEvent, QKeySequence
    from highlight_pattern import high_light_pattern
    from save_for_ui import Ui_Form_save
    from tools_ui import Ui_Form_tools
    from short_cut_ui import Ui_Form_short_cut
    from edit_run_com_ui import Ui_Form_edit_run_com
    from set_editor import Ui_Form_set_editor
    from add_dir_ui import Ui_Form_add_dir
    from dialog_ui import Ui_Form_del_dialog
    from about_ui import AboutDialog
    print('LOG: Import OK')
except ImportError:
    print('LOG: Import ERROR')



# Class
class Editor(QMainWindow):
    """MAIN CLASS"""
    def __init__(self):
        try:
            #class init and load config, set layout, setup UI
            super().__init__()
            self.menubar = self.menuBar()
            self.helpMenu = self.menubar.addMenu('Help')
            self.aboutAction = QAction('About', self)
            self.helpMenu.addAction(self.aboutAction)
            self.setWindowTitle('PyPaIDE')
            self.window_width, self.window_height = 1200, 800
            self.del_accest = False
            with open('paremetrs.json') as f:
                self.data = json.load(f)
            with open('file_list.json') as fi:
                self.directory_file_dict = json.load(fi)
            self.run_command = self.data["run_command"]
            self.font_size = self.data["font-size"]
            self.italic = self.data["italic-text"]
            self.high_light_editor = high_light_pattern(self)
            self.setMinimumSize(self.window_width, self.window_height)
            self.setStyleSheet(f'font-size: {self.font_size}px;')
            self.central_widget = QWidget(self)
            self.setCentralWidget(self.central_widget)

            self.ui_save = Ui_Form_save()
            self.ui_save.setupUi(Form_save)
            self.ui_tools = Ui_Form_tools()
            self.ui_tools.setupUi(Form_tools)
            self.ui_short_cut = Ui_Form_short_cut()
            self.ui_short_cut.setupUi(Form_short_cut)
            self.ui_edit_run_com = Ui_Form_edit_run_com()
            self.ui_edit_run_com.setupUi(Form_edit_run_com)
            self.ui_set_editor = Ui_Form_set_editor()
            self.ui_set_editor.setupUi(Form_set_editor)
            self.ui_add_dir = Ui_Form_add_dir()
            self.ui_add_dir.setupUi(Form_add_dir)
            self.ui_del_dialog = Ui_Form_del_dialog()
            self.ui_del_dialog.setupUi(Form_del_dialog)
            self.ui_about = AboutDialog()
            self.ui_about.setupUi(Form_about)

            self.layout = QHBoxLayout()

            self.tool_button = QtWidgets.QPushButton('T\no\no\nl\ns', self.central_widget)
            self.File_list = QtWidgets.QListWidget(self.central_widget)

            self.layout.addWidget(self.File_list)
            self.layout.addWidget(self.tool_button)
            self.high_light_editor.setUpEditor()
            self.layout.addWidget(self.high_light_editor.ai_editor.editor)
            self.File_list.setFixedWidth(150)
            self.tool_button.setFixedHeight(500)
            self.tool_button.setFixedWidth(40)
            self.central_widget.setLayout(self.layout)
            with open('file_list.json') as f:
                self.data_file = json.load(f)
            self.File_list.addItems(self.data_file)

            self.index = None
            self.directory_save = None
            self.directory_file_list = None
            self.format_file = '.py'
            self.FORMATING_MAP = {
                0: '.py',
                1: '.doc',
                2: '.txt',
                3: '.html',
                4: '.cpp',
                5: '.c',
                6: '.cs',
                7: '.css',
            }
            for format_ in self.FORMATING_MAP:
                self.ui_save.comboBox.addItem(self.FORMATING_MAP[format_])
            self.ui_edit_run_com.lineEdit.setText(self.run_command)
            self.ui_set_editor.lineEdit.setText(self.font_size)
            self.ui_short_cut.lineEdit.setText(self.data["short_cuts"]["save"])
            self.ui_short_cut.lineEdit_2.setText(self.data["short_cuts"]["run-and-save"])
            self.ui_short_cut.lineEdit_3.setText(self.data["short_cuts"]["edit-file"])
            self.ui_short_cut.lineEdit_4.setText(self.data["short_cuts"]["add-file"])
            self.ui_short_cut.lineEdit_5.setText(self.data["short_cuts"]["delete-file"])
            self.ui_short_cut.lineEdit_6.setText(self.data["short_cuts"]["add-dir"])
            # init Shortcuts
            self.save_short_cut = QShortcut(QKeySequence(self.data["short_cuts"]["save"]), self)
            self.edit_file_short_cut = QShortcut(QKeySequence(self.data["short_cuts"]["edit-file"]), self)
            self.add_file_short_cut = QShortcut(QKeySequence(self.data["short_cuts"]["add-file"]), self)
            self.delete_file_short_cut = QShortcut(QKeySequence(self.data["short_cuts"]["delete-file"]), self)
            self.add_dir_short_cut = QShortcut(QKeySequence(self.data["short_cuts"]["add-dir"]), self)
            self.run_and_save = QShortcut(QKeySequence(self.data["short_cuts"]["run-and-save"]), self)
            self.remove_file_from_list = QShortcut(QKeySequence('Ctrl+P'), self)
        except AttributeError or FileNotFoundError:
            if AttributeError:
                print(f'LOG: Error {AttributeError}')
                sys.exit()
            else:
                print(f'LOG: Error {FileNotFoundError}')
                sys.exit()


    # Function init
    try:
        @staticmethod
        def _show_tool_window():
            Form_tools.show()

        @staticmethod
        def _show_short_cut_tool():
            Form_short_cut.show()

        @staticmethod
        def _show_set_editor():
            Form_set_editor.show()

        @staticmethod
        def _show_edit_run_com():
            Form_edit_run_com.show()

        @staticmethod
        def _show_save_form():
            Form_save.show()

        @staticmethod
        def _show_add_dir_form():
            Form_add_dir.show()

        @staticmethod
        def _show_del_dialog():
            Form_del_dialog.show()

        def _show_about(self):
            Form_about.show()

        #set format file for save
        def _set_format_file(self, index):
            self.format_file = self.FORMATING_MAP[index]

        def _button_run_and_save_tool(self):
            """This function saved file if he is nor there and run file at the command of run_command"""
            try:
                if self.directory_file_list:
                    with open(self.directory_file_list, 'w+') as file:
                        file.write(self.high_light_editor.ai_editor.editor.toPlainText())
                    path = os.path.dirname(self.directory_file_list)
                    command = f'cd {path} && open -a Terminal .'
                    command_run = f'{self.run_command} {self.directory_file_list}'
                    subprocess.call(command, shell=True)
                    subprocess.call(command_run, shell=True)
            except OSError or FileNotFoundError:
                self._react_to_err()

        def _save(self):
            """This function saved file according to the selected format"""
            try:
                self.directory_save = QFileDialog.getExistingDirectory()
                with open(f'{self.directory_save}/{self.ui_save.lineEdit.text()}{self.format_file}', 'w+') as file:
                    file.write(self.high_light_editor.ai_editor.editor.toPlainText())
                Form_save.hide()
                with open('file_list.json') as f:
                    data = json.load(f)
                data.append(f'{self.ui_save.lineEdit.text()}{self.format_file}')
                self.File_list.addItem(f'{self.ui_save.lineEdit.text()}{self.format_file}')
                with open('file_list.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False)
                with open('directory_file.json') as f:
                    data = json.load(f)
                data.append(f'{self.directory_save}/{self.ui_save.lineEdit.text()}{self.format_file}')
                with open('directory_file.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False)
            except OSError or FileNotFoundError:
                self._react_to_err()


        def _edit_file_tool(self):
            """This function open file on Editor"""
            try:
                directory_file, _ = QFileDialog.getOpenFileName()
                with open(directory_file) as file:
                    content = file.read()
                self.high_light_editor.ai_editor.editor.setPlainText(content)
            except OSError or FileNotFoundError:
                self._react_to_err()

        def _edit_com_run_tool(self):
            """This function saved run command"""
            with open('paremetrs.json') as f:
                self.data = json.load(f)
            self.data['run_command'] = self.ui_edit_run_com.lineEdit.text()
            with open('paremetrs.json', 'w') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)

        def _set_editor_tool(self):
            """This function saved config Editor"""
            with open('paremetrs.json') as f:
                self.data = json.load(f)
            self.data["font-size"] = self.ui_set_editor.lineEdit.text()
            self.setStyleSheet(f'font-size: {self.font_size}px;')
            if self.italic:
                self.data["italic-text"] = True
            else:
                self.data["italic-text"] = False
            with open('paremetrs.json', 'w') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)

        def _edit_short_cut_config(self):
            """This function saved short cuts config"""
            with open('paremetrs.json') as f:
                self.data = json.load(f)
            self.data["short_cuts"]["save"] = self.ui_short_cut.lineEdit.text()
            self.data["short_cuts"]["run-and-save"] = self.ui_short_cut.lineEdit_2.text()
            self.data["short_cuts"]["delete-file"] = self.ui_short_cut.lineEdit_5.text()
            self.data["short_cuts"]["edit-file"] = self.ui_short_cut.lineEdit_3.text()
            self.data["short_cuts"]["add-file"] = self.ui_short_cut.lineEdit_4.text()
            self.data["short_cuts"]["add-dir"] = self.ui_short_cut.lineEdit_6.text()
            with open('paremetrs.json', 'w') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)

        def _add_file(self):
            """This function add file to list in main window and saved in json file name file and directory file"""
            try:
                directory_file, _ = QFileDialog.getOpenFileName()
                with open('file_list.json') as f:
                    data = json.load(f)
                data.append(os.path.basename(directory_file))
                self.File_list.addItem(os.path.basename(directory_file))
                with open('file_list.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False)
                with open('directory_file.json') as f:
                    data = json.load(f)
                data.append(directory_file)
                with open('directory_file.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False)
            except OSError or FileNotFoundError:
                self._react_to_err()

        def _set_file(self, current_item):
            """This function set file is target in list"""
            with open('file_list.json') as f:
                data_file_list = json.load(f)
            with open('directory_file.json') as f:
                directory_file_list = json.load(f)
            try:
                self.index = self.File_list.row(current_item)
                self.data_file_list = data_file_list[self.index]
                self.directory_file_list = directory_file_list[self.index]
            except IndexError:
                print(IndexError)

        def _open_file(self):
            """This function open file"""
            try:
                with open(self.directory_file_list) as file:
                    content = file.read()
                self.high_light_editor.ai_editor.editor.setPlainText(content)
            except OSError or FileNotFoundError:
                self._react_to_err()
                if OSError:
                    with open('file_list.json') as f:
                        data_file_list = json.load(f)
                    del data_file_list[self.index]
                    with open('file_list.json', 'w') as f:
                        json.dump(data_file_list, f, ensure_ascii=False)
                    with open('directory_file.json') as f:
                        directory_file_list = json.load(f)
                    del directory_file_list[self.index]
                    with open('directory_file.json', 'w') as f:
                        json.dump(directory_file_list, f, ensure_ascii=False)
                    self.File_list.takeItem(self.index)


        def _open_terminal_path(self):
            """This function opens a terminal in the path file if it is open"""
            try:
                if not self.directory_file_list:
                    print('LOG: Path not selected to open terminal')
                    os.system('open $SHELL')
                else:
                    path = os.path.dirname(self.directory_file_list)
                    command = f'cd {path} && open -a Terminal .'
                    subprocess.call(command, shell=True)
            except AttributeError or TypeError:
                print('LOG: Path not selected to open terminal')
                os.system('open $SHELL')

        def _del_file(self):
            """This function delete elected file"""
            try:
                if self.directory_file_list:
                    self._show_del_dialog()
                    if self.del_accest:
                        if self.index >= 0:
                            with open('file_list.json') as f:
                                data_file_list = json.load(f)
                            del data_file_list[self.index]
                            with open('file_list.json', 'w') as f:
                                json.dump(data_file_list, f, ensure_ascii=False)
                            with open('directory_file.json') as f:
                                directory_file_list = json.load(f)
                            self.high_light_editor.ai_editor.editor.setPlainText('')
                            os.remove(directory_file_list[self.index])
                            del directory_file_list[self.index]
                            with open('directory_file.json', 'w') as f:
                                json.dump(directory_file_list, f, ensure_ascii=False)
                            self.File_list.takeItem(self.index)
                        else:
                            pass
            except AttributeError:
                print(AttributeError)

        def _add_dir(self):
            """This function add target directory"""
            try:
                directory_dir = QFileDialog.getExistingDirectory()
                directory = self.ui_add_dir.lineEdit.text()
                path = os.path.join(directory_dir, directory)
                os.mkdir(path)
            except OSError or FileNotFoundError:
                self._react_to_err()

        def _del_dir(self):
            """This function delete target directory"""
            try:
                directory_dir = QFileDialog.getExistingDirectory()
                path = os.path.join(directory_dir, self.directory_file_list)
                os.rmdir(path)
            except OSError or FileNotFoundError:
                self._react_to_err()

        def _accept_del_dialog(self):
            """This function accept del file"""
            self.del_accest = True
            self._del_file()
            self.del_accest = False
            Form_del_dialog.hide()

        def _reject_del_dialog(self):
            """This function reject del file"""
            self.del_accest = False
            Form_del_dialog.hide()

        def _remove_file_from_list(self):
            """This function remove target file from list"""
            try:
                if self.index >= 0:
                    with open('file_list.json') as f:
                        data_file_list = json.load(f)
                    del data_file_list[self.index]
                    with open('file_list.json', 'w') as f:
                        json.dump(data_file_list, f, ensure_ascii=False)
                    with open('directory_file.json') as f:
                        directory_file_list = json.load(f)
                    self.high_light_editor.ai_editor.editor.setPlainText('')
                    del directory_file_list[self.index]
                    with open('directory_file.json', 'w') as f:
                        json.dump(directory_file_list, f, ensure_ascii=False)
                    self.File_list.takeItem(self.index)
                else:
                    pass
            except IndexError:
                self._react_to_err()

    except OSError or FileNotFoundError or ImportError or FileExistsError:
        print('LOG: function init error')
    finally:
        print('LOG: function has init!')

    @staticmethod
    def _react_to_err():
        """This function react to error"""
        if OSError:
            print('LOG: OSError')
        else:
            print('LOG: FileNotFoundError')

    def _all_button_connect(self):
        """This function connect function to button"""
        try:
            # show tool form
            self.tool_button.clicked.connect(editor._show_tool_window)
            # show save form
            self.ui_tools.pushButton_6.clicked.connect(editor._show_save_form)
            # show terminal on path
            self.ui_tools.pushButton.clicked.connect(editor._open_terminal_path)
            # run and save python script
            self.ui_tools.pushButton_2.clicked.connect(editor._button_run_and_save_tool)
            # edit file tool
            self.ui_tools.pushButton_7.clicked.connect(editor._edit_file_tool)
            # show short cut edit
            self.ui_tools.pushButton_11.clicked.connect(editor._show_short_cut_tool)
            # show run command edit
            self.ui_tools.pushButton_10.clicked.connect(editor._show_edit_run_com)
            # show set editor
            self.ui_tools.pushButton_8.clicked.connect(editor._show_set_editor)
            # add file
            self.ui_tools.pushButton_5.clicked.connect(editor._add_file)
            # delete file
            self.ui_tools.pushButton_3.clicked.connect(editor._del_file)
            # show add dir form
            self.ui_tools.pushButton_4.clicked.connect(editor._show_add_dir_form)
            # add dir
            self.ui_add_dir.pushButton.clicked.connect(editor._add_dir)
            # delete dir
            self.ui_tools.pushButton_9.clicked.connect(editor._del_dir)
            # save run command
            self.ui_edit_run_com.pushButton.clicked.connect(editor._edit_com_run_tool)
            # button save edit command tool
            self.ui_short_cut.pushButton.clicked.connect(editor._edit_short_cut_config)
            # set italic text
            self.ui_set_editor.radioButton.pressed.connect(lambda: editor.italic == True)
            # save button set editor
            self.ui_set_editor.pushButton.clicked.connect(editor._set_editor_tool)
            # save button
            self.ui_save.pushButton.clicked.connect(editor._save)
            # set target format
            self.ui_save.comboBox.currentIndexChanged.connect(editor._set_format_file)
            # set target file
            editor.File_list.currentItemChanged.connect(editor._set_file)
            # open file in file explorer
            editor.File_list.itemDoubleClicked.connect(editor._open_file)
            # short cut save
            self.save_short_cut.activated.connect(self._show_save_form)
            # short cut delete file
            self.delete_file_short_cut.activated.connect(self._del_file)
            # short cut add dir
            self.add_dir_short_cut.activated.connect(self._add_dir)
            # short cut run and save file
            self.run_and_save.activated.connect(self._button_run_and_save_tool)
            # short cut add file
            self.add_file_short_cut.activated.connect(self._add_file)
            # short cut edit file
            self.edit_file_short_cut.activated.connect(self._edit_file_tool)
            # short cut remove file from list
            self.remove_file_from_list.activated.connect(self._remove_file_from_list)
            # dialog del accept
            self.ui_del_dialog.buttonBox.accepted.connect(self._accept_del_dialog)
            # dialog del eject
            self.ui_del_dialog.buttonBox.rejected.connect(self._reject_del_dialog)
            # connect show about
            self.aboutAction.triggered.connect(self._show_about)
        finally:
            print('LOG: All button is connected')


if __name__ == '__main__':
    #set loop Editor
    app = QApplication(sys.argv)
    #set loop for all window except main loop
    app_save = QtWidgets.QMdiSubWindow()
    Form_save = QtWidgets.QWidget()
    app_tools = QtWidgets.QMdiSubWindow()
    Form_tools = QtWidgets.QWidget()
    app_short_cut = QtWidgets.QMdiSubWindow()
    Form_short_cut = QtWidgets.QWidget()
    app_edit_run_com = QtWidgets.QMdiSubWindow()
    Form_edit_run_com = QtWidgets.QWidget()
    app_set_editor = QtWidgets.QMdiSubWindow()
    Form_set_editor = QtWidgets.QWidget()
    app_add_dir = QtWidgets.QMdiSubWindow()
    Form_add_dir = QtWidgets.QWidget()
    app_del_dialog = QtWidgets.QMdiSubWindow()
    Form_del_dialog = QtWidgets.QWidget()
    app_about = QtWidgets.QMdiSubWindow()
    Form_about = QtWidgets.QWidget()
    app_about = QtWidgets.QMdiSubWindow()
    Form_about = QtWidgets.QWidget()
    #set main class and show main window
    editor = Editor()
    editor.show()
    save = save_for_ui.Ui_Form_save()
    editor._all_button_connect()
    sys.exit(app.exec_())
