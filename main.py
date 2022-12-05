import dearpygui.dearpygui as gui
import easygui
import pandas as pd

# internal file importing ======================================================================

from Popups.Popups import *
from Msg_Str.msg_str import *
from Main_tab.table_rander import *

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

# theme for green color text for target text object
with gui.theme() as green_txt_color_theme:
    with gui.theme_component(gui.mvText):
        gui.add_theme_color(gui.mvThemeCol_Text, (0, 255, 0), category=gui.mvThemeCat_Core)

# theme for red color text for target text object
with gui.theme() as red_txt_color_theme:
    with gui.theme_component(gui.mvText):
        gui.add_theme_color(gui.mvThemeCol_Text, (255, 0, 0), category=gui.mvThemeCat_Core)


# event section ===========================================================================================

# node click events

# callback runs when user attempts to connect attributes
def link_callback(sender, app_data):
    # app_data -> (link_id1, link_id2)
    gui.add_node_link(app_data[0], app_data[1], parent=sender)


# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data):
    # app_data -> link_id
    gui.delete_item(app_data)


# browse button click event
def btn_main_tab_browse_file_browse_callback():
    global FILE_PATH, DATA_TABLE
    # print("sender:- ", sender)
    # print("refuser data:- ", user_data)
    file_type_name = gui.get_value("cb_file_type_main_tab")

    FILE_PATH = easygui.fileopenbox(msg=f'Please locate the {file_type_name} file',
                                    default=f"*.{FILE_TYPE[file_type_name]}",
                                    filetypes=[f"*.{FILE_TYPE[file_type_name]}"],
                                    multiple=False)

    try:
        if list(FILE_TYPE.values())[0] == FILE_TYPE[file_type_name]:
            DATA_TABLE = pd.read_csv(FILE_PATH)

        elif list(FILE_TYPE.values())[1] == FILE_TYPE[file_type_name]:
            DATA_TABLE = pd.read_excel(FILE_PATH)

        # print(DATA_TABLE)

        gui.set_value("txt_file_log", FILE_PATH)
        gui.set_value("txt_file_selected_log", "File is Selected")
        gui.bind_item_theme(TXT_FILE_SELECTION_LOG, green_txt_color_theme)

        # table view
        main_tab_table_view_render(gui=gui, df=DATA_TABLE)

        # node tab ==========================================================

        gui.delete_item("node_tab")

        with gui.tab(label="node tab", tag="node_tab", parent="main_tab_bar"):
            with gui.node_editor(callback=link_callback, delink_callback=delink_callback):
                with gui.node(label="Node 1"):
                    with gui.node_attribute(label="Node A1"):
                        gui.add_input_float(label="F1", width=150)

                    with gui.node_attribute(label="Node A2", attribute_type=gui.mvNode_Attr_Output):
                        gui.add_input_float(label="F2", width=150)

                with gui.node(label="Node 2"):                                        
                    with gui.node_attribute(label="Node A3"):
                        gui.add_input_float(label="F3", width=200)

                    with gui.node_attribute(label="Node A4", attribute_type=gui.mvNode_Attr_Output):
                        gui.add_input_float(label="F4", width=200)

    except (pd.errors.ParserError, SystemError):
        basic_popup(easygui=easygui, title=error_msg_title, message=file_not_support_msg_str,
                    button_name="Retry To Browse File")


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
    gui.add_input_text(tag="txt_file_log", enabled=False)
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
