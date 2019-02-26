# -*- coding: utf-8 -*-

import sys
import random
import time

def testfunc(var):
    print(var.get())
    print(type(var.get()))

def auto_key(key_entry):
    key_entry.delete(0, "end")
    insert_string = ""
    for i in range(6):
        insert_string += str(random.randint(1, 9)) + " "
    key_entry.insert(0, insert_string)

def enable_alphabet_key(entry_to_activate, button_to_activate):
    entry_to_activate.config(state="normal")
    button_to_activate.config(state="normal")

def disable_alphabet_key(entry_to_dactivate, button_to_dactivate):
    entry_to_dactivate.config(state="disabled")
    button_to_dactivate.config(state="disabled")

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

    start_time = time.time()

    original_msg = input_box.get("1.0", "end")
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

    if key_entry2["state"] != "disabled" and key_entry2.get() != "":
        alphabet_key = [int(i) for i in key_entry2.get().split()]
        alphabet = encipher_key(alphabet, alphabet_key)

    encrypted_msg = encipher_key(original_msg, key)

    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", encrypted_msg)
    end_time = time.time()
    runtime_label["text"] = str(len(original_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."



# def decryption(input_box, key_entry, output_box, alphabet_index, runtime_label):
#     start_time = time.time()
#
#     encrypted_msg = input_box.get("1.0", "end")
#     key = [int(i) for i in key_entry.get().split()]
#     if key == []:
#         output_box.config(state="normal")
#         output_box.delete("1.0", "end")
#         output_box.insert("1.0", encrypted_msg)
#         end_time = time.time()
#         runtime_label["text"] = str(len(encrypted_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."
#         return 0
#
#     if alphabet_index.get() == 1:
#         alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
#     elif alphabet_index.get() == 2:
#         alphabet = "abcdefghijklmnñopqrstuvwxyzäöüßáàâéèêëíîïóôúùûçœæøåABCDEFGHIJKLMNÑOPQRSTUVWXYZÄÖÜÁÀÂÉÈÊËÍÎÏÓÔÚÙÛÇŒÆØÅ !\"$%&'()*+,-./:;<=>?@[\]_0123456789"
#     elif alphabet_index.get() == 3:
#         with open("alphabets/zh_shuffled.txt") as zh_alphabet:
#             alphabet = zh_alphabet.read()
#     elif alphabet_index.get() == 4:
#         alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІЎЃЅЈЉЊЌЏЂЋЄЇҐҒҚҢҮҰҺӘӨабвгдеёжзийклмнопрстуфхцчшщъыьэюяіўѓѕјљњќџђћʼєїґғқңүұһәө !\"$%&'()*+,-./:;<=>?@[\]_"
#
#     def encipher(string, n):
#         res = ""
#         for ltr in string:
#             if ltr in alphabet:
#                 encipher_index = alphabet.find(ltr)+n
#                 if encipher_index >= len(alphabet):
#                     res += alphabet[encipher_index-len(alphabet)]
#                 else:
#                     res += alphabet[encipher_index]
#             else:
#                 res += ltr
#         return res
#     def encipher_key(string, key):
#         if len(string) <= len(key):
#             return "".join([enciphered for enciphered in map(encipher,string,key)])
#         else:
#             str_segs = sublist(string, len(key))
#             res = ""
#             for string in str_segs:
#                 res += "".join([enciphered for enciphered in map(encipher,string,key)])
#             return res
#
#     decrypted_msg = encipher_key(encrypted_msg, key)
#
#     output_box.config(state="normal")
#     output_box.delete("1.0", "end")
#     output_box.insert("1.0", decrypted_msg)
#     end_time = time.time()
#     runtime_label["text"] = str(len(encrypted_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."


def sublist(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]



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
