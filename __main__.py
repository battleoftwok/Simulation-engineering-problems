from tkinter import filedialog
from tkinter import *
import json
import os


def find(name):
    return os.path.exists(name)


class App:
    canvas_opts = {
        'width': 720,
        'height': 720,
        'bg': 'black'
    }

    settings_window_opts = {
        'width': 470,
        'height': 720
    }

    border_effects = {
        "flat": FLAT,
        "sunken": SUNKEN,
        "raised": RAISED,
        "groove": GROOVE,
        "ridge": RIDGE,
    }

    data = {}
    buttons = []

    def __init__(self):
        self.root = Tk()
        self.root.title('Лабораторная работа')
        self.root.resizable(width=False, height=False)

        self.canvas = Canvas(self.root, **self.canvas_opts)
        self.canvas.pack(side='left')

        self.chart()

        self.settings_window = Frame(self.root, **self.settings_window_opts)
        self.settings_window.pack(side='right')

        self.read_data_json_file()

        # Текст
        self.label = Label(self.settings_window, text='Hello')

        # self.print_screen()
        self.new_method_screen()

        # self.decor()

    def new_method_screen(self):
        height, factor = 50, 35

        Label(self.settings_window, text='Задача №2. Вариант 59',
              font=("Courier", 18, "bold")).place(x=0, y=0)

        # Первый блок данных
        Label(self.settings_window, text="1.Входные данные:",
              font=("Courier", 14, "bold")).place(x=0, y=height)

        for key, value in self.data["Входные данные"].items():
            Label(self.settings_window, text=f'  {key}: {value}',
                  font=("Courier", 14, "italic")).place(x=0, y=height + factor)
            height += factor

        # Второй блок данных
        Label(self.settings_window, text="2.Дополнительные условия:",
              font=("Courier", 14, "bold")).place(x=0, y=height + factor)

        for key, value in self.data["Дополнительные условия"].items():
            Label(self.settings_window, text=f'  {key}: {value}',
                  font=("Courier", 14, "italic")).place(x=0, y=height + 2 * factor)
            height += factor

        # Третий блок данных
        Label(self.settings_window, text="3.Выберете один из вариантов расчёта:",
              font=("Courier", 14, "bold")).place(x=0, y=height + 2 * factor)

        i = 0
        for value in self.data["Особые условия"]:
            checkbutton = Button(self.settings_window, text=f'{value}'.center(40),
                                 font=("Courier", 14, "italic"), relief=GROOVE)
            self.buttons.append(checkbutton)
            checkbutton.place(x=5, y=height + 3 * factor)
            i += 1
            height += 50

        self.buttons[0]['command'] = self.title

        # Подпись
        Label(self.settings_window,
              text="Подготовил: Коновалов Ф.Д., группа: М1О-302С-18",
              font=("Georgia", 13, "italic")).place(x=20, y=height + 3.3 * factor)

    def title(self):
        print('Hello')

    def chart(self):
        self.canvas.create_line(0, self.canvas_opts['height'] // 2,
                                self.canvas_opts['width'], self.canvas_opts['height'] // 2,
                                fill='white', arrow=LAST, arrowshape=(10, 20, 5))

        self.canvas.create_line(self.canvas_opts['width'] // 2, self.canvas_opts['height'],
                                self.canvas_opts['width'] // 2, 0,
                                fill='white', arrow=LAST, arrowshape=(10, 20, 5))

    def print_screen(self):
        # TODO: Попытка сделать универсальный метод для считывания файла.json.
        # TODO: На данный же момент присутствует зависимость от положения данных
        # TODO: в файле + данные в файле могу быть различных типов...

        height = 50
        factor = 20
        for key, value in self.data.items():
            Label(self.settings_window, text=f'{key}:', font=("Courier", 14, "italic")).place(x=0, y=height)
            height += factor

            if isinstance(value, dict):
                for inside_key, inside_value in value.items():
                    height += 10
                    Label(self.settings_window, text=f"    {inside_key}: {inside_value}",
                          font=("Courier", 14, "italic")).place(x=0, y=height)

                    height += factor

            elif isinstance(value, list):
                for step in value:
                    height += 10
                    var = IntVar()
                    self.check = Checkbutton(self.settings_window, text=f"{step}", font=("Courier", 14, "italic"))
                    self.check.place(x=10, y=height)
                    height += factor
            else:
                Label(self.settings_window, text=f"    {key}: {value}\n",
                      font=("Courier", 14, "italic")).place(x=0, y=height)
                height += factor

    def read_data_json_file(self):
        """
        Метод считывает данные из файла 'Input_data.json'
        """
        if find('Input_data.json'):
            with open('Input_data.json', encoding="utf-8") as file:
                self.data = json.loads(file.read())
        else:
            with open(filedialog.askopenfilename(), encoding="utf-8") as file:
                self.data = json.loads(file.read())

    def decor(self):
        task_text = "Горизонтальный реальный пружинный маятник, " \
                    "закреплённый двумя пружинами. Тело - куб."

        print("Задача №2. Вариант 59.".center(len(task_text)))
        print("Подготовил студент группы М1О-302С-18 Коновалов Ф.Д.\n".center(len(task_text)))
        print("Условие задачи:")
        print(task_text)

        for key, value in self.data.items():
            print()
            print(f"{key}:")

            if isinstance(value, dict):
                for inside_key, inside_value in value.items():
                    print(f"    {inside_key}: {inside_value}")
            elif isinstance(value, list):
                for step in value:
                    print(f"   - {step}")
            else:
                print(f"    {key}: {value}\n")

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
