import tkinter as tk
from tkinter import messagebox, scrolledtext
from deep_translator import GoogleTranslator

class TranslatorAppGUI:
    def __init__(self, master):
        self.master = master
        master.title("Translator App")
        master.geometry("500x450")

        master.columnconfigure(0, weight=1)
        for i in range(6):
            master.rowconfigure(i, weight=1)

        font_size = 12

        # Input label
        tk.Label(master, text="Enter text to translate:", font=("Arial", font_size)).grid(row=0, column=0, sticky="w", padx=10, pady=5)

        # Input text
        self.text_entry = tk.Entry(master, font=("Arial", font_size))
        self.text_entry.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        # Destination label
        tk.Label(master, text="Enter destination language:", font=("Arial", font_size)).grid(row=2, column=0, sticky="w", padx=10, pady=5)

        # Language entry (instead of dropdown)
        self.language_entry = tk.Entry(master, font=("Arial", font_size))
        self.language_entry.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

        # Button
        tk.Button(master, text="Translate", command=self.translate_text, font=("Arial", font_size)).grid(row=4, column=0, pady=10)

        # Output
        self.translated_text = scrolledtext.ScrolledText(master, height=10, font=("Arial", font_size))
        self.translated_text.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def translate_text(self):
        text_to_translate = self.text_entry.get().strip()
        dest_language = self.language_entry.get().strip().lower()

        if not text_to_translate:
            messagebox.showerror("Error", "Please enter text to translate.")
            return

        if not dest_language:
            messagebox.showerror("Error", "Please enter destination language.")
            return

        try:
            translated = GoogleTranslator(source='auto', target=dest_language).translate(text_to_translate)
            self.translated_text.delete("1.0", tk.END)
            self.translated_text.insert(tk.END, translated)
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed:\n{str(e)}")

def main():
    root = tk.Tk()
    app = TranslatorAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()