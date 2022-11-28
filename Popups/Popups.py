# popups =================================================================================================

def basic_popup(gui=None, easygui=None, title: str = "", message: str = "", button_name: str = "OK"):
    popup_output = easygui.msgbox(message, title, button_name)
    print(f'Basic popup output:- {popup_output}')
