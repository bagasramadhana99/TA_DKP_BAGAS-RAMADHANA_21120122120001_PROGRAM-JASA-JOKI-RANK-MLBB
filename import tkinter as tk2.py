import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainForm(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Joki Rank MLBB")
        self.geometry("800x600")
        
        # Membuat label judul
        self.title_label = tk.Label(self, text="Joki Rank MLBB", font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Membuat label dan combobox untuk memilih tier
        self.tier_label = tk.Label(self, text="Pilih Tier:", font=("Arial", 12))
        self.tier_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.tier_combo_box = ttk.Combobox(self, values=["Grandmaster", "Epic", "Legend", "Mythic"], state="readonly")
        self.tier_combo_box.grid(row=1, column=1, padx=20, pady=10)

        # Membuat label dan option menu untuk memilih target bintang
        self.target_label = tk.Label(self, text="Target Bintang:", font=("Arial", 12))
        self.target_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.target_var = tk.StringVar()
        self.target_option_menu = ttk.OptionMenu(self, self.target_var, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.target_option_menu.grid(row=2, column=1, padx=20, pady=10)

        # Membuat tombol untuk menghitung harga
        self.calculate_button = tk.Button(self, text="Hitung", command=self.calculate_price, font=("Arial", 12))
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

        # Membuat label dan kotak teks untuk menampilkan total harga
        self.result_label = tk.Label(self, text="Total Harga:", font=("Arial", 12))
        self.result_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.result_text_box = tk.Entry(self, state="readonly", font=("Arial", 12))
        self.result_text_box.grid(row=4, column=1, padx=20, pady=10)

        # Membuat label dan combobox untuk memilih metode pembayaran
        self.payment_method_label = tk.Label(self, text="Metode Pembayaran:", font=("Arial", 12))
        self.payment_method_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.payment_method_var = tk.StringVar()
        self.payment_method_combo_box = ttk.Combobox(self, textvariable=self.payment_method_var,
                                                     values=["Shopepay", "Dana", "Pulsa"], state="readonly")
        self.payment_method_combo_box.grid(row=5, column=1, padx=20, pady=10)

        # Membuat tombol untuk melakukan pembayaran
        self.pay_button = tk.Button(self, text="Bayar", command=self.pay, font=("Arial", 12))
        self.pay_button.grid(row=6, column=0, padx=20, pady=10)

        # Membuat tombol untuk keluar
        self.exit_button = tk.Button(self, text="Keluar", command=self.exit_loop, font=("Arial", 12))
        self.exit_button.grid(row=6, column=1, padx=20, pady=10)

        # Membuat label untuk histori pembelian
        self.purchase_history_label = tk.Label(self, text="Histori Pembelian:", font=("Arial", 12))
        self.purchase_history_label.grid(row=7, column=0, padx=20, pady=10, sticky="w")

        # Membuat kotak teks untuk menampilkan histori pembelian
        self.purchase_history_text_box = tk.Text(self, height=5, width=50, state="disabled", font=("Arial", 12))
        self.purchase_history_text_box.grid(row=8, column=0, columnspan=2, padx=20, pady=10)

        # Inisialisasi variabel tier dan target
        self._tier = ""
        self._target = ""

        # List untuk menyimpan histori pembelian
        self.purchase_history = []

    @property
    def tier(self):
        return self._tier

    @tier.setter
    def tier(self, value):
        self._tier = value

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value

    def calculate_price(self):
        # Menghitung total harga berdasarkan tier dan target yang dipilih
        selected_tier = self.tier_combo_box.get()
        selected_target = self.target_var.get()

        if selected_tier == "Grandmaster":
            result = 6000
        elif selected_tier == "Epic":
            result = 7000
        elif selected_tier == "Legend":
            result = 8000
        elif selected_tier == "Mythic":
            result = 9000
        else:
            result = -1  # Pilihan tidak valid

        result *= int(selected_target)

        # Menampilkan hasil perhitungan di kotak teks
        self.result_text_box.configure(state="normal")
        self.result_text_box.delete(0, tk.END)
        self.result_text_box.insert(0, str(result))
        self.result_text_box.configure(state="readonly")

    def pay(self):
        # Memproses pembayaran berdasarkan nilai yang ada di kotak teks
        result = self.result_text_box.get()
        payment_method = self.payment_method_var.get()
        if result != "":
            # Mengganti pernyataan print berikut dengan kode pembayaran Anda
            self.purchase_history.append(f"Total Harga: {result}, Metode Pembayaran: {payment_method}")
            print(f"Processing payment: {result}")

            # Menampilkan notifikasi setelah pembayaran berhasil
            messagebox.showinfo("Notification", "Payment Successful!")
            self.update_purchase_history()
        else:
            messagebox.showwarning("Warning", "No amount to pay.")

    def update_purchase_history(self):
        # Mengupdate tampilan histori pembelian
        self.purchase_history_text_box.configure(state="normal")
        self.purchase_history_text_box.delete("1.0", tk.END)
        for purchase in self.purchase_history:
            self.purchase_history_text_box.insert(tk.END, f"{purchase}\n")
        self.purchase_history_text_box.configure(state="disabled")

    def exit_loop(self):
        self.destroy()

if __name__ == "__main__":
    app = MainForm()
    while True:
        app.update()
        if app.winfo_exists() == 0:
            break
    app.destroy()
