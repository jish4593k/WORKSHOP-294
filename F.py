import torch
from torchtext import data
from tkinter import Tk, Label, Text, Button, filedialog

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def get_most_frequent_words(text, top_k=10):
    # Use torchtext to tokenize and count words
    tokenizer = data.get_tokenizer("basic_english")
    tokens = tokenizer(text)
    counter = torchtext.vocab.Counter(tokens)

    # Get the most frequent words
    most_frequent_words = counter.most_common(top_k)
    return most_frequent_words

class TextAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Text Analyzer")

        self.label = Label(master, text="Select a text file to analyze:")
        self.label.pack()

        self.text_display = Text(master, height=10, width=40)
        self.text_display.pack()

        self.analyze_button = Button(master, text="Analyze Text", command=self.analyze_text)
        self.analyze_button.pack()

    def analyze_text(self):
        file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])
        if file_path:
            text = load_data(file_path)
            most_frequent_words = get_most_frequent_words(text)

            result_str = "Most Frequent Words:\n"
            for word, frequency in most_frequent_words:
                result_str += f"{word}: {frequency}\n"

            self.text_display.delete(1.0, 'end')
            self.text_display.insert('end', result_str)

if __name__ == '__main__':
    root = Tk()
    app = TextAnalyzerGUI(root)
    root.mainloop()
