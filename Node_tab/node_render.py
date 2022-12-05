# import dearpygui.dearpygui as gui


# node click events

# callback runs when user attempts to connect attributes
def link_callback(sender, app_data, gui):
    # app_data -> (link_id1, link_id2)
    gui.add_node_link(app_data[0], app_data[1], parent=sender)


# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data, gui):
    # app_data -> link_id
    gui.delete_item(app_data)


# ============================================================================================
# ============================================================================================

# main node tab
def node_render(gui):
# def node_render():

    gui.delete_item("node_tab")

    with gui.tab(label="node tab", tag="node_tab", parent="main_tab_bar"):

        with gui.node_editor(callback=link_callback, delink_callback=delink_callback, user_data=gui):
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
