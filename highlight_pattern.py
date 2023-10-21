#Mini IDE
#Lang python
#By Imm0rtall
try:
    import sys
    from PyQt5.QtWidgets import QPlainTextEdit, QTextEdit
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QFont, QFontDatabase, QColor, QTextCharFormat
    from high_light import HighLight
except ImportError:
    print(f'LOG: {ImportError}')
    sys.exit()

class high_light_pattern:
    def __init__(self, ai_editor):
        self.ai_editor = ai_editor
        self.highlighter = HighLight()

    def setUpEditor(self):
        import_format = QTextCharFormat()
        import_format.setForeground(Qt.cyan)
        pattern = r'^import|^from|^\s+import|^\s+from'
        self.highlighter.add_mapping(pattern, import_format)

        class_format = QTextCharFormat()
        class_format.setForeground(QColor("#ff8000"))
        class_format.setFontWeight(QFont.Bold)
        pattern = r'^\s*class\s+\w+\(.*$|^\s*class\s+\w+\.*$|^\s*class\s+\w+\(.*$|^\s*class\s+\w+\:.*$'
        self.highlighter.add_mapping(pattern, class_format)

        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#ff8000"))
        function_format.setFontItalic(True)
        pattern = r'^\s*def\s+\w+\s*\(.*\)\s*:\s*$'
        self.highlighter.add_mapping(pattern, function_format)

        call_function_format = QTextCharFormat()
        call_function_format.setForeground(QColor("#003899"))
        pattern = r'(\w+)\(([^)]*)\)'
        self.highlighter.add_mapping(pattern, call_function_format)

        key_words_format = QTextCharFormat()
        key_words_format.setForeground(Qt.darkRed)
        pattern = r'^\s+if|^\s+elif|^\s+else|^\s+while|^\s+for|^\s+try|^s+except|^\s+finally|^if|^elif|^else|^while|^for|^try|^except|^finally'
        self.highlighter.add_mapping(pattern, key_words_format)

        str_format = QTextCharFormat()
        str_format.setForeground(QColor("#964B00"))
        pattern = r'"[0-9a-zA-z !@#\$%\^&*(){}\[\]:.,/~`\<\>\?:\';\+\|]+"|f"[0-9a-zA-z !@#\$%\^&*(){}\[\]:.,/~`\<\>\?:\';\+\|]+"|r"[0-9a-zA-z !@#\$%\^&*(){}\[\]:.,/~`\<\>\?:\";\+]+"'
        self.highlighter.add_mapping(pattern, str_format)
        pattern = r"'[0-9a-zA-z !@#\$%\^&*(){}\[\]:.,/~`\<\>\?:\";\+\|]+'|f'[0-9a-zA-z !@#\$%\^&*(){}\[\]:.,/~`\<\>\?:\";\+\|]+|r'[0-9a-zA-z !@#\$%\^&*(){}\[\]:.,/~`\<\>\?:\";\+]+'"
        self.highlighter.add_mapping(pattern, str_format)

        self_format = QTextCharFormat()
        self_format.setForeground(QColor("#EA4D72"))
        pattern = r'self'
        self.highlighter.add_mapping(pattern, self_format)

        boolean_format = QTextCharFormat()
        boolean_format.setForeground(QColor("#800080"))
        pattern = r'True|False'
        self.highlighter.add_mapping(pattern, boolean_format)

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#808080"))
        pattern = r'^#.*$|^\s+#.*$'
        self.highlighter.add_mapping(pattern, comment_format)

        class_decorator = QTextCharFormat()
        class_decorator.setForeground(QColor("#008dd9"))
        pattern = r'^\s+@\w+'
        self.highlighter.add_mapping(pattern, class_decorator)

        self.ai_editor.editor = QPlainTextEdit()

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.ai_editor.editor.setFont(font)

        self.highlighter.setDocument(self.ai_editor.editor.document())
