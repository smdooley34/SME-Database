########################################################################################################################
# main.py
#
# Serves as the main entrypoint for the application. This consists of a Tkinter window that displays the main
# application.
#
# @see https://docs.python.org/3/library/tkinter.html
########################################################################################################################

import tkinter as tk
import json

if __name__ == '__main__':
    # Opens JSON File To Bring In Data (Mock Data, For Now, With Attributes That May Or May Not Really Be Useful)
    file_handle = open('mocks/subject-matter-experts.json')

    # Returns JSON Object As A Dictionary
    subject_matter_experts = json.load(file_handle)

    file_handle.close()

    # Root Window GUI
    main_window = tk.Tk()

    main_window.geometry('500x500')
    main_window.resizable(0, 0)
    main_window.title('SME Database')

    tk.Label(main_window, font=('Arial', 25), text='The SME Database').pack(pady=20)

    search_box = tk.Entry(main_window)
    search_box.insert(0, 'Search SMEs, Topics Of Interest, etc...') # Placeholder Text
    search_box.pack(fill='x', padx=20)

    tk.Label(main_window, font=('Arial', 25), text='Results').pack(pady=20)

    for subject_matter_expert in subject_matter_experts:
        tk.Label(main_window, font=('Arial', 14), text=subject_matter_expert['name']).pack(pady=5)

    # This Starts An Infinite Loop That Is The Main Window (Infinite Meaning The Program/Window Waits For User Interaction)
    tk.mainloop()
