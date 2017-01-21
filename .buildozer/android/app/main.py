import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string("""

<CustButton@Button>:
    font_size: 32

<AppLayout>:
    id: calculator
    display: entry
    rows: 5
    padding: 10
    spacing: 10

    BoxLayout:
        TextInput:
            id: entry
            font_name: 'computer'
            font_size: 80
            background_color: (0,0,0,1)
            foreground_color: (0,1,0,1)
            multiline: False

    BoxLayout:
        spacing: 10
        CustButton:
            text: "7"
            on_press: entry.text += self.text
        CustButton:
            text: "8"
            on_press: entry.text += self.text
        CustButton:
            text: "9"
            on_press: entry.text += self.text
        CustButton:
            background_color: (0,0,1,1) if self.state == 'normal' else (0,0,0,0)
            background_normal: ""
            text: "+"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "4"
            on_press: entry.text += self.text
        CustButton:
            text: "5"
            on_press: entry.text += self.text
        CustButton:
            text: "6"
            on_press: entry.text += self.text
        CustButton:
            background_color: (0,0,1,1) if self.state == 'normal' else (0,0,0,0)
            background_normal: ""
            text: "-"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "1"
            on_press: entry.text += self.text
        CustButton:
            text: "2"
            on_press: entry.text += self.text
        CustButton:
            text: "3"
            on_press: entry.text += self.text
        CustButton:
            background_color: (0,0,1,1) if self.state == 'normal' else (0,0,0,0)
            background_normal: ""
            text: "*"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            background_color: (1,0,0,1) if self.state == 'normal' else (0,1,0,1)
            background_normal: ""
            text: "AC"
            on_press: entry.text = ""
        CustButton:
            text: "0"
            on_press: entry.text += self.text
        CustButton:
            text: "."
            on_press: entry.text += self.text
        CustButton:
            background_color: (0,1,0,1) if self.state == 'normal' else (0,0,0,0)
            background_normal: ""
            text: "="
            on_press: calculator.result(entry.text)
        CustButton:
            background_color: (0,0,1,1) if self.state == 'normal' else (0,0,0,0)
            background_normal: ""
            text: "/"
            on_press: entry.text += self.text

""")


class AppLayout(GridLayout):

    def result(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return AppLayout()

AppResult = CalculatorApp()
AppResult.run()
