import tkinter as tk
from tkinter import messagebox

class CodeQuest:
    def __init__(self, master):
        self.master = master
        self.master.title("Кодовый квест")

        self.intro_label = tk.Label(self.master, text="Добро пожаловать в Квест игру, которая поможет тебе начать изучать язык  Python!\nВаша задача - пройти все уровни, решая задачи на программирование.")
        self.intro_label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Начать игру", command=self.start_game)
        self.start_button.pack(pady=10)

        self.output_text = tk.Text(self.master, wrap=tk.WORD, width=50, height=10)
        self.output_text.pack(pady=10)

        self.input_text = tk.Text(self.master, wrap=tk.WORD, width=50, height=5)
        self.input_text.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Отправить код", command=self.submit_code)
        self.submit_button.pack(pady=10)

        self.hint_button = tk.Button(self.master, text="Подсказка", command=self.show_hint)
        self.hint_button.pack(pady=10)

        self.levels = [
            {
                "task": "Создайте переменную 'a' со значением 5 и переменную 'b' со значением 7. Выведите сумму 'a' и 'b'.",
                "hint": "Используйте оператор '+', чтобы сложить две переменные.",
                "solution": "a = 5\nb = 7\nprint(a + b)"
            },
            {
                "task": "Напишите условный оператор, который проверяет, является ли число 'x' положительным. Если да, выведите 'Положительное'.",
                "hint": "Используйте оператор 'if' для проверки условия.",
                "solution": "x = 5\nif x > 0:\n    print('Положительное')"
            },
            {
                "task": "Напишите цикл 'for', который выводит числа от 1 до 5.",
                "hint": "Используйте функцию 'range()' для создания диапазона чисел.",
                "solution": "for i in range(1, 6):\n    print(i)"
            }
        ]
        self.current_level = 0

    def start_game(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Уровень {self.current_level + 1}: {self.levels[self.current_level]['task']}")

    def submit_code(self):
        user_code = self.input_text.get(1.0, tk.END).strip()
        if user_code == self.levels[self.current_level]['solution']:
            messagebox.showinfo("Результат", "Правильно! Вы переходите на следующий уровень.")
            self.current_level += 1
            if self.current_level < len(self.levels):
                self.start_game()
            else:
                messagebox.showinfo("Поздравляем!", "Вы прошли все уровни!")
        else:
            messagebox.showerror("Результат", "Неправильно! Попробуйте еще раз.")

    def show_hint(self):
        messagebox.showinfo("Подсказка", self.levels[self.current_level]['hint'])

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeQuest(root)
    root.mainloop()