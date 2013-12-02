import sublime, sublime_plugin
import codecs, os

history = []
load_history = []
menuitems = []
history_index = 0
flag = False

__file__ = os.path.normpath(os.path.abspath(__file__))
__path__ = os.path.dirname(__file__)

CACHE_PATH = __path__ + '/.cache/cache'

f = codecs.open(CACHE_PATH, 'r', 'utf-8')
str = f.read()
load_history = str.split('\n********************\n')
f.close()

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
        if load_history != ['']:
            menuitems = load_history

        print(menuitems)

        self.view.window().show_quick_panel(menuitems, self.on_chosen, sublime.MONOSPACE_FONT)

class Clip_round_prevCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global history_index
        if history and flag == True:
            clip = sublime.get_clipboard()
            history_index = min(history_index + 1, len(history) - 1)
            sublime.set_clipboard(history[history_index])

            sublime.set_timeout(lambda:
                self.view.run_command('undo'), 0)

            sublime.set_timeout(lambda:
                self.view.run_command('paste'), 1)

            sublime.set_timeout(lambda:
                sublime.set_clipboard(clip), 2)

class Clip_round_nextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global history_index
        if history and flag == True:
            clip = sublime.get_clipboard()
            history_index = max(history_index - 1, 0)
            sublime.set_clipboard(history[history_index])

            sublime.set_timeout(lambda:
                self.view.run_command('undo'), 0)

            sublime.set_timeout(lambda:
                self.view.run_command('paste'), 1)

            sublime.set_timeout(lambda:
                sublime.set_clipboard(clip), 2)

class Clip_round_clearCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global menuitems, history, history_index
        del menuitems[:]
        del history[:]
        history_index = 0
        print('clipboardRound: clear Clipboard History.')

class ClipboardRoundListener(sublime_plugin.EventListener):
    def on_query_context(self, view, key, operator, operand, match_all):
        global history_index, flag

        vi_copy = False

        if operand == 'vi_copy' or operand == 'vi_delete':
            vi_copy = True

        elif key == 'clipboard_round_paste':
            flag = True
            return None
        elif key != 'clipboard_round':
            if vi_copy == False:
                flag = False
                return None

        settings = sublime.load_settings('Sublime-clipboardRound.sublime-settings')
        limit = settings.get('limit')

        for selected in view.sel():
            selected = view.sel()[0]
            if selected.empty():
                selected = view.line(selected)

            text = view.substr(selected)

            if not history or history[0] != text:
                history.insert(0, text)
                history_index = 0

            if not menuitems or menuitems[0] != text:
                menuitems.insert(0, text)

        if limit < len(history):
            for i in xrange(len(history) - limit):
                history.pop()
                menuitems.pop()

        return None

    def on_load(self, view):
        global load_history
        f = codecs.open(CACHE_PATH, 'wr', 'utf-8')
        contents = f.read()
        f.write('')
        load_history = contents.split('\n********************\n')
        f.close()

    def on_pre_save(self, view):
        savelist = '\n********************\n'.join(history)
        f = codecs.open(CACHE_PATH, 'wb', 'utf-8')
        f.write(savelist)
        f.close()
