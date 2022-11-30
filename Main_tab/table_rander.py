
def main_tab_table_view_render(gui=None, df=None):
    # table view
    gui.delete_item("main_tab_table_view")

    with gui.table(header_row=True, row_background=True,
                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                   borders_outerV=True, parent="main_tab", tag="main_tab_table_view"):

        for i in list(df.columns):
            gui.add_table_column(label=i)

        # print(DATA_TABLE.iloc[1, 2])

        for i in range(df.shape[0]):
            with gui.table_row():
                for j in range(df.shape[1]):
                    gui.add_text(f"{df.iloc[i, j]}")
