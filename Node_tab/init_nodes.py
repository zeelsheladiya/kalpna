# import dearpygui.dearpygui as gui


# node functions
def table_column_node(sender, app_data, user_data):

    gui = user_data["gui"]

    # close a menu window
    gui.configure_item("right_click_menu_node_menu", show=False)

    print(f"Menu Item: {sender}")

    with gui.node(label="Node 1", parent="node_ground_node_tab"):
        with gui.node_attribute(label="Node A1"):
            gui.add_input_float(label="F1", width=150)

        with gui.node_attribute(label="Node A2", attribute_type=gui.mvNode_Attr_Output):
            gui.add_input_float(label="F2", width=150)
