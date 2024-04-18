from flet import *
from .controls import add_to_control_reference


class AppDataTable(UserControl):
    
    def app_data_table_instance(self):
        add_to_control_reference("AppDataTable", self)


    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, '#ebebeb'),
                    horizontal_lines=border.BorderSide(1, '#ebebeb'),
                    columns=[
                        DataColumn(Text("Column 1", size=12, color="black", weight="bold")),
                        DataColumn(Text("Column 2", size=12, color="black", weight="bold")),
                        DataColumn(Text("Column 3", size=12, color="black", weight="bold")),
                        DataColumn(Text("Column 4", size=12, color="black", weight="bold")),
                    ],
                    rows=[]
                )
            ]
        )