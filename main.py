import customtkinter
import threading
import logic
from logic import forza_instructions

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("340x100")
app.title("Forza Horizon 5 bot by CiNEK")
app.iconbitmap("icon.ico")


def button_event():

    current_text = button.cget("text")
    if current_text == "START":
        button.configure(text="STOP", fg_color="red", hover_color="darkred")
        threading.Thread(target=forza_instructions).start()

    else:
        button.configure(text="START", fg_color="green", hover_color="darkgreen")
        logic.running = False


button = customtkinter.CTkButton(app, width=150, height=50, text="START", font=("Unispace", 24),
                                 fg_color="green", hover_color="darkgreen", command=button_event)
button.pack(pady=30)

label = customtkinter.CTkLabel(app, text="Github: przecinek6", font=("Unispace", 10), text_color="gold")
label.place(relx=1.0, rely=1.0, anchor='se', x=-10)

app.mainloop()
