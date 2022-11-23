import dearpygui.dearpygui as dpg

dpg.create_context()

def print_text():
    print("yoyo")

def init_main_tab():

    dpg.add_text("Kalpna")

    dpg.add_combo(["zeel","zeel"],default_value="Plot",width=250, tag="plot")

    button1 = dpg.add_button(label="Press Me!", callback=print_text)

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
