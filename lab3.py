import tkinter as tk
from tkinter import messagebox
import random

# Генератор ключа
def generate():
    word = entry.get().strip().upper()

    block1 = ''.join(random.choices(word, k=3))
    
    block2 = ''
    for ch in word:
        number = ord(ch) - ord('A') + 1
        block2 += str(number % 10)

    block3 = ''.join(random.choices(word, k=3))
    key = f'{block1}-{block2}-{block3}'
    keyres.set(key)
    return keyres

# Создание окна
window = tk.Tk()
window.title('Маленьките ночные кошмарики KEYGEN')
window.geometry('600x500')

# Добавление фона (арт)
img = tk.PhotoImage(file='арт-л3.png')
lbl_img = tk.Label(window, image=img)
lbl_img.place(x=0, y=0, relwidth=1, relheight=1)

# Ввод слова
txt = tk.Label(
    window,
    text='Введите слово из 6 латинских букв:',
    bg='#000000',
    fg='#ffd700',
    font=('Verdana', 12)
)
txt.grid(row=1, column=3, pady=5)

entry = tk.Entry(window, width=10, font=('Verdana', 14))
entry.grid(row=2, column=3, pady=5)

# Кнопка
btn = tk.Button(
    window,
    text='Сгенерировать ключ',
    command=generate,
    font=('Verdana', 12),
    bg='#ffd700',
    fg='#000000'
)
btn.grid(row=3, column=3, pady=5)

# Результат
res = tk.Label(
    window,
    text='Ваш ключ:',
    bg='#000000',
    fg='#ffd700',
    font=('Verdana', 12)
)
res.grid(row=4, column=3)

keyres = tk.StringVar()
keyres.set('--- ------ ---')

entry_key = tk.Entry(
    window,
    textvariable=keyres,
    width=20,
    font=('Verdana', 12),
    bg='#ffd700',
    fg='#000000'
)
entry_key.grid(row=5, column=3)

window.mainloop()
