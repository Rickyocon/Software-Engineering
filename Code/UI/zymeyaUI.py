# Import the tkinter library
import tkinter as tk

# Function to display the Settings page
def display_settings():
    update_main_frame("Settings will be displayed here")

# Function to display the Scanning options page
def display_scanning():
    switch_to_scan_page()

# Function to display the Options page
def display_options():
    update_main_frame("Options will be configured here")

# Function to display the Quarantine page
def display_quarantine():
    update_main_frame("Quarantine will be managed here")

# Function to display the Home page
def display_home():
    switch_to_home_page()

# Function to switch to the Scanning page
def switch_to_scan_page():
    clear_main_frame()
    scan_page_title = tk.Label(main_frame, text="Scan Options", bg='#202A44', fg='white', font='Helvetica 16 bold')
    scan_page_title.pack(pady=20)
    
    btn_quick_scan = tk.Button(main_frame, text="Quick Scan", command=display_quick_scan_options, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    btn_schedule_scan = tk.Button(main_frame, text="Schedule Scan", command=display_schedule_scan_options, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    btn_custom_scan = tk.Button(main_frame, text="Custom Drive Scan", command=display_custom_scan_options, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
    
    btn_quick_scan.pack(pady=10, padx=10)
    btn_schedule_scan.pack(pady=10, padx=10)
    btn_custom_scan.pack(pady=10, padx=10)

# Function to display the Quick Scan options
def display_quick_scan_options():
    update_main_frame("Quick Scan options will be displayed here")

# Function to display the Schedule Scan options
def display_schedule_scan_options():
    update_main_frame("Schedule Scan options will be displayed here")

# Function to display the Custom Drive Scan options
def display_custom_scan_options():
    update_main_frame("Custom Drive Scan options will be displayed here")

# Function to update the main frame's content
def update_main_frame(content):
    clear_main_frame()
    if content:
        tk.Label(main_frame, text=content, bg='#202A44', fg='white', font='Helvetica 12 bold').pack(pady=20)

# Function to clear the main frame
def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Function to switch to the Home page
def switch_to_home_page():
    clear_main_frame()
    display_home_content()

# Function to display the content on the Home page
def display_home_content():
    logo = tk.PhotoImage(file='zmeya.gif')
    logo_label = tk.Label(main_frame, image=logo, bg='#202A44')
    welcome_label = tk.Label(main_frame, text="Welcome to Zmeya", bg='#202A44', fg='white', font='Helvetica 16 bold')

    logo_label.image = logo  # Keep a reference to prevent garbage collection
    logo_label.pack(pady=(60, 20))
    welcome_label.pack(pady=20)

# Create the main tkinter window
root = tk.Tk()
root.title("Zmeya Anti-Malware")
root.configure(bg='#202A44')

# Create the side frame for navigation buttons
side_frame = tk.Frame(root, bg='#293B5A')
side_frame.pack(side='left', fill='y', padx=(0, 20))

# Create navigation buttons to switch between pages
btn_settings = tk.Button(side_frame, text="Settings", command=display_settings, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_scanning = tk.Button(side_frame, text="Scanning", command=display_scanning, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_options = tk.Button(side_frame, text="Options", command=display_options, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_quarantine = tk.Button(side_frame, text="Quarantine", command=display_quarantine, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')
btn_home = tk.Button(side_frame, text="Home", command=display_home, bg='light blue', width=15, relief='solid', bd=1, highlightbackground='light blue', highlightthickness=10, font='Helvetica 12 bold')

btn_settings.pack(pady=10, padx=10)
btn_scanning.pack(pady=10, padx=10)
btn_options.pack(pady=10, padx=10)
btn_quarantine.pack(pady=10, padx=10)
btn_home.pack(side='bottom', pady=(0, 10), padx=10)

# Create the main content frame
main_frame = tk.Frame(root, bg='#202A44')
main_frame.pack(side='right', expand=True, fill='both')

# Display the Home content at startup
display_home_content()

# Starting the main application loop
root.mainloop()
