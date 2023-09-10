# ar.py: An Arabic version of almost every built-in function in Python
# Version 1.0 - 2023
#
# Copyright (C) 2023 - 2024  Youssef Mostafa
# email: youssefmostafa952008@gmail.com
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but != required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.

# This module aims to facilitate the learning journey of Python for Arabic people
# In this module you will find every if not all built-in functions in python replicated using the Arabic language
# The functions are able to accept Arabic words or symbols as input and send the desired output
# This module also provides arabic error handling, so if you run into a problem you could easily identify it

import random
import time
import os
import subprocess
import re
import shutil
import math
import statistics
import numpy as np
import asyncio

ق = "r"

ك = "w"

صحيح = True

خاطئ = False

لا_شيئ = None

أحمر = "red"

بتقالي = "orange"

أصفر = "yellow"

أزرق = "blue"

أخضر = "green"

بنفسجي = "purple"

وردي = "pink"


# The below code defines a function called "طبع" (which means "print" in Arabic) that takes a
# parameter called "text". The function attempts to print the value of "text" using the print()
# function. If an exception occurs during the printing process, the function catches the exception and
# returns an error message indicating the failure to print the text.
def طبع(text):
    try:
        print(text)
    except Exception as e:
        return f"خطأ: فشل في طباعة النص - {e}"


# The above code is defining a function called "مدخل" (which means "input" in Arabic) that takes a
# text parameter. The function attempts to get user input by calling the input() function with the
# provided text as a prompt. If an exception occurs during the input process, the function catches the
# exception and returns an error message indicating that getting the input failed.
def مدخل(text):
    try:
        return input(text)
    except Exception as e:
        return f"خطأ: فشل في الحصول على المدخل - {e}"


# The above code defines a function called "رقأتم" which is short for "الرمز القياسي الأمريكي لتبادل المعلومات"that takes a text as input. The function tries to
# convert the text into ASCII characters using the "ascii" function. If the conversion is successful,
# it returns the ASCII representation of the text. If there is an exception during the conversion, it
# returns an error message indicating the failure.
def رقأتم(text):
    try:
        return ascii(text)
    except Exception as e:
        return f"خطأ: فشل في تحويل النص إلى رموز ASCII - {e}"


def إلى_رقم(text):
    """
    The function "إلى_رقم" converts a text into an integer, and if the text is not a valid integer, it
    returns an error message.
    
    :param text: The parameter "text" is a string that represents a number
    :return: The function `إلى_رقم` returns an integer if the input `text` can be converted to an
    integer successfully. If the conversion fails, it returns a string that indicates an error message.
    """
    try:
        return int(text)
    except ValueError as e:
        return f"خطأ: النص ليس رقمًا صحيحًا - {e}"


def إلى_نص(number):
    """
    The function "إلى_نص" converts a number to a string and handles any errors that may occur.
    
    :param number: The parameter "number" is the value that you want to convert to a string
    :return: the input number as a string. If there is an error in converting the number to a string, it
    will return an error message indicating the failure.
    """
    try:
        return str(number)
    except ValueError as e:
        return f"خطأ: فشل في تحويل الرقم إلى نص - {e}"


def إلى_عدد_عشري(text):
    """
    The function "إلى_عدد_عشري" converts a given text into a decimal number.
    
    :param text: The parameter "text" is a string that represents a number in decimal format
    :return: either the converted decimal number if the input text can be converted to a float, or an
    error message if the input text is not a decimal number.
    """
    try:
        return float(text)
    except ValueError as e:
        return f"خطأ: النص ليس عددًا عشريًا - {e}"


def قائمة_إلى_نص(list):
    """
    The function converts a list of elements into a string by joining the elements with spaces.
    
    :param list: The parameter "list" is a list of elements that you want to convert into a string
    :return: a string that represents the elements of the input list.
    """
    try:
        return ' '.join(map(str, list))
    except ValueError as e:
        return f"خطأ: فشل في تحويل القائمة إلى نص - {e}"


def نص_إلى_قائمة(text):
    """
    The function "نص_إلى_قائمة" takes a text as input and splits it into a list of words.
    
    :param text: The parameter "text" is a string that represents the text that you want to convert into
    a list
    :return: either a list of words if the text can be successfully split, or an error message if there
    is a ValueError during the splitting process.
    """
    try:
        return text.split()
    except ValueError as e:
        return f"خطأ: فشل في تحويل النص إلى قائمة - {e}"


def قائمة_إلى_عدد_عشري(text):
    """
    The function converts a string of numbers separated by spaces into a list of floating-point numbers.
    
    :param text: The parameter "text" is a string that represents a list of numbers separated by spaces
    :return: either a list of decimal numbers or an error message if the conversion fails.
    """
    try:
        return [float(i) for i in text.split()]
    except ValueError as e:
        return f"خطأ: فشل في تحويل النص إلى قائمة من الأعداد العشرية - {e}"


def قائمة_إلى_رقم(text):
    """
    The function "قائمة_إلى_رقم" takes a string as input and tries to convert it into a list of
    integers, returning an error message if the conversion fails.
    
    :param text: The parameter "text" is a string that represents a list of numbers separated by spaces
    :return: The function `قائمة_إلى_رقم` returns either a list of integers or an error message if the
    conversion fails.
    """
    try:
        return [int(i) for i in text.split()]
    except ValueError as e:
        return f"خطأ: فشل في تحويل النص إلى قائمة من الأعداد الصحيحة - {e}"


def طبع_قائمة(list):
    """
    The function "طبع_قائمة" takes a list as input and prints each item in the list, with error
    handling.
    
    :param list: The parameter "list" is a variable that represents the list of items that you want to
    print
    :return: a string that indicates an error message if there is an exception while printing the list.
    Otherwise, it does not return anything.
    """
    try:
        for item in list:
            print(item)
    except Exception as e:
        return f"خطأ: فشل في طباعة القائمة - {e}"


def مدخل_قائمة(prompt):
    """
    The function `مدخل_قائمة` takes a prompt as input and returns a list of user inputs.
    
    :param prompt: The prompt is a string that will be displayed to the user to ask for input
    :return: the user input as a list, or an error message if there was an exception while getting the
    input.
    """
    try:
        return input(prompt).split()
    except Exception as e:
        return f"خطأ: فشل في الحصول على المدخل كقائمة - {e}"


# The above code defines a function called "الطول" (which means "length" in Arabic) that takes an
# object as input. The function tries to return the length of the object using the len() function. If
# the object is not iterable (i.e., it does not have a length), a TypeError is raised. In this case,
# the function catches the error and returns a string that indicates the error message along with a
# custom message in Arabic.
def الطول(obj):
    try:
        return len(obj)
    except TypeError as e:
        return f"خطأ: الكائن ليس قابلاً للتكرار - {e}"


# The above code is defining a function called "نوع" (which means "type" in Arabic) that takes an
# object as input and returns a string indicating the type of the object. The function uses a series
# of if-elif statements to check the type of the object and returns the corresponding string. The
# function handles various types such as strings, integers, floats, lists, dictionaries, sets,
# booleans, and custom types like "قائمة" (list), "تابل" (table), and "رقم" (number). If the type of
# the object
def نوع(obj):
    try:
        if type(obj) == str:
            return "نص"
        elif type(obj) == int:
            return "رقم"
        elif type(obj) == float:
            return "عدد عشري"
        elif type(obj) == list:
            return "قائمة"
        elif type(obj) == dict:
            return "قاموس"
        elif type(obj) == set:
            return "مجموعة"
        elif type(obj) == bool:
            return "منطقية"
        elif type(obj) == قائمة:
            return "قائمة"
        elif type(obj) == تابل:
            return "تابل"
        elif type(obj) == رقم:
            return "رقم"
        elif type(obj) == "قاموس":
            return "قاموس"
    except Exception as e:
        return f"خطأ: لا يمكن اكتشاف نوع الجسم - {e}"


# The above code defines a function called "الأقصى" (which means "maximum" in Arabic) that takes an
# iterable as input. It tries to find the maximum value in the iterable using the max() function. If
# the iterable is empty or does not contain any comparable elements, a ValueError is raised. In this
# case, the code catches the exception and returns a string that indicates the error message.
def الأقصى(iterable):
    try:
        return max(iterable)
    except ValueError as e:

        return f"خطأ: فشل في الحصول على العنصر الأكبر - {e}"


# The above code defines a function called "الأدنى" (which means "minimum" in Arabic) that takes an
# iterable as input. It tries to find the maximum value in the iterable using the max() function. If
# the iterable is empty and a ValueError is raised, the function returns a string that indicates the
# failure to get the minimum element.
def الأدنى(iterable):
    try:
        return max(iterable)
    except ValueError as e:

        return f"خطأ: فشل في الحصول على العنصر الأدنى - {e}"


# The above code defines a function called "مجموع" (which means "sum" in Arabic) that calculates the
# sum of an iterable. The function takes two parameters: "iterable" (the collection of items to be
# summed) and "start" (the initial value of the sum, which defaults to 0 if not provided).
def مجموع(iterable, start=0):
    try:
        total = start
        for item in iterable:
            total += item
        return total
    except Exception as e:
        return f"خطأ: فشل في حساب المجموع - {e}"


def هل_زوجي(int):
    """
    The function `هل_زوجي` checks if a given integer is even or not.
    
    :param int: The parameter "int" is an integer that represents a number
    :return: True if the input number is even, and False if it is odd. If the input is not a number, it
    returns an error message indicating that the input was not a number.
    """
    try:
        if int % 2 == 0:
            return True

        else:
            return False
    except Exception as e:
        return f"خطأ: المُدخل لم يكن رقماً - {e}"


# The above code defines a function called "مدى" (which means "range" in Arabic) that takes three
# parameters: "start", "stop", and "step".
def مدى(start, stop=None, step=1):
    try:
        if stop is None:
            stop = start
            start = 0
        return range(start, stop, step)
    except Exception as e:
        return f"خطأ: فشل في إنشاء المدى - {e}"


# The above code is defining a function called "مرتب" (which means "sorted" in Arabic) that takes in
# an iterable, an optional key function, and an optional reverse flag. It then attempts to sort the
# iterable using the built-in "sorted" function, with the key and reverse parameters if provided. If
# any exception occurs during the sorting process, it catches the exception and returns an error
# message indicating the failure.
def مرتب(iterable, key=None, reverse=False):
    try:
        return sorted(iterable, key=key, reverse=reverse)
    except Exception as e:
        return f"خطأ: فشل في ترتيب العناصر - {e}"


def فتح_ملف(file, mode=ق, encoding=None):
    """
    The function `فتح_ملف` opens a file with the specified mode and encoding, and returns the file
    object or an error message if the file cannot be opened.
    
    :param file: The file parameter is the name or path of the file that you want to open
    :param mode: The mode parameter specifies the mode in which the file should be opened. It can have
    the following values:
    :param encoding: The encoding parameter specifies the character encoding to be used when reading or
    writing the file. It determines how the bytes in the file are interpreted as characters. If the
    encoding parameter is not specified, the default encoding for the system will be used
    :return: either the opened file object or an error message if there was an exception while opening
    the file.
    """
    try:
        return open(file, mode, encoding=encoding)
    except Exception as e:
        return f"خطأ: فشل في فتح الملف - {e}"


def إغلاق_ملف(file):
    """
    The function `إغلاق_ملف` attempts to close a file and returns an error message if it fails.
    
    :param file: The parameter "file" is the file object that you want to close
    :return: a string that indicates whether the file was successfully closed or if there was an error.
    """
    try:
        file.close()
    except Exception as e:
        return f"خطأ: فشل في إغلاق الملف - {e}"


def قراءة_محتوى(file):
    """
    The function `قراءة_محتوى` reads the content of a file and returns it, or returns an error message
    if the reading fails.
    
    :param file: The parameter "file" is the file object that you want to read its content
    :return: the content of the file if it is successfully read. If there is an exception or error
    during the reading process, it will return an error message indicating the failure.
    """
    try:
        return file.read()
    except Exception as e:
        return f"خطأ: فشل في قراءة المحتوى - {e}"


def كتابة_محتوى(file, content):
    """
    The function `كتابة_محتوى` writes content to a file.
    
    :param file: The "file" parameter is the file object that you want to write the content to. It
    should be opened in write mode using the "open" function before passing it to the function
    :param content: The content parameter is the text or data that you want to write to the file. It can
    be a string or any other data type that can be converted to a string
    :return: a string that indicates an error message if there is an exception while writing the content
    to the file. Otherwise, it does not return anything.
    """
    try:
        file.write(content)
    except Exception as e:
        return f"خطأ: فشل في كتابة المحتوى - {e}"


# The above code defines a function called `مساعدة` (which means "help" in Arabic) that takes an
# optional argument `topic`. If `topic` is not provided, the function returns a message asking for a
# topic. If `topic` is provided, the function calls the `help()` function with the provided topic and
# returns the output of the `help()` function. If an exception occurs during the execution of the
# code, the function returns an error message indicating the failure.
def مساعدة(topic=None):
    try:
        if topic is None:
            return "قم بتوفير الموضوع للمساعدة"
        else:
            return help(topic)
    except Exception as e:
        return f"خطأ: فشل في تنفيذ الأمر - {e}"


def قائمة_الملفات(obj=None):
    """
    The function `قائمة_الملفات` returns a list of files in the current scope or in the scope of the
    given object.
    
    :param obj: The parameter "obj" is an optional argument that represents an object. If no object is
    provided, the function will return a list of all the files in the current scope. If an object is
    provided, the function will return a list of all the files in that object
    :return: a list of files or attributes. If the `obj` parameter is not provided, it returns a list of
    files in the current scope. If the `obj` parameter is provided, it returns a list of attributes or
    methods of the object.
    """
    try:
        if obj is None:
            return dir()
        else:
            return dir(obj)
    except Exception as e:
        return f"خطأ: فشل في الحصول على قائمة الملفات - {e}"


def clear():
    """
    The `clear` function clears the terminal screen.
    """
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


def مسح_الشاشة():
    """
    The function `مسح_الشاشة()` clears the terminal screen.
    """
    clear()


# The above code defines a function called "تأخير" (which means "delay" in Arabic) that takes in a
# parameter called "seconds". Inside the function, it uses the "time.sleep()" function to pause the
# execution of the program for the specified number of seconds.
def تأخير(seconds):
    time.sleep(seconds)


def رقم_عشوائي(start, end):
    """
    The function generates a random number between a given start and end range.
    
    :param start: The start parameter is the lower bound of the range from which the random number will
    be generated
    :param end: The "end" parameter represents the upper limit of the range from which the random number
    will be generated
    :return: a random number between the start and end values. If an error occurs during the execution
    of the command, it will return an error message indicating the failure.
    """
    try:
        return random.randint(start, end)

    except Exception as e:
        return f"خطأ: فشل في تنفيذ الأمر - {e}"


def اختيار_عشوائي(sequence):
    """
    The function `اختيار_عشوائي` takes a sequence as input and returns a random element from that
    sequence.
    
    :param sequence: The parameter "sequence" is a list or any iterable object from which you want to
    select a random element
    :return: a randomly chosen element from the given sequence. If an error occurs during the random
    selection process, it will return an error message indicating the failure.
    """
    try:
        return random.choice(sequence)
    except Exception as e:
        return f"خطأ: فشل في اختيار عنصر عشوائي - {e}"


def اختيارات_عشوائية(sequence, k=1):
    try:
        return random.choices(sequence, k=k)
    except Exception as e:
        return f"خطأ: فشل في اختيار عناصر عشوائية - {e}"


def تشفير(text, shift):
    try:
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr(
                    (ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
            return encrypted_text
    except Exception as e:
        return f"خطأ: فشل في التشفير - {e}"


def فك_تشفير(encrypted_text, shift):
    try:
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr(
                    (ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text
    except Exception as e:
        return f"خطأ: فشل في فك التشفير - {e}"


def match(pattern, string):
    try:
        match = re.search(pattern, string)
        if match:
            return match.group()
        else:
            return None
    except Exception as e:
        return e


def انقل_الملف(source, destination):
    try:
        shutil.move(source, destination)
    except Exception as e:
        return f"خطأ: فشل في نقل الملف - {e}"


def حذف_الملف(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        return f"خطأ: فشل في حذف الملف - {e}"


def جمع(number1, number2):
    try:
        return number1 + number2
    except Exception as e:
        return f"خطأ: فشل في عملية الجمع - {e}"


def طرح(number1, number2):
    try:
        return number1 - number2
    except Exception as e:
        return f"خطأ: فشل في عملية الطرح - {e}"


def قسم(number1, number2):
    try:
        return number1 / number2
    except Exception as e:
        return f"خطأ: فشل في عملية القسم - {e}"


def ضرب(number1, number2):
    try:
        return number1 * number2
    except Exception as e:
        return f"خطأ: فشل في عملية الضرب - {e}"


def ضرب_مصفوف(matrix1, matrix2):
    try:
        return np.dot(matrix1, matrix2)
    except Exception as e:
        return f"خطأ: فشل في عملية ضرب المصفوفات - {e}"


def جذر_تربيعي(number):
    try:
        return number ** 0.5
    except Exception as e:
        return f"خطأ: فشل في حساب الجذر التربيعي - {e}"


def قوة(number, exponent):
    try:
        return number ** exponent
    except Exception as e:
        return f"خطأ: فشل في حساب القوة - {e}"


def جذر(number, root):
    try:
        return number ** (1 / root)
    except Exception as e:
        return f"خطأ: فشل في حساب الجذر - {e}"


def مطلق(number):
    try:
        return abs(number)
    except Exception as e:
        return f"خطأ: فشل في حساب القيمة المطلقة - {e}"


def جزء_صحيح(number):
    try:
        return int(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجزء الصحيح - {e}"


def جزء_عشري(number):
    try:
        return number - int(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجزء العشري - {e}"


def تقريب_أعلى(number):
    try:
        return math.ceil(number)
    except Exception as e:
        return f"خطأ: فشل في التقريب لأعلى - {e}"


def تقريب_أدنى(number):
    try:
        return math.floor(number)
    except Exception as e:
        return f"خطأ: فشل في التقريب لأدنى - {e}"


def تقريب(number):
    try:
        return round(number)
    except Exception as e:
        return f"خطأ: فشل في التقريب - {e}"


def مجموع_قائمة(list):
    try:
        return sum(list)
    except Exception as e:
        return f"خطأ: فشل في حساب مجموع القائمة - {e}"


def متوسط(list):
    try:
        return sum(list) / len(list)
    except Exception as e:
        return f"خطأ: فشل في حساب المتوسط - {e}"


def مجموع_ترتيبي(list):
    try:
        return statistics.mean(list)
    except Exception as e:
        return f"خطأ: فشل في حساب المجموع الترتيبي - {e}"


def وسيط(list):
    try:
        return statistics.median(list)
    except Exception as e:
        return f"خطأ: فشل في حساب الوسيط - {e}"


def وسيط_مجموعة_بيانات(list):
    try:
        return statistics.median_grouped(list)
    except Exception as e:
        return f"خطأ: فشل في حساب الوسيط لمجموعة البيانات - {e}"


def وسيط_مجموعة_بيانات_مجمعة(list):
    try:
        return statistics.median_high(list)
    except Exception as e:
        return f"خطأ: فشل في حساب الوسيط لمجموعة البيانات المجمعة - {e}"


def جيب(number):
    try:
        return math.sin(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب - {e}"


def الجيب_التام(number):
    try:
        return math.cos(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب التام - {e}"


def جيب_معكوس(number):
    try:
        return math.asin(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المعكوس - {e}"


def جيب_التام_معكوس(number):
    try:
        return math.acos(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب التام المعكوس - {e}"


def جيب_مستدير(number):
    try:
        return math.sinh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المستدير - {e}"


def جيب_تام_مستدير(number):
    try:
        return math.cosh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب التام المستدير - {e}"


def جيب_معكوس_مستدير(number):
    try:
        return math.asinh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المعكوس المستدير - {e}"


def جيب_تام_معكوس_مستدير(number):
    try:
        return math.acosh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب التام المعكوس المستدير - {e}"


def جيب_مزدوج(number):
    try:
        return math.sin(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج - {e}"


def جيب_التام_مزدوج(number):
    try:
        return math.sin(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب التام المزدوج - {e}"


def جيب_معكوس_مزدوج(number):
    try:
        return math.degrees(math.asin(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المعكوس المزدوج - {e}"


def جيب_التام_معكوس_مزدوج(number):
    try:
        return math.degrees(math.asin(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المعكوس المزدوج - {e}"


def جيب_مستدير_مزدوج(number):
    try:
        return math.sinh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المستدير المزدوج - {e}"


def جيب_التام_مستدير_مزدوج(number):
    try:
        return math.sinh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المستدير المزدوج - {e}"


def جيب_معكوس_مستدير_مزدوج(number):
    try:
        return math.degrees(math.asinh(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المعكوس المستدير المزدوج - {e}"


def جيب_التام_معكوس_مستدير_مزدوج(number):
    try:
        return math.degrees(math.asinh(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المعكوس المستدير المزدوج - {e}"


def جيب_مزدوج_معكوس(number):
    try:
        return math.degrees(math.asin(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المعكوس - {e}"


def جيب_التام_مزدوج_معكوس(number):
    try:
        return math.degrees(math.asin(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المعكوس - {e}"


def جيب_مزدوج_مستدير(number):
    try:
        return math.sinh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المستدير - {e}"


def جيب_التام_مزدوج_مستدير(number):
    try:
        return math.sinh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المستدير - {e}"


def جيب_مزدوج_معكوس_مستدير(number):
    try:
        return math.degrees(math.asinh(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المعكوس المستدير - {e}"


def جيب_تام_مزدوج_معكوس_مستدير(number):
    try:
        return math.degrees(math.asinh(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المعكوس المستدير - {e}"


def جيب_مستدير_معكوس_مزدوج(number):
    try:
        return math.degrees(math.asin(math.sinh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المستدير المعكوس المزدوج - {e}"


def جيب_التام_مستدير_معكوس_مزدوج(number):
    try:
        return math.degrees(math.asin(math.sinh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المستدير المعكوس المزدوج - {e}"


def جيب_مزدوج_مستدير_معكوس(number):
    try:
        return math.degrees(math.asinh(math.sin(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المستدير المعكوس - {e}"


def جيب_التام_مزدوج_مستدير_معكوس(number):
    try:
        return math.degrees(math.asinh(math.sin(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المزدوج المستدير المعكوس - {e}"


def جيب_مستدير_مزدوج_معكوس(number):
    try:
        return math.degrees(math.asin(math.sinh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المستدير المزدوج المعكوس - {e}"


def جيب_التام_مستدير_مزدوج_معكوس(number):
    try:
        return math.degrees(math.asin(math.sinh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب الجيب المستدير المزدوج المعكوس - {e}"


class قائمة(list):
    def __init__(self, *args):
        self.value = list(args)

    def انضمام(self, separator):
        try:
            return separator.join(self.value)
        except Exception as e:
            return f"خطأ: فشل في تنفيذ عملية الانضمام - {e}"

    def تحويل_إلى_قائمة(self):
        try:
            return list(self.value)
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قائمة - {e}"

    def تحويل_إلى_مجموعة(self):
        try:
            return set(self.value)
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى مجموعة - {e}"

    def تحويل_إلى_سلسلة(self):
        try:
            return str(self.value)
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى سلسلة - {e}"

    def تحويل_إلى_مجموعة_مرتبة(self):
        try:
            return sorted(set(self.value))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى مجموعة مرتبة - {e}"

    def تحويل_إلى_قاموس(self):
        try:
            return dict(enumerate(self.value))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس - {e}"

    def تحويل_إلى_قاموس_مرتب(self):
        try:
            return dict(zip(range(1, len(self.value) + 1), self.value))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس مرتب - {e}"

    def تحويل_إلى_قاموس_عكسي(self):
        try:
            return dict(zip(self.value, range(1, len(self.value) + 1)))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس عكسي - {e}"

    def تحويل_إلى_قاموس_عكسي_مرتب(self):
        try:
            return dict(zip(self.value, range(len(self.value), 0, -1)))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس عكسي مرتب - {e}"

    def تحويل_إلى_قاموس_مرتب_عكسي(self):
        try:
            return dict(zip(range(len(self.value), 0, -1), self.value))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس مرتب عكسي - {e}"

    def تحويل_إلى_قاموس_مرتب_عكسي_مرتب(self):
        try:
            return dict(zip(range(len(self.value), 0, -1), sorted(self.value)))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس مرتب عكسي مرتب - {e}"


class نص(str):
    def __init__(self, value):
        self.value = value

    def انضمام(self, separator):
        try:
            return separator.join(self.value)
        except Exception as e:
            return f"خطأ: فشل في تنفيذ عملية الانضمام - {e}"

    def match(self, pattern):
        try:
            match = re.search(pattern, self)
            if match:
                return match.group()
            else:
                return None
        except Exception as e:
            return e

    def مطابقة(self, pattern):
        try:
            match = re.search(pattern, self)
            if match:
                return match.group()
            else:
                return None
        except Exception as e:
            return f"خطأ: فشل في تنفيذ الأمر - {e}"

    def استبدال(self, old, new):
        try:
            return self.replace(old, new)
        except Exception as e:
            return f"خطأ: فشل في تنفيذ عملية الاستبدال - {e}"

    def تقسيم(self, separator):
        try:
            return self.split(separator)
        except Exception as e:
            return f"خطأ: فشل في تنفيذ عملية التقسيم - {e}"

    def يبدأ_بـ(self, prefix):
        try:
            return self.startswith(prefix)
        except Exception as e:
            return f"خطأ: فشل في تنفيذ الأمر - {e}"

    def ينتهى_بـ(self, suffix):
        try:
            return self.endswith(suffix)
        except Exception as e:
            return f"خطأ: فشل في تنفيذ الأمر - {e}"

    def عدد_الظهور(self, substring):
        try:
            return self.count(substring)
        except Exception as e:
            return f"خطأ: فشل في تنفيذ الأمر - {e}"

    def تحويل_إلى_أعلى(self):
        try:
            return self.value.upper()
        except Exception as e:
            return f"خطأ: فشل في تنفيذ عملية التحويل إلى أعلى - {e}"

    def تحويل_إلى_أسفل(self):
        try:
            return self.value.lower()
        except Exception as e:
            return f"خطأ: فشل في تنفيذ عملية التحويل إلى أسفل - {e}"

    def تحويل_إلى_عنوان(self):
        try:
            return self.value.title()
        except Exception as e:
            return f"خطأ: فشل في تنفيذ عملية التحويل إلى عنوان - {e}"


class قاموس(dict):
    def __init__(self, value):
        self.value = value

    def تحويل_إلى_قاموس(self):
        try:
            return dict(self.value)
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس - {e}"

    def تحويل_إلى_قاموس_مرتب(self):
        try:
            return dict(enumerate(self.value))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس مرتب - {e}"

    def تحويل_إلى_قاموس_عكسي(self):
        try:
            return dict(zip(self.value, range(1, len(self.value) + 1)))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس عكسي - {e}"

    def تحويل_إلى_قاموس_عكسي_مرتب(self):
        try:
            return dict(zip(self.value, range(len(self.value), 0, -1)))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس عكسي مرتب - {e}"

    def تحويل_إلى_قاموس_مرتب_عكسي(self):
        try:
            return dict(zip(range(len(self.value), 0, -1), self.value))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس مرتب عكسي - {e}"

    def تحويل_إلى_قاموس_مرتب_عكسي_مرتب(self):
        try:
            return dict(zip(range(len(self.value), 0, -1), sorted(self.value)))
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قاموس مرتب عكسي مرتب - {e}"


class تابل(tuple):
    def __init__(self, *args):
        self.value = args

    def تحويل_إلى_قائمة(self):
        try:
            return list(self.value)
        except Exception as e:
            return f"خطأ: فشل في تحويل القيمة إلى قائمة - {e}"


class رقم(int):
    def __init__(self, value):
        self.value = value

    def تحويل_إلى_ثنائي(self):
        try:
            return bin(self.value)[2:]
        except Exception as e:
            return f"خطأ: فشل في تحويل الرقم إلى ثنائي - {e}"

    def تحويل_إلى_ثماني(self):
        try:
            return oct(self.value)[2:]
        except Exception as e:
            return f"خطأ: فشل في تحويل الرقم إلى ثماني - {e}"

    def تحويل_إلى_سداسي_عشري(self):
        try:
            return hex(self.value)[2:]
        except Exception as e:
            return f"خطأ: فشل في تحويل الرقم إلى سداسي عشري - {e}"

    def تحويل_إلى_عشري(self):
        try:
            return int(self.value, 2)
        except Exception as e:
            return f"خطأ: فشل في تحويل الرقم الثنائي إلى عشري - {e}"

# The above code defines a function called "إذا" (which means "if" in Arabic) that takes two
# parameters: "condition" and "body". The "condition" parameter is a boolean expression that
# determines whether the "body" should be executed or not. The "body" parameter is a string that
# contains the code to be executed if the condition is true.
def إذا(condition, body):
    # Body has to be a string
    try:
        if condition:
            exec(f"{body}")
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو(condition, body, condition2, body2):
    """
    The function إذا_أو takes two conditions and two bodies of code, and executes the first body if the
    first condition is true, or the second body if the second condition is true.
    
    :param condition: The condition parameter is a boolean expression that determines whether to execute
    the body or not. If the condition is true, the body will be executed
    :param body: The "body" parameter is a string that represents the code that will be executed if the
    "condition" is true
    :param condition2: The parameter `condition2` is the second condition that will be checked. If
    `condition` is False, then `condition2` will be evaluated
    :param body2: The parameter `body2` is the code that will be executed if `condition2` is true
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_أو(condition, body, condition2, body2, condition3, body3):
    """
    The function `إذا_أو_أو` is a conditional statement that executes different bodies of code based on
    multiple conditions.
    
    :param condition: The condition parameter is a boolean expression that determines whether to execute
    the body parameter or not. If the condition is true, the body will be executed
    :param body: The "body" parameter is a string that represents the code that will be executed if the
    corresponding condition is true
    :param condition2: The parameter `condition2` is the second condition that will be checked in the
    `if-elif` statement. If `condition2` evaluates to `True`, then `body2` will be executed
    :param body2: The parameter `body2` is a string that represents the code that will be executed if
    `condition2` is true
    :param condition3: The parameter `condition3` is a condition that is checked after `condition` and
    `condition2`. If `condition3` is `True`, then `body3` is executed
    :param body3: The parameter `body3` is a string that represents the code that will be executed if
    `condition3` is true
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
        elif condition3:
            exec(f"{body3}")
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_أو_أو(condition, body, condition2, body2, condition3, body3, condition4, body4):
    """
    The function `إذا_أو_أو_أو` is a conditional statement that executes different bodies of code based
    on multiple conditions.
    
    :param condition: The `condition` parameter is a boolean expression that determines whether to
    execute the `body` code block or not. If the `condition` is `True`, the `body` code block will be
    executed
    :param body: The "body" parameter is a string that represents the code that will be executed if the
    corresponding condition is true
    :param condition2: The parameter `condition2` is the second condition that will be checked in the
    `if-elif` chain. If `condition2` evaluates to `True`, then `body2` will be executed
    :param body2: The parameter `body2` is a string that represents the code that will be executed if
    `condition2` is true
    :param condition3: The parameter `condition3` is a condition that is checked in the `if` statement.
    If this condition evaluates to `True`, then the code in `body3` will be executed
    :param body3: The parameter `body3` is a string that represents the code that will be executed if
    `condition3` is true
    :param condition4: The parameter `condition4` is the fourth condition that will be evaluated in the
    `إذا_أو_أو_أو` function. If this condition is true, then the corresponding `body4` will be executed
    :param body4: The parameter `body4` is the code that will be executed if `condition4` is true
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
        elif condition3:
            exec(f"{body3}")
        elif condition4:
            exec(f"{body4}")
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_أو_أو_أو(condition=False, body="", condition2=False, body2="", condition3=False, body3="", condition4=False, body4="", condition5=False, body5=""):
    """
    The function `إذا_أو_أو_أو_أو` is a conditional statement that executes different bodies of code
    based on multiple conditions.
    
    :param condition: The `condition` parameter is a boolean value that determines whether or not to
    execute the code in the `body` parameter. If `condition` is `True`, the code in `body` will be
    executed, defaults to False (optional)
    :param body: The `body` parameter is a string that contains the code that will be executed if the
    corresponding condition is true
    :param condition2: The parameter `condition2` is a boolean variable that represents the second
    condition to be checked. If this condition is true, the code inside `body2` will be executed,
    defaults to False (optional)
    :param body2: The parameter `body2` is a string that represents the code that will be executed if
    `condition2` is `True`
    :param condition3: The parameter `condition3` is a boolean variable that determines whether or not
    to execute the code in `body3`. If `condition3` is `True`, the code in `body3` will be executed,
    defaults to False (optional)
    :param body3: The parameter `body3` is a string that represents the code that will be executed if
    `condition3` is `True`
    :param condition4: The parameter `condition4` is a boolean variable that determines whether to
    execute the code in `body4` or not. If `condition4` is `True`, the code in `body4` will be executed,
    defaults to False (optional)
    :param body4: The parameter `body4` is a string that represents the code that will be executed if
    `condition4` is `True`
    :param condition5: The parameter `condition5` is a boolean value that represents the condition for
    the fifth block of code to be executed. If `condition5` is `True`, then the code in `body5` will be
    executed, defaults to False (optional)
    :param body5: The parameter `body5` is a string that represents the code that will be executed if
    `condition5` is `True`
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
        elif condition3:
            exec(f"{body3}")
        elif condition4:
            exec(f"{body4}")
        elif condition5:
            exec(f"{body5}")
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_لكن(condition, body, elsebody):
    """
    The function إذا_لكن is a custom implementation of an if-else statement in Python, with support for
    executing code blocks as strings.
    
    :param condition: The condition is a boolean expression that determines whether the body or elsebody
    should be executed. If the condition is true, the body will be executed. If the condition is false,
    the elsebody will be executed
    :param body: The `body` parameter is a string that represents the code that will be executed if the
    `condition` is true
    :param elsebody: The `elsebody` parameter is a string that contains the code to be executed if the
    condition in the `إذا_لكن` function is `False`
    """
    try:
        if condition:
            exec(f"{body}")
        else:
            exec(elsebody)
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_لكن(condition=False, body="", condition2=False, body2="", elsebody=""):
    """
    The function إذا_أو_لكن is a custom implementation of an if-elif-else statement in Python, with
    support for executing code blocks based on conditions and handling exceptions.
    
    :param condition: The condition parameter is a boolean value that determines whether or not to
    execute the body parameter. If the condition is True, the body parameter will be executed, defaults
    to False (optional)
    :param body: The "body" parameter is a string that contains the code that will be executed if the
    first condition is true
    :param condition2: The `condition2` parameter is a boolean value that represents the second
    condition to be checked. If this condition is true, the code in `body2` will be executed, defaults
    to False (optional)
    :param body2: The parameter `body2` is a string that represents the code that will be executed if
    `condition2` is `True`
    :param elsebody: The `elsebody` parameter is a string that contains the code to be executed if none
    of the conditions specified in the `if` and `elif` statements are met
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
        else:
            exec(elsebody)
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_أو_لكن(condition=False, body="", condition2=False, body2="", condition3=False, body3="", elsebody=""):
    """
    The function `إذا_أو_أو_لكن` is a conditional statement that executes different code blocks based on
    multiple conditions.
    
    :param condition: The condition parameter is a boolean value that determines whether or not to
    execute the code in the body parameter. If the condition is True, the code in the body parameter
    will be executed, defaults to False (optional)
    :param body: The "body" parameter is a string that contains the code that will be executed if the
    corresponding condition is true
    :param condition2: The parameter `condition2` is a boolean value that represents the second
    condition to be checked. If this condition is true, the code in `body2` will be executed, defaults
    to False (optional)
    :param body2: The parameter `body2` is a string that represents the code that will be executed if
    `condition2` is `True`
    :param condition3: The parameter `condition3` is a boolean value that represents a condition. If
    this condition is true, the code in `body3` will be executed, defaults to False (optional)
    :param body3: The parameter `body3` is a string that represents the code that will be executed if
    `condition3` is `True`
    :param elsebody: The `elsebody` parameter is a string that contains the code to be executed if none
    of the conditions specified in the `if` statements are met
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
        elif condition3:
            exec(f"{body3}")
        else:
            exec(elsebody)
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_أو_أو_لكن(condition=False, body="", condition2=False, body2="", condition3=False, body3="", condition4=False, body4="", elsebody=""):
    """
    The function `إذا_أو_أو_أو_لكن` is a conditional statement that executes different code blocks based
    on multiple conditions.
    
    :param condition: The `condition` parameter is a boolean value that determines whether or not to
    execute the code in the `body` parameter. If `condition` is `True`, the code in `body` will be
    executed, defaults to False (optional)
    :param body: The "body" parameter is a string that contains the code that will be executed if the
    corresponding condition is true
    :param condition2: The parameter `condition2` is a boolean value that represents the second
    condition to be checked. If this condition is true, the code in `body2` will be executed, defaults
    to False (optional)
    :param body2: The parameter `body2` is a string that represents the code that will be executed if
    `condition2` is `True`
    :param condition3: The parameter "condition3" is a boolean value that represents the third condition
    to be checked in the function. If this condition is true, the corresponding "body3" will be
    executed, defaults to False (optional)
    :param body3: The parameter `body3` is a string that represents the code that will be executed if
    `condition3` is `True`
    :param condition4: The parameter "condition4" is a boolean value that represents the fourth
    condition to be checked. If this condition is true, the code in "body4" will be executed, defaults
    to False (optional)
    :param body4: The parameter `body4` is a string that represents the code that will be executed if
    `condition4` is `True`
    :param elsebody: The `elsebody` parameter is a string that contains the code to be executed if none
    of the conditions specified in the `if` statements are met
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
        elif condition3:
            exec(f"{body3}")
        elif condition4:
            exec(f"{body4}")
        else:
            exec(elsebody)
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_أو_أو_أو_لكن(condition=False, body="", condition2=False, body2="", condition3=False, body3="", condition4=False, body4="", condition5=False, body5="", elsebody=""):
    """
    The function `إذا_أو_أو_أو_أو_لكن` is a conditional statement that allows for multiple conditions
    and corresponding bodies of code to be executed.
    
    :param condition: The `condition` parameter is a boolean value that determines whether or not to
    execute the code in the `body` parameter. If `condition` is `True`, the code in `body` will be
    executed, defaults to False (optional)
    :param body: The "body" parameter is a string that contains the code that will be executed if the
    corresponding condition is true
    :param condition2: The parameter `condition2` is a boolean value that represents the second
    condition to be checked. If this condition is true, the code in `body2` will be executed, defaults
    to False (optional)
    :param body2: The parameter `body2` is a string that contains the code that will be executed if
    `condition2` is `True`
    :param condition3: The parameter `condition3` is a boolean value that determines whether to execute
    the code in `body3` or not. If `condition3` is `True`, the code in `body3` will be executed,
    defaults to False (optional)
    :param body3: The parameter `body3` is a string that contains the code that will be executed if
    `condition3` is `True`
    :param condition4: The parameter `condition4` is a boolean value that represents the condition for
    the fourth block of code to be executed. If `condition4` is `True`, then the code in `body4` will be
    executed, defaults to False (optional)
    :param body4: The parameter `body4` is a string that contains the code that will be executed if
    `condition4` is `True`
    :param condition5: The parameter `condition5` is a boolean value that represents the fifth condition
    to be checked. If `condition5` is `True`, then the code in `body5` will be executed, defaults to
    False (optional)
    :param body5: The parameter `body5` is a string that represents the code that will be executed if
    `condition5` is `True`
    :param elsebody: The `elsebody` parameter is the code that will be executed if none of the
    conditions specified in the `if` statements are met
    """
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
        elif condition3:
            exec(f"{body3}")
        elif condition4:
            exec(f"{body4}")
        elif condition5:
            exec(f"{body5}")
        else:
            exec(elsebody)
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")

# The above code is defining a function called "استيراد" (which means "import" in Arabic) that takes a
# parameter called "module_name". Inside the function, it tries to import the module specified by
# "module_name" using the "import" statement. If the import is successful, nothing happens. If there
# is an exception (error) during the import, the function returns a string that indicates the error
# message.
def استيراد(module_name):
    try:
        exec(f"import {str(module_name)}")
    except Exception as e:
        return f"خطأ: فشل في استيراد الوحدة - {e}"


def استيراد_باسم(module_name, name):
    """
    The function "استيراد_باسم" imports a module with a specified name and assigns it a new name.
    
    :param module_name: The name of the module you want to import
    :param name: The name parameter is the name you want to give to the imported module. For example, if
    you want to import the module "math" and give it the name "m", you would call the function like
    this: استيراد_باسم("math", "m")
    :return: a string. If the import of the module is successful, it will return a string indicating
    that the import was successful. If there is an error during the import, it will return a string
    indicating the error message.
    """
    try:
        exec(f"import {str(module_name)} as {str(name)}")
    except Exception as e:
        return f"خطأ: فشل في استيراد الوحدة - {e}"


def استيراد_دالة_من(module_name, function):
    """
    The function allows importing a specific function from a module in Python.
    
    :param module_name: The name of the module from which you want to import a function
    :param function: The `function` parameter is the name of the specific function you want to import
    from the module
    :return: a string that indicates whether the import was successful or if there was an error. If the
    import is successful, it will return "None". If there is an error, it will return a string that
    starts with "خطأ: فشل في استيراد الوحدة -" followed by the error message.
    """
    try:
        exec(f"from {str(module_name)} import {str(function)}")
    except Exception as e:
        return f"خطأ: فشل في استيراد الوحدة - {e}"


# The above code defines a function called "يكون" (which means "be" in Arabic) that takes two
# arguments, "val1" and "val2". The function checks if "val1" is equal to "val2" using the "is"
# operator. If they are equal, the function returns True. Otherwise, it returns False.
def يكون(val1, val2):
    if val1 is val2:
        return True
    else:
        return False


# The above code defines a function called "ليس" (which means "not" in Arabic) that takes two
# arguments, val1 and val2. The function checks if val1 is not equal to val2 and returns True if they
# are not equal, otherwise it returns False.
def ليس(val1, val2):
    if val1 != val2:
        return True
    else:
        return False


# The above code defines a function called "في" that takes two arguments, "val1" and "val2". The
# function checks if "val1" is present in "val2" and returns True if it is, and False otherwise.
def في(val1, val2):
    if val1 in val2:
        return True
    else:
        return False


# The above code defines a function named "و" (which means "and" in Arabic) that takes two conditions
# as input. It checks if both conditions are true and returns True if they are, otherwise it returns
# False.
def و(condition1, condition2):
    if condition1 and condition2:
        return True
    else:
        return False


# The above code defines a function named "أو" (which means "or" in Arabic) that takes two conditions
# as input. It checks if either of the conditions is true and returns True if at least one of the
# conditions is true. Otherwise, it returns False.
def أو(condition1, condition2):
    if condition1 or condition2:
        return True
    else:
        return False


def حلقة_إلى(list, body):
    """
    The function `حلقة_إلى` takes a list and a body of code as input, and executes the code for each
    element in the list.
    
    :param list: A list of elements that will be iterated over in the loop
    :param body: The `body` parameter is a string that represents the code that will be executed in each
    iteration of the loop
    :return: a string that indicates whether the loop was executed successfully or if there was an
    error.
    """
    try:
        for i in list:
            exec(f"{str(body)}")
    except Exception as e:
        return f"خطأ: فشل في تنفيذ الحلقة - {e}"


def حلقة_حتى(condition, body):
    """
    The function `حلقة_حتى` is a helper function that executes a given body of code repeatedly until a
    specified condition is no longer true.
    
    :param condition: The condition is a boolean expression that determines whether the loop should
    continue executing or not. If the condition evaluates to True, the loop will continue executing. If
    it evaluates to False, the loop will terminate
    :param body: The `body` parameter is a string that represents the code that will be executed in each
    iteration of the loop
    :return: a string that indicates whether the loop was executed successfully or if there was an
    error.
    """
    try:
        while condition:
            exec(f"{str(body)}")
    except Exception as e:
        return f"خطأ: فشل في تنفيذ الحلقة - {e}"


# The above code defines a function called "حساب" (which means "calculate" in Arabic) that takes in a
# string representing a mathematical expression. The function attempts to evaluate the expression
# using the eval() function. If the evaluation is successful, the result is returned. If there is an
# error during the evaluation, an error message is returned instead.
def حساب(equ):
    try:
        return (eval(str(equ)))
    except Exception as e:
        return f"خطأ: فشل في حساب العملية - {e}"


# The above code defines a function called "تجربة" (which means "trying" in Arabic) that takes two
# statements as arguments. The function attempts to execute the first statement using the "exec"
# function. If an exception occurs, it catches the exception and executes the second statement
# instead.
def تجربة(statement1, statement2):
    try:
        exec(f"{str(statement1)}")
    except:
        exec(f"{str(statement2)}")


# The above code defines a function called "التأكيد" (which means "confirm" in Arabic) that takes two
# parameters: "condition" and "message". It uses the "assert" statement to check if the given
# condition is true. If the condition is false, it raises an AssertionError with the given message.
def التأكيد(condition, message):
    assert condition, message


# The below code defines an asynchronous function called "انتظر" (which means "wait" in Arabic).
# Inside the function, it uses the "await" keyword to pause the execution of the function for n
# seconds using the "asyncio.sleep" function. This allows other code to run concurrently while the
# function is waiting.
async def انتظر(n):
    await asyncio.sleep(n)


# The below code defines a function called "خروج" (which means "exit" in Arabic) that calls the
# "exit()" function to terminate the program.
def خروج():
    exit()


# The below code defines a function called "انهاء" (which means "quit" in Arabic) that terminates the
# program when called.
def انهاء():
    quit()