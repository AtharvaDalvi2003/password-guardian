# password_checker.py

import tkinter as tk
from tkinter import messagebox
import re
import random
import string

# 🚨 CHANGE 1: Import all necessary components from theme.py
from theme import (
    BG_MAIN, CARD_BG, CARD_INNER, ACCENT, ACCENT_SOFT, 
    ACCENT_GREEN, ACCENT_RED, TEXT_PRIMARY, TEXT_MUTED, 
    ACCENT_GREEN_HOVER, BUTTON_DARK, BUTTON_DARK_HOVER, TEXT_DARK,
    TEXT_DANGER, # <--- THIS IS THE NEW LINE
    add_hover_effect
)
# 🚨 DELETED: The entire local color block (BG_MAIN = "#020617"...)


# ================== MAIN WINDOW ======================
window = tk.Tk()
window.title("Password Guardian – Regex Based Strength Checker")
window.geometry("760x540")
window.config(bg=BG_MAIN)
window.resizable(False, False)

# ================== GRADIENT HEADER ==================
header_canvas = tk.Canvas(window, height=120, width=760, highlightthickness=0, bd=0)
header_canvas.pack(fill="x")

# Manually draw a soft gradient using rectangles
gradient_colors = ["#1d2543", "#20295b", "#262f72", "#273891", "#273eac"]
step_width = 760 // len(gradient_colors)
for i, color in enumerate(gradient_colors):
    x1 = i * step_width
    x2 = (i + 1) * step_width
    header_canvas.create_rectangle(x1, 0, x2, 120, fill=color, outline=color)

header_canvas.create_text(
    30, 35,
    anchor="w",
    text="🔐 Password Guardian",
    font=("Segoe UI", 20, "bold"),
    fill="white"
)
header_canvas.create_text(
    30, 75,
    anchor="w",
    text="Real-time regex-based strength meter • Suggestions • Strong password generator",
    font=("Segoe UI", 10),
    fill="#e5e7eb"
)

# Subtle badge on the right
header_canvas.create_rounded_rect = lambda *args, **kwargs: None  # placeholder to avoid confusion
header_canvas.create_rectangle(
    560, 30, 730, 85,
    outline="#4b5563",
    width=1,
    fill="#020617"
)
header_canvas.create_text(
    645, 45,
    text="Cyber Security Lab",
    font=("Segoe UI", 9, "bold"),
    fill="#a5b4fc"
)
header_canvas.create_text(
    645, 65,
    text="Regex • UI • Security",
    font=("Segoe UI", 8),
    fill="#e5e7eb"
)

# ================== MAIN CARD ========================
card_outer = tk.Frame(window, bg=BG_MAIN)
card_outer.pack(fill="both", expand=True, padx=20, pady=(5, 20))

card = tk.Frame(card_outer, bg=CARD_BG, bd=0, highlightthickness=1, highlightbackground="#1f2937")
card.pack(fill="both", expand=True)

# We split the card into left (form) and right (checklist + info)
left_panel = tk.Frame(card, bg=CARD_BG)
left_panel.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=20)

right_panel = tk.Frame(card, bg=CARD_BG)
right_panel.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)

# Inner panel for input
input_panel = tk.Frame(left_panel, bg=CARD_INNER, bd=0, highlightthickness=1, highlightbackground="#1f2937")
input_panel.pack(fill="x", pady=(0, 10))

title_label = tk.Label(
    input_panel,
    text="🔑 Check Your Password",
    font=("Segoe UI", 13, "bold"),
    bg=CARD_INNER,
    fg=TEXT_PRIMARY
)
title_label.pack(anchor="w", padx=15, pady=(12, 0))

subtitle_label = tk.Label(
    input_panel,
    text="We never store your password. This tool only evaluates strength locally.",
    font=("Segoe UI", 9),
    bg=CARD_INNER,
    fg=TEXT_MUTED,
    wraplength=320,
    justify="left"
)
subtitle_label.pack(anchor="w", padx=15, pady=(2, 10))

# Entry + visibility toggle
entry_frame = tk.Frame(input_panel, bg=CARD_INNER)
entry_frame.pack(padx=15, pady=(0, 12), fill="x")

entry = tk.Entry(
    entry_frame,
    show="*",
    font=("Segoe UI", 11),
    width=28,
    bd=0,
    relief="flat",
    bg="#020617",
    fg=TEXT_PRIMARY,
    insertbackground=TEXT_PRIMARY,
    highlightthickness=1,
    highlightbackground="#374151",
    highlightcolor=ACCENT
)
entry.grid(row=0, column=0, sticky="ew", padx=(0, 8), ipady=6)
entry_frame.columnconfigure(0, weight=1)

show_password = False
def toggle_visibility():
    global show_password
    show_password = not show_password
    entry.config(show="" if show_password else "*")
    toggle_button.config(text="Hide" if show_password else "Show")

toggle_button = tk.Button(
    entry_frame,
    text="Show",
    font=("Segoe UI", 9),
    bd=0,
    relief="flat",
    bg=BUTTON_DARK, # Use imported color
    fg=TEXT_PRIMARY,
    activebackground=BUTTON_DARK,
    activeforeground=TEXT_PRIMARY,
    padx=10,
    pady=4,
    cursor="hand2"
)
toggle_button.grid(row=0, column=1)

policy_label = tk.Label(
    input_panel,
    text="Policy: ≥ 8 chars • uppercase • lowercase • number • special character",
    font=("Segoe UI", 8),
    bg=CARD_INNER,
    fg=TEXT_MUTED,
    wraplength=320,
    justify="left"
)
policy_label.pack(anchor="w", padx=15, pady=(0, 10))

# ========= BUTTONS WITH HOVER EFFECTS ===============
button_bar = tk.Frame(left_panel, bg=CARD_BG)
button_bar.pack(fill="x", pady=(0, 10))

# 🚨 DELETED: The local def add_hover_effect(...) function.

check_button = tk.Button(
    button_bar,
    text="Check Strength",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    relief="flat",
    bg=ACCENT,
    fg="white",
    activebackground=ACCENT_SOFT,
    activeforeground="white",
    padx=16,
    pady=6,
    cursor="hand2"
)
check_button.grid(row=0, column=0, padx=(0, 6))

clear_button = tk.Button(
    button_bar,
    text="Clear",
    font=("Segoe UI", 10),
    bd=0,
    relief="flat",
    bg=BUTTON_DARK,
    fg=TEXT_PRIMARY,
    activebackground=BUTTON_DARK_HOVER,
    activeforeground=TEXT_PRIMARY,
    padx=14,
    pady=6,
    cursor="hand2"
)
clear_button.grid(row=0, column=1, padx=6)

generate_button = tk.Button(
    button_bar,
    text="Generate Strong Password",
    font=("Segoe UI", 10),
    bd=0,
    relief="flat",
    bg=ACCENT_GREEN,
    fg=TEXT_DARK,
    activebackground=ACCENT_GREEN_HOVER,
    activeforeground=TEXT_DARK,
    padx=14,
    pady=6,
    cursor="hand2"
)
generate_button.grid(row=0, column=2, padx=(6, 0))

# 🚨 CHANGE 3: Update hover calls to use the imported function and specify foreground
add_hover_effect(check_button, ACCENT, ACCENT_SOFT, default_fg="white", hover_fg="white")
add_hover_effect(clear_button, BUTTON_DARK, BUTTON_DARK_HOVER, default_fg=TEXT_PRIMARY, hover_fg=TEXT_PRIMARY)
add_hover_effect(generate_button, ACCENT_GREEN, ACCENT_GREEN_HOVER, default_fg=TEXT_DARK, hover_fg=TEXT_DARK)
add_hover_effect(toggle_button, BUTTON_DARK, BUTTON_DARK_HOVER, default_fg=TEXT_PRIMARY, hover_fg=TEXT_PRIMARY)

# ================== STRENGTH BAR & RESULT =============
strength_panel = tk.Frame(left_panel, bg=CARD_BG)
strength_panel.pack(fill="both", expand=True)

w = tk.Canvas(strength_panel, height=90, width=360, bg=CARD_BG, highlightthickness=0, bd=0)
w.pack(pady=(0, 0))

result_frame = tk.Frame(strength_panel, bg=CARD_BG)
result_frame.pack()

label1 = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 11, "bold"),
    bg=CARD_BG,
    fg=TEXT_PRIMARY
)
label1.pack(pady=(0, 2))

strong_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 10),
    bg=CARD_BG,
    fg=ACCENT_GREEN
)
strong_label.pack()

suggestion_label = tk.Label(
    strength_panel,
    text="",
    font=("Segoe UI", 9),
    bg=CARD_BG,
    fg=TEXT_DANGER,
    justify="left",
    wraplength=360
)
suggestion_label.pack(pady=(4, 0))

# ================== RIGHT PANEL – CHECKLIST ============
requirements_box = tk.Frame(right_panel, bg=CARD_INNER, bd=0, highlightthickness=1, highlightbackground="#1f2937")
requirements_box.pack(fill="x", pady=(0, 10))

req_title = tk.Label(
    requirements_box,
    text="✅ Password Checklist",
    font=("Segoe UI", 11, "bold"),
    bg=CARD_INNER,
    fg=TEXT_PRIMARY
)
req_title.pack(anchor="w", padx=15, pady=(10, 0))

req_sub = tk.Label(
    requirements_box,
    text="These requirements turn green when satisfied:",
    font=("Segoe UI", 9),
    bg=CARD_INNER,
    fg=TEXT_MUTED
)
req_sub.pack(anchor="w", padx=3, pady=(0, 6))

requirements_frame = tk.Frame(requirements_box, bg=CARD_INNER)
requirements_frame.pack(padx=15, pady=(0, 10), anchor="w")

req_labels = {}

def create_req(label_text, row):
    lbl = tk.Label(
        requirements_frame,
        text=f"○ {label_text}",
        font=("Segoe UI", 9),
        bg=CARD_INNER,
        fg=TEXT_MUTED,
        anchor="w"
    )
    lbl.grid(row=row, column=0, sticky="w", pady=2)
    return lbl

req_labels["length"] = create_req("At least 8 characters", 0)
req_labels["upper"] = create_req("Contains an uppercase letter (A–Z)", 1)
req_labels["lower"] = create_req("Contains a lowercase letter (a–z)", 2)
req_labels["digit"] = create_req("Contains a number (0–9)", 3)
req_labels["special"] = create_req("Contains a special character (!@#$ etc.)", 4)

# Tip area
tip_box = tk.Frame(right_panel, bg=CARD_INNER, bd=0, highlightthickness=1, highlightbackground="#1f2937")
tip_box.pack(fill="both", expand=True, pady=(10, 0))

tip_title = tk.Label(
    tip_box,
    text="💡 Pro Tip",
    font=("Segoe UI", 11, "bold"),
    bg=CARD_INNER,
    fg="#a5b4fc"
)
tip_title.pack(anchor="w", padx=15, pady=(10, 0))

tip_label = tk.Label(
    tip_box,
    text="Avoid using names, birthdays, or common words. A mix of random words and symbols is harder to crack.",
    font=("Segoe UI", 9),
    bg=CARD_INNER,
    fg=TEXT_MUTED,
    wraplength=210,
    justify="left"
)
tip_label.pack(anchor="w", padx=15, pady=(4, 12))

# ================== PASSWORD LOGIC ======================
def evaluate_password(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if re.search(r"[A-Z]", pw): score += 1
    if re.search(r"[a-z]", pw): score += 1
    if re.search(r"\d", pw): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw): score += 1
    return score

def suggest_improvements(pw):
    suggestions = []
    if len(pw) < 8:
        suggestions.append("• Use at least 8 characters.")
    if not re.search(r"[A-Z]", pw):
        suggestions.append("• Add at least one uppercase letter.")
    if not re.search(r"[a-z]", pw):
        suggestions.append("• Include at least one lowercase letter.")
    if not re.search(r"\d", pw):
        suggestions.append("• Add at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        suggestions.append("• Use at least one special character (!@#...).")
    return "\n".join(suggestions)

def update_checklist(pw):
    checks = {
        "length": len(pw) >= 8,
        "upper": bool(re.search(r"[A-Z]", pw)),
        "lower": bool(re.search(r"[a-z]", pw)),
        "digit": bool(re.search(r"\d", pw)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw)),
    }
    for key, ok in checks.items():
        label = req_labels[key]
        base_text = label.cget("text")[2:]  # remove "○ " or "✔ "
        if ok:
            label.config(text="✔ " + base_text, fg=ACCENT_GREEN)
        else:
            label.config(text="○ " + base_text, fg=TEXT_MUTED)

def draw_strength_bar(score):
    w.delete("all")
    if score == 0:
        return

    start_x = 30
    end_x = 330
    top_y = 35
    bottom_y = 65
    segment_width = (end_x - start_x) / 5

    colors = ["#ef4444", "#f97316", "#facc15", "#22c55e", "#16a34a"]
    for i in range(5):
        x1 = start_x + i * segment_width
        x2 = start_x + (i + 1) * segment_width - 3

        if i < score:
            fill_color = colors[i]
        else:
            fill_color = "#111827"

        w.create_rectangle(
            x1, top_y, x2, bottom_y,
            fill=fill_color,
            outline="#020617",
            width=1
        )

    # Label above bar
    w.create_text(
        (start_x + end_x) / 2, 20,
        text="Strength meter",
        font=("Segoe UI", 9),
        fill=TEXT_MUTED
    )

def update_strength_display(pw, show_warning=False):
    suggestion_label["text"] = ""
    label1["text"] = ""
    strong_label["text"] = ""
    w.delete("all")

    if not pw:
        update_checklist("")
        if show_warning:
            messagebox.showinfo("Error", "Password can't be empty")
        return

    score = evaluate_password(pw)
    percent = int((score / 5) * 100)
    label1["text"] = f"{percent} %"

    update_checklist(pw)
    draw_strength_bar(score)

    # Note: ACCENT_GREEN is imported from theme.py
    if score == 5:
        strong_label["text"] = "✅ Excellent password! Hard to guess and brute-force."
        strong_label.config(fg=ACCENT_GREEN)
    elif 3 <= score < 5:
        strong_label["text"] = "🟡 Fair – improve it using the suggestions below."
        strong_label.config(fg="#facc15")
        suggestion_label["text"] = suggest_improvements(pw)
    else:
        strong_label["text"] = "❌ Weak password. Highly vulnerable to attacks."
        strong_label.config(fg=ACCENT_RED)
        suggestion_label["text"] = suggest_improvements(pw)

def check():
    pw = entry.get()
    update_strength_display(pw, show_warning=True)

def clear_all():
    entry.delete(0, tk.END)
    suggestion_label["text"] = ""
    label1["text"] = ""
    strong_label["text"] = ""
    w.delete("all")
    update_checklist("")

def generate_password():
    length = 12
    pw_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+-=[]{}|;:,.<>/?")
    ]
    remaining = length - len(pw_chars)
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>/?"
    pw_chars.extend(random.choice(all_chars) for _ in range(remaining))
    random.shuffle(pw_chars)
    pw = "".join(pw_chars)

    entry.delete(0, tk.END)
    entry.insert(0, pw)

    window.clipboard_clear()
    window.clipboard_append(pw)
    messagebox.showinfo("Password Generated", "A strong password was generated and copied to your clipboard.")
    update_strength_display(pw)

def on_key_release(event):
    pw = entry.get()
    update_strength_display(pw, show_warning=False)

# ================== BINDINGS ===========================
entry.bind("<KeyRelease>", on_key_release)
check_button.config(command=check)
clear_button.config(command=clear_all)
generate_button.config(command=generate_password)
toggle_button.config(command=toggle_visibility)

# ================== START APP =========================
update_checklist("")  # initialize checklist
window.mainloop()
