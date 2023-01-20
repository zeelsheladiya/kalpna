import dearpygui.dearpygui as gui
from Popups.Popups import *
from Msg_Str.msg_str import *


# global variable for node
# NODE_COUNTER = 0

# TODO:  need to solve node spawn problem. Help could be node counter
# node functions
def table_column_node(sender, app_data, user_data):
    try:
        # gui = user_data["gui"]
        data_table = user_data["Data_table"]
        col_name = user_data["col_name"]

        if not gui.does_item_exist(col_name + "_node"):

            # close a menu window
            gui.configure_item("right_click_menu_node_menu", show=False)

            print(f"Menu Item: {sender}")

            with gui.node(label=col_name, parent="node_ground_node_tab", tag=col_name + "_node"):

                with gui.node_attribute(label="Node A2", attribute_type=gui.mvNode_Attr_Output,
                                        tag=col_name + "_node_attribute"):
                    # column table view
                    with gui.table(tag=col_name + "_node_table_view",
                                   user_data=gui, policy=gui.mvTable_SizingFixedSame,
                                   scrollY=True, width=150, height=200):
                        # header part (header_row is false that is why commented if it isn't then it is true)
                        gui.add_table_column(label=col_name)

                        for i in range(data_table[col_name].shape[0]):
                            with gui.table_row():
                                gui.add_text(f"{data_table[col_name][i]}")

            # To set node position on the mouse position
            gui.set_item_pos(col_name + "_node", gui.get_mouse_pos(local=False))

        else:
            # TODO: need to pop up message for duplicate column or put item in focus instead

            # close a menu window
            gui.configure_item("right_click_menu_node_menu", show=False)

            # basic_popup(gui=gui, parent_window_name="primary_window", title=duplicate_column_node_error_title,
            #             message=duplicate_column_node_error, button_name="Close PopUp")

            pass

    except Exception as error:

        # TODO: not accurate error need to be fixed
        basic_popup(gui=gui, parent_window_name="node_ground_node_tab", title=duplicate_column_node_error_title,
                    message=duplicate_column_node_error, button_name="Close PopUp", error=str(error))
