# import dearpygui.dearpygui as gui

# variable for node editor

# Create the popup menu items
node_menu_items = [
    {"item1": "Option 1"},
    {"item2": "Option 2"},
    {"item3": "Option 3"},
]


# node click events callbacks

def on_right_click_callback(gui):
    with gui.popup():
        gui.add_text("A popup")


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
    pass
