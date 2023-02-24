# import dearpygui.dearpygui as gui

from Node_tab.init_nodes import *

# variable for node editor

# To check which node attribute is connected
node_connection = {
    "Basic plot node": {
        "x_axis": 0,
        "y_axis": 0
    }
}


# To get and set the column data for nodes
node_attribute_data = {
    "Basic plot node": {
        "x_axis": [],
        "y_axis": []
    }
}


# helper functions =======================================

def basic_plot_node_plot_select_type(gui):

    # if node_connection["Basic plot node"]["x_axis"] == 1 and node_connection["Basic plot node"]["y_axis"] == 1:
    #
    #     if gui.get_value("basic_plot_node_plot_type") == "Line Plot":
    #
    #         gui.set_value('basic_plot_node_plot_draw', [list(node_attribute_data["Basic plot node"]["x_axis"]),
    #                                                     list(node_attribute_data["Basic plot node"]["y_axis"])])


# =========================================================

# node clicks events callbacks

def right_click_node_menu_callback(sender, app_data, user_data):
    gui = user_data["gui"]

    # get active tab based on it position
    if gui.get_item_state("node_tab")["pos"] == [8, 31]:
        gui.configure_item("right_click_menu_node_menu", show=True)
        gui.set_item_pos("right_click_menu_node_menu", gui.get_mouse_pos(local=False))


def left_click_node_menu_callback(sender, app_data, user_data):
    gui = user_data["gui"]

    # get active tab based on it position
    if gui.get_item_state("node_tab")["pos"] == [8, 31]:
        if gui.get_item_state(gui.get_active_window())["hovered"] is not True:
            gui.configure_item("right_click_menu_node_menu", show=False)


# TODO: need to check functionality of this link function
# callback runs when user attempts to connect attributes
def link_callback(sender, app_data, user_data):
    gui = user_data["gui"]
    data_table = user_data["Data_table"]
    # print(sender)
    gui.add_node_link(app_data[0], app_data[1], parent=sender)
    # print(app_data[0], app_data[1])
    # print(gui.get_item_parent(app_data[1]))
    # print(gui.get_item_user_data(app_data[0])["col_name"])

    # for the basic plot node ========================
    # TODO: make focus on x and y range in plot
    if gui.get_item_parent(app_data[1]) == "basic_plot_node":

        if app_data[1] == "basic_plot_x_input_node":
            node_connection["Basic plot node"]["x_axis"] = 1
            node_attribute_data["Basic plot node"]["x_axis"] = data_table[gui.get_item_user_data(app_data[0])["col_name"]]

        if app_data[1] == "basic_plot_y_input_node":
            node_connection["Basic plot node"]["y_axis"] = 1
            node_attribute_data["Basic plot node"]["y_axis"] = data_table[gui.get_item_user_data(app_data[0])["col_name"]]

        basic_plot_node_plot_select_type(gui=gui)


# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data, user_data):
    gui = user_data["gui"]
    # app_data -> link_id
    gui.delete_item(app_data)


# ============================================================================================
# ============================================================================================

# init node menu

def init_node_menu(gui, DATA_TABLE):
    # main table node
    gui.add_menu_item(label="Table", callback=table_node, user_data={"gui": gui, "Data_table": DATA_TABLE})

    # column node
    with gui.menu(label="Table Columns"):
        for col in DATA_TABLE.columns:
            gui.add_menu_item(label=col, tag=col, callback=table_column_node, user_data={"gui": gui,
                                                                                         "Data_table": DATA_TABLE,
                                                                                         "col_name": col})
    # graph plotting node
    with gui.menu(label="Graph Plotting"):
        gui.add_menu_item(label="Basic plot", callback=basic_plot_node, user_data={"gui": gui})


# ============================================================================================
# ============================================================================================

# main node tab
# this comment is just for development purpose
# def node_render():
def node_render(gui, DATA_TABLE):
    gui.delete_item("node_tab")

    # node tab
    with gui.tab(label="node tab", tag="node_tab", parent="main_tab_bar"):
        # node editor ground
        with gui.node_editor(tag="node_ground_node_tab", callback=link_callback, delink_callback=delink_callback,
                             user_data={"gui": gui, "Data_table": DATA_TABLE},
                             minimap=True, minimap_location=True, parent="node_tab"):
            # created right click registry
            with gui.handler_registry():
                gui.add_mouse_click_handler(button=gui.mvMouseButton_Right, callback=right_click_node_menu_callback,
                                            user_data={"gui": gui})
                gui.add_mouse_click_handler(button=gui.mvMouseButton_Left, callback=left_click_node_menu_callback,
                                            user_data={"gui": gui})

            with gui.window(label="Right click node menu", modal=True, show=False, id="right_click_menu_node_menu",
                            no_title_bar=True, tag="right_click_menu_node_menu", width=150):
                init_node_menu(gui=gui, DATA_TABLE=DATA_TABLE)
