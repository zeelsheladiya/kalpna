# popups =================================================================================================

def basic_popup(gui=None, parent_window_name: str = "primary_window", title: str = "", message: str = "", button_name: str = "OK", error: str = "Not defined"):

    try:
        main_width = gui.get_item_width(parent_window_name)
        main_height = gui.get_item_height(parent_window_name)

        with gui.window(label=title, modal=True, show=True, tag="modal_id"):
            gui.add_text(message)
            gui.add_text(error)
            gui.add_separator()
            # gui.add_checkbox(label="Don't ask me next time")
            with gui.group(horizontal=True):
                gui.add_button(label=button_name, width=150, callback=lambda: gui.configure_item("modal_id", show=False))

        gui.set_item_pos("modal_id", (int(0.2 * main_width), int(0.4 * main_height)))

    except Exception as e:
        # need to something but not that important
        pass
