import time
import tkinter.messagebox
from tkinter import *


class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Chatbot-NLP")

        self.configure_styles()

        self.create_menu()
        self.create_text_frame()
        self.create_entry_frame()
        self.create_send_button_frame()

    def configure_styles(self):
        self.default_bg = "#EEEEEE"
        self.default_fg = "#000000"
        self.default_font = "Verdana 10"

    def create_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)

        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Chat", command=self.clear_chat)
        file_menu.add_command(label="Exit", command=self.chat_exit)

        preferences_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Preferences", menu=preferences_menu)

        font_menu = Menu(preferences_menu, tearoff=0)
        preferences_menu.add_cascade(label="Font", menu=font_menu)
        font_menu.add_command(label="Default", command=self.font_change_default)
        font_menu.add_command(label="System", command=self.font_change_system)

        theme_menu = Menu(preferences_menu, tearoff=0)
        preferences_menu.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Default", command=self.color_theme_default)
        theme_menu.add_command(label="Dark Blue", command=self.color_theme_dark_blue)
        theme_menu.add_command(label="Hacker", command=self.color_theme_hacker)

        about_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Chatbot", command=self.show_info)

    def create_text_frame(self):
        text_frame = Frame(self.master, bd=6, bg=self.default_bg)
        text_frame.pack(expand=True, fill=BOTH)

        text_box_scrollbar = Scrollbar(text_frame, bd=0)
        text_box_scrollbar.pack(fill=Y, side=RIGHT)

        self.text_box = Text(text_frame, yscrollcommand=text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font=self.default_font, relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        text_box_scrollbar.config(command=self.text_box.yview)

    def create_entry_frame(self):
        entry_frame = Frame(self.master, bd=1, bg=self.default_bg)
        entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.entry_field = Entry(entry_frame, bd=1, justify=LEFT, font=self.default_font)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)

        self.last_sent_label(date="No messages sent.")

    def create_send_button_frame(self):
        send_button_frame = Frame(self.master, bd=0, bg=self.default_bg)
        send_button_frame.pack(fill=BOTH)

        send_button = Button(send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                             bd=1, command=self.send_message_insert, activebackground="#FFFFFF",
                             activeforeground="#000000")
        send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)

    def last_sent_label(self, date):
        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.default_bg, fg=self.default_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chat_exit(self):
        exit()

    def show_info(self):
        tkinter.messagebox.showinfo("NLP - Neural Network based chatbot")

    def send_message_insert(self, event=None):
        user_input = self.entry_field.get()
        user_message = "Human : " + user_input + "\n"

        self.update_text_box(user_message)

        # Assuming you have a function 'get_bot_response' for the bot response
        response = "Hello"
        bot_message = "Bot : " + response + "\n"

        self.update_text_box(bot_message)
        self.last_sent_label(str(time.strftime("Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.entry_field.delete(0, END)

    def update_text_box(self, message):
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, message)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)

    def font_change_default(self):
        self.text_box.config(font=self.default_font)
        self.entry_field.config(font=self.default_font)

    def font_change_system(self):
        self.text_box.config(font="System")
        self.entry_field.config(font="System")

    def color_theme_default(self):
        self.master.config(bg=self.default_bg)
        self.text_frame.config(bg=self.default_bg)
        self.entry_frame.config(bg=self.default_bg)
        self.text_box.config(bg="#FFFFFF", fg="#000000")
        self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
        self.send_button_frame.config(bg=self.default_bg)
        self.sent_label.config(bg=self.default_bg, fg="#000000")

    def color_theme_dark_blue(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.entry_frame.config(bg="#263b54")
        self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

    def color_theme_hacker(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.entry_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#33FF33")
        self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
        self.send_button_frame.config(bg="#0F0F0F")
        self.sent_label.config(bg="#0F0F0F", fg="#33FF33")


if __name__ == "__main__":
    root = Tk()
    ob = ChatInterface(root)
    root.mainloop()
