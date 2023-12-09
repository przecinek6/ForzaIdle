from imagefinding import *
import customtkinter
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("340x100")
app.title("Forza Horizon 5 bot by CiNEK")
app.iconbitmap("icon.ico")

done = False

def main_fun():
    global done
    time.sleep(1)  # waiting time before program runs
    while not done:
        press_esc()
        findimage(1)
        findimage(2)
        findimage(3)
        findimage(4)
        findimage(5)
        findimage(6)
        findimage(7)
        findimage(8)
        time.sleep(3) # animation time
        hold_space(43)
        findimage_end()


def button_event():
    global done

    current_text = button.cget("text")
    if current_text == "START":
        button.configure(text="STOP", fg_color="red", hover_color="red")
        done = False
        threading.Thread(target=main_fun).start()

    else:
        button.configure(text="START", fg_color="green", hover_color="green")
        done = True

# frame = customtkinter.CTkFrame(app, width=400, height=20)
# frame.pack(fill="both")
#
# label = customtkinter.CTkLabel(frame, text="Simple bot for Forza Horizon 5", font=("Unispace", 24))
# label.pack(pady=20)

button = customtkinter.CTkButton(app, width=150, height=50,
                                 text="START", font=("Unispace", 24), fg_color="green", hover_color="green",
                                 command=button_event)
button.pack(pady=30)

app.mainloop()
