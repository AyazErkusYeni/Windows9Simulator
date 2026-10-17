import tkinter as tk
from tkinter import messagebox
import time

class Windows9Sim:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 9 Professional - Simulator")
        self.root.geometry("1024x768")
        self.root.minsize(800, 600)
        
        # Tema Renkleri (Retro/Windows 9X Konsepti)
        self.bg_color = "#008080"      # Klasik Camgöbeği Masaüstü
        self.win_bg = "#d4d0c8"        # Pencere Arka Planı
        self.win_title_bg = "#000080"  # Aktif Pencere Başlığı
        self.win_title_fg = "#ffffff"  # Pencere Başlık Yazısı
        
        self.root.configure(bg=self.bg_color)
        
        # Arayüz Elemanları
        self.create_desktop()
        self.create_taskbar()
        self.update_clock()
        
    def create_desktop(self):
        # Masaüstü İkonları İçin Alan
        self.desktop_frame = tk.Frame(self.root, bg=self.bg_color)
        self.desktop_frame.pack(fill="both", expand=True)
        
        # Örnek Masaüstü İkonları
        icons = [
            ("Bilgisayarım", self.open_my_computer),
            ("Not Defteri", self.open_notepad),
            ("Hesap Makinesi", self.open_calculator),
            ("Komut İstemi", self.open_cmd)
        ]
        
        for i, (name, cmd) in enumerate(icons):
            btn = tk.Button(self.desktop_frame, text=name, bg=self.win_bg, fg="black",
                            font=("Arial", 10, "bold"), width=12, height=2, relief="raised", command=cmd)
            btn.grid(row=i, column=0, padx=20, pady=20, sticky="w")

    def create_taskbar(self):
        # Alt Görev Çubuğu
        self.taskbar = tk.Frame(self.root, bg=self.win_bg, height=40, bd=2, relief="raised")
        self.taskbar.pack(fill="x", side="bottom")
        
        # Başlat Butonu
        self.start_btn = tk.Button(self.taskbar, text="Başlat", font=("Arial", 10, "bold"),
                                  bg=self.win_bg, relief="raised", width=10, command=self.toggle_start_menu)
        self.start_btn.pack(side="left", padx=5, pady=5)
        
        # Saat Paneli
        self.clock_label = tk.Label(self.taskbar, text="", font=("Arial", 10, "bold"),
                                    bg=self.win_bg, fg="black", bd=1, relief="sunken", width=12)
        self.clock_label.pack(side="right", padx=10, pady=5)
        
        # Başlat Menüsü Penceresi (Gizli Başlar)
        self.start_menu = tk.Frame(self.root, bg=self.win_bg, bd=2, relief="raised", width=180, height=250)
        self.start_menu_visible = False
        
        # Başlat Menüsü Elemanları
        tk.Label(self.start_menu, text="WINDOWS 9", bg="#808080", fg="white", font=("Arial", 12, "bold"), width=16).pack(fill="x", pady=2)
        tk.Button(self.start_menu, text="Not Defteri", anchor="w", relief="flat", bg=self.win_bg, command=lambda: [self.open_notepad(), self.toggle_start_menu()]).pack(fill="x", padx=5, pady=2)
        tk.Button(self.start_menu, text="Hesap Makinesi", anchor="w", relief="flat", bg=self.win_bg, command=lambda: [self.open_calculator(), self.toggle_start_menu()]).pack(fill="x", padx=5, pady=2)
        tk.Button(self.start_menu, text="Komut İstemi", anchor="w", relief="flat", bg=self.win_bg, command=lambda: [self.open_cmd(), self.toggle_start_menu()]).pack(fill="x", padx=5, pady=2)
        tk.Frame(self.start_menu, height=2, bg="#808080").pack(fill="x", pady=5)
        tk.Button(self.start_menu, text="Sistemi Kapat", anchor="w", relief="flat", bg=self.win_bg, fg="red", command=self.root.quit).pack(fill="x", padx=5, pady=2)

    def toggle_start_menu(self):
        if self.start_menu_visible:
            self.start_menu.place_forget()
            self.start_menu_visible = False
        else:
            self.start_menu.place(x=5, y=self.root.winfo_height() - 285, width=180, height=240)
            self.start_menu.lift()
            self.start_menu_visible = True

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.configure(text=current_time)
        self.root.after(1000, self.update_clock)

    # --- Sürüklenebilir Pencere Şablonu ---
    def create_window(self, title, width=400, height=300):
        win = tk.Frame(self.desktop_frame, bg=self.win_bg, bd=2, relief="raised")
        win.place(x=150, y=100, width=width, height=height)
        
        # Başlık Çubuğu
        title_bar = tk.Frame(win, bg=self.win_title_bg, height=25)
        title_bar.pack(fill="x", side="top")
        
        title_lbl = tk.Label(title_bar, text=title, bg=self.win_title_bg, fg=self.win_title_fg, font=("Arial", 9, "bold"))
        title_lbl.pack(side="left", padx=5)
        
        close_btn = tk.Button(title_bar, text="X", bg=self.win_bg, fg="black", font=("Arial", 8, "bold"),
                              width=3, height=1, command=win.destroy, relief="raised")
        close_btn.pack(side="right", padx=2, pady=2)
        
        # Sürükleme Mekanizması
        def start_drag(event):
            win._drag_x = event.x
            win._drag_y = event.y
            win.lift()

        def do_drag(event):
            x = win.winfo_x() - win._drag_x + event.x
            y = win.winfo_y() - win._drag_y + event.y
            win.place(x=x, y=y)

        title_bar.bind("<Button-1>", start_drag)
        title_bar.bind("<B1-Motion>", do_drag)
        
        # İçerik Alanı
        body = tk.Frame(win, bg=self.win_bg)
        body.pack(fill="both", expand=True, padx=5, pady=5)
        return body

    # --- Uygulamalar ---
    def open_my_computer(self):
        body = self.create_window("Bilgisayarım", 350, 250)
        tk.Label(body, text="Windows 9 OS Pro", font=("Arial", 12, "bold"), bg=self.win_bg).pack(pady=10)
        tk.Label(body, text="Geliştirici: AyazXS, XS / MNX Team\nYıl: 2023\nSistem Durumu: Kararlı", bg=self.win_bg, justify="center").pack(pady=10)

    def open_notepad(self):
        body = self.create_window("Not Defteri - Adsız", 450, 350)
        txt = tk.Text(body, font=("Courier New", 10), bd=2, relief="sunken")
        txt.pack(fill="both", expand=True)
        txt.insert("1.0", "Buraya notlarınızı yazabilirsiniz...")

    def open_calculator(self):
        body = self.create_window("Hesap Makinesi", 250, 320)
        
        display = tk.Entry(body, font=("Arial", 14), justify="right", bd=4, relief="sunken")
        display.pack(fill="x", pady=5)
        
        btn_frame = tk.Frame(body, bg=self.win_bg)
        btn_frame.pack(fill="both", expand=True)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        def calc_press(key):
            if key == '=':
                try:
                    res = eval(display.get())
                    display.delete(0, tk.END)
                    display.insert(tk.END, str(res))
                except:
                    display.delete(0, tk.END)
                    display.insert(tk.END, "Hata")
            elif key == 'C':
                display.delete(0, tk.END)
            else:
                display.insert(tk.END, key)

        for i, btn_text in enumerate(buttons):
            r, c = i // 4, i % 4
            b = tk.Button(btn_frame, text=btn_text, font=("Arial", 11, "bold"), width=4, height=2,
                          command=lambda k=btn_text: calc_press(k), relief="raised")
            b.grid(row=r, column=c, padx=3, pady=3)

    def open_cmd(self):
        body = self.create_window("Komut İstemi (CMD)", 500, 350)
        body.configure(bg="black")
        
        out_txt = tk.Text(body, bg="black", fg="#00ff00", font=("Courier New", 10), wrap="word")
        out_txt.pack(fill="both", expand=True)
        out_txt.insert("1.0", "Windows 9 [Version 9.0.2023]\n(c) AyazXS, XS / MNX Team. Tüm hakları saklıdır.\n\nYardım için 'help' yazın.\n\nC:\\> ")
        out_txt.config(state="disabled")
        
        cmd_entry = tk.Entry(body, bg="black", fg="#00ff00", font=("Courier New", 10), insertbackground="#00ff00", bd=0)
        cmd_entry.pack(fill="x", side="bottom", padx=5, pady=5)
        cmd_entry.focus_set()
        
        def execute_cmd(event):
            cmd = cmd_entry.get().strip().lower()
            cmd_entry.delete(0, tk.END)
            
            output = f"\nC:\\> {cmd}\n"
            if cmd == "help":
                output += "Kullanılabilir komutlar: help, version, clear, date, team"
            elif cmd == "version":
                output += "Windows 9 Professional [Sürüm 9.0.2023]"
            elif cmd == "team":
                output += "Geliştirici: AyazXS & XS / MNX Team"
            elif cmd == "date":
                output += f"Geçerli Tarih: {time.strftime('%d.%m.%Y')}"
            elif cmd == "clear":
                out_txt.config(state="normal")
                out_txt.delete("1.0", tk.END)
                out_txt.insert("1.0", "C:\\> ")
                out_txt.config(state="disabled")
                return
            elif cmd == "":
                pass
            else:
                output += f"'{cmd}' geçerli bir komut olarak tanınmadı."
                
            out_txt.config(state="normal")
            out_txt.insert(tk.END, output + "\n")
            out_txt.see(tk.END)
            out_txt.config(state="disabled")

        cmd_entry.bind("<Return>", execute_cmd)

if __name__ == "__main__":
    root = tk.Tk()
    app = Windows9Sim(root)
    root.mainloop()
