import tkinter as tk
from tkinter import ttk


yoruba_dict= {
    'Good morning':'Ẹ káàárọ̀',
    'Good afternoon':'Ẹ káàsán' ,
    'Good evening':'Ẹ kúrọ̀lẹ́',
    'Good night':'Ẹ káalẹ́',
    'How are you?':'Báwo ni',
    'I am fine':'Dádá ni',
    'Thank you':'Ẹ ṣé',
    'Please':'Jọ̀ọ́',
    'Yes':'Bẹ́ẹ̀ni',
     'No':'Rárá',
     'one': "ọ̀kan",
    'two': "èjì",
    'three': "ẹ̀ta",
    'four': "ẹ̀rin",
    'five': "àrún",
    'six': "ẹ̀fà",
    'seven': "èje",
    'eight': "ẹ̀jọ",
    'nine': "ẹ̀sán",
    'ten': "ẹ̀wá",
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

igbo_dict= {
    "morning":"ụtụtụ",
    "afternoon":"ehihie",
    "evening":"mgbede",
    "night":"abalị",
    "we":"anyị",
    "children":"ụmụaka",
    "house":"ụlọ",
    "book":"akwụkwọ",
    "school": "ụlọ akwụkwọ",
    "we":"anyị",
    "fire":"ọkụ",
    "water":"mmiri"
}

fulani_dict={
    'go':'dillu',
    'food':'yamdu',
    'money':'sehde',
    'fire':'hete',
    'shoe':'padeh',
    'stop':'alu',
    'rice':'marori',
    'water':'diyam',
    'nothing':'wala',
    'head':'hore',
    'road':'lawol',
    'ear':'noppi',
    'market':'lumor',
    'study':'jangirde',
    'good':'jam',
    'GOD':'allah',
    'cow':'nakgeh',
    'enough':'wahdi',
    'farm':'gehsa',
}
Hausa_dict={
    'come':'zo',
    'go':'tafi',
    'food':'abinchi',
    'water':'ruwa',
    'fish':'kifi',
    'onion':'albassa',
    'hand':'hannu',
    'ear':'kunne',
    'nose':'hanchi',
    'bed':'gado',
    'fanka':'fan',
    'lion':'zaki',
    'one':'daya',
    'four':'hudu',
    'six':'shida',
    'spoon':'chokali',
    'book':'littafi',
    'bag':'jaka',
    'shoe':'takalmi',
}



language_dicts = {
    "Yoruba": yoruba_dict,
    "Edo": edo_dict,
    "Igbo": igbo_dict,
    "Fulani":fulani_dict,
    "Hausa": Hausa_dict,
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
