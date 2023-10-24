from setuptools import setup

APP = ['Editor.py']
DATA_FILES = ['about_ui.py', 'add_dir_ui.py', 'dialog_ui.py', 'directory_file.json', 'edit_run_com_ui.py', 'file_list.json', 'high_light.py', 'highlight_pattern.py', 'paremetrs.json', 'save_for_ui.py', 'set_editor.py', 'short_cut_ui.py', 'tools_ui.py']
OPTIONS = {
     'iconfile': 'icon.icns',
     'plist':{
     'CFBundleName': 'PyPaIDE',
     'CFBundleShortVersionString': '1.0',
     'CFBundleGetInfoString': 'Python IDE',
     'CFBundleExecutable': 'main',
     'CFBundleIdentifier': 'com.apple.icns',
     'CFBundleSignature': '????',
     }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
