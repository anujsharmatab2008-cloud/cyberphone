import customtkinter as ctk
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GlobalAIAggregator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main window configurations
        self.title("AI Mobile Marketplace & Comparer Hub")
        self.geometry("980x760")
        self.configure(fg_color="#0A0F14")  # Deep cyber black

        # --- COMPLETE COMPREHENSIVE INTEGRATED DATABASE ---
        self.global_database = [
            # --- BUDGET CHAMPIONS & RECENT MID-RANGERS (₹14k - ₹20k) ---
            {"name": "OnePlus Nord CE 6 Lite 5G", "brand": "OnePlus", "price": 18999, "ram": 6, "storage": 128, "cpu": "Dimensity 7400 Apex", "battery": 7000},
            {"name": "POCO M8 5G", "brand": "Poco", "price": 17999, "ram": 6, "storage": 128, "cpu": "Snapdragon 6 Gen 3", "battery": 5520},
            {"name": "Moto G96 5G", "brand": "Motorola", "price": 17999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7s Gen 2", "battery": 5500},
            {"name": "Vivo T4X 5G", "brand": "Vivo", "price": 16999, "ram": 6, "storage": 128, "cpu": "Dimensity 7300", "battery": 6500},
            {"name": "Realme P4x 5G", "brand": "Realme", "price": 15999, "ram": 6, "storage": 128, "cpu": "Dimensity 7400 Ultra", "battery": 7000},
            {"name": "Realme P3 5G", "brand": "Realme", "price": 15999, "ram": 6, "storage": 128, "cpu": "Snapdragon 6 Gen 4", "battery": 6000},
            {"name": "Samsung Galaxy F36 5G", "brand": "Samsung", "price": 17999, "ram": 6, "storage": 128, "cpu": "Exynos 1380", "battery": 6000},
            {"name": "POCO X7 5G", "brand": "Poco", "price": 16999, "ram": 8, "storage": 128, "cpu": "Dimensity 7300", "battery": 5500},
            {"name": "CMF by Nothing Phone 2 Pro", "brand": "Nothing", "price": 17999, "ram": 8, "storage": 128, "cpu": "Dimensity 7400", "battery": 5000},
            {"name": "iQOO Z10x 5G", "brand": "iQOO", "price": 14998, "ram": 6, "storage": 128, "cpu": "Dimensity 7300", "battery": 6500},
            {"name": "Motorola Moto G86 Power 5G", "brand": "Motorola", "price": 17500, "ram": 8, "storage": 128, "cpu": "Dimensity 7400", "battery": 6720},
            {"name": "iQOO Z9x 5G", "brand": "iQOO", "price": 17499, "ram": 8, "storage": 128, "cpu": "Snapdragon 6 Gen 1", "battery": 6000},
            {"name": "iQOO Z9 5G", "brand": "iQOO", "price": 19999, "ram": 8, "storage": 128, "cpu": "Dimensity 7200", "battery": 5000},
            {"name": "Samsung Galaxy M35 5G", "brand": "Samsung", "price": 19999, "ram": 8, "storage": 128, "cpu": "Exynos 1380", "battery": 6000},
            {"name": "Motorola G64 5G", "brand": "Motorola", "price": 15999, "ram": 8, "storage": 128, "cpu": "Dimensity 7025", "battery": 6000},
            {"name": "Realme P1 5G", "brand": "Realme", "price": 15999, "ram": 6, "storage": 128, "cpu": "Dimensity 7050", "battery": 5000},
            {"name": "Realme Narzo 70 Pro", "brand": "Realme", "price": 18999, "ram": 8, "storage": 128, "cpu": "Dimensity 7050", "battery": 5000},
            {"name": "Xiaomi Redmi Note 13 5G", "brand": "Xiaomi", "price": 16999, "ram": 6, "storage": 128, "cpu": "Dimensity 6080", "battery": 5000},
            {"name": "Xiaomi Redmi Note 14 5G", "brand": "Xiaomi", "price": 19999, "ram": 8, "storage": 128, "cpu": "Dimensity 7025 Ultra", "battery": 5110},
            {"name": "POCO X6 Neo 5G", "brand": "Poco", "price": 15999, "ram": 8, "storage": 128, "cpu": "Dimensity 6080", "battery": 5000},
            {"name": "OPPO K14x 5G", "brand": "OPPO", "price": 14749, "ram": 6, "storage": 128, "cpu": "Dimensity 6300", "battery": 6500},
            {"name": "Vivo T3x 5G", "brand": "Vivo", "price": 16499, "ram": 8, "storage": 128, "cpu": "Snapdragon 6 Gen 1", "battery": 6000},
            {"name": "Lava Agni 2 5G", "brand": "Lava", "price": 17999, "ram": 8, "storage": 256, "cpu": "Dimensity 7050", "battery": 4700},

            # --- APPLE PREMIUM ECOSYSTEM ---
            {"name": "Apple iPhone 17 Pro Max", "brand": "Apple", "price": 149900, "ram": 12, "storage": 256, "cpu": "A19 Pro", "battery": 4832},
            {"name": "Apple iPhone 17 Pro", "brand": "Apple", "price": 129900, "ram": 12, "storage": 128, "cpu": "A19 Pro", "battery": 4200},
            {"name": "Apple iPhone 17 Standard", "brand": "Apple", "price": 79900, "ram": 8, "storage": 128, "cpu": "A19", "battery": 4000},
            {"name": "Apple iPhone 16 Pro Max", "brand": "Apple", "price": 139900, "ram": 8, "storage": 256, "cpu": "A18 Pro", "battery": 4685},
            {"name": "Apple iPhone 16 Standard", "brand": "Apple", "price": 69900, "ram": 8, "storage": 128, "cpu": "A18", "battery": 3561},
            {"name": "Apple iPhone 15 Pro Max", "brand": "Apple", "price": 124900, "ram": 8, "storage": 256, "cpu": "A17 Pro", "battery": 4441},
            {"name": "Apple iPhone 15 Standard", "brand": "Apple", "price": 59900, "ram": 6, "storage": 128, "cpu": "A16 Bionic", "battery": 3349},
            {"name": "Apple iPhone SE 4 (AI Edition)", "brand": "Apple", "price": 49900, "ram": 8, "storage": 128, "cpu": "A18", "battery": 3200},

            # --- SAMSUNG ULTRA FLAGSHIP & HIGH TIERS ---
            {"name": "Samsung Galaxy S26 Ultra", "brand": "Samsung", "price": 121998, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 5000},
            {"name": "Samsung Galaxy S26 Plus", "brand": "Samsung", "price": 84999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 4900},
            {"name": "Samsung Galaxy S25 Ultra", "brand": "Samsung", "price": 104400, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 5000},
            {"name": "Samsung Galaxy S24 Ultra", "brand": "Samsung", "price": 99999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Gen 3", "battery": 5000},
            {"name": "Samsung Galaxy S24 FE", "brand": "Samsung", "price": 54999, "ram": 8, "storage": 128, "cpu": "Exynos 2400e", "battery": 4700},
            {"name": "Samsung Galaxy A57 5G", "brand": "Samsung", "price": 38999, "ram": 8, "storage": 128, "cpu": "Exynos 1580", "battery": 5000},
            {"name": "Samsung Galaxy A37 5G", "brand": "Samsung", "price": 27999, "ram": 8, "storage": 128, "cpu": "Exynos 1480", "battery": 5000},
            {"name": "Samsung Galaxy M55 5G", "brand": "Samsung", "price": 24999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7 Gen 1", "battery": 5000},

            # --- ONEPLUS HIGH PERFORMANCE ---
            {"name": "OnePlus 15 Pro", "brand": "OnePlus", "price": 79999, "ram": 16, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 6500},
            {"name": "OnePlus 13 Standard", "brand": "OnePlus", "price": 69999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 6000},
            {"name": "OnePlus 13R 5G", "brand": "OnePlus", "price": 42999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Gen 3", "battery": 6000},
            {"name": "OnePlus 12R", "brand": "OnePlus", "price": 37999, "ram": 8, "storage": 128, "cpu": "Snapdragon 8 Gen 2", "battery": 5500},
            {"name": "OnePlus Nord 6 5G", "brand": "OnePlus", "price": 42999, "ram": 8, "storage": 256, "cpu": "Snapdragon 8s Gen 4", "battery": 9000},
            {"name": "OnePlus Nord CE 4 5G", "brand": "OnePlus", "price": 23499, "ram": 8, "storage": 128, "cpu": "Snapdragon 7 Gen 3", "battery": 5500},

            # --- ADVANCED POWER MID-RANGERS (₹20k - ₹120k) ---
            {"name": "Xiaomi 17 Ultra", "brand": "Xiaomi", "price": 119999, "ram": 16, "storage": 512, "cpu": "Snapdragon 8 Elite", "battery": 5500},
            {"name": "Xiaomi Redmi Note 15 Pro+", "brand": "Xiaomi", "price": 33999, "ram": 12, "storage": 256, "cpu": "Dimensity 7500 Ultra", "battery": 5500},
            {"name": "POCO F6 5G", "brand": "Poco", "price": 29999, "ram": 8, "storage": 256, "cpu": "Snapdragon 8s Gen 3", "battery": 5000},
            {"name": "POCO X6 Pro 5G", "brand": "Poco", "price": 22499, "ram": 8, "storage": 256, "cpu": "Dimensity 8300 Ultra", "battery": 5000},
            {"name": "Realme GT 6T 5G", "brand": "Realme", "price": 29999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7+ Gen 3", "battery": 5500},
            {"name": "Motorola Edge 50 Pro", "brand": "Motorola", "price": 29999, "ram": 8, "storage": 256, "cpu": "Snapdragon 7 Gen 3", "battery": 4500},
            {"name": "Motorola Edge 50 Fusion", "brand": "Motorola", "price": 21999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7s Gen 2", "battery": 5000},
            {"name": "iQOO Neo 11 Pro", "brand": "iQOO", "price": 36999, "ram": 8, "storage": 256, "cpu": "Snapdragon 8 Gen 4", "battery": 7500},
            {"name": "Vivo V40 Pro 5G", "brand": "Vivo", "price": 49999, "ram": 8, "storage": 256, "cpu": "Dimensity 9200+", "battery": 5500},
            {"name": "OPPO Reno 12 Pro 5G", "brand": "OPPO", "price": 34999, "ram": 12, "storage": 256, "cpu": "Dimensity 7300 Energy", "battery": 5000},
            {"name": "Google Pixel 9 Pro XL", "brand": "Google", "price": 89999, "ram": 16, "storage": 128, "cpu": "Tensor G4", "battery": 5060},
            {"name": "Nothing Phone (2a) Plus", "brand": "Nothing", "price": 27999, "ram": 8, "storage": 256, "cpu": "Dimensity 7350 Pro", "battery": 5000}
        ]

        self.filtered_products = list(self.global_database)
        self.selected_to_compare = []
        self.checkbox_vars = {}

        self.setup_ui_layout()

    def setup_ui_layout(self):
        # --- LEFT PANEL: NAVIGATION & SELECTION TARGET ---
        self.left_container = ctk.CTkFrame(self, fg_color="transparent", width=460)
        self.left_container.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        self.title_label = ctk.CTkLabel(
            self.left_container, text="CYBER AGGREGATOR", 
            font=ctk.CTkFont(family="Helvetica", size=22, weight="bold"), text_color="#00FF66"
        )
        self.title_label.pack(pady=15)  # FIXED: Clean layout padding metric execution

        self.filter_box = ctk.CTkFrame(self.left_container, fg_color="#121B22", border_color="#00E5FF", border_width=1)
        self.filter_box.pack(fill="x", pady=5, padx=5)

        self.budget_label = ctk.CTkLabel(self.filter_box, text="Max Budget: ₹1,50,000", text_color="#FFFFFF", font=ctk.CTkFont(size=12, weight="bold"))
        self.budget_label.pack(anchor="w", padx=15, pady=(10, 2))
        
        # Performance Slider Core Module
        self.budget_slider = ctk.CTkSlider(self.filter_box, from_=10000, to=150000, number_of_steps=140, fg_color="#0A0F14", progress_color="#00FF66", button_color="#00E5FF", command=self.sync_budget_label)
        self.budget_slider.set(150000)
        self.budget_slider.pack(fill="x", padx=15, pady=(0, 10))
        
        # Non-blocking filter refresh hook binded to active mouse release
        self.budget_slider.bind("<ButtonRelease-1>", lambda event: self.apply_filters())

        self.cpu_label = ctk.CTkLabel(self.filter_box, text="Preferred Chip Core Type:", text_color="#888888", font=ctk.CTkFont(size=11))
        self.cpu_label.pack(anchor="w", padx=15)
        self.cpu_dropdown = ctk.CTkOptionMenu(self.filter_box, values=["All Processors", "Snapdragon", "Dimensity", "Apple", "Tensor", "Exynos"], fg_color="#0A0F14", button_color="#121B22", button_hover_color="#00E5FF", dropdown_fg_color="#121B22", command=lambda _: self.apply_filters())
        self.cpu_dropdown.pack(fill="x", padx=15, pady=(0, 15))

        self.search_frame = ctk.CTkFrame(self.left_container, fg_color="transparent")
        self.search_frame.pack(fill="x", pady=10)
        
        self.search_input = ctk.CTkEntry(self.search_frame, placeholder_text="Type keyword (e.g., Ultra, Pro Max, Nord)...", fg_color="#121B22", border_color="#00E5FF", text_color="#FFFFFF")
        self.search_input.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.search_btn = ctk.CTkButton(self.search_frame, text="Apply Filter", fg_color="#00E5FF", text_color="#0A0F14", font=ctk.CTkFont(weight="bold"), width=90, command=self.apply_filters)
        self.search_btn.pack(side="right")

        self.scroll_frame = ctk.CTkScrollableFrame(self.left_container, fg_color="#121B22", border_color="#00FF66", border_width=1)
        self.scroll_frame.pack(fill="both", expand=True, pady=10)

        # --- RIGHT PANEL: REAL-TIME COMPARATIVE BENCHMARK ---
        self.right_container = ctk.CTkFrame(self, fg_color="#121B22", border_color="#00E5FF", border_width=1)
        self.right_container.pack(side="right", fill="both", expand=True, padx=(0, 15), pady=25)

        self.matrix_title = ctk.CTkLabel(self.right_container, text="LIVE MATRIX BENCHMARK", font=ctk.CTkFont(size=14, weight="bold"), text_color="#00E5FF")
        self.matrix_title.pack(pady=10)

        self.table_frame = ctk.CTkFrame(self.right_container, fg_color="#0A0F14")
        self.table_frame.pack(fill="both", expand=True, padx=15, pady=5)
        
        self.table_placeholder = ctk.CTkLabel(self.table_frame, text="// Select devices on the left to map comparison nodes...", text_color="#666666", font=ctk.CTkFont(family="Courier"))
        self.table_placeholder.pack(expand=True)

        self.compare_btn = ctk.CTkButton(self.right_container, text="RUN INTELLECT VERDICT ⚡", fg_color="#00FF66", text_color="#0A0F14", font=ctk.CTkFont(size=14, weight="bold"), command=self.trigger_ai_thread)
        self.compare_btn.pack(fill="x", padx=15, pady=10)

        self.output_box = ctk.CTkTextbox(self.right_container, height=180, fg_color="#0A0F14", border_color="#00FF66", border_width=1, text_color="#00FF66", font=ctk.CTkFont(family="Courier", size=12))
        self.output_box.pack(fill="x", padx=15, pady=(0, 15))
        self.output_box.insert("0.0", "// AI Engine: Standing by...")

        self.render_filtered_view()

    def sync_budget_label(self, value):
        # UI Optimization: instantly updates display string label smoothly without blocking
        self.budget_label.configure(text=f"Max Budget: ₹{int(value):,}")

    def apply_filters(self):
        query = self.search_input.get().lower().strip()
        max_budget = int(self.budget_slider.get())
        selected_cpu = self.cpu_dropdown.get()

        filtered = []
        for p in self.global_database:
            if p["price"] > max_budget:
                continue
            if selected_cpu != "All Processors":
                if selected_cpu.lower() == "apple" and "a1" not in p["cpu"].lower():
                    continue
                elif selected_cpu.lower() != "apple" and selected_cpu.lower() not in p["cpu"].lower():
                    continue
            if query and query not in p["name"].lower() and query not in p["brand"].lower():
                continue
            filtered.append(p)

        self.filtered_products = filtered
        self.render_filtered_view()

    def render_filtered_view(self):
        for w in self.scroll_frame.winfo_children():
            w.destroy()

        if not self.filtered_products:
            ctk.CTkLabel(self.scroll_frame, text="No mobile assets align with criteria matches.", text_color="#666666").pack(pady=20)
            return

        for prod in self.filtered_products:
            row = ctk.CTkFrame(self.scroll_frame, fg_color="#1A2630", corner_radius=6)
            row.pack(fill="x", pady=4, padx=5)

            info_str = f"{prod['name']}\nPrice: ₹{prod['price']:,} | Core: {prod['cpu']}\nAvailable via Amazon & Flipkart"
            lbl = ctk.CTkLabel(row, text=info_str, justify="left", text_color="#FFFFFF", font=ctk.CTkFont(size=11))
            lbl.pack(side="left", padx=12, pady=8)

            if prod["name"] not in self.checkbox_vars:
                self.checkbox_vars[prod["name"]] = ctk.StringVar(value="off")

            cb = ctk.CTkCheckBox(
                row, text="", variable=self.checkbox_vars[prod["name"]],
                onvalue="on", offvalue="off", border_color="#00E5FF", fg_color="#00FF66",
                command=self.update_comparison_matrix
            )
            cb.pack(side="right", padx=12)

    def update_comparison_matrix(self):
        self.selected_to_compare = [p for p in self.global_database if self.checkbox_vars.get(p["name"], ctk.StringVar(value="off")).get() == "on"]

        for w in self.table_frame.winfo_children():
            w.destroy()

        if not self.selected_to_compare:
            self.table_placeholder = ctk.CTkLabel(self.table_frame, text="// Select devices on the left to map comparison nodes...", text_color="#666666", font=ctk.CTkFont(family="Courier"))
            self.table_placeholder.pack(expand=True)
            return

        # Cap table node visual processing columns to a clean maximum width allocation of 3
        display_nodes = self.selected_to_compare[:3]

        for trait in ["Model Label", "Retail Rate", "System RAM", "Chip Core", "Cell Power"]:
            tr_frame = ctk.CTkFrame(self.table_frame, fg_color="transparent")
            tr_frame.pack(fill="x", pady=3)
            
            lbl_key = ctk.CTkLabel(tr_frame, text=trait.ljust(15), font=ctk.CTkFont(family="Courier", size=11, weight="bold"), text_color="#00E5FF", width=120, anchor="w")
            lbl_key.pack(side="left", padx=5)

            for item in display_nodes:
                val = ""
                if trait == "Model Label": val = item["name"][:15] + ".."
                elif trait == "Retail Rate": val = f"₹{item['price']:,}"
                elif trait == "System RAM": val = f"{item['ram']} GB"
                elif trait == "Chip Core": val = item["cpu"][:14]
                elif trait == "Cell Power": val = f"{item['battery']} mAh"

                lbl_val = ctk.CTkLabel(tr_frame, text=val.ljust(16), font=ctk.CTkFont(family="Courier", size=11), text_color="#FFFFFF", width=110, anchor="w")
                lbl_val.pack(side="left", padx=5)

    def trigger_ai_thread(self):
        self.output_box.delete("0.0", "end")
        if len(self.selected_to_compare) < 2:
            self.output_box.insert("0.0", "[CRITICAL ERROR] Target matrix operations require a minimum of 2 selected nodes.")
            return
        
        self.compare_btn.configure(text="PROCESSING VERDICT...")
        threading.Thread(target=self.execute_mock_ai_evaluation, daemon=True).start()

    def execute_mock_ai_evaluation(self):
        import time
        time.sleep(1.0)

        # Hardware evaluation comparison layer logic loop
        target_winner = self.selected_to_compare[0]
        for current in self.selected_to_compare:
            if current["ram"] > target_winner["ram"] or (current["price"] < target_winner["price"] and current["battery"] >= target_winner["battery"]):
                target_winner = current

        verdict_text = f"[SYSTEM ENGINE ANALYSIS ACTIVATED]\n"
        verdict_text += f"-> Processing comparative datasets across your selections.\n"
        verdict_text += "------------------------------------------------------\n"
        verdict_text += f"🏆 AI RECOMMENDED OPTION: {target_winner['name'].upper()}\n\n"
        verdict_text += f"💡 HARDWARE RUN DOWN:\n"
        verdict_text += f"The {target_winner['name']} holds the performance balance here. "
        verdict_text += f"Featuring a {target_winner['cpu']} setup alongside an efficient {target_winner['battery']} mAh battery tier, it delivers optimal specification metrics for its target cost bracket."
        
        self.after(0, lambda: self._update_ai_output(verdict_text))

    def _update_ai_output(self, text):
        self.output_box.delete("0.0", "end")
        self.output_box.insert("0.0", text)
        self.compare_btn.configure(text="RUN INTELLECT VERDICT ⚡")

if __name__ == "__main__":
    app = GlobalAIAggregator()
    app.mainloop()
