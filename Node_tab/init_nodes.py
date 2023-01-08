# import dearpygui.dearpygui as gui


# TODO: need to fix table view height into node.
# node functions
def table_column_node(sender, app_data, user_data):

    gui = user_data["gui"]
    data_table = user_data["Data_table"]
    col_name = user_data["col_name"]

    # close a menu window
    gui.configure_item("right_click_menu_node_menu", show=False)

    print(f"Menu Item: {sender}")

    with gui.node(label=col_name, parent="node_ground_node_tab", tag=col_name+"_node"):

        with gui.node_attribute(label="Node A2", attribute_type=gui.mvNode_Attr_Output):

            # column table view
            with gui.table(header_row=True, row_background=True,
                           borders_innerH=True, borders_outerH=True, borders_innerV=True,
                           borders_outerV=True, tag=col_name + "_node_table_view", sortable=False,
                           user_data=gui,
                           resizable=True, policy=gui.mvTable_SizingStretchProp, width=100, parent=col_name):

                # header part (header_row is false that is why commented if it isn't then it is true)
                gui.add_table_column(label=col_name)

                for i in range(data_table[col_name].shape[0]):
                    with gui.table_row():
                        gui.add_text(f"{data_table[col_name][i]}")

    # to set node position on the mouse position
    gui.set_item_pos(col_name + "_node", gui.get_mouse_pos(local=False))


