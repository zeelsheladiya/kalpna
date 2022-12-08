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
def node_render(gui, DATA_TABLE):
# def node_render():

    gui.delete_item("node_tab")

    # node tab
    with gui.tab(label="node tab", tag="node_tab", parent="main_tab_bar"):

        # node editor ground
        with gui.node_editor(callback=link_callback, delink_callback=delink_callback, user_data=gui):
            with gui.node(label="Table"):
                for header in DATA_TABLE.columns:
                    with gui.node_attribute(tag=header):
                        gui.add_input_text(value=header, width=400)

