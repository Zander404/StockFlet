from flet import *
from .controls import return_control_reference
from .form_helper import FormHelper

controls_map = return_control_reference()


def update_text(e):
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

def get_input_data(e):
    for key, value in controls_map.items():
        if key == 'AppForm':

            data = DataRow(cells=[])

            # Primeira ROW com um TextField
            for user_input in value.controls[0].content.controls[0].controls[:]:
                data.cells.append(
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e)
                    )

                )
                print(user_input.content.controls[1].value)

            # Segunda ROW de TEXTFIELD
            for user_input in value.controls[0].content.controls[1].controls[:]:
                data.cells.append(
                      DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e)
                    )

                )
                print(user_input.content.controls[1].value)

        if key == 'AppDataTable':
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()


def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor='#081d33',
            color='white',
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    Text(
                        'Add Input Field To Table',
                        size=11,
                        weight='bold',
                    )
                ]
            ),
            style=ButtonStyle(
                shape={
                    '': RoundedRectangleBorder(radius=6),
                },
                color={
                    '': 'white'
                },
            ),
            height=42,
            width=220,
        )
    )
