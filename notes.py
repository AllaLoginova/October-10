import tkinter as tk
import json

class NoteModel:
    """База данных для хранения заметок"""

    def __init__(self):
        self._notes = self._load_from_file()

    def get_notes(self):
        return self._notes

    def add_note(self, text):
        """Добавление новой заметки"""
        next_id = self._get_last_id() + 1  # получаем новый id
        note = {"id": next_id, "text": text}  # создаем заметку
        self._notes.append(note)  # добавляем в список

        self.save_to_file()

    def delete_by_id(self, note_id):
        """Удаление по id"""
        for number, note in enumerate(self._notes):
            if note['id'] == note_id:
                self._notes.pop(number)
                break
        else:
            print('Такой заметки нет')

    def find_by_text(self, text):
        """Поиск заметки"""
        res_notes = []
        for note in self._notes:
            if text in note['text']:
                res_notes.append(note)
        return res_notes

    def _load_from_file(self):
        """Загрузка данных из файла"""
        with open('notes.json', 'r', encoding='utf-8') as f:
            notes = json.load(f)
        return notes

    def save_to_file(self):
        with open('notes.json', 'w', encoding='utf-8') as f:
            notes = json.dump(self._notes, f)
        return notes

    def _get_last_id(self):
        """Поиск максимального id"""
        if self._notes:
            max = self._notes[0]['id']
            for note in self._notes:
                if note['id'] > max:
                    max = note['id']
        else:
            max = 0
        return max


class NoteWindow:
    def __init__(self, model):
        self.model = model
        self.create_window()
        self.show_notes()
        self.root.mainloop() # всегда должен идти последним

    def create_window(self):
        self.root = tk.Tk() # создается глобальное окно
        self.root.title('Заметки')
        # self.root.geometry('500x350')
        # self.root['bg'] = 'green'
        # self.root.wm_attributes('-alpha', 0.7) прозрачность окна

        # окошко для ввода текста
        self.input = tk.Text(self.root, height=10, width=20)
        self.input.grid(row=0, column=0, padx=10, pady=10)

        # окошко для вывода
        self.output = tk.Listbox(self.root, height=10, width=20)
        self.output.grid(row=0, column=1, padx=10, pady=10)

        self.button = tk.Button(self.root, text='Добавить заметку', command=self.add_note)
        self.button.grid(row=1, column=0, padx=10, pady=10)

    def show_notes(self):
        notes = self.model.get_notes()

        self.output.delete(0, tk.END)
        for note in notes:
            self.output.insert(tk.END, note['text'])

    def add_note(self):
        text = self.input.get('1.0', tk.END)
        self.model.add_note(text)
        self.show_notes()

        self.input.delete('1.0', tk.END)


model = NoteModel()
window = NoteWindow(model)