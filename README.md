import tkinter as tk
from tkinter import ttk


yoruba_dict= {
    'Ẹ káàárọ̀': 'Good morning',
    'Ẹ káàsán': 'Good afternoon',
    'Ẹ kúrọ̀lẹ́': 'Good evening',
    'Ẹ káalẹ́': 'Good night',
    'Báwo ni': 'How are you?',
    'Dádá ni': 'I am fine',
    'Ẹ ṣé': 'Thank you',
    'Jọ̀ọ́': 'Please',
    'Bẹ́ẹ̀ni': 'Yes',
    'Rárá': 'No',
     1: "ọ̀kan",
    2: "èjì",
    3: "ẹ̀ta",
    4: "ẹ̀rin",
    5: "àrún",
    6: "ẹ̀fà",
    7: "èje",
    8: "ẹ̀jọ",
    9: "ẹ̀sán",
    10: "ẹ̀wá",
    "run": "sáré",
    "eat": "jẹun",
    "sleep": "sùn",
    "read": "ka",
    "write": "kọ",
    "speak": "sọ",
    "walk": "rìn",
    "dance": "jó",
    "sing": "kọrin",
    "jump": "fo",
}
edo_dict = {
    "ọmọ": {
        "translation": "Child",
        "example": "Ọmọ ni mosi."
    },
    "iye": {
        "translation": "Mother",
        "example": "iye mi ni."
    },
    "bàbá": {
        "translation": "Daddy",
        "example": "Bàbá mi n'ibè."
    },
    "egbo": {
        "translation": "Bag",
        "example": "egbo yìí dára."
    },
    "osei": {
        "translation": "Friend",
        "example": "oseí mi ni."
    },
    "ebei": {
        "translation": "book",
        "example": "ebei yìí lẹ́wa."
    },
    "egogo": {
        "translation": "Time",
        "example": "egogo ni?"
    },
    "amen": {
        "translation": "water",
        "example": "Mo ní amen."
    },
    "upai": {
        "translation": "Light",
        "example": "upa dára."
    },
    "haiga": {
        "translation": "chair",
        "example": "haiga ni."
    },
    "ofura": {
        "translation": "Peace",
        "example": "ofura ni."
    },
    "òsa": {
        "translation": "God",
        "example": "Òsa ni."
    },
    "aigbo": {
        "translation": "Life",
        "example": "Aigbo yìí dára."
    },
    "eki": {
        "translation": "Market",
        "example": "eki ni."
    },
    "oba": {
        "translation": "King",
        "example": "oba ni."
    },
    "okuta": {
        "translation": "stone",
        "example": "okuta ni."
    }
}

igbo_dict = {
    "ụtụtụ": "morning",
    "ehihie": "afternoon",
    "mgbede": "evening",
    "abalị": "night",
    "anyị": "we",
    "ụmụaka": "children",
    "ụlọ": "house",
    "akwụkwọ": "book",
    "ụlọ akwụkwọ": "school",
    "anyị": "we",
    "ọkụ": "fire",
    "mmiri": "water"
}

german_dict = {
    "hello": "hallo",
    "world": "welt",
    "apple": "apfel",
    "banana": "banane",
    




language_dicts = {
    "Yoruba": yoruba_dict,
    "Edo": edo_dict,
    "Igbo": igbo_dict,
}

class LanguageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Dictionary App")
        self.geometry("400x300")

        self.language_var = tk.StringVar(value="English")
        self.word_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):

        language_label = tk.Label(self, text="Select Language:")
        language_label.pack(pady=10)

        language_menu = ttk.Combobox(self, textvariable=self.language_var, values=list(language_dicts.keys()))
        language_menu.pack(pady=10)


        word_label = tk.Label(self, text="Enter Word:")
        word_label.pack(pady=10)

        word_entry = tk.Entry(self, textvariable=self.word_var)
        word_entry.pack(pady=10)

    
        search_button = tk.Button(self, text="Search", command=self.search_word)
        search_button.pack(pady=10)

    
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def search_word(self):
        language = self.language_var.get()
        word = self.word_var.get().lower()
        translation = language_dicts.get(language, {}).get(word, "Word not found")
        self.result_label.config(text=f"{word.capitalize()} in {language}: {translation}")

if __name__ == "__main__":
    app = LanguageApp()
    app.mainloop()
