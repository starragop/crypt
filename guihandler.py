from tkinter import *
from config import *

def begin(begin_enc):
  window = Tk()
  window.title("Crypt")
  window.geometry(str(gui_conf["x"])+"x"+str(gui_conf["y"]))
  title = Label(window, text="Crypt")
  modevar = IntVar()
  M1 = Radiobutton(window, text="Encrypt", variable=modevar, value=True)
  M2 = Radiobutton(window, text="Decrypt", variable=modevar, value=False)
  typevar = IntVar()
  T1 = Radiobutton(window, text="File", variable=typevar, value=True)
  T2 = Radiobutton(window, text="Directory", variable=typevar, value=False)
  key = Entry(window, bd=2)
  target = Entry(window, bd=2)
  destination = Entry(window, bd=2)
  status = Label(window, text="Idle")
  def throwMsg(msg,type):
    if type == 1:
      window.messagebox.showinfo("Notice",msg)
    elif type == 2:
      window.messagebox.showerror("Error",msg)
  def start():
    print("Start")
    success = begin_enc(modevar.get(), typevar.get(), key.get(), target.get(), destination.get())
    if success == True:
      throwMsg("Successful operation",1)
    else:
      throwMsg("Operation failed: " + success,2)
  enc_btn = Button(window, text="Encrypt", command=start)
  middle_align = gui_conf["x"]/2
  places = []
  for i in range(gui_conf["button_count"]):
    places.append((gui_conf["y"] - (gui_conf["tb_padding"] * 2)/gui_conf["button_count"]) * i + gui_conf["tb_padding"])
  title.place(x=middle_align,y=places[0])
  M1.place(x=gui_conf["radio_out"],y=places[1])
  M2.place(x=gui_conf["x"] - gui_conf["radio_out"],y=places[1])
  T1.place(x=gui_conf["radio_out"],y=places[2])
  T2.place(x=gui_conf["x"] - gui_conf["radio_out"],y=places[2])
  key.place(x=middle_align,y=places[3])
  target.place(x=middle_align,y=places[4])
  destination.place(x=middle_align,y=places[5])
  enc_btn.place(x=middle_align,y=places[6])
  status.place(x=middle_align,y=gui_conf["x"] - gui_conf["status_placement"])
  window.mainloop()
