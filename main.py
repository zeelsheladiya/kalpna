import dearpygui.dearpygui as gui
import easygui
import pandas as pd

gui.create_context()

# global variable
FILE_PATH = ""

FILE_TYPE = {
    "CSV": "csv",
    "Excel": "xlsx"
}

DATA_TABLE = pd.DataFrame()


# event section
def btn_browse_file_browse_callback(sender, _, user_data):
    global FILE_PATH, DATA_TABLE
    print(f'sender:- {sender}')
    print(f'user data:- {user_data}')
    file_type_name = gui.get_value("cb_file_type_main_tab")

    FILE_PATH = easygui.fileopenbox(msg=f'Please locate the {file_type_name} file',
                                    default=f"*.{FILE_TYPE[file_type_name]}",
                                    filetypes=[f"*.{FILE_TYPE[file_type_name]}"])

    DATA_TABLE = pd.read_csv(FILE_PATH)
    print(DATA_TABLE)

    gui.set_value("txt_file_log", FILE_PATH)
    gui.set_value("txt_file_selected_log", "File is Selected")
    # gui.add_color_value("txt_file_selected_log", (0, 255, 0))

# tab section
def init_main_tab():
    # file type sector
    gui.add_combo(["CSV", "Excel"], default_value="CSV", width=400, tag="cb_file_type_main_tab",
                  label="Select File Type")

    # browse button
    gui.add_button(label="Browse", callback=btn_browse_file_browse_callback, user_data="btn_browse", width=200)

    # file selection section
    gui.add_input_text(tag="txt_file_log", enabled=False)
    gui.add_text("File Not Selected", tag="txt_file_selected_log", color=(255, 0, 0))

    # table for visualization data


with gui.window(tag="primary_window"):
    with gui.tab_bar():
        with gui.tab(label="main_tab"):
            init_main_tab()

gui.create_viewport(title='Kalpana')
gui.setup_dearpygui()
gui.show_viewport()
gui.maximize_viewport()
gui.set_primary_window("primary_window", True)
gui.start_dearpygui()
gui.destroy_context()
