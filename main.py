import dearpygui.dearpygui as dpg

dpg.create_context()

def print_text():
    print("yoyo")

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")

    button1 = dpg.add_button(label="Press Me!", callback=print_text)

    dpg.add_simple_plot(label="Simpleplot1", default_value=(0.3, 0.9, 0.5, 0.3), height=300)

dpg.create_viewport(title='Custom Title', width=800, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
