import dearpygui.dearpygui as gui
import pandas as pd

# internal file importing ======================================================================

# from Popups.Popups import *
# from Msg_Str.msg_str import *
# from Main_tab.table_rander import *
# from Node_tab.node_render import *

# global variable ============================================================================

FILE_PATH: str

FILE_TYPE = {
    "CSV": "csv",
    "Excel": "xlsx"
}

DATA_TABLE: pd.DataFrame()

# global component =======================================================================================

TXT_FILE_SELECTION_LOG: int

# ==============================================================================================

gui.create_context()

# Themes ==================================================================================================
# global main theme
with gui.theme() as global_theme:
    with gui.theme_component(gui.mvAll):
        gui.add_theme_style(gui.mvStyleVar_FrameRounding, 5, category=gui.mvThemeCat_Core)
        gui.add_theme_style(gui.mvStyleVar_FrameBorderSize, 1, category=gui.mvThemeCat_Core)
        gui.add_theme_style(gui.mvStyleVar_ButtonTextAlign, x=0.50, y=0.50, category=gui.mvThemeCat_Core)

# theme for green color text for a target text object
with gui.theme() as green_txt_color_theme:
    with gui.theme_component(gui.mvText):
        gui.add_theme_color(gui.mvThemeCol_Text, (0, 255, 0), category=gui.mvThemeCat_Core)

# theme for red color text for a target text object
with gui.theme() as red_txt_color_theme:
    with gui.theme_component(gui.mvText):
        gui.add_theme_color(gui.mvThemeCol_Text, (255, 0, 0), category=gui.mvThemeCat_Core)


# event section ===========================================================================================


# file browsed file name
# TODO: need to fix file is not supported issue
def file_browse_for_table_callback(_, app_data):
    global FILE_PATH, DATA_TABLE
    # print("App Data: ", app_data["file_path_name"])
    FILE_PATH = app_data["file_path_name"]

    file_type_name = gui.get_value("cb_file_type_main_tab")

    try:
        if list(FILE_TYPE.values())[0] == FILE_TYPE[file_type_name]:
            DATA_TABLE = pd.read_csv(FILE_PATH)

        elif list(FILE_TYPE.values())[1] == FILE_TYPE[file_type_name]:
            DATA_TABLE = pd.read_excel(FILE_PATH)

        # print(DATA_TABLE)

        gui.set_value("txt_file_log_main_tab", FILE_PATH)
        gui.set_value("txt_file_selected_log", "File is Selected")
        gui.bind_item_theme(TXT_FILE_SELECTION_LOG, green_txt_color_theme)

        # table view
        main_tab_table_view_render(gui=gui, df=DATA_TABLE)

        # node tab ==========================================================
        node_render(gui=gui, DATA_TABLE=DATA_TABLE)

    except (pd.errors.ParserError, SystemError, FileNotFoundError) as error:
        # print(str(error))

        gui.set_value("txt_file_log_main_tab", "")
        gui.set_value("txt_file_selected_log", "File Not Selected")
        gui.delete_item("node_tab")
        clear_table_view_main_tab(gui)
        gui.bind_item_theme(TXT_FILE_SELECTION_LOG, red_txt_color_theme)

        basic_popup(gui=gui, parent_window_name="primary_window", title=error_msg_title,
                    message=file_not_support_msg_str, button_name="Retry To Browse File", error=str(error))


# browse button click event
def btn_main_tab_browse_file_browse_callback():
    global FILE_PATH, DATA_TABLE
    # print("sender:- ", sender)
    # print("refuser data:- ", user_data)

    file_type_name = gui.get_value("cb_file_type_main_tab")

    # browse file
    with gui.file_dialog(directory_selector=False, callback=file_browse_for_table_callback, show=True,
                         height=600, width=800):
        gui.add_file_extension(f".{FILE_TYPE[file_type_name]}", color=(0, 255, 0))


# tab section==============================================================================================
# main initial tab
def init_main_tab():
    # file type sector
    global TXT_FILE_SELECTION_LOG, FILE_TYPE

    gui.add_combo(list(FILE_TYPE), default_value="CSV", width=400, tag="cb_file_type_main_tab",
                  label="Select File Type")

    # browse button
    gui.add_button(label="Browse", callback=btn_main_tab_browse_file_browse_callback, user_data="btn_main_tab_browse",
                   width=200)

    # file selection section
    gui.add_input_text(tag="txt_file_log_main_tab", enabled=False)
    TXT_FILE_SELECTION_LOG = gui.add_text("File Not Selected", tag="txt_file_selected_log")
    gui.bind_item_theme(TXT_FILE_SELECTION_LOG, red_txt_color_theme)


# main windows with tabs ====================================================================================
with gui.window(tag="primary_window") as primary_win:
    # init window
    with gui.tab_bar(tag="main_tab_bar"):
        # main tab
        with gui.tab(label="main tab", tag="main_tab"):
            init_main_tab()

# GUI functions ==============================================================================================

# gui.show_debug()
# gui.show_style_editor()
gui.bind_theme(global_theme)
gui.create_viewport(title='Kalpana')
gui.setup_dearpygui()
gui.show_viewport()
gui.maximize_viewport()
gui.set_primary_window("primary_window", True)
gui.start_dearpygui()
gui.destroy_context()
