# -*- coding: utf-8 -*-

import sys
import random
import time
import tkinter.filedialog
import tkinter.messagebox
import pyperclip

def auto_key(key_entry):
    key_entry.delete(0, "end")
    key_entry.insert(0, " ".join([str(random.randint(1,9)) for i in range(6)]))

def enable_alphabet_key(entry_to_activate, button_to_activate):
    entry_to_activate.config(state="normal")
    entry_to_activate.delete(0, "end")
    button_to_activate.config(state="normal")

def disable_alphabet_key(entry_to_deactivate, button_to_deactivate):
    entry_to_deactivate.delete(0, "end")
    entry_to_deactivate.insert(0, "enable 2-step encryption to enter")
    entry_to_deactivate.config(state="disabled")
    button_to_deactivate.config(state="disabled")

def encryption(input_box, key_entry1, key_entry2, output_box, alphabet_index, runtime_label):
    def encipher(string, n):
        res = ""
        for ltr in string:
            if ltr in alphabet:
                encipher_index = alphabet.find(ltr)+n
                if encipher_index >= len(alphabet):
                    res += alphabet[encipher_index-len(alphabet)]
                else:
                    res += alphabet[encipher_index]
            else:
                res += ltr
        return res
    def encipher_key(string, key):
        if len(string) <= len(key):
            return "".join([enciphered for enciphered in map(encipher,string,key)])
        else:
            str_segs = sublist(string, len(key))
            res = ""
            for string in str_segs:
                res += "".join([enciphered for enciphered in map(encipher,string,key)])
            return res

# key error handling
    try:
        int("".join(key_entry1.get().split()))
    except ValueError:
        tkinter.messagebox.showinfo("", "Key error!")
        return 0
# key error handling

    start_time = time.time()

    original_msg = input_box.get("1.0", "end").strip()
    key = [int(i) for i in key_entry1.get().split()]

    if key == []:
        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", original_msg)
        end_time = time.time()
        runtime_label["text"] = str(len(original_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."
        return 0

    if alphabet_index.get() == 1:
        alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
    elif alphabet_index.get() == 2:
        alphabet = "abcdefghijklmnñopqrstuvwxyzäöüßáàâéèêëíîïóôúùûçœæøåABCDEFGHIJKLMNÑOPQRSTUVWXYZÄÖÜÁÀÂÉÈÊËÍÎÏÓÔÚÙÛÇŒÆØÅ !\"$%&'()*+,-./:;<=>?@[\]_0123456789"
    elif alphabet_index.get() == 3:
        with open("alphabets/zh_shuffled.txt") as zh_alphabet:
            alphabet = zh_alphabet.read()
    elif alphabet_index.get() == 4:
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІЎЃЅЈЉЊЌЏЂЋЄЇҐҒҚҢҮҰҺӘӨабвгдеёжзийклмнопрстуфхцчшщъыьэюяіўѓѕјљњќџђћʼєїґғқңүұһәө !\"$%&'()*+,-./:;<=>?@[\]_"

    encrypted_msg = encipher_key(original_msg, key)
    if key_entry2["state"] != "disabled" and key_entry2.get() != "":
        second_key = [int(i) for i in key_entry2.get().split()]
        encrypted_msg = encipher_key(encrypted_msg, second_key)

    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", encrypted_msg)
    end_time = time.time()
    runtime_label["text"] = str(len(original_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."

def decryption(input_box, key_entry1, key_entry2, output_box, alphabet_index, runtime_label):
    def decipher(string, n):
        res = ""
        for ltr in string:
            if ltr in alphabet:
                decipher_index = alphabet.find(ltr)-n
                if decipher_index < 0:
                    res += alphabet[decipher_index+len(alphabet)]
                else:
                    res += alphabet[decipher_index]
            else:
                res += ltr
        return res
    def decipher_key(string, key):
        if len(string) <= len(key):
            return "".join([deciphered for deciphered in map(decipher,string,key)])
        else:
            str_segs = sublist(string, len(key))
            res = ""
            for string in str_segs:
                res += "".join([deciphered for deciphered in map(decipher,string,key)])
            return res

# key error handling
    try:
        int("".join(key_entry1.get().split()))
    except ValueError:
        tkinter.messagebox.showinfo("", "Key error!")
        return 0
# key error handling

    start_time = time.time()

    encrypted_msg = input_box.get("1.0", "end").strip()
    key = [int(i) for i in key_entry1.get().split()]
    if key == []:
        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", encrypted_msg)
        end_time = time.time()
        runtime_label["text"] = str(len(encrypted_msg)) + " char(s) decrypted in " + str(round(end_time-start_time, 2)) + " second(s)."
        return 0

    if alphabet_index.get() == 1:
        alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
    elif alphabet_index.get() == 2:
        alphabet = "abcdefghijklmnñopqrstuvwxyzäöüßáàâéèêëíîïóôúùûçœæøåABCDEFGHIJKLMNÑOPQRSTUVWXYZÄÖÜÁÀÂÉÈÊËÍÎÏÓÔÚÙÛÇŒÆØÅ !\"$%&'()*+,-./:;<=>?@[\]_0123456789"
    elif alphabet_index.get() == 3:
        with open("alphabets/zh_shuffled.txt") as zh_alphabet:
            alphabet = zh_alphabet.read()
    elif alphabet_index.get() == 4:
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІЎЃЅЈЉЊЌЏЂЋЄЇҐҒҚҢҮҰҺӘӨабвгдеёжзийклмнопрстуфхцчшщъыьэюяіўѓѕјљњќџђћʼєїґғқңүұһәө !\"$%&'()*+,-./:;<=>?@[\]_"

    if key_entry2["state"] != "disabled" and key_entry2.get() != "":
        second_key = [int(i) for i in key_entry2.get().split()]
        decrypted_msg = decipher_key(encrypted_msg, second_key)
        decrypted_msg = decipher_key(decrypted_msg, key)
    else:
        decrypted_msg = decipher_key(encrypted_msg, key)

    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", decrypted_msg)
    end_time = time.time()
    runtime_label["text"] = str(len(decrypted_msg)) + " char(s) decrypted in " + str(round(end_time-start_time, 2)) + " second(s)."

def sublist(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]

def copy_output(output_box):
    pyperclip.copy(output_box.get("1.0", "end"))

def open_file(input_box):
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("text files", ".txt")])
    if not file_path:
        tkinter.messagebox.showinfo("", "No file chosen.")
        return 0
    with open(file_path) as file:
        input_box.delete("1.0", "end")
        input_box.insert("1.0", file.read().strip())
    # if not filename.endswith('.txt'):

def enc_file(key_entry1, key_entry2, alphabet_index, runtime_label):
    tkinter.messagebox.showinfo("", "Translated file will end in .cv.txt and will be in the same directory as the original file.")
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("text files", ".txt")])
    if not file_path:
        tkinter.messagebox.showinfo("", "No file chosen.")
        return 0

    def encipher(string, n):
        res = ""
        for ltr in string:
            if ltr in alphabet:
                encipher_index = alphabet.find(ltr)+n
                if encipher_index >= len(alphabet):
                    res += alphabet[encipher_index-len(alphabet)]
                else:
                    res += alphabet[encipher_index]
            else:
                res += ltr
        return res
    def encipher_key(string, key):
        if len(string) <= len(key):
            return "".join([enciphered for enciphered in map(encipher,string,key)])
        else:
            str_segs = sublist(string, len(key))
            res = ""
            for string in str_segs:
                res += "".join([enciphered for enciphered in map(encipher,string,key)])
            return res

    start_time = time.time()

    with open(file_path) as file:
        original_msg = file.read().strip()
    key = [int(i) for i in key_entry1.get().split()]
    if key == []:
        tkinter.messagebox.showinfo("", "Not encrypted, key empty.")
        return 0

    if alphabet_index.get() == 1:
        alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
    elif alphabet_index.get() == 2:
        alphabet = "abcdefghijklmnñopqrstuvwxyzäöüßáàâéèêëíîïóôúùûçœæøåABCDEFGHIJKLMNÑOPQRSTUVWXYZÄÖÜÁÀÂÉÈÊËÍÎÏÓÔÚÙÛÇŒÆØÅ !\"$%&'()*+,-./:;<=>?@[\]_0123456789"
    elif alphabet_index.get() == 3:
        with open("alphabets/zh_shuffled.txt") as zh_alphabet:
            alphabet = zh_alphabet.read()
    elif alphabet_index.get() == 4:
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІЎЃЅЈЉЊЌЏЂЋЄЇҐҒҚҢҮҰҺӘӨабвгдеёжзийклмнопрстуфхцчшщъыьэюяіўѓѕјљњќџђћʼєїґғқңүұһәө !\"$%&'()*+,-./:;<=>?@[\]_"

    encrypted_msg = encipher_key(original_msg, key)
    if key_entry2["state"] != "disabled" and key_entry2.get() != "":
        second_key = [int(i) for i in key_entry2.get().split()]
        encrypted_msg = encipher_key(encrypted_msg, second_key)

    output_filepath = file_path[:-4] + ".cv.txt"
    with open(output_filepath, "w") as output_file:
        output_file.write(encrypted_msg)

    end_time = time.time()
    msg = str(len(original_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."
    tkinter.messagebox.showinfo("", msg)



def dec_file(key_entry1, key_entry2, alphabet_index, runtime_label):
    tkinter.messagebox.showinfo("", "Translated file will end in .txt and will be in the same directory as the original file.")
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("cv files", ".txt")])
    if not file_path:
        tkinter.messagebox.showinfo("", "No file chosen.")
        return 0

    def decipher(string, n):
        res = ""
        for ltr in string:
            if ltr in alphabet:
                decipher_index = alphabet.find(ltr)-n
                if decipher_index < 0:
                    res += alphabet[decipher_index+len(alphabet)]
                else:
                    res += alphabet[decipher_index]
            else:
                res += ltr
        return res
    def decipher_key(string, key):
        if len(string) <= len(key):
            return "".join([deciphered for deciphered in map(decipher,string,key)])
        else:
            str_segs = sublist(string, len(key))
            res = ""
            for string in str_segs:
                res += "".join([deciphered for deciphered in map(decipher,string,key)])
            return res

    start_time = time.time()

    with open(file_path) as file:
        original_msg = file.read().strip()
    key = [int(i) for i in key_entry1.get().split()]
    if key == []:
        tkinter.messagebox.showinfo("", "Not decrypted, key empty.")
        return 0

    if alphabet_index.get() == 1:
        alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
    elif alphabet_index.get() == 2:
        alphabet = "abcdefghijklmnñopqrstuvwxyzäöüßáàâéèêëíîïóôúùûçœæøåABCDEFGHIJKLMNÑOPQRSTUVWXYZÄÖÜÁÀÂÉÈÊËÍÎÏÓÔÚÙÛÇŒÆØÅ !\"$%&'()*+,-./:;<=>?@[\]_0123456789"
    elif alphabet_index.get() == 3:
        with open("alphabets/zh_shuffled.txt") as zh_alphabet:
            alphabet = zh_alphabet.read()
    elif alphabet_index.get() == 4:
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІЎЃЅЈЉЊЌЏЂЋЄЇҐҒҚҢҮҰҺӘӨабвгдеёжзийклмнопрстуфхцчшщъыьэюяіўѓѕјљњќџђћʼєїґғқңүұһәө !\"$%&'()*+,-./:;<=>?@[\]_"

    decrypted_msg = decipher_key(original_msg, key)
    if key_entry2["state"] != "disabled" and key_entry2.get() != "":
        second_key = [int(i) for i in key_entry2.get().split()]
        decrypted_msg = decipher_key(decrypted_msg, second_key)

    output_filepath = file_path[:-7] + ".txt"
    with open(output_filepath, "w") as output_file:
        output_file.write(decrypted_msg)

    end_time = time.time()
    msg = str(len(original_msg)) + " char(s) decrypted in " + str(round(end_time-start_time, 2)) + " second(s)."
    tkinter.messagebox.showinfo("", msg)

def hide_keys(key_entry1, key_entry2):
    if key_entry1["show"] != "*":
        key_entry1.config(show="*")
        if key_entry2["state"] != "disabled" and key_entry2.get() != "":
            key_entry2.config(show="*")
    else:
        key_entry1.config(show="")
        if key_entry2["state"] != "disabled" and key_entry2.get() != "":
            key_entry2.config(show="")
