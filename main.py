
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
            height=350,
            bgcolor=BG_COLOR,
            border_radius=8,
            padding=10,
            animate=animation.Animation(550, AnimationCurve.EASE_IN_OUT)
        )

        self.login_box = Row(
            alignment=MainAxisAlignment.CENTER,
            spacing=20,
            opacity=100,
            animate_opacity=800,
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
        self.login.width = 620
        self.login.update()

    def close_modal(self):
        self.login_box.width = 0
        self.login_box.opacity = 0
        self.login_box.update()
        sleep(0.35)

        self.login.width = 0
        self.login.opacity = 0
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
        self.main_box = Container(
            padding=10,
            height=360,
            bgcolor=BG_SUB_COLOR,
            visible=False,
            animate=animation.Animation(550, AnimationCurve.BOUNCE_IN),
        )

        self.logo = Icon(icons.SPORTS_SOCCER, color='white')
        self.title = Text("SHOW DE BOLA SOFTWARE")

 
        self.cashier_path = self.mainpage_btn('Caixa', icon_selected=icons.PERSON_2_OUTLINED, btn_function=lambda x: print('Hello'))
 
        self.products_path = self.mainpage_btn("Produtos", icon_selected=icons.PRODUCTION_QUANTITY_LIMITS_OUTLINED,  btn_function=lambda x: print("Ola produto") )
        # self.orders_path = ElevatedButton(
        #     "Pedidos", icon=icons.LIST_ALT_OUTLINED)
        self.orders_path = self.mainpage_btn("Pedidos", icon_selected=icons.LIST_ALT_OUTLINED, btn_function=lambda x: print('HOLA ORDERS'))

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

    def open_mainpage(self):
        self.main_box.visible = True
        self.main_box.update()

    def close_mainpage(self):
        ...

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

        self.main_box.content = main_column
        return self.main_box


def main(page: Page):
    # page settings
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # login = Login()
    mainpage = MainPage()
    # Class
    # page.add(login)
    page.add(mainpage)

    page.update()

    # login.open_modal()
    mainpage.open_mainpage()


if __name__ == '__main__':
    flet.app(target=main)

# class Authetication(UserControl):
#     def __init__(self):
#         self.authbox = Container(
#             width=0,
#             height=350,
#             bgcolor='#ffffff',
#             animate=animation.Animation(550, 'easeOutBack'),
#             border_radius=8,
#             padding=10
#         )

#         self.authbox_row = Row(
#             alignment=MainAxisAlignment.CENTER,
#             spacing=30,
#             opacity=0,
#             animate_opacity=800,
#         )

#         # Sign in
#         self.sign_in_email = self.auth_options('Enter your email', False)
#         self.sign_in_password = self.auth_options("Enter your password", True)
#         self.sign_in_button = self.auth_button(
#             'Sign in', lambda e: self.autheticate_users(e))

#         # Register
#         self.register_email = self.auth_options('Create an new email', False)
#         self.register_password = self.auth_options("Create a password", True)
#         self.register_button = self.auth_button('Register', None)

#         # User Session

#         self.user_id = ''
#         self.email = ''

#         super().__init__()

#     def autheticate_users(self, event):
#         try:
#             # print(self.sign_in_email.value, self.sign_in_password.value)
#             # user = login(self.sign_in_email.value, self.sign_in_password.value)
#             # self.user_It = user['']
#             # self.email = user['email']

#             self.userIt = 1
#             self.email = 'teste@teste.com'

#             self.close_auth()
#         except Exception as e:
#             print(e)

#     # Card de Altenticação

#     def open_auth(self):
#         sleep(1)
#         self.authbox.width = 620
#         self.authbox.update()
#         sleep(0.35)
#         self.authbox_row.opacity = 1
#         self.authbox_row.update()

#     def close_auth(self):
#         self.authbox_row.opacity = 0
#         self.authbox_row.update()
#         sleep(0.8)

#         self.authbox.width = 0
#         self.authbox.update()
#         sleep(0.75)

#         self.page.controls.remove(self)
#         sleep(0.25)

#         self.chat = Chat(self.user_id, self.email)

#         self.page.controls.insert(0, self.chat),
#         self.page.update()

#         sleep(0.25)

#         self.chat.open_chat_box()

#     def auth_options(self, label, password):
#         return TextField(
#             label=label,
#             label_style=TextStyle(size=8, color='black', weight='bold'),
#             width=240,
#             height=50,
#             text_size=12,
#             cursor_width=1,
#             color='black',
#             border_color='black',
#             border='underline',
#             password=password

#         )

#     def auth_button(self, label, btn_function):
#         return ElevatedButton(
#             content=Text(label, size=13, color='white', weight='bold'),
#             width=240,
#             height=45,
#             style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=8)}),
#             on_click=btn_function
#         )
#         ...

#     def build(self):
#         labels: list = ['Sign In', 'Register']
#         texts: list = [
#             # Sign In
#             self.sign_in_email,
#             self.sign_in_password,
#             self.sign_in_button,

#             # Register
#             self.register_email,
#             self.register_password,
#             self.register_button,

#             # User session
#         ]

#         for label in labels:
#             column = Column(
#                 horizontal_alignment=CrossAxisAlignment.CENTER,
#                 alignment=MainAxisAlignment.CENTER,
#                 spacing=30,
#             )

#             items = []
#             items.append(Text(label, color='black', size=21, weight='bold'))

#             for _ in range(3):
#                 items.append(texts.pop(0))

#             column.controls = items
#             self.authbox_row.controls.append(column)

#         self.authbox_row.controls.insert(
#             1, Text("OR", size=9, color='black', weight='bold')
#         )

#         self.authbox.content = self.authbox_row
#         return self.authbox

# class Chat(UserControl):
#   def __init__(self, user_id, email):
#         self.user_id = user_id
#         self.email = email
#         self.count = 0

#         self.chat_box = Container(
#             width=620,
#             height=0,
#             bgcolor='#ffffff',
#             border_radius=8,
#             animate=animation.Animation(550, 'easeOutBack'),
#             clip_behavior=ClipBehavior.HARD_EDGE
#         )

#         self.chat_area = Column(
#             expand=True,
#             scroll='hidden',
#             auto_scroll=True
#         )
#         self.chat_input = TextField(
#             label_style=TextStyle(size=8, color='black', weight='bold'),
#             width=540,
#             height=45,
#             text_size=12,
#             cursor_width=1,
#             color='black',
#             border_color='black',
#             border_width=1,
#             content_padding=0
#         )

#         self.chat_send_button = ElevatedButton(
#             content=Icon(
#                 name=icons.SEND,
#                 size=13,
#                 color='white',
#                 rotate=transform.Rotate(5.5, alignment.center),
#             ),
#             height=45,
#             style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=8)}),
#             bgcolor='#202224',
#             on_click=lambda e: self.push_message_to_db(e),


#         )

#         self.set_chat_history()
#         self.start_listening()


#         super().__init__()

#     def open_chat_box(self):
#         self.chat_box.height = 630
#         self.chat_box.update()

#     def chat_box_header(self):
#         return Card(
#             width=620,
#             height=65,
#             elevation=10,
#             margin=-10,
#             content=Container(
#                 alignment=alignment.center,
#                 padding=padding.only(top=10),
#                 bgcolor='#202224',
#                 content=Text('Flet Chat Application', weight='bold', size=21)
#             )
#         )

#     def push_message_to_db(self, event):
#         try:
#             data = {
#                 'timestamp': int(time.time() * 1000),
#                 'message': self.chat_input.value,
#                 'uuid': self.user_id,
#                 'email': self.email,
#             }
#             db.child('message').child(int(time.time() * 1000)).set(data)

#         except Exception as e:
#             print(e)

#         finally:
#             self.chat_input.value = ''
#             self.chat_input.update()

#     def chat_message_ui(self,
#                         sent_time,
#                         name,
#                         text_message,
#                         col_pos,
#                         row_pos,
#                         bg):
#         return Container(
#             padding=padding.only(left=25, top=12, bottom=12, right=25),
#             bgcolor=bg,
#             border_radius=0,
#             margin=5,
#             content=Column(
#                 horizontal_alignment=col_pos,
#                 spacing=5,
#                 controls=[
#                     Row(
#                         alignment=row_pos,
#                         controls=[
#                             Text(
#                                 name + '0' + sent_time,
#                                 color='black',
#                                 size=8,
#                                 weight='bold'
#                             )
#                         ]
#                     ),
#                     Row(
#                         alignment=row_pos,
#                         controls=[
#                             Text(
#                                 text_message,
#                                 color='black',
#                                 size=15,
#                                 weight='bold'
#                             )
#                         ]
#                     ),

#                 ]
#             )
#         )

#     def set_chat_history(self):
#         keys = list(db.child('message').get().val().keys())
#         sorted_keys = sorted(keys, key=lambda x: int(x))

#         try:
#             if sorted_keys is not None:
#                 items = []
#                 for key in sorted_keys:
#                     value = db.child('message').child(key).get().val()
#                     time = datetime.datetime.fromtimestamp(
#                         value['timestamp']/1000.0).strftime('%H:%M')

#                     if value['uuid'] == self.user_id:
#                         items.append(
#                             self.chat_message_ui(
#                                 time,
#                                 value['email'],
#                                 value['message'],
#                                 CrossAxisAlignment.END,
#                                 MainAxisAlignment.END,
#                                 'teal100'
#                             ),
#                         )
#                         self.chat_area.controls = items

#                     else:
#                         items.append(
#                             self.chat_message_ui(
#                                 time,
#                                 value['email'],
#                                 value['message'],
#                                 CrossAxisAlignment.END,
#                                 MainAxisAlignment.END,
#                                 'teal100'
#                             ),
#                         )
#         except Exception as e:
#             print(e)

#     def stream_handler(self, value):
#         if self.count > 0:
#             time = datetime.datetime.fromtimestamp(
#                 value['data']['timestamp']/1000.0).strftime('%H:%M')

#             if value['uuid'] == self.user_id:
#                 self.chat_area.controls.append(
#                     self.chat_message_ui(
#                         time,
#                         value['data']['email'],
#                         value['data']['message'],
#                         CrossAxisAlignment.END,
#                         MainAxisAlignment.END,
#                         'teal100'
#                     ),
#                 )

#             else:
#                 self.chat_area.controls.append(
#                     self.chat_message_ui(
#                         time,
#                       value['data']['email'],
#                         value['data']['message'],
#                         CrossAxisAlignment.END,
#                         MainAxisAlignment.END,
#                         'teal100'
#                     ),
#                 )
#             self.chat_area.update()
#         else:
#             pass

#         self.count+=1


#     def start_listening(self):
#         self.stream = db.child('message').stream(self.stream_handler)

#     def build(self):

#         chat_column = Column(
#             controls=[
#                 self.chat_box_header(),
#                 Divider(height=2, color='transparent'),
#                 Container(
#                     width=620,
#                     height=480,
#                     bgcolor='lightblue',
#                     border=border.only(bottom=border.BorderSide(0.25, 'black'),
#                                        ),
#                     content=self.chat_area,
#                 ),
#                 Row(
#                     alignment=MainAxisAlignment.CENTER,
#                     vertical_alignment=CrossAxisAlignment.CENTER,
#                     controls=[
#                         self.chat_input,
#                         self.chat_send_button
#                     ]
#                 ),
#             ]
#         )
#         self.chat_box.content = chat_column
#         return self.chat_box


# def main(page: Page):
#     # page settings
#     page.horizontal_alignment = 'center'
#     page.vertical_alignment = 'center'

#     # Class
#     auth = Authetication()
#     chat = Chat("test", "test")

#     page.add(chat)
#     page.add(auth)

#     page.update()

#     auth.open_auth()


# if __name__ == '__main__':
#     flet.app(target=main)
