#!/usr/local/bin/python3

import time
import tkinter
import tkinter.messagebox
import locale
import datetime
import guikit


root = tkinter.Tk()
root.geometry('1100x550')
root.title('CVGUI')
intro = tkinter.Label(root, text = "CVGUI\n", font = 'Verdana 18 bold').grid(row = 0, column=0, sticky="w", padx=5)

menubar = tkinter.Menu(root)
root.config(menu = menubar)
option_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="About", command=lambda: tkinter.messagebox.showinfo("About", "about"))
option_menu.add_separator()
option_menu.add_command(label="Read File")#, command=NewFile)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)

input_label = tkinter.Label(root, text = "Enter message here:", font = "Verdana 12 bold").grid(row = 2, column=0, sticky="w", padx=5)
input_box = tkinter.Text(root, height=20, width=40, font="Verdana 13", wrap="word", padx=5, highlightbackground="black", highlightthickness=1)
input_box.grid(row=3, column=0, padx=10, pady=10)

below_input_frame = tkinter.Frame(root)
encrypt_button = tkinter.Button(below_input_frame, text="ENCRYPT", width=18, command=lambda: guikit.encryption(input_box, key_entry1, output_box, alphabet_index, runtime_label)).grid(row=0, column=0, sticky="w")
decrypt_button = tkinter.Button(below_input_frame, text="DECRYPT", width=18, command=root.destroy).grid(row=0, column=1, sticky="w")
below_input_frame.grid(row=4, column=0)

output_label = tkinter.Label(root, text = "Result appears here:", font = "Verdana 12 bold").grid(row = 2, column=1, sticky="w", padx=5)
output_box = tkinter.Text(root, height=20, width=40, state="disabled", font = "Verdana 13", wrap="word", padx=5, highlightbackground="black", highlightthickness=1)
output_box.grid(row = 3, column = 1, padx=10, pady=10)

below_output_frame = tkinter.Frame(root)
runtime_label = tkinter.Label(below_output_frame, text = "runtime information appears here", font = "Verdana 12 italic", width=35, anchor="w")
runtime_label.grid(row=0, column=0, sticky="we", padx=5)   # force-set width because copy button won't stick to the right side; anchor w aligns label text to the left
copy_output = tkinter.Button(below_output_frame, text="COPY OUTPUT", command=root.destroy).grid(row=0, column=1, sticky="e")
below_output_frame.grid(row=4, column=1, sticky="w")    # sticky w attaches the frame & runtime info to the left edge below the output box

alph_key_frame = tkinter.Frame(root)
alphabet_label = tkinter.Label(alph_key_frame, text="Alphabet selection:", font = "Verdana 12 bold").grid(row=0, column=0, sticky="w", padx=5)
alphabet_index = tkinter.IntVar()   # use this index later to determine which alphabet to use
std85 = tkinter.Radiobutton(alph_key_frame, text="std85(DE/EN)", variable=alphabet_index, value=1)
std85.grid(row=1, column=0, sticky="w", padx=5, pady=(5,0))    # pady 5 between alphabet label and first alphabet button
std85.select()  # default alphabet, therefore can only be grided afterwards
std137 = tkinter.Radiobutton(alph_key_frame, text="std137(DA/DE/EN/ES/FR/IT/NO/SV)", variable=alphabet_index, value=2).grid(row=2, column=0, sticky="w", padx=5)
zh_shuffled = tkinter.Radiobutton(alph_key_frame, text="Chinese(ZH_CN/ZH_TW)", variable=alphabet_index, value=3).grid(row=3, column=0, sticky="w", padx=5)
cyrillic111 = tkinter.Radiobutton(alph_key_frame, text="Cyrillic(BE/KK/MK/MN/RU/SR/UK)", variable=alphabet_index, value=4).grid(row=4, column=0, sticky="w", padx=5)

# padx creates more space between the output box and the button list
# pady extends the spacing in between the radio buttons

cipher_key_label_frame = tkinter.Frame(alph_key_frame)
key_label1 = tkinter.Label(cipher_key_label_frame, text="Cipher key:", font = "Verdana 12 bold", width=25, anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=(10,0))  # pady 10 between key-label-1 and last alphabet button
auto_key_1 = tkinter.Button(cipher_key_label_frame, text="Generate", command=lambda: guikit.auto_key(key_entry1)).grid(row=0, column=1, sticky="e", padx=5, pady=(10,0))   # pady 10 between generate-key and last alphabet button, lambda allows parameters in command function
cipher_key_label_frame.grid(row=5, column=0, sticky="we")

key_entry1 = tkinter.Entry(alph_key_frame, width=32)
key_entry1.grid(row=6, column=0, sticky="w", padx=5)
# widths of two entry boxes and key labels must be adjusted to help align auto-gen buttons in the same row

two_step_cryp_label = tkinter.Label(alph_key_frame, text="Use two-step encryption:", font = "Verdana 12 bold").grid(row=7, column=0, sticky="w", padx=5, pady=(15,0))    # pady 15 between two-step-cryp label and entry box above (should be 10 but not far enough)
two_step_cryp_var = tkinter.IntVar()   # 1 = enabled, 2 = disabled
enable_2s_cryp = tkinter.Radiobutton(alph_key_frame, text="enabled", variable=two_step_cryp_var, value=1, command=lambda: guikit.enable_alphabet_key(key_entry2, auto_key_2))
enable_2s_cryp.grid(row=8, column=0, sticky="w", padx=5, pady=(5,0))    # pady 5 between 2-step label and first button
disable_2s_cryp = tkinter.Radiobutton(alph_key_frame, text="disabled", variable=two_step_cryp_var, value=2, command=lambda: guikit.disable_alphabet_key(key_entry2, auto_key_2))
disable_2s_cryp.grid(row=9, column=0, sticky="w", padx=5)
disable_2s_cryp.select() # default disable 2-step cryp

alpha_key_label_frame = tkinter.Frame(alph_key_frame)
key_label2 = tkinter.Label(alpha_key_label_frame, text="Alphabet key:", font = "Verdana 12 bold", width=25, anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=(10,0))  # pady pushes the label down a line from the radio buttons
auto_key_2 = tkinter.Button(alpha_key_label_frame, text="Generate", command=lambda: guikit.auto_key(key_entry2))
auto_key_2.config(state="disabled")
auto_key_2.grid(row=0, column=1, sticky="e", padx=5, pady=(10,0))
alpha_key_label_frame.grid(row=10, column=0, sticky="we") # pady tuple adds only padding on top

key_entry2 = tkinter.Entry(alph_key_frame, width=32)
key_entry2.grid(row=11, column=0, sticky="w", padx=5)
key_entry2.insert(0, "enable 2-step encryption to enter")
key_entry2["state"] = "disabled"

alph_key_frame.grid(row=2, rowspan=2, column=2, sticky="n") # frame starts from row 2 (parallel to input/output labels)
                                                            # row span covers input/output labels and boxes

# activate_if_necessary = tkinter.Entry(root, width=32).grid(row=4, column=2)

root.mainloop()
