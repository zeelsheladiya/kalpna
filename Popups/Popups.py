# popups =================================================================================================

def basic_popup(gui=None, easygui=None, title: str = "", message: str = ""):
    popup_output = easygui.msgbox(message, title)
    print(f'Basic popup output:- {popup_output}')

