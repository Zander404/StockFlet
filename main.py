
import flet
from flet import *
import requests
from time import sleep

BG_COLOR = '#252A41'
BG_SUB_COLOR = '#1E2757'


TEXT_COLOR = '#ffffff'
TEXT_SUB_COLOR = '#ffffff'


BTN_TXT = ''
BTN_COLOR = '#6D7CBF'

WIDTH_SCREEN = 1400
HEIGHT_SCREEN = 640


class Login(UserControl):
    def __init__(self):
        self.login = Container(
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_COLOR,
            border_radius=8,
            padding=10,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT),
        )

        self.login_box = Row(
            alignment=MainAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False
        )

        self.login_email = self.login_option('Email', False)

        self.login_password = self.login_option('Senha', True)

        self.error_message = Text("EMAIL OU SENHA INVÁLIDO!",
                                  color='red',
                                  style=TextStyle(
                                      size=12, color='white', weight='w800'),
                                  opacity=100,
                                  visible=False)

        self.login_btn = self.login_button(
            "Logar", lambda e: self.authentication(e))

        super().__init__()

    def open_modal(self):
        sleep(0.2)
        self.login.width = WIDTH_SCREEN
        self.login.update()
        sleep(0.5)

        self.login_box.visible = True
        self.login_box.update()

    def close_modal(self):
        self.login_box.visible = False
        sleep(0.35)

        self.login.width = 0
        self.login.update()
        sleep(0.75)

        self.page.controls.remove(self)
        self.main = MainPage()

        self.page.controls.insert(0, self.main)

        self.page.update()
        sleep(0.35)

        self.main.open_mainpage()

    def login_option(self, label: str, password: bool):
        option = TextField(
            width=240,
            height=50,
            color=TEXT_COLOR,
            text_size=12,
            filled=True,

            label=label,
            label_style=TextStyle(size=8, color=TEXT_COLOR, weight='bold'),

            password=password,
            can_reveal_password=password,

            cursor_color=TEXT_COLOR,
            cursor_width=1,

            border='underline',
            border_color=TEXT_COLOR,

        )

        return option

    def login_button(self, label: str, btn_fuction):
        return ElevatedButton(
            content=Text(label, style=TextStyle(
                size=12, weight='bold', color='white')),
            on_click=btn_fuction,
            color=BTN_COLOR,
            width=240,
            height=45,
            style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=8)})


        )

    def authentication(self, e):

        try:

            self.error_message.visible = False
            self.login_box.update()

            email = self.login_email.value
            password = self.login_password.value

            # TODO
            # data = requests.post('https://localhost:8000/api/login/', data=[email, password])

            if email == "sim" and password == "sim":
                self.close_modal()
            else:
                raise Exception("Senha Inválida")

        except Exception as e:
            self.login_email.value = ''
            self.login_password.value = ''

            self.login_email.border_color = 'red'
            self.login_password.border_color = 'red'

            self.error_message.visible = True
            self.login_box.update()

            self.error_message.update()

    def build(self):
        texts: list = [
            Text('Login', size=12, color='white', style=TextStyle(
                size=8, color='white', weight='w800')),
            self.login_email,
            self.login_password,
            self.error_message,
            Divider(height=2, color='transparent'),
            self.login_btn,
        ]

        columns = Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )

        for i in texts:
            columns.controls.append(i)

        self.login_box.controls.append(columns)

        self.login.content = self.login_box

        return self.login


class MainPage(UserControl):
    def __init__(self):
        self.main = Container(
            padding=10,
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_SUB_COLOR,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT),
        )

        self.main_box = Row(
            alignment=MainAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False
        )

        self.logo = Icon(icons.SPORTS_SOCCER, color='white')
        self.title = Text("SHOW DE BOLA SOFTWARE")

        self.cashier_path = self.mainpage_btn(
            'Caixa', icon_selected=icons.PERSON_2_OUTLINED, btn_function=lambda e: self.routes(e, 'cashier'))

        self.products_path = self.mainpage_btn(
            "Produtos", icon_selected=icons.PRODUCTION_QUANTITY_LIMITS_OUTLINED,  btn_function=lambda e: self.routes(e, 'products'))

        self.orders_path = self.mainpage_btn(
            "Pedidos", icon_selected=icons.LIST_ALT_OUTLINED, btn_function=lambda e: self.routes(e, 'orders'))

        self.row_paths = Row(
            controls=[
                self.cashier_path,
                self.products_path,
                self.orders_path,
            ],
            alignment=MainAxisAlignment.CENTER,
            expand=True,

        )

        super().__init__()

    def routes(self, e, route_path: str):
        self.close_mainpage(go_to=route_path)

    def open_mainpage(self):
        sleep(0.3)
        self.main.width = WIDTH_SCREEN
        self.main.update()
        sleep(0.35)

        self.main_box.visible = True
        self.main_box.update()
        sleep(0.2)

    def close_mainpage(self, go_to):
        self.main_box.visible = False
        self.main_box.update()
        sleep(0.35)

        self.main.width = 0
        self.main.update()
        sleep(0.75)

        self.page.controls.remove(self)

        if go_to == 'cashier':
            self.cashier = Cashier()
            self.page.controls.insert(0, self.cashier)
            self.page.update()
            sleep(0.35)

            self.cashier.open_modal()

        if go_to == 'products':
            self.products = Product()
            self.page.controls.insert(0, self.products)
            self.page.update()
            sleep(0.35)

            self.products.open_modal()

        if go_to == 'orders':
            self.orders = Order()
            self.page.controls.insert(0, self.orders)
            self.page.update()
            sleep(0.35)

            self.orders.open_modal()

    def mainpage_btn(self, label: str, btn_function, icon_selected):
        return ElevatedButton(
            on_click=btn_function,
            color=BTN_COLOR,
            width=160,
            height=45,
            style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=8)}),
            text=label,
            icon=icon_selected
        )

    def build(self):

        main_column = Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )

        main_column.controls.append(self.logo)
        main_column.controls.append(self.title)
        main_column.controls.append(Divider(height=6, color='transparent'))
        main_column.controls.append(self.row_paths)

        self.main_box.controls.append(main_column)
        self.main.content = self.main_box

        return self.main


class Cashier(UserControl):

    def __init__(self):
        self.page_number = 0
        self.page_size = 30

        self.cashier = Container(
            padding=10,
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_COLOR,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT),

        )

        self.cashier_box = Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False,
        )

        self.title = Text('Caixa', style=TextStyle(16, weight='bold'))

        self.search_bar = Row(
            spacing=20,
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.END,
            controls=[
                TextField(
                    border_color='transparent',
                    height=20,
                    text_size=14,
                    content_padding=0,
                    cursor_color='white',
                    cursor_width=1,
                    color='white',
                    hint_text='Pesquisar',
                    on_change=lambda e: self.filter_data_table(e),
                ),

                Icon(
                    name=icons.SEARCH_ROUNDED,
                    size=17,
                    opacity=0.85,
                    color='red10'
                ),
            ]
        )

        self.new_cashier = Column(
            alignment=MainAxisAlignment.END,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[Row(
                controls=[
                    self.btn_cashier("Voltar", lambda x: self.close_modal(
                    ), icon=icons.ARROW_BACK_IOS_NEW_OUTLINED),
                    self.btn_cashier("Adicionar Caixa", lambda e: self.open_dlg() , icon=icons.PERSON_ADD),

                ],
                vertical_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),]

        )

        self.list_cashier = ListView(expand=True, spacing=10, padding=20)

        self.table_cashier = DataTable(
            expand=True,
            border_radius=8,
            border=border.all(2, TEXT_COLOR),
            horizontal_lines=BorderSide(1),
            columns=[
                DataColumn(Text('ID')),
                DataColumn(Text('CPF')),
                DataColumn(Text('NOME')),
                DataColumn(Text('EMAIL')),
            ],
            rows=[

            ]
        )

        self.btns = Row(
            alignment=MainAxisAlignment.SPACE_AROUND,
            controls=[
                self.btn_cashier("Anterior", lambda x: self.move_page(
                    "previous"), icon=icons.ARROW_BACK),
                self.btn_cashier('Próximo', lambda x: self.move_page(
                    'next'), icon=icons.ARROW_FORWARD)
            ],

        )
        self.btns.controls[0].disabled = True

        # Modal
        self.cashier_dlg_items = Column(controls=[
            TextField(label="CPF"),
            TextField(label="NOME"),
            TextField(label="EMAIL"),
            TextField(label="SENHA"),
            TextField(label="CONFIRMAR SENHA"),
        ],
        )

        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Adicionar Produto"),
            content=self.cashier_dlg_items,
            actions=[
                TextButton("Voltar", on_click=lambda e: self.close_dlg()),
                TextButton("Salvar", on_click=lambda e: self.save_cashier_dlg(
                    self.cashier_dlg_items.controls[:])),
            ],
            actions_alignment=MainAxisAlignment.CENTER,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        super().__init__()

    def open_modal(self):
        sleep(1)
        self.cashier.width = WIDTH_SCREEN
        self.cashier.update()

        sleep(0.5)

        self.cashier_box.visible = True
        self.cashier_box.update()

    def close_modal(self):
        self.cashier_box.visible = False
        self.cashier_box.update()
        sleep(0.35)

        self.cashier.width = 0
        self.cashier.update()
        sleep(0.75)

        self.page.controls.remove(self)

        self.main = MainPage()
        self.page.controls.insert(0, self.main)

        self.page.update()

        self.main.open_mainpage()

    def btn_cashier(self, label: str, btn_function, icon):
        return ElevatedButton(
            text=label,
            icon=icon,
            on_click=btn_function,
            color=BTN_COLOR,
            width=200,
            height=35,
            style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=8)})


        )

    def move_page(self, direction: str):

        if direction == 'next':
            self.page_number += 1

        elif direction == 'previous':
            self.page_number -= 1

        if self.page_number <= 0:

            self.page_number = 0
            # Previous Btn
            self.btns.controls[0].disabled = True
            self.btns.controls[0].update()

        elif self.page_number >= 5:
            self.btns.controls[1].disabled = True
            self.btns.controls[1].update()

        else:
            # Previous Btn
            self.btns.controls[0].disabled = False
            self.btns.controls[0].update()

            # Next Btn
            self.btns.controls[1].disabled = False
            self.btns.controls[1].update()

        start_index = self.page_size*self.page_number

        self.table_cashier.rows.clear()

        for i in range(self.page_size):
            row = DataRow(
                cells=[
                    DataCell(Text(start_index+i)),
                    DataCell(Text("12345678910")),
                    DataCell(Text("Fulano")),
                    DataCell(Text("email@email.com")),
                ]
            )
            self.table_cashier.rows.append(row)

        self.table_cashier.update()

    def filter_data_table(self, e):
        print(self.search_bar.controls[0].value)

        for data in self.cashier_box.controls[0].controls[2].controls[0].rows[:]:

            if e.data in data.cells[1].content.value:
                data.visible = True
                data.update()

            elif e.data.lower() in data.cells[2].content.value.lower():
                data.visible = True
                data.update()

            else:
                data.visible = False
                data.update()

    def open_dlg(self):
        self.dlg_modal.open = True
        self.cashier_box.update()

    def close_dlg(self):
        self.dlg_modal.open = False
        self.cashier_box.update()

    def save_cashier_dlg(self, items):
        for i in items:
            print(i.value)

        self.dlg_modal.open = False
        self.cashier_box.update()

    def build(self):

        container = Column(
            expand=True,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )

        self.list_cashier.controls.append(self.table_cashier)

        for n in range(self.page_size):
            row = DataRow(
                cells=[
                    DataCell(Text(n+1)),
                    DataCell(Text("12345678910")),
                    DataCell(Text("Fulano")),
                    DataCell(Text("email@email.com")),
                ]
            )

            self.table_cashier.rows.append(row)

        container.controls.append(self.title)
        container.controls.append(self.new_cashier)
        # container.controls.append(self.search_bar)
        container.controls.append(self.list_cashier)

        container.controls.append(self.btns)
        container.controls.append(self.dlg_modal)

        self.cashier_box.controls.append(container)

        self.cashier.content = self.cashier_box

        return self.cashier


class Product(UserControl):
    def __init__(self):

        self.page_number = 0
        self.page_size = 30

        self.product = Container(
            padding=10,
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_SUB_COLOR,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT),
        )

        self.product_box = Row(
            alignment=MainAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False
        )

        self.title = Text('Lista de Produtos',
                          style=TextStyle(16, weight='bold'))

        self.new_product = Row(
            controls=[
                self.product_btn('Voltar', lambda e: self.close_modal(
                ), icon_selected=icons.ARROW_BACK_IOS),
                self.product_btn(
                    'Adicionar', lambda e: self.open_dlg(), icon_selected=icons.NOTE_ADD)
            ],
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.SPACE_AROUND,
        )

        self.product_view = ListView(expand=True, spacing=20, padding=10,
                                     controls=[DataTable(
                                         expand=True,
                                         border_radius=8,
                                         border=border.all(2, TEXT_COLOR),
                                         horizontal_lines=BorderSide(1),
                                         columns=[
                                             DataColumn(Text('COD')),
                                             DataColumn(Text('PRODUTO')),
                                             DataColumn(Text('OBSERVAÇÕES')),
                                             DataColumn(Text('PREÇO')),
                                             DataColumn(Text('ESTOQUE')),
                                         ],
                                         rows=[

                                         ]
                                     )])
        self.btns = Row(
            alignment=MainAxisAlignment.SPACE_AROUND,
            controls=[
                self.product_btn("Anterior", lambda x: self.move_page(
                    "previous"), icon_selected=icons.ARROW_BACK),
                self.product_btn('Próximo', lambda x: self.move_page(
                    'next'), icon_selected=icons.ARROW_FORWARD)
            ],

        )
        self.btns.controls[0].disabled = True

        # Modal
        self.product_dlg_items = Column(controls=[
            TextField(label="Código de Barras"),
            TextField(label="Produto"),
            TextField(label="Observações"),
            TextField(label="Preço"),
            TextField(label="Estoque"),
        ],
        )

        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Adicionar Produto"),
            content=self.product_dlg_items,
            actions=[
                TextButton("Voltar", on_click=lambda e: self.close_dlg()),
                TextButton("Salvar", on_click=lambda e: self.save_product_dlg(
                    self.product_items.controls[:])),
            ],
            actions_alignment=MainAxisAlignment.CENTER,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        super().__init__()

    def open_modal(self):
        self.product.width = WIDTH_SCREEN
        self.product.update()

        sleep(0.2)
        self.product_box.visible = True
        self.product_box.update()

    def close_modal(self):
        self.product_box.visible = False
        self.product_box.update()
        sleep(0.35)

        self.product.width = 0
        self.product.update()
        sleep(0.75)

        self.page.controls.remove(self)

        self.main = MainPage()
        self.page.controls.insert(0, self.main)

        self.page.update()
        sleep(0.35)

        self.main.open_mainpage()

    def product_btn(self, label: str, btn_function, icon_selected):
        return ElevatedButton(
            on_click=btn_function,
            color=BTN_COLOR,
            width=160,
            height=45,
            style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=8)}),
            text=label,
            icon=icon_selected
        )

    def move_page(self, direction: str):

        if direction == 'next':
            self.page_number += 1

        elif direction == 'previous':
            self.page_number -= 1

        if self.page_number <= 0:

            self.page_number = 0
            # Previous Btn
            self.btns.controls[0].disabled = True
            self.btns.controls[0].update()

        elif self.page_number >= 5:
            self.btns.controls[1].disabled = True
            self.btns.controls[1].update()

        else:
            # Previous Btn
            self.btns.controls[0].disabled = False
            self.btns.controls[0].update()

            # Next Btn
            self.btns.controls[1].disabled = False
            self.btns.controls[1].update()

        start_index = self.page_size*self.page_number

        self.product_view.controls[0].rows.clear()

        for i in range(self.page_size):
            row = DataRow(
                cells=[
                    DataCell(Text(start_index+i)),
                    DataCell(Text("Carro")),
                    DataCell(Text('4 portas')),
                    DataCell(Text('R$ 100',)),
                    DataCell(Text('1000 und')),
                ]
            )
            self.product_view.controls[0].rows.append(row)

        self.product_view.update()

    def open_dlg(self):
        self.dlg_modal.open = True
        self.product_box.update()

    def close_dlg(self):
        self.dlg_modal.open = False
        self.product_box.update()

    def save_product_dlg(self, items):
        for i in items:
            print(i.value)

        self.dlg_modal.open = False
        self.order_box.update()

    def build(self):

        container = Column(
            expand=True,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )

        container.controls.append(self.title)
        container.controls.append(self.new_product)
        container.controls.append(self.product_view)
        container.controls.append(self.btns)
        container.controls.append(self.dlg_modal)

        for i in range(self.page_size):
            row = DataRow(
                cells=[
                    DataCell(Text(i+1)),
                    DataCell(Text("Carro")),
                    DataCell(Text('4 portas')),
                    DataCell(Text('R$ 100',)),
                    DataCell(Text('1000 und')),
                ]
            )

            self.product_view.controls[0].rows.append(row)

        self.product_box.controls.append(container)
        self.product.content = self.product_box
        return self.product


class Order(UserControl):
    def __init__(self):

        self.page_size: int = 30
        self.page_number: int = 0

        self.order = Container(
            padding=10,
            width=0,
            height=HEIGHT_SCREEN,
            bgcolor=BG_SUB_COLOR,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT),
        )

        self.order_box = Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
            visible=False,
        )

        self.title = Text('Lista de Pedidos',
                          style=TextStyle(16, weight='bold'))

        self.new_order = Row(
            alignment=MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.order_btn("Voltar", lambda e:  self.close_modal(),
                               icon_selected=icons.ARROW_BACK),
                self.order_btn('Adicionar', lambda e: self.open_dlg(),
                               icon_selected=icons.ADD_CARD)
            ],
        )

        self.order_list = ListView(
            expand=True,
            spacing=20,
            padding=10,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, TEXT_COLOR),
                    horizontal_lines=BorderSide(1),
                    columns=[
                        DataColumn(Text('ID')),
                        DataColumn(Text('DIA')),
                        DataColumn(Text('CLIENTE')),
                        DataColumn(Text('CAIXA')),
                        DataColumn(Text('PAGAMENTO')),
                        DataColumn(Text('LISTA DE PRODUTOS')),

                    ],
                    rows=[

                    ]
                )
            ]
        )

        self.btns = Row(
            alignment=MainAxisAlignment.SPACE_AROUND,
            controls=[
                self.order_btn("Anterior", lambda x: self.move_page(
                    "previous"), icon_selected=icons.ARROW_BACK),
                self.order_btn('Próximo', lambda x: self.move_page(
                    'next'), icon_selected=icons.ARROW_FORWARD)
            ],
        )

        self.btns.controls[0].disabled = True

        # Modal
        self.order_dlg_items = Column(controls=[
            TextField(label="Dia da Compra "),
            TextField(label="Cliente"),
            TextField(label="Caixa"),
            TextField(label="Pagamento"),
            TextField(label="Produtos"),
        ],
        )

        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Adicionar Pedido"),
            content=self.order_dlg_items,
            actions=[
                TextButton("Voltar", on_click=lambda e: self.close_dlg()),
                TextButton("Salvar", on_click=lambda e: self.save_order_dlg(
                    self.order_dlg_items.controls[:])),
            ],
            actions_alignment=MainAxisAlignment.CENTER,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        super().__init__()

    def open_modal(self):
        self.order.width = WIDTH_SCREEN
        self.order.update()

        sleep(0.2)
        self.order_box.visible = True
        self.order_box.update()

    def close_modal(self):
        self.order_box.visible = False
        self.order_box.update()
        sleep(0.35)

        self.order.width = 0
        self.order.update()
        sleep(0.75)

        self.page.controls.remove(self)

        self.main = MainPage()
        self.page.controls.insert(0, self.main)
        self.page.update()
        sleep(0.35)

        self.main.open_mainpage()

    def order_btn(self, label: str, btn_function, icon_selected):
        return ElevatedButton(text=label,
                              icon=icon_selected,
                              on_click=btn_function)

    def move_page(self, direction: str):

        if direction == 'next':
            self.page_number += 1

        elif direction == 'previous':
            self.page_number -= 1

        if self.page_number <= 0:

            self.page_number = 0
            # Previous Btn
            self.btns.controls[0].disabled = True
            self.btns.controls[0].update()

        elif self.page_number >= 5:
            self.btns.controls[1].disabled = True
            self.btns.controls[1].update()

        else:
            # Previous Btn
            self.btns.controls[0].disabled = False
            self.btns.controls[0].update()

            # Next Btn
            self.btns.controls[1].disabled = False
            self.btns.controls[1].update()

        start_index = self.page_size*self.page_number

        self.order_list.controls[0].rows.clear()

        for i in range(self.page_size):
            row = DataRow(
                cells=[
                    DataCell(Text(start_index+i)),
                    DataCell(Text("12/01/01")),
                    DataCell(Text('Carlos')),
                    DataCell(Text('Almeida')),
                    DataCell(Text('R$ 100',)),
                    DataCell(Text('1000 und')),
                ]
            )

            self.order_list.controls[0].rows.append(row)

        self.order_list.update()

    def open_dlg(self):
        self.dlg_modal.open = True
        self.order_box.update()

    def close_dlg(self):
        self.dlg_modal.open = False
        self.order_box.update()

    def save_order_dlg(self, items):
        for i in items:
            print(i.value)

        self.dlg_modal.open = False
        self.order_box.update()

    def build(self):
        self.page_size: int = 30
        self.page_number: int = 0

        container = Column(
            expand=True,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        )

        container.controls.append(self.title)
        container.controls.append(self.new_order)
        container.controls.append(self.order_list)
        # container.controls

        for i in range(self.page_size):
            row = DataRow(
                cells=[
                    DataCell(Text(i+1)),
                    DataCell(Text("12/01/01")),
                    DataCell(Text('Carlos')),
                    DataCell(Text('Almeida')),
                    DataCell(Text('R$ 100',)),
                    DataCell(Text('1000 und')),
                ]
            )
            self.order_list.controls[0].rows.append(row)

        container.controls.append(self.dlg_modal)
        container.controls.append(self.btns)
        self.order_box.controls.append(container)
        self.order.content = self.order_box
        return self.order


def main(page: Page):
    # page settings
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # login = Login()
    # page.add(login)
    # page.update()
    # login.open_modal()

    # Class

    # mainpage = MainPage()
    # page.add(mainpage)
    # mainpage.open_mainpage()

    cashier = Cashier()
    page.add(cashier)
    cashier.open_modal()

    # product = Product()
    # page.add(product)
    # product.open_modal()

    # order = Order()
    # page.add(order)
    # order.open_modal()

    page.update()


if __name__ == '__main__':
    flet.app(target=main)
