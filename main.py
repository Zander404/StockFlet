
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


class Login(UserControl):
    def __init__(self):
        self.login = Container(
            width=0,
            height=360,
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
        self.login.width = 630
        self.login.update()
        sleep(0.2)
        
        self.login_box.visible = True
        self.login_box.update()

    def close_modal(self):
        self.login_box.width = 0
        self.login_box.visible = False
        sleep(0.35)

        self.login.width = 0
        self.login.height = 0
        self.login.update()
        sleep(0.75)

        self.page.controls.remove(self)
        self.main = MainPage()

        self.page.controls.insert(1, self.main)
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
            height=0,
            width=0,
            bgcolor=BG_SUB_COLOR,
            animate=animation.Animation(550, 'easeOutBack'),
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
        sleep(1)
        self.main.width = 620
        self.main.height = 360
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
        self.main.height = 0
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
        self.cashier = Container(
            padding=10,
            width=0,
            height=0,
            bgcolor=BG_COLOR,
            animate=animation.Animation(1000, AnimationCurve.BOUNCE_IN),
        )

        self.cashier_box = Row()

        super().__init__()

    def open_modal(self):
        self.cashier.width = 630
        self.cashier.height = 360
        self.cashier.update()

    def close_modal(self):
        self.cashier_box.visible = False
        self.cashier_box.update()
        sleep(0.35)

        self.cashier.width = 0
        self.cashier.height = 0
        self.cashier.update()
        sleep(0.75)

        self.main = MainPage()
        self.page.controls.insert(0, self.main)
        self.page.update()

        self.main.open_mainpage()


    def build(self):
        return self.cashier


class Product(UserControl):
    def __init__(self):

        self.product = Container(
            padding=10,
            width=0,
            height=0,
            bgcolor="green",
            animate=animation.Animation(550, AnimationCurve.BOUNCE_IN),
        )

        self.product_box = Row()


        self.btn = self.product_btn("Teste", lambda e: (self.back(e)), '1')

        super().__init__()

    def back(self, e):
        self.close_modal()


    def open_modal(self):
        self.product.width = 630
        self.product.height = 360
        self.product.update()

        sleep(0.2)
        self.product_box.visible = True
        self.product_box.update()


    def close_modal(self):
        self.product_box.visible = False
        self.product_box.update()
        sleep(0.35)

        self.product.width = 0
        self.product.height = 0
        self.product.update()
        sleep(0.75)

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


    def build(self):

        self.product_box.controls.append(self.btn)
        self.product.content = self.product_box
        return self.product


class Order(UserControl):
    def __init__(self):
        self.order = Container(
            padding=10,
            width=0,
            height=0,
            bgcolor="yellow",
            animate=animation.Animation(550, AnimationCurve.BOUNCE_IN),
        )

        self.order_box = Row()

        super().__init__()

    def open_modal(self):
        self.order.width = 630
        self.order.height = 360
        self.order.update()

        sleep(0.2)
        self.order_box.visible = True
        self.order_box.update()


    def close_modal(self):
        self.order_box.visible = False
        self.order_box.update()
        sleep(0.75)

        self.order.width = 0
        self.order.height = 0
        self.order.update()
        sleep(0.35)

        self.main = MainPage()
        self.page.controls.insert(0, self.main)
        self.page.update()
        sleep(0.35)


    def build(self):
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
