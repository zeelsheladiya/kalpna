import dearpygui.dearpygui as gui

gui.create_context()

# event section
def file_browse_callback(sender, _, user_data):
    print(f'sender:- {sender}')
    print(f'user data:- {user_data}')


# tab section
def init_main_tab():
    gui.add_combo(["CSV", "Excel"], default_value="CSV", width=250, tag="plot", label="Select File Type")

    gui.add_button(label="Browse", callback=file_browse_callback, user_data="btn_browse")

    with gui.plot(label="plot", height=300, width=400):
        pass


with gui.window(tag="Primary Window"):
    with gui.tab_bar():
        with gui.tab(label="Main"):
            init_main_tab()


gui.create_viewport(title='Kalpna', width=800, height=500)
gui.setup_dearpygui()
gui.show_viewport()
gui.set_primary_window("Primary Window", True)
gui.start_dearpygui()
gui.destroy_context()
