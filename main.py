import dearpygui.dearpygui as dpg

dpg.create_context()


def select_file():
    return "zeel"

def init_main_tab():

    dpg.add_text("Kalpna")

    selected_file_type = dpg.add_combo(["CSV","Excel"],default_value="CSV",width=250, tag="plot", label="Select File Type")

    dpg.add_button(label="Browse", callback=select_file())


    with dpg.plot(label="Sine curve", height=300, width=400):
        pass



with dpg.window(tag="Primary Window"):

    with dpg.tab_bar():

        with dpg.tab(label="Main"):

            init_main_tab()



dpg.create_viewport(title='Custom Title', width=800, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
