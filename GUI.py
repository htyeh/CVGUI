#!/usr/local/bin/python3

import time
import tkinter
import tkinter.messagebox
import locale
import datetime

def newEntry():
    if english['state'] == 'disabled':
        locale.setlocale(locale.LC_TIME, 'en_US')
        inputWindow = tkinter.Tk()
        inputWindow.title('NEW ENTRY')
        newEntryLabel = tkinter.Label(inputWindow, text = 'Put in a New Entry\n', font = 'Verdana 14 bold')
        newEntryLabel.grid(row = 0, columnspan = 2)
        name = tkinter.Label(inputWindow, text = 'Name of the language: ').grid(row = 1, column = 0, sticky = 'e')
        nameEntry = tkinter.Entry(inputWindow)
        nameEntry.grid(row = 1, column = 1)
        code = tkinter.Label(inputWindow, text = 'Language code (or leave empty): ').grid(row = 2, column = 0, sticky = 'e')
        codeEntry = tkinter.Entry(inputWindow)
        codeEntry.grid(row = 2, column = 1)
        numCases = tkinter.Label(inputWindow, text = 'Number of cases: ').grid(row = 3, column = 0, sticky = 'e')
        numCasesEntry = tkinter.Entry(inputWindow)
        numCasesEntry.grid(row = 3, column = 1)
        numSpeakers = tkinter.Label(inputWindow, text = 'Number of speakers in millions: ').grid(row = 4, column = 0, sticky = 'e')
        numSpeakersEntry = tkinter.Entry(inputWindow)
        numSpeakersEntry.grid(row = 4, column = 1)
        emptyLine = tkinter.Label(inputWindow).grid(row = 5)

        def confirmNewEntry():
            allErrorMessages = ''
            getName = nameEntry.get().strip().title()
            if getName == '':
                allErrorMessages += 'Please enter the name of the language\n\n'
            validCode = True
            getCode = codeEntry.get().strip()
            accepted_length = [0,2,3]
            if len(getCode) not in accepted_length or (not getCode.isalpha() and len(getCode) != 0):
                allErrorMessages += 'Please enter a valid 2-3 character lang code or leave it empty\n\n'
                validCode = False
            if getCode:
                getCode = '[' + getCode.upper() + ']'
            getNumCases = numCasesEntry.get().strip()
            if not getNumCases.isdigit():
                allErrorMessages += 'Please enter a number for number of cases\n\n'
            getNumSpeakers = numSpeakersEntry.get().strip()
            invalidNumSpeakers = True
            if invalidNumSpeakers:
                try:
                    float(getNumSpeakers)
                    invalidNumSpeakers = False
                except ValueError:
                    allErrorMessages += 'Please enter a number for number of speakers\n\n'
            if getName and getNumCases and getNumSpeakers and validCode:
                if float(getNumSpeakers) < 1000:
                    reviewMessage = 'Review: The language ' + getName + getCode + ' has ' + getNumCases + ' cases and ' + getNumSpeakers + ' million speakers.'
                else:
                    reviewMessage = 'Review: The language ' + getName + getCode + ' has ' + getNumCases + ' cases and ' + str(float(getNumSpeakers)/1000) + ' billion speakers.'
                confirmWrite = tkinter.messagebox.askquestion('Confirm', reviewMessage + '\n\nAdd this entry?')
                if confirmWrite == 'yes':
                    with open('LangSystem.txt', 'a') as langFile:
                        if float(getNumSpeakers) < 1000:
                            langFile.write('The language ' + getName + getCode + ' has ' + getNumCases + ' cases and ' + getNumSpeakers + ' million speakers.\n')
                        else:
                            langFile.write('The language ' + getName + getCode + ' has ' + getNumCases + ' cases and ' + str(float(getNumSpeakers)/1000) + ' billion speakers.\n')
                    with open('LangRecord.txt', 'a') as langRecord:
                        langRecord.write('You added language "' + getName + '" on ' + str(datetime.datetime.now().strftime('%a, %x, %X')) + '\n')
                    nameEntry.delete(0, 'end')
                    codeEntry.delete(0, 'end')
                    numCasesEntry.delete(0, 'end')
                    numSpeakersEntry.delete(0, 'end')
            else:
                tkinter.messagebox.showinfo('', allErrorMessages)

        cancel = tkinter.Button(inputWindow, text = 'Cancel', command = inputWindow.destroy).grid(row = 6, column = 0)
        confirm = tkinter.Button(inputWindow, text = 'Confirm', command = confirmNewEntry).grid(row = 6, column = 1)
        inputWindow.mainloop()


#option2: display existing entries
def displayEntries():
    if english['state'] == 'disabled':
        with open('LangSystem.txt', 'r') as langFile:
            entries = langFile.read()
            tkinter.messagebox.showinfo('Existing Entries', entries)

#option3: delete all entries
def deleteEntries():
    if english['state'] == 'disabled':
        locale.setlocale(locale.LC_TIME, 'en_US')
        confirm = tkinter.messagebox.askquestion('Please Confirm', 'Are you sure to delete all entries? This cannot be undone.')
        if confirm == 'yes':
            langFile = open('LangSystem.txt', 'w')
            langFile.close()
            langRecord = open('LangRecord.txt', 'a')
            langRecord.write('You deleted all entries on ' + str(datetime.datetime.now().strftime('%a, %x, %X')) + '\n')
            langRecord.close()

#option4: display record of added entries
def displayRecords():
    if english['state'] == 'disabled':
        with open('LangRecord.txt') as langRecord:
            records = langRecord.read()
            tkinter.messagebox.showinfo('Record of Added Entries', records)

#option5: about
def about():
    tkinter.messagebox.showinfo('About', 'CaeVige(GUI) en-/decrypter')

##############################################################################

root = tkinter.Tk()
root.geometry('1100x550')
root.title('CVGUI')
intro = tkinter.Label(root, text = "CVGUI\n", font = 'Verdana 18 bold').grid(row = 0, column=0, sticky="w", padx=5)

menubar = tkinter.Menu(root)
root.config(menu = menubar)
option_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="From File")#, command=NewFile)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)

input_label = tkinter.Label(root, text = "Enter message here:", font = "Verdana 12 bold").grid(row = 2, column=0, sticky="w", padx=5)
input_box = tkinter.Text(root, height=20, width=40, font="Verdana 13", wrap="word", padx=5, highlightbackground="black", highlightthickness=1).grid(row=3, column=0, padx=10, pady=10)

below_input_frame = tkinter.Frame(root)
encrypt_button = tkinter.Button(below_input_frame, text="ENCRYPT", width=18, command=root.destroy).grid(row=0, column=0, sticky="w")
decrypt_button = tkinter.Button(below_input_frame, text="DECRYPT", width=18, command=root.destroy).grid(row=0, column=1, sticky="w")
below_input_frame.grid(row=4, column=0)

output_label = tkinter.Label(root, text = "Result appears here:", font = "Verdana 12 bold").grid(row = 2, column=1, sticky="w", padx=5)
output_box = tkinter.Text(root, height=20, width=40, state="disabled", font = "Verdana 13", wrap="word", padx=5, highlightbackground="black", highlightthickness=1).grid(row = 3, column = 1, padx=10, pady=10)

below_output_frame = tkinter.Frame(root)
runtime_label = tkinter.Label(below_output_frame, text = "runtime information appears here", font = "Verdana 12 italic", width=35, anchor="w").grid(row=0, column=0, sticky="we", padx=5)   # force-set width because copy button won't stick to the right side; anchor w aligns label text to the left
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
auto_key_1 = tkinter.Button(cipher_key_label_frame, text="Generate", command=root.destroy).grid(row=0, column=1, sticky="e", padx=5, pady=(10,0))   # pady 10 between generate-key and last alphabet button
cipher_key_label_frame.grid(row=5, column=0, sticky="we")

key_entry1 = tkinter.Entry(alph_key_frame, width=32).grid(row=6, column=0, sticky="w", padx=5)
# widths of two entry boxes and key labels must be adjusted to help align auto-gen buttons in the same row

two_step_cryp_label = tkinter.Label(alph_key_frame, text="Use two-step encryption:", font = "Verdana 12 bold").grid(row=7, column=0, sticky="w", padx=5, pady=(15,0))    # pady 15 between two-step-cryp label and entry box above (should be 10 but not far enough)
two_step_cryp_var = tkinter.IntVar()   # 1 = enabled, 2 = disabled
enable_2s_cryp = tkinter.Radiobutton(alph_key_frame, text="enabled", variable=two_step_cryp_var, value=1, command=lambda: key_entry2.config(state="normal"))
enable_2s_cryp.grid(row=8, column=0, sticky="w", padx=5, pady=(5,0))    # pady 5 between 2-step label and first button
disable_2s_cryp = tkinter.Radiobutton(alph_key_frame, text="disabled", variable=two_step_cryp_var, value=2, command=lambda: key_entry2.config(state="disabled"))
disable_2s_cryp.grid(row=9, column=0, sticky="w", padx=5)
disable_2s_cryp.select() # default disable 2-step cryp

alpha_key_label_frame = tkinter.Frame(alph_key_frame)
key_label2 = tkinter.Label(alpha_key_label_frame, text="Alphabet key:", font = "Verdana 12 bold", width=25, anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=(10,0))  # pady pushes the label down a line from the radio buttons
auto_key_2 = tkinter.Button(alpha_key_label_frame, text="Generate", command=root.destroy).grid(row=0, column=1, sticky="e", padx=5, pady=(10,0))
alpha_key_label_frame.grid(row=10, column=0, sticky="we") # pady tuple adds only padding on top

key_entry2 = tkinter.Entry(alph_key_frame, width=32)
key_entry2.grid(row=11, column=0, sticky="w", padx=5)
key_entry2.insert(0, "enable 2-step encryption to enter")
key_entry2["state"] = "disabled"

alph_key_frame.grid(row=2, rowspan=2, column=2, sticky="n") # frame starts from row 2 (parallel to input/output labels)
                                                            # row span covers input/output labels and boxes

# activate_if_necessary = tkinter.Entry(root, width=32).grid(row=4, column=2)

root.mainloop()
