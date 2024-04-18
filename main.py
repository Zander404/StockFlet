import flet
from flet import *
from components.forms.header import AppHeader
from components.forms.form import AppForm
from components.forms.data_table import AppDataTable


def main(page: Page):
    page.bgcolor = '#fdfdfd'
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height=2,color='transparent' ),
                AppForm(),
                
                Column(
                    scroll='hidden',
                    expand=True,
                    controls=[
                        AppDataTable()
                    ]
                )
            ]
        )
    )



    page.update()


if __name__ == '__main__':
    flet.app(target=main) 