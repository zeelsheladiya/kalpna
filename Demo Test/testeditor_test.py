import dearpygui.dearpygui as dpg

def save_file(sender, data):
    # Get the contents of the text editor
    text = dpg.get_value("Text Editor")

    # Open a file dialog to select a file to save to
    filename = dpg.file_dialog()

    # Save the contents of the text editor to the selected file
    with open(filename, "w") as f:
        f.write(text)

    # Update the status bar
    dpg.set_value("Status Bar", "File saved")

def open_file(sender, data):
    # Open a file dialog to select a file to open
    filename = dpg.file_dialog()

    # Read the contents of the selected file
    with open(filename, "r") as f:
        text = f.read()

    # Set the contents of the text editor to the selected file's contents
    dpg.set_value("Text Editor", text)

    # Update the status bar
    dpg.set_value("Status Bar", "File opened")

with dpg.window(label="Text Editor"):
    # Create a menu bar and add menus and actions
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save", callback=save_file)
            dpg.add_menu_item(label="Open", callback=open_file)

    # Create a text editor widget
    dpg.add_input_text(label="Text Editor", multiline=True, width=700, height=500, on_enter=True, tab_input=True, tab_size=4, source="Text Editor", autocompletions=["if", "else", "elif", "for", "while", "def", "class"])

    # Create a status bar
    dpg.add_text(label="Status Bar", source="Status Bar")

# Run the application
dpg.create_viewport(title='test editor test')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.set_primary_window("Text Editor", True)
dpg.start_dearpygui()
dpg.destroy_context()
