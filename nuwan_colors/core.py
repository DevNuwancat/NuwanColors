import csv

class Colors:

    all = ["\033[30m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m", "\033[0m"]
    bg_all = ["\033[40m", "\033[41m", "\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m","\033[7m", "\033[0m"]
    

    def __init__(self):
        pass
           

    @staticmethod
    def black(text):
        return f"{Colors.all[0]}{text}{Colors.all[-1]}"
    
    @staticmethod
    def red(text):
        return f"{Colors.all[1]}{text}{Colors.all[-1]}"
    
    @staticmethod
    def green(text):
        return f"{Colors.all[2]}{text}{Colors.all[-1]}"
    
    @staticmethod
    def yellow(text):
        return f"{Colors.all[3]}{text}{Colors.all[-1]}"
    
    @staticmethod
    def blue(text):
        return f"{Colors.all[4]}{text}{Colors.all[-1]}"
    
    @staticmethod
    def magneta(text):
        return f"{Colors.all[5]}{text}{Colors.all[-1]}"
    
    @staticmethod
    def cyan(text):
        return f"{Colors.all[6]}{text}{Colors.all[-1]}"
    
    @staticmethod
    def white(text):
        return f"{Colors.all[7]}{text}{Colors.all[-1]}"
    
    """BG_COLORS"""

    @staticmethod
    def bg_black(text):
        return f"{Colors.bg_all[0]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_red(text):
        return f"{Colors.bg_all[1]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_green(text):
        return f"{Colors.bg_all[2]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_yellow(text):
        return f"{Colors.bg_all[3]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_blue(text):
        return f"{Colors.bg_all[4]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_magneta(text):
        return f"{Colors.bg_all[5]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_cyan(text):
        return f"{Colors.bg_all[6]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_white(text):
        return f"{Colors.bg_all[7]}{text}{Colors.bg_all[-1]}"
    
    @staticmethod
    def bg_reverse_white(text):
        return f"{Colors.bg_all[8]}{text}{Colors.bg_all[-1]}"
    
    """TEXT STYLE"""

class Texts:

    text_all =[ "\033[1m", "\033[3m", "\033[4m", "\033[7m", "\033[9m","\033[4m", "\033[0m"]

    def __init__(self):
        pass

    @staticmethod
    def bold(text):
        return f"{Texts.text_all[0]}{text}{Texts.text_all[-1]}"
    
    @staticmethod
    def italic(text):
        return f"{Texts.text_all[1]}{text}{Texts.text_all[-1]}"
    
    @staticmethod
    def blink(text):
        return f"{Texts.text_all[2]}{text}{Texts.text_all[-1]}"
    
    @staticmethod
    def concealed(text):
        return f"{Texts.text_all[4]}{text}{Texts.text_all[-1]}"
    
    @staticmethod
    def underline(text):
        return f"{Texts.text_all[5]}{text}{Texts.text_all[-1]}"





