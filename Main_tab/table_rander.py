
# TODO: make table sortable "this function is not completed need to fix and need to make ot workable"
def sort_callback(sender, sort_specs, user_data):
    gui = user_data
    # sort_specs scenarios:
    #   1. no sorting -> sort_specs == None
    #   2. single sorting -> sort_specs == [[column_id, direction]]
    #   3. multi sorting -> sort_specs == [[col umn_id, direction], [column_id, direction], ...]
    #
    # notes:
    #   1. direction is ascending if == 1
    #   2. direction is ascending if == -1

    # no sorting case
    if sort_specs is None:
        return

    rows = gui.get_item_children(sender, 1)

    # create a list that can be sorted based on first cell
    # value, keeping track of row and value used to sort
    sortable_list = []
    for row in rows:
        first_cell = gui.get_item_children(row, 1)[0]
        sortable_list.append([row, gui.get_value(first_cell)])

    def _sorter(e):
        return e[1]

    sortable_list.sort(key=_sorter, reverse=sort_specs[0][1] < 0)

    # create list of just sorted row ids
    new_order = []
    for pair in sortable_list:
        new_order.append(pair[0])

    gui.reorder_items(sender, 1, new_order)


def clear_table_view_main_tab(gui):
    gui.delete_item("main_tab_table_view")


def main_tab_table_view_render(gui=None, df=None):
    # table view
    gui.delete_item("main_tab_table_view")

    # main table form
    with gui.table(header_row=True, row_background=True,
                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                   borders_outerV=True, parent="main_tab", tag="main_tab_table_view", sortable=True, user_data=gui,
                   resizable=True, policy=gui.mvTable_SizingStretchProp, scrollY=True):

        # header part
        for i in list(df.columns):
            gui.add_table_column(label=i)

        # print(DATA_TABLE.iloc[1, 2])

        # column part
        for i in range(df.shape[0]):
            with gui.table_row():
                for j in range(df.shape[1]):
                    gui.add_text(f"{df.iloc[i, j]}")
