import tkinter as tk
from tkinter import ttk
import webbrowser
from urllib.parse import quote_plus

root = tk.Tk()
root.title("Search Launcher")
root.geometry("480x520")
root.resizable(True, True)
root.configure(bg="#eef4f7")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TFrame", background="#eef4f7")
style.configure("Header.TLabel", background="#eef4f7", font=("Segoe UI", 18, "bold"), foreground="#2c3e50")
style.configure("Subtitle.TLabel", background="#eef4f7", font=("Segoe UI", 10), foreground="#34495e")
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=10)
style.configure("TEntry", font=("Segoe UI", 11), padding=6)
style.map("TButton",
          background=[("active", "#3498db"), ("!disabled", "#5dade2")],
          foreground=[("active", "#ffffff")])

main_frame = ttk.Frame(root, padding=(20, 20, 20, 20))
main_frame.pack(fill="both", expand=True)

header = ttk.Label(main_frame, text="Search Anywhere", style="Header.TLabel")
header.pack(pady=(0, 8))
subheading = ttk.Label(main_frame, text="Type a keyword or username and choose a platform.", style="Subtitle.TLabel")
subheading.pack(pady=(0, 18))

entry_var = tk.StringVar()
entry = ttk.Entry(main_frame, textvariable=entry_var, width=40)
entry.pack(pady=(0, 16))
entry.focus()

status_var = tk.StringVar(value="Ready")
status_label = ttk.Label(main_frame, textvariable=status_var, style="Subtitle.TLabel")
status_label.pack(pady=(0, 12))

button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=(0, 8))

platforms = [
    ("Google", "https://www.google.com/search?q={}"),
    ("YouTube", "https://www.youtube.com/results?search_query={}"),
    ("Instagram", "https://www.instagram.com/{}/"),
    ("Facebook", "https://www.facebook.com/{}/"),
    ("TikTok", "https://www.tiktok.com/@{}"),
    ("LinkedIn", "https://www.linkedin.com/search/results/all/?keywords={}"),
    ("GitHub", "https://github.com/{}/"),
    ("Twitter", "https://twitter.com/{}/"),
]

def open_search(platform_name: str, url_template: str):
    query = entry_var.get().strip()
    if not query:
        status_var.set("Enter a search term or username first.")
        return
    encoded = quote_plus(query)
    webbrowser.open(url_template.format(encoded))
    status_var.set(f"Opened {platform_name} for '{query}'.")


def open_all():
    query = entry_var.get().strip()
    if not query:
        status_var.set("Enter a search term or username first.")
        return
    encoded = quote_plus(query)
    for name, template in platforms:
        webbrowser.open(template.format(encoded))
    status_var.set(f"Opened all platforms for '{query}'.")
    entry_var.set("")  # Clear the entry after opening all

for index, (name, template) in enumerate(platforms):
    button = ttk.Button(button_frame, text=name, command=lambda n=name, t=template: open_search(n, t))
    button.grid(row=index // 2, column=index % 2, sticky="ew", padx=6, pady=6)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

bottom_frame = ttk.Frame(main_frame)
bottom_frame.pack(fill="x", pady=(10, 0))

open_all_button = ttk.Button(bottom_frame, text="Open All", command=open_all)
open_all_button.pack(fill="x", pady=(0, 8))

exit_button = ttk.Button(bottom_frame, text="Exit", command=root.destroy)
exit_button.pack(fill="x")

root.bind("<Return>", lambda event: open_search("Google", "https://www.google.com/search?q={}"))

root.mainloop()
