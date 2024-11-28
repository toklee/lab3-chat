import tkinter as tk
from chat import connector, reader, send_msg, read_msg
import threading
import time
from time import strftime
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from PIL import Image, ImageTk

USERNAME = 'nn'
MSG_HEIGHT = 2
msg = []
msg_lbls = []
MAXM = 10


def init_gui():
    root = tk.Tk()
    return root


def init_input(fr_input, fr_list):
    txt_entry = tk.Entry(fr_input)
    label = tk.Label(text="name", bg='pink')
    name_entry = tk.Entry()
    name_entry.insert(0, USERNAME)


    def click(txt_entry):
        text = txt_entry.get()
        if text:
            msg = {
                'user': name_entry.get(),
                'text': text
            }
            send_msg(msg)
            add_label(text)
            txt_entry.delete(0, tk.END)


    def choose_image():
        file_path = fd.askopenfilename(
            initialdir = "/", title="Select File",
            filetypes = (("Image files", ".jpg .jpeg .png"), ("all files", "."))
        )
        if file_path:
            try:
                image = Image.open(file_path)
                resized_image = image.resize((128, 128))
                photo = ImageTk.PhotoImage(resized_image)
                add_image(photo, file_path)
            except Exception as e:
                mb.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")


    def send_emoji(emoji):
        msg = {
            'user': name_entry.get(),
            'text': emoji
        }
        send_msg(msg)
        add_label(emoji)

    emoji_buttons = [
        tk.Button(fr_input, bg='pink', text="😄", command=lambda: send_emoji("😄")),
        tk.Button(fr_input, bg='pink', text="😊", command=lambda: send_emoji("😊")),
        tk.Button(fr_input, bg='pink', text="😉", command=lambda: send_emoji("😉")),
        tk.Button(fr_input, bg='pink', text="😁", command=lambda: send_emoji("😁")),
        tk.Button(fr_input, bg='pink', text="😂", command=lambda: send_emoji("😂")),
        tk.Button(fr_input, bg='pink', text="🤣", command=lambda: send_emoji("🤣")),
        tk.Button(fr_input, bg='pink', text="😍", command=lambda: send_emoji("😍")),
        tk.Button(fr_input, bg='pink', text="🤟", command=lambda: send_emoji("🤟")),
        tk.Button(fr_input, bg='pink', text="😘", command=lambda: send_emoji("😘")),
        tk.Button(fr_input, bg='pink', text="💩", command=lambda: send_emoji("💩")),
        tk.Button(fr_input, bg='pink', text="🤮", command=lambda: send_emoji("🤮")),
    ]

    tk_bt = tk.Button(fr_input, bg = 'pink', text = "send", command = lambda: click(txt_entry))
    tk_bt_image = tk.Button(fr_input, bg = 'pink', text = "Image", command = choose_image)

    txt_entry.pack(side = tk.LEFT, fill = tk.X, expand = True)
    tk_bt.pack(side = tk.LEFT)
    tk_bt_image.pack(side = tk.LEFT)
    label.pack(side = tk.LEFT)
    name_entry.pack(side = tk.LEFT)

    for button in emoji_buttons:
        button.pack(side = tk.LEFT)


def add_label(text):
    lbl_msg = tk.Label(fr_list_msg, text=text, height=MSG_HEIGHT, wraplength=300)
    lbl_msg.pack(anchor = 'ne', side = tk.TOP, padx = 2, pady = 2)
    msg_lbls.append(lbl_msg)
    if len(msg_lbls) > MAXM:
        label = msg_lbls.pop(0)
        label.destroy()


def add_image(photo, file_path):
    img_label = tk.Label(fr_list_msg, image=photo)
    img_label.image = photo
    img_label.pack(anchor = 'ne', side = tk.TOP, padx = 2, pady = 2)
    msg_lbls.append(img_label)
    if len(msg_lbls) > MAXM:
        label = msg_lbls.pop(0)
        label.destroy()


def init_frames(root):
    fr_list_msg = tk.Frame(root)
    fr_input_msg = tk.Frame(root)
    fr_list_msg.pack(fill=tk.BOTH, expand=True)
    fr_input_msg.pack(fill=tk.X, side=tk.BOTTOM)
    lbl_grit = tk.Label(fr_list_msg, text = "chatik", height = MSG_HEIGHT)
    lbl_grit.pack(side = tk.TOP)
    return fr_list_msg, fr_input_msg

if __name__ == "__main__":
    root = init_gui()
    fr_list_msg, fr_input_msg = init_frames(root)
    th = threading.Thread(target = read_msg, args = (add_label,))
    th.start()
    init_input(fr_input_msg, fr_list_msg)
    root.mainloop()
