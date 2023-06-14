import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import subprocess


# Задачи и головоломки
tasks = [
    {
        'description': 'Напишите программу, которая выводит на экран фразу "Привет, мир!"',
        'solution': 'begin\n  writeln("Привет, мир!");\nend.\n',
        'hint': 'Используйте функцию writeln для вывода текста на экран.',
        'reference': 'https://www.example.com/pascal-introduction'
    },
    {
        'description': 'Напишите программу, которая запрашивает имя пользователя и выводит приветствие с использованием введенного имени.',
        'solution': 'var\n  name: string;\nbegin\n  write("Введите ваше имя: ");\n  readln(name);\n  writeln("Привет, ", name, "!");\nend.\n',
        'hint': 'Используйте переменную для хранения введенного имени и функции write и readln для ввода и вывода данных.',
        'reference': 'https://www.example.com/pascal-variables'
    },
    {
        'description': 'Напишите программу, которая вычисляет сумму двух чисел.',
        'solution': 'var\n  a, b, sum: integer;\nbegin\n  write("Введите первое число: ");\n  readln(a);\n  write("Введите второе число: ");\n  readln(b);\n  sum := a + b;\n  writeln("Сумма двух чисел: ", sum);\nend.\n',
        'hint': 'Используйте переменные и оператор сложения (+) для вычисления суммы.',
        'reference': 'https://www.example.com/pascal-variables'
    },
    {
        'description': 'Напишите программу, которая определяет, является ли число четным или нечетным.',
        'solution': 'var\n  num: integer;\nbegin\n  write("Введите число: ");\n  readln(num);\n  if num mod 2 = 0 then\n    writeln(num, " - четное число")\n  else\n    writeln(num, " - нечетное число");\nend.\n',
        'hint': 'Используйте оператор mod для определения остатка от деления числа на 2.',
        'reference': 'https://www.example.com/pascal-conditional-statements'
    },
    {
    'description': 'Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму.',
    'solution': 'var\n  a, b, sum: integer;\nbegin\n  write("Введите первое число: ");\n  readln(a);\n  write("Введите второе число: ");\n  readln(b);\n  sum := a + b;\n  writeln("Сумма двух чисел: ", sum);\nend.\n',
    'hint': 'Используйте переменные для хранения чисел и оператор сложения (+) для вычисления суммы.',
    'reference': 'https://www.example.com/pascal-variables'
    },
    {
    'description': 'Напишите программу, которая запрашивает у пользователя радиус круга и вычисляет его площадь.',
    'solution': 'var\n  radius: real;\n  area: real;\nbegin\n  write("Введите радиус круга: ");\n  readln(radius);\n  area := pi * radius * radius;\n  writeln("Площадь круга: ", area);\nend.\n',
    'hint': 'Используйте переменные для хранения радиуса и площади, а также константу pi для вычисления площади круга.',
    'reference': 'https://www.example.com/pascal-variables'
    },
    {
    'description': 'Напишите программу, которая определяет, является ли заданное число положительным, отрицательным или нулем.',
    'solution': 'var\n  num: integer;\nbegin\n  write("Введите число: ");\n  readln(num);\n  if num > 0 then\n    writeln("Число положительное")\n  else if num < 0 then\n    writeln("Число отрицательное")\n  else\n    writeln("Число равно нулю");\nend.\n',
    'hint': 'Используйте условные операторы if-else для определения знака числа.',
    'reference': 'https://www.example.com/pascal-conditional-statements'
    },
    {
    'description': 'Напишите программу, которая запрашивает у пользователя год его рождения и выводит его возраст.',
    'solution': 'var\n  birthYear, currentYear, age: integer;\nbegin\n  write("Введите год вашего рождения: ");\n  readln(birthYear);\n  currentYear := Year();\n  age := currentYear - birthYear;\n  writeln("Ваш возраст: ", age);\nend.\n',
    'hint': 'Используйте переменные для хранения года рождения, текущего года и возраста. Для получения текущего года используйте встроенную функцию Year().',
    'reference': 'https://www.example.com/pascal-variables'
    },
    {
    'description': 'Напишите программу, которая выводит на экран таблицу умножения для числа 5.',
    'solution': 'var\n  num, result: integer;\nbegin\n  num := 5;\n  for i := 1 to 10 do\n  begin\n    result := num * i;\n    writeln(num, " * ", i, " = ", result);\n  end;\nend.\n',
    'hint': 'Используйте цикл for для перебора чисел от 1 до 10 и вычисления результатов умножения.',
    'reference': 'https://www.example.com/pascal-loops'
    },
    {
    'description': 'Напишите программу, которая запрашивает у пользователя имя и выводит его длину.',
    'solution': 'var\n  name: string;\n  length: integer;\nbegin\n  write("Введите ваше имя: ");\n  readln(name);\n  length := Length(name);\n  writeln("Длина имени: ", length);\nend.\n',
    'hint': 'Используйте переменную для хранения имени и функцию Length() для вычисления его длины.',
    'reference': 'https://www.example.com/pascal-strings'
    },
    {
    'description': 'Напишите программу, которая запрашивает у пользователя число и проверяет, является ли оно простым.',
    'solution': 'var\n  num, i: integer;\n  isPrime: boolean;\nbegin\n  write("Введите число: ");\n  readln(num);\n  isPrime := true;\n  for i := 2 to num div 2 do\n  begin\n    if num mod i = 0 then\n    begin\n      isPrime := false;\n      break;\n    end;\n  end;\n  if isPrime then\n    writeln("Число простое")\n  else\n    writeln("Число не является простым");\nend.\n',
    'hint': 'Используйте цикл for для проверки делителей числа. Если найден делитель, то число не является простым.',
    'reference': 'https://www.example.com/pascal-loops'
    },
    {
    'description': 'Напишите программу, которая запрашивает у пользователя длины трех сторон треугольника и определяет, является ли он прямоугольным.',
    'solution': 'var\n  side1, side2, side3: real;\n  isRightTriangle: boolean;\nbegin\n  write("Введите длину первой стороны: ");\n  readln(side1);\n  write("Введите длину второй стороны: ");\n  readln(side2);\n  write("Введите длину третьей стороны: ");\n  readln(side3);\n  isRightTriangle := (side1 * side1 + side2 * side2 = side3 * side3) or (side1 * side1 + side3 * side3 = side2 * side2) or (side2 * side2 + side3 * side3 = side1 * side1);\n  if isRightTriangle then\n    writeln("Треугольник является прямоугольным")\n  else\n    writeln("Треугольник не является прямоугольным");\nend.\n',
    'hint': 'Используйте переменные для хранения длин сторон треугольника и проверьте, выполняется ли теорема Пифагора для какой-либо из трех сторон.',
    'reference': 'https://www.example.com/pascal-conditional-statements'
    },
    {
    'description': 'Напишите программу, которая выводит на экран числа от 1 до 100, пропуская числа, кратные 3.',
    'solution': 'var\n  i: integer;\nbegin\n  for i := 1 to 100 do\n  begin\n    if i mod 3 <> 0 then\n      writeln(i);\n  end;\nend.\n',
    'hint': 'Используйте цикл for для перебора чисел от 1 до 100 и проверку деления на 3 с остатком.',
    'reference': 'https://www.example.com/pascal-loops'
    },
    {
    'description': 'Напишите программу, которая запрашивает у пользователя число и выводит его факториал.',
    'solution': 'var\n  num, factorial: integer;\nbegin\n  write("Введите число: ");\n  readln(num);\n  factorial := 1;\n  for i := 2 to num do\n  begin\n    factorial := factorial * i;\n  end;\n  writeln("Факториал числа ", num, ": ", factorial);\nend.\n',
    'hint': 'Используйте цикл for для вычисления факториала числа, умножая текущее значение на каждую итерацию.',
    'reference': 'https://www.example.com/pascal-loops'
    },

]

# Глобальные переменные
current_task = 0  # Текущая задача
output_text = None  # Текстовый виджет для вывода результата
correct_answers = 0  # Количество правильных ответов


def check_solution():
    global output_text, correct_answers
    solution = code_editor.get("1.0", "end-1c")  # Получаем введенное решение из текстового виджета
    expected_solution = tasks[current_task]['solution']

    if solution == expected_solution:
        output_text.config(text="Правильно! Задача решена.")
        correct_answers += 1
    else:
        output_text.config(text="Неправильное решение. Попробуйте еще раз.")




def show_hint():
    hint = tasks[current_task]['hint']
    output_text.config(text=hint)


def show_solution():
    solution = tasks[current_task]['solution']
    code_editor.delete("1.0", tk.END)
    code_editor.insert(tk.END, solution)

def show_disclaimer():
    disclaimer_text = "После написания программы нажмите кнопку 'Показать решение', чтобы сравнить свой код с правильным."
    output_text.config(text=disclaimer_text)

def show_reference():
    reference_url = tasks[current_task]['reference']
    webbrowser.open_new_tab(reference_url)


def next_task():
    global current_task
    if current_task < len(tasks) - 1:
        current_task += 1
        output_text.config(text="")
        code_editor.delete("1.0", tk.END)
        task_description.config(text=tasks[current_task]['description'])
        previous_button.config(state=tk.NORMAL)  # Активируем кнопку "Предыдущая задача"
    elif current_task == len(tasks) - 1:
        current_task += 1
        output_text.config(text="")
        code_editor.delete("1.0", tk.END)
        task_description.config(text="Поздравляем! Вы прошли все задачи.")
        next_button.config(state=tk.DISABLED)  # Деактивируем кнопку "Следующая задача"


def previous_task():
    global current_task
    if current_task > 0:
        current_task -= 1
        output_text.config(text="")
        code_editor.delete("1.0", tk.END)
        task_description.config(text=tasks[current_task]['description'])
        next_button.config(state=tk.NORMAL)  # Активируем кнопку "Следующая задача"
    elif current_task == 0:
        current_task -= 1
        output_text.config(text="")
        code_editor.delete("1.0", tk.END)
        task_description.config(text="Поздравляем! Вы прошли все задачи.")
        previous_button.config(state=tk.DISABLED)  # Деактивируем кнопку "Предыдущая задача"

def play_game():
    subprocess.call(["python", "game.py"])

def play_gamesec():
    subprocess.call(["python", "gamesec.py"])


# Создание графического интерфейса
window = tk.Tk()
window.title("Игра по изучению Pascal")
window.geometry("1000x600")
window.resizable(False, False)  # Запретить изменение размеров окна

left_image = Image.open("2a38210b-7e1e-44dd-8729-f963917859c4.png")
left_image = left_image.resize((100, 100), Image.ANTIALIAS)
left_photo = ImageTk.PhotoImage(left_image)

right_image = Image.open("free-icon-zombie-249380.png")
right_image = right_image.resize((100, 100), Image.ANTIALIAS)
right_photo = ImageTk.PhotoImage(right_image)

image = Image.open("2a38210b-7e1e-44dd-8729-f963917859c4.png")
image = image.resize((100, 100), Image.ANTIALIAS)  # Изменение размера изображения
photo = ImageTk.PhotoImage(image)

image_label = ttk.Label(window, image=photo)
image_label.place(x=10, y=10)  # Задайте координаты x и y в пикселях

left_image_label = ttk.Label(window, image=photo)
left_image_label.place(x=900, y=10)  # Задайте координаты x и y в пикселях

# Стили ttk
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TText", font=("Courier New", 12))

#left_image_label = ttk.Label(window, image=left_photo)
#left_image_label.pack(side=tk.LEFT, fill=tk.Y)


task_description = ttk.Label(window, text=tasks[current_task]['description'], wraplength=500)
task_description.pack(pady=10)

code_editor = tk.Text(window, width=70, height=10)
code_editor.pack()

check_button = ttk.Button(window, text="Проверить", command=check_solution)
check_button.pack(pady=5)

hint_button = ttk.Button(window, text="Подсказка", command=show_hint)
hint_button.pack(pady=5)

solution_button = ttk.Button(window, text="Показать решение", command=show_solution)
solution_button.pack(pady=5)

reference_button = ttk.Button(window, text="Дополнительные материалы", command=show_reference)
reference_button.pack(pady=5)

disclaimer_button = ttk.Button(window, text="Дисклеймер", command=show_disclaimer)
disclaimer_button.pack(pady=5)

right_image_label = ttk.Label(window, image=right_photo)
right_image_label.pack(side=tk.RIGHT, fill=tk.Y)

right_image_label = ttk.Label(window, image=right_photo)
right_image_label.pack(side=tk.LEFT, fill=tk.Y)

play_button = ttk.Button(window, text="Поиграть", command=play_game)
play_button.pack(pady=5)
play_button = ttk.Button(window, text="Поиграть на 2-х", command=play_gamesec)
play_button.pack(pady=5)

output_text = ttk.Label(window, text="")
output_text.pack(pady=10)


previous_button = ttk.Button(window, text="Предыдущая задача", state=tk.DISABLED, command=previous_task)
previous_button.pack(side=tk.LEFT, padx=5)

next_button = ttk.Button(window, text="Следующая задача", command=next_task)
next_button.pack(side=tk.RIGHT, padx=5)


window.mainloop()