# import dearpygui.dearpygui as gui
from Popups.Popups import *
from Msg_Str.msg_str import *


# global variable for node
# NODE_COUNTER = 0


PLOT_TYPE_LIST = {
    "line_plot": "Line Plot",
    "bar_plot": "Bar Plot",
    "scatter_plot": "Scatter Plot"
}


# node functions =======================================================================

# support functions =======================================================================

def duplicate_node_else_func(gui, parent_window_name: str = "primary_window",
                             title: str = "unknown",
                             message: str = "duplicate column node error", button_name: str = "Close PopUp"):
    # TODO: need to pop up message for duplicate column or put item in focus instead

    # close a menu window
    gui.configure_item("right_click_menu_node_menu", show=False)

    # basic_popup(gui=gui, parent_window_name="primary_window", title=duplicate_column_node_error_title,
    #             message=duplicate_column_node_error, button_name="Close PopUp")


def node_exception_pop_up_msg_func(gui, parent_window_name: str = "primary_window",
                                   title: str = "unknown",
                                   message: str = "duplicate column node error", button_name: str = "Close PopUp"):
    # TODO: not accurate error need to be fixed
    # basic_popup(gui=gui, parent_window_name="node_ground_node_tab", title=duplicate_column_node_error_title,
    #             message=duplicate_column_node_error, button_name="Close PopUp", error=str(error))

    pass


# node functions ===========================================================================


# table node
def table_node(sender, app_data, user_data):
    try:
        gui = user_data["gui"]
        data_table = user_data["Data_table"]

        if not gui.does_item_exist("table_node"):

            # close a menu window
            gui.configure_item("right_click_menu_node_menu", show=False)

            print(f"Menu Item: {sender}")

            with gui.node(label="Main Table", parent="node_ground_node_tab", tag="table_node"):

                with gui.node_attribute(label="table_output_node", attribute_type=gui.mvNode_Attr_Output,
                                        tag="table_output_node", user_data={"gui": gui, "Data_table": data_table}):
                    # table view
                    with gui.table(tag="table_node_view", sortable=True, user_data=gui,
                                   resizable=True, policy=gui.mvTable_SizingFixedFit, scrollY=True, scrollX=True,
                                   width=250, height=200):

                        # header part

                        for i in list(data_table.columns):
                            gui.add_table_column(label=i)

                        # print(DATA_TABLE.iloc[1, 2])

                        # column part
                        for i in range(data_table.shape[0]):
                            with gui.table_row():
                                for j in range(data_table.shape[1]):
                                    gui.add_text(f"{data_table.iloc[i, j]}")

            # To set node position on the mouse position
            gui.set_item_pos("table_node", gui.get_mouse_pos(local=False))

        else:

            duplicate_node_else_func(gui=gui)

    except Exception as error:

        node_exception_pop_up_msg_func(gui=gui)


# # column node
# def table_column_node(sender, app_data, user_data):
#     try:
#         gui = user_data["gui"]
#         data_table = user_data["Data_table"]
        col_name = user_data["col_name"]

        if not gui.does_item_exist(col_name + "_node"):

            # close a menu window
            gui.configure_item("right_click_menu_node_menu", show=False)

            print(f"Menu Item: {sender}")

            with gui.node(label=col_name, parent="node_ground_node_tab", tag=col_name + "_node"):

                with gui.node_attribute(label=col_name + "_output_node", attribute_type=gui.mvNode_Attr_Output,
                                        tag=col_name + "_output_node", user_data={"gui": gui,
                                                                                  "Data_table": data_table,
                                                                                  "col_name": col_name}):
                    # column table view
                    with gui.table(tag=col_name + "_node_table_view",
                                   user_data=gui, policy=gui.mvTable_SizingFixedSame,
                                   scrollY=True, scrollX=True, width=150, height=200):
                        # header part (header_row is false that is why commented if it isn't then it is true)
                        gui.add_table_column(label=col_name)

                        for i in range(data_table[col_name].shape[0]):
                            with gui.table_row():
                                gui.add_text(f"{data_table[col_name][i]}")

            # To set node position on the mouse position
            gui.set_item_pos(col_name + "_node", gui.get_mouse_pos(local=False))

        else:

            duplicate_node_else_func(gui=gui)

    except Exception as error:

        node_exception_pop_up_msg_func(gui=gui)


# TODO: complete basic plot with customizable label and legend
def basic_plot_node(sender, app_data, user_data):
    try:
        gui = user_data["gui"]

        if not gui.does_item_exist("basic_plot_node"):

            # close a menu window
            gui.configure_item("right_click_menu_node_menu", show=False)

            print(f"Menu Item: {sender}")

            with gui.node(label="Basic plot node", parent="node_ground_node_tab", tag="basic_plot_node"):

                # X axis
                with gui.node_attribute(label="X Axis", attribute_type=gui.mvNode_Attr_Input,
                                        tag="basic_plot_x_input_node"):
                    gui.add_text("X Axis")

                # Y axis
                with gui.node_attribute(label="Y Axis", attribute_type=gui.mvNode_Attr_Input,
                                        tag="basic_plot_y_input_node"):
                    gui.add_text("Y Axis")

                with gui.node_attribute(label="plot Selection", attribute_type=gui.mvNode_Attr_Static,
                                        tag="basic_plot_node_plot_type_combo"):
                    # combo box for the type of plot
                    gui.add_combo(list(PLOT_TYPE_LIST.values()), default_value="Line Plot", width=150,
                                  tag="basic_plot_node_plot_type", label="Select Plot Type",
                                  parent="basic_plot_node_plot_type_combo")

                with gui.node_attribute(label="basic plot", attribute_type=gui.mvNode_Attr_Static,
                                        tag="basic_plot_node_plot"):
                    with gui.plot(label="basic plot", height=400, width=400):

                        # optionally create legend
                        gui.add_plot_legend()

                        # REQUIRED: create x and y axes
                        gui.add_plot_axis(gui.mvXAxis, label="X Axis", tag="basic_plot_node_x_axis")
                        gui.add_plot_axis(gui.mvYAxis, label="Y Axis", tag="basic_plot_node_y_axis")

                        # TODO: need to put more plots options
                        # draw plot default one the line plot
                        gui.add_line_series([], [], label="X * Y", parent="basic_plot_node_y_axis",
                                            tag="basic_plot_node_line_plot_draw")

                        # draw scatter plot
                        gui.add_scatter_series([], [], label="X * Y", parent="basic_plot_node_y_axis",
                                               tag="basic_plot_node_scatter_plot_draw")

                        # draw bar plot
                        gui.add_bar_series([], [], label="X * Y", parent="basic_plot_node_y_axis",
                                           tag="basic_plot_node_bar_plot_draw")

            # To set node position on the mouse position
            gui.set_item_pos("basic_plot_node", gui.get_mouse_pos(local=False))

        else:

            duplicate_node_else_func(gui=gui)

    except Exception as error:

        node_exception_pop_up_msg_func(gui=gui)
