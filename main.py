import dearpygui.dearpygui as gui


gui.create_context()


# event section
def file_browse_callback(sender, _, user_data):
    print(f'sender:- {sender}')
    print(f'user data:- {user_data}')


# tab section
def init_main_tab():

    # file type sector
    gui.add_combo(["CSV", "Excel"], default_value="CSV", width=400, tag="plot", label="Select File Type")

    # browse button
    gui.add_button(label="Browse", callback=file_browse_callback, user_data="btn_browse", width=200)

    # file selection section
    gui.add_input_text(enabled=False)
    gui.add_text("File Not Selected", color=(255, 0, 0))


with gui.window(tag="primary_window"):
    with gui.tab_bar():
        with gui.tab(label="main_tab"):
            init_main_tab()


gui.create_viewport(title='Kalpna')
gui.setup_dearpygui()
gui.show_viewport()
gui.maximize_viewport()
gui.set_primary_window("primary_window", True)
gui.start_dearpygui()
gui.destroy_context()
