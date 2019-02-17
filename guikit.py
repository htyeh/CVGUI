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

def encryption(input_box, key_entry, output_box, alphabet_index, runtime_label):
    start_time = time.time()

    encrypted_msg = input_box.get("1.0", "end")
    key = [int(i) for i in key_entry.get().split()]
    if key == []:
        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", encrypted_msg)
        end_time = time.time()
        runtime_label["text"] = str(len(encrypted_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."
        return 0

    if alphabet_index.get() == 1:
        decrypted_msg = la85encipher_key(encrypted_msg, key)
    elif alphabet_index.get() == 2:
        decrypted_msg = la137encipher_key(encrypted_msg, key)
    elif alphabet_index.get() == 3:
        decrypted_msg = zh_encipher_key(encrypted_msg, key)
    elif alphabet_index.get() == 4:
        decrypted_msg = cy111encipher_key(encrypted_msg, key)
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", decrypted_msg)
    end_time = time.time()
    runtime_label["text"] = str(len(encrypted_msg)) + " char(s) encrypted in " + str(round(end_time-start_time, 2)) + " second(s)."

    # handle 2-step cryp


def sublist(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]

### explaination for separate encipher/decipher functions instead of sole alphabet change: unsolved error when mapping alphabet into the parameter list ###

def la85encipher(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
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

def la85decipher(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ !\"$%&'()*+,-./:;<=>?@[\]_"
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


def la85encipher_key(string, key):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(la85encipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(la85encipher,string,key)])
        return res

def la85decipher_key(string, key):
    if len(string) <= len(key):
        return "".join([deciphered for deciphered in map(la85decipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([deciphered for deciphered in map(la85decipher,string,key)])
        return res

def la137encipher(string, n):
    alphabet = "abcdefghijklmnñopqrstuvwxyzäöüßáàâéèêëíîïóôúùûçœæøåABCDEFGHIJKLMNÑOPQRSTUVWXYZÄÖÜÁÀÂÉÈÊËÍÎÏÓÔÚÙÛÇŒÆØÅ !\"$%&'()*+,-./:;<=>?@[\]_0123456789"
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

def la137decipher(string, n):
    alphabet = "abcdefghijklmnñopqrstuvwxyzäöüßáàâéèêëíîïóôúùûçœæøåABCDEFGHIJKLMNÑOPQRSTUVWXYZÄÖÜÁÀÂÉÈÊËÍÎÏÓÔÚÙÛÇŒÆØÅ !\"$%&'()*+,-./:;<=>?@[\]_0123456789"
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


def la137encipher_key(string, key):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(la137encipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(la137encipher,string,key)])
        return res

def la137decipher_key(string, key):
    if len(string) <= len(key):
        return "".join([deciphered for deciphered in map(la137decipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([deciphered for deciphered in map(la137decipher,string,key)])
        return res



def zh_encipher(string, n):
    with open("alphabets/zh_shuffled.txt") as zh_alphabet:
        alphabet = zh_alphabet.read()
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


def zh_decipher(string, n):
    with open("alphabets/zh_shuffled.txt") as zh_alphabet:
        alphabet = zh_alphabet.read()
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


def zh_encipher_key(string, key):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(zh_encipher, string, key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(zh_encipher, string, key)])
        return res


def zh_decipher_key(string, key):
    if len(string) <= len(key):
        return "".join([deciphered for deciphered in map(zh_decipher, string, key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([deciphered for deciphered in map(zh_decipher, string, key)])
        return res

def cy111encipher(string, n):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІЎЃЅЈЉЊЌЏЂЋЄЇҐҒҚҢҮҰҺӘӨабвгдеёжзийклмнопрстуфхцчшщъыьэюяіўѓѕјљњќџђћʼєїґғқңүұһәө !\"$%&'()*+,-./:;<=>?@[\]_"
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

def cy111decipher(string, n):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯІЎЃЅЈЉЊЌЏЂЋЄЇҐҒҚҢҮҰҺӘӨабвгдеёжзийклмнопрстуфхцчшщъыьэюяіўѓѕјљњќџђћʼєїґғқңүұһәө !\"$%&'()*+,-./:;<=>?@[\]_"
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


def cy111encipher_key(string, key):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(cy111encipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(cy111encipher,string,key)])
        return res

def cy111decipher_key(string, key):
    if len(string) <= len(key):
        return "".join([deciphered for deciphered in map(cy111decipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([deciphered for deciphered in map(cy111decipher,string,key)])
        return res
