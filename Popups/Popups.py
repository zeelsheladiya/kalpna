# popups =================================================================================================

def basic_popup(gui=None, easygui=None, title: str = "", message: str = "", button_name: str = "OK", error: str = "Not defined"):

    try:
        easygui.msgbox(message + "\n" + "error := " + error, title, button_name)
        # popup_output = easygui.msgbox(message, title, button_name)
        # print(f'Basic popup output:- {popup_output}')
    except Exception as e:
        pass
