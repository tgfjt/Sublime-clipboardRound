import sublime, sublime_plugin

history = []
menuitems = []
history_index = 0

def setClipboardHistory():
    global history_index, menuitems, history

    try:# win32
        import win32clipboard
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        pass

    try:# windows7
        import ctypes
        ctypes.windll.user32.OpenClipboard(None)
        pc = ctypes.windll.user32.GetClipboardData(1)
        data = ctypes.c_char_p(pc).value.decode()
        ctypes.windll.user32.CloseClipboard()
    except:
        pass

    try:# mac
        import subprocess
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        clip = p.stdout.read()
        data = clip.decode()
    except:
        pass

    try:# xclip (Linux)
        import subprocess
        p = subprocess.Popen(['xclip', '-o'], stdout=subprocess.PIPE)
        retcode = p.wait()
        clip = p.stdout.read()
        data = clip.decode()
    except:
        pass

    if not 'data' in locals():
        return None
    elif data in history:
        return None
    elif data == '':
        return None

    settings = sublime.load_settings('Sublime-clipboardRound.sublime-settings')
    limit = settings.get('limit')

    if not history or history[0] != data:
        history.insert(0, data)
        history_index = 0
        menuitems = history

    if limit < len(history):
        for i in xrange(len(history) - limit):
            history.pop()
            menuitems.pop()

    return None

def pasteClipboardHistory(self, text):
    self.view.run_command('undo')
    self.view.run_command('paste')
    sublime.set_clipboard(text)

class Clip_round_showCommand(sublime_plugin.TextCommand):
    def on_chosen(self, index):
        global flag
        if index == -1:
            return

        sublime.set_clipboard(menuitems[index])
        self.view.run_command('paste')
        flag = True

    def run(self, edit):
        global menuitems
        if menuitems == []:
            return None

        self.view.window().show_quick_panel(menuitems, self.on_chosen, sublime.MONOSPACE_FONT)

class Clip_round_prevCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global history_index
        if history:
            clip = sublime.get_clipboard()
            history_index = min(history_index + 1, len(history) - 1)
            sublime.set_clipboard(history[history_index])

            sublime.set_timeout(lambda:
                pasteClipboardHistory(self, clip), 0)

class Clip_round_nextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global history_index
        if history:
            clip = sublime.get_clipboard()
            history_index = max(history_index - 1, 0)
            sublime.set_clipboard(history[history_index])

            sublime.set_timeout(lambda:
                pasteClipboardHistory(self, clip), 0)

class Clip_round_clearCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global history, history_index, menuitems, data
        del menuitems[:]
        del history[:]
        history_index = 0
        sublime.set_clipboard('')
        print('clipboardRound: clear Clipboard History.')

class ClipboardRoundListener(sublime_plugin.EventListener):
    def on_query_context(self, view, *args):
        sublime.set_timeout(lambda:
            setClipboardHistory(), 0)
        return None

    def on_text_command(self, view, command, *args):
        sublime.set_timeout(lambda:
            setClipboardHistory(), 0)
