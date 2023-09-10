# ar.py: An Arabic version of almost every built-in function in Python
# Version in-dev 1.1 - 2023
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
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.

# This module aims to facilitate the learning journey of Python for Arabic people
# In this module you will find every if not all built-in functions in python replicated using the Arabic language
# The functions are able to accept Arabic words or symbols as input and send the desired output
# This module also provides arabic error handling, so if you run into a problem you could easily identify it

# ! This is the "in development" version, it's unstable and full function that don't 

# TODO: Lots of functions need Arabic error handling, write it

import random
import time
import os
import subprocess
import re
import shutil
import math
import statistics
import numpy as np
import turtle
import asyncio
import inspect

# TODO: Make a list of every key bind in arabic so that it can be used in onkey function

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

def طبع(text):
    try:
        print(text)
    except Exception as e:
        return f"خطأ: فشل في طباعة النص - {e}"


def مدخل(text):
    try:
        return input(text)
    except Exception as e:
        return f"خطأ: فشل في الحصول على المدخل - {e}"


def رقأتم(text):
    try:
        return ascii(text)
    except Exception as e:
        return f"خطأ: فشل في تحويل النص إلى رموز ASCII - {e}"


def إلى_رقم(text):
    try:
        return int(text)
    except ValueError as e:
        return f"خطأ: النص ليس رقمًا صحيحًا - {e}"


def إلى_نص(number):
    try:
        return str(number)
    except ValueError as e:
        return f"خطأ: فشل في تحويل الرقم إلى نص - {e}"


def إلى_عدد_عشري(text):
    try:
        return float(text)
    except ValueError as e:
        return f"خطأ: النص ليس عددًا عشريًا - {e}"


def قائمة_إلى_نص(list):
    try:
        return ' '.join(map(str, list))
    except ValueError as e:
        return f"خطأ: فشل في تحويل القائمة إلى نص - {e}"


def نص_إلى_قائمة(text):
    try:
        return text.split()
    except ValueError as e:
        return f"خطأ: فشل في تحويل النص إلى قائمة - {e}"


def قائمة_إلى_عدد_عشري(text):
    try:
        return [float(i) for i in text.split()]
    except ValueError as e:
        return f"خطأ: فشل في تحويل النص إلى قائمة من الأعداد العشرية - {e}"


def قائمة_إلى_رقم(text):
    try:
        return [int(i) for i in text.split()]
    except ValueError as e:
        return f"خطأ: فشل في تحويل النص إلى قائمة من الأعداد الصحيحة - {e}"


def طبع_قائمة(list):
    try:
        for item in list:
            print(item)
    except Exception as e:
        return f"خطأ: فشل في طباعة القائمة - {e}"


def مدخل_قائمة(prompt):
    try:
        return input(prompt).split()
    except Exception as e:
        return f"خطأ: فشل في الحصول على المدخل كقائمة - {e}"


def الطول(obj):
    try:
        return len(obj)
    except TypeError as e:
        return f"خطأ: الكائن ليس قابلاً للتكرار - {e}"


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
        elif type(obj) == قاموس:
            return "قاموس"
        elif type(obj) == سلحفاة:
            return "سلحفاة"
        elif type(obj) == شاشة:
            return "شاشة"
    except Exception as e:
        return f"خطأ: لا يمكن اكتشاف نوع الجسم - {e}"


def الأقصى(iterable):
    try:
        return max(iterable)
    except ValueError as e:

        return f"خطأ: فشل في الحصول على العنصر الأكبر - {e}"


def الأدنى(iterable):
    try:
        return max(iterable)
    except ValueError as e:

        return f"خطأ: فشل في الحصول على العنصر الأدنى - {e}"


def مجموع(iterable, start=0):
    try:
        total = start
        for item in iterable:
            total += item
        return total
    except Exception as e:
        return f"خطأ: فشل في حساب المجموع - {e}"


def هل_زوجي(int):
    try:
        if int % 2 == 0:
            return True

        else:
            return False
    except Exception as e:
        return f"خطأ: المُدخل لم يكن رقماً - {e}"


def مدى(start, stop=None, step=1):
    try:
        if stop is None:
            stop = start
            start = 0
        return range(start, stop, step)
    except Exception as e:
        return f"خطأ: فشل في إنشاء المدى - {e}"


def مرتب(iterable, key=None, reverse=False):
    try:
        return sorted(iterable, key=key, reverse=reverse)
    except Exception as e:
        return f"خطأ: فشل في ترتيب العناصر - {e}"


def فتح_ملف(file, mode=ق, encoding=None):
    try:
        return open(file, mode, encoding=encoding)
    except Exception as e:
        return f"خطأ: فشل في فتح الملف - {e}"


def إغلاق_ملف(file):
    try:
        file.close()
    except Exception as e:
        return f"خطأ: فشل في إغلاق الملف - {e}"


def قراءة_محتوى(file):
    try:
        return file.read()
    except Exception as e:
        return f"خطأ: فشل في قراءة المحتوى - {e}"


def كتابة_محتوى(file, content):
    try:
        file.write(content)
    except Exception as e:
        return f"خطأ: فشل في كتابة المحتوى - {e}"


def مساعدة(topic=None):
    try:
        if topic is None:
            return "قم بتوفير topic للمساعدة"
        else:
            return help(topic)
    except Exception as e:
        return f"خطأ: فشل في تنفيذ الأمر - {e}"


def قائمة_الملفات(obj=None):
    try:
        if obj is None:
            return dir()
        else:
            return dir(obj)
    except Exception as e:
        return f"خطأ: فشل في الحصول على قائمة الملفات - {e}"


def clear():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


def مسح_المخرجات():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)


def نوم(seconds):
    time.sleep(seconds)


def رقم_عشوائي(start, end):
    try:
        return random.randint(start, end)

    except Exception as e:
        return f"خطأ: فشل في تنفيذ الأمر - {e}"


def اختيار_عشوائي(sequence):
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


def مضروب(numeber):
    return math.factorial(numeber)


def جيب(number):
    try:
        return math.sin(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب - {e}"


def جيب_التمام(number):
    try:
        return math.cos(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام - {e}"


def جيب_معكوس(number):
    try:
        return math.asin(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المعكوس - {e}"


def جيب_التمام_معكوس(number):
    try:
        return math.acos(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المعكوس - {e}"


def جيب_مستدير(number):
    try:
        return math.sinh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المستدير - {e}"


def جيب_تام_مستدير(number):
    try:
        return math.cosh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المستدير - {e}"


def جيب_معكوس_مستدير(number):
    try:
        return math.asinh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المعكوس المستدير - {e}"


def جيب_تام_معكوس_مستدير(number):
    try:
        return math.acosh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المعكوس المستدير - {e}"


def جيب_مزدوج(number):
    try:
        return math.sin(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المزدوج - {e}"


def جيب_تام_مزدوج(number):
    try:
        return math.cos(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المزدوج - {e}"


def جيب_معكوس_مزدوج(number):
    try:
        return math.degrees(math.asin(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المعكوس المزدوج - {e}"


def جيب_تام_معكوس_مزدوج(number):
    try:
        return math.degrees(math.acosh(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المعكوس المزدوج - {e}"


def جيب_مستدير_مزدوج(number):
    try:
        return math.sinh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المستدير المزدوج - {e}"


def جيب_تام_مستدير_مزدوج(number):
    try:
        return math.cosh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المستدير المزدوج - {e}"


def جيب_معكوس_مستدير_مزدوج(number):
    try:
        return math.degrees(math.acosh(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المعكوس المستدير المزدوج - {e}"


def جيب_التمام_معكوس_مستدير_مزدوج(number):
    try:
        return math.degrees(math.acosh(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المعكوس المستدير المزدوج - {e}"


def جيب_مزدوج_معكوس(number):
    try:
        return math.degrees(math.asin(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المزدوج المعكوس - {e}"


def جيب_تام_مزدوج_معكوس(number):
    try:
        return math.degrees(math.acos(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المزدوج المعكوس - {e}"


def جيب_مزدوج_مستدير(number):
    try:
        return math.sinh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المزدوج المستدير - {e}"


def جيب_تام_مزدوج_مستدير(number):
    try:
        return math.cosh(math.radians(number))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المزدوج المستدير - {e}"


def جيب_مزدوج_معكوس_مستدير(number):
    try:
        return math.degrees(math.asinh(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المزدوج المعكوس المستدير - {e}"


def جيب_تام_مزدوج_معكوس_مستدير(number):
    try:
        return math.degrees(math.acosh(math.radians(number)))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المزدوج المعكوس المستدير - {e}"


def جيب_مستدير_معكوس_مزدوج(number):
    try:
        return math.degrees(math.asin(math.sinh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المستدير المعكوس المزدوج - {e}"


def جيب_تام_مستدير_معكوس_مزدوج(number):
    try:
        return math.degrees(math.acos(math.cosh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المستدير المعكوس المزدوج - {e}"


def جيب_مزدوج_مستدير_معكوس(number):
    try:
        return math.degrees(math.asinh(math.sin(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المزدوج المستدير المعكوس - {e}"


def جيب_تام_مزدوج_مستدير_معكوس(number):
    try:
        return math.degrees(math.acosh(math.cos(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب التمام المزدوج المستدير المعكوس - {e}"


def جيب_مستدير_مزدوج_معكوس(number):
    try:
        return math.degrees(math.asin(math.sinh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المستدير المزدوج المعكوس - {e}"


def جيب_تام_مستدير_مزدوج_معكوس(number):
    try:
        return math.degrees(math.acos(math.cosh(math.radians(number))))
    except Exception as e:
        return f"خطأ: فشل في حساب جيب المستدير المزدوج المعكوس - {e}"


def مماس(number):
    try:
        return math.tan(number)
    except Exception as e:
        return f"خطأ: فشل في حساب المماس - {e}"


def مماس_عكوس(number):
    try:
        return math.atan(number)
    except Exception as e:
        return f"خطأ: فشل في حساب المماس - {e}"


def مماس_مستدير(number):
    try:
        return math.tanh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب المماس - {e}"


def مماس_معكوس_مستدير(number):
    try:
        return math.atanh(number)
    except Exception as e:
        return f"خطأ: فشل في حساب المماس - {e}"


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

# TODO:  Commented function could have been useful if it worked, find a way to make it work

# def إذا_أو_لكن(condition=False, body="", condition2=False, body2="", condition3=False, body3="", condition4=False, body4="", condition5=False, body5="", elsebody="", *args):
#     # Body has to be a string
#     l = len(args)
#     try:
#         print(args)
#         if l == 0:
#             print(f"خطأ: مدخلات خاطئة")

#         elif l == 1:
#             if condition:
#                 exec(body)

#         elif l == 2:
#             if condition:
#                 exec(body)
#             elif condition2:
#                 exec(body2)

#         elif l == 3:
#             if condition:
#                 exec(body)
#             elif condition2:
#                 exec(body2)
#             elif condition3:
#                 exec(body3)

#         elif l == 4:
#             if condition:
#                 exec(body)
#             elif condition2:
#                 exec(body2)
#             elif condition3:
#                 exec(body3)
#             elif condition4:
#                 exec(body4)

#         elif l == 5:
#             if condition:
#                 exec(body)
#             elif condition2:
#                 exec(body2)
#             elif condition3:
#                 exec(body3)
#             elif condition4:
#                 exec(body4)
#             elif condition5:
#                 exec(body5)

#         elif l == 6:
#             if condition:
#                 exec(body)
#             elif condition2:
#                 exec(body2)
#             elif condition3:
#                 exec(body3)
#             elif condition4:
#                 exec(body4)
#             elif condition5:
#                 exec(body5)
#             else:
#                 exec(elsebody)
#     except Exception as e:
#         print(f"خطأ: مدخلات خاطئة - {e}")


def إذا(condition, body):
    # Body has to be a string
    try:
        if condition:
            exec(f"{body}")
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو(condition, body, condition2, body2):
    try:
        if condition:
            exec(f"{body}")
        elif condition2:
            exec(f"{body2}")
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_أو(condition, body, condition2, body2, condition3, body3):
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
    try:
        if condition:
            exec(f"{body}")
        else:
            exec(elsebody)
    except Exception as e:
        print(f"خطأ: مدخلات خاطئة - {e}")


def إذا_أو_لكن(condition=False, body="", condition2=False, body2="", elsebody=""):
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

# ? Find a work-around for the issue in this function
def تعريف(name, parameters, body):
    try:
        exec(f"""
def {str(name)}({str(parameters)}): {str(body)}
globals()[str(name)] = {str(name)}
        """)
    except Exception as e:
        print(f"خطأ: فشل في تعريف الدالة - {e}")


def استيراد(module_name):
    try:
        exec(f"import {str(module_name)}")
    except Exception as e:
        return f"خطأ: فشل في استيراد الوحدة - {e}"


def استيراد_باسم(module_name, name):
    try:
        exec(f"import {str(module_name)} as {str(name)}")
    except Exception as e:
        return f"خطأ: فشل في استيراد الوحدة - {e}"


def استيراد_دالة_من(module_name, function):
    try:
        exec(f"from {str(module_name)} import {str(function)}")
    except Exception as e:
        return f"خطأ: فشل في استيراد الوحدة - {e}"


def يكون(val1, val2):
    if val1 is val2:
        return True
    else:
        return False


def ليس(val1, val2):
    if val1 is not val2:
        return True
    else:
        return False


def في(val1, val2):
    if val1 in val2:
        return True
    else:
        return False


def و(condition, condition2):
    if condition and condition2:
        return True
    else:
        return False


def أو(condition, condition2):
    if condition or condition2:
        return True
    else:
        return False


def حلقة_إلى(list, body):
    try:
        for i in list:
            exec(f"{str(body)}")
    except Exception as e:
        return f"خطأ: فشل في تنفيذ الحلقة - {e}"


def حلقة_حتى(condition, body):
    try:
        while condition:
            exec(f"{str(body)}")
    except Exception as e:
        return f"خطأ: فشل في تنفيذ الحلقة - {e}"


def حساب(equ):
    try:
        return (eval(str(equ)))
    except Exception as e:
        return f"خطأ: فشل في حساب العملية - {e}"


def ارجاع(obj):
    return obj


def تجربة(statement1, statement2):
    try:
        exec(f"{str(statement1)}")
    except:
        exec(f"{str(statement2)}")


def التأكيد(condition, message):
    assert condition, message


async def متزامن():
    pass


async def انتظر():
    await asyncio.sleep(0)


def خروج():
    exit()


def انهاء():
    quit()


class سلحفاة:
    def __init__(self):
        self.turtle = turtle.Turtle()

    def ضبط_الاتجاه(self, angle):
        self.turtle.setheading(float(angle))

    def للأمام(self, steps):
        self.turtle.forward(float(steps))

    def للخلف(self, steps):
        self.turtle.backward(float(steps))

    def لليمين(self, angle):
        self.turtle.right(float(angle))

    def لليسار(self, angle):
        self.turtle.left(float(angle))

    def رفع_القلم(self):
        self.turtle.penup()

    def إنزال_القلم(self):
        self.turtle.pendown()

    def مسح(self):
        self.turtle.clear()

    def الطابع_مسح(self, stampname):
        self.turtle.clearstamp(stampname)

    def الطوابع_مسح(self, stampname=None):
        self.turtle.clearstamps(stampname)

    def السرعة(self, speed):
        self.turtle.speed(float(speed))

    def إعادة_ضبط(self):
        self.turtle.reset()

    def بدء_الملء(self):
        self.turtle.begin_fill()

    def إنهاء_الملء(self):
        self.turtle.end_fill()

    def لون_الملء(self, color):
        self.turtle.fillcolor(f"{str(color)}")

    # TODO: FIX THIS FUNCTION
    def لون_السلحفاة(self, color="#000000", *args):
        if args:
            self.turtle.color(f"{str(color)}")
        else:
            self.turtle.color()

    def لون_القلم(self, color):
        self.turtle.pencolor(f"{str(color)}")

    def حجم_القلم(self, size):
        self.turtle.pensize(int(size))

    def هل_يرسم(self):
        return self.turtle.isdown()

    def الشكل(self, shape):
        self.turtle.shape(f"{str(shape)}")

    def حجم_الشكل(self, w=1, h=1, o=1):
        self.turtle.shapesize(float(w), float(h), float(o))

    def اذهب_إلى(self, x, y):
        self.turtle.goto(float(x), float(y))

    def دائرة(self, radius):
        self.turtle.circle(float(radius))

    def نقطة(self, size, color):
        self.turtle.dot(int(size), str(color))

    def مكان(self):
        return self.turtle.pos()

    def مكان_x(self):
        self.turtle.xcor()

    def مكان_y(self):
        self.turtle.ycor()

    def المنزل(self):
        self.turtle.home()

    def ضبط_x(self, pos):
        self.turtle.setx(float(pos))

    def ضبط_y(self, pos):
        self.turtle.sety(float(pos))

    def مسافة_بين(self, x, y):
        if x is not None and y is not None and y != 0 and x != 0:
            return self.turtle.distance(float(x), float(y))
        else:
            return "يجب أن يكون الرقمان أعلى من صفر"

    def مسافة_باتجاه(self, x, y):
        if x is not None and y is not None and y != 0 and x != 0:
            return self.turtle.towards(float(x), float(y))
        else:
            return "يجب أن يكون الرقمان أعلى من صفر"

    def اتجاه(self):
        return self.turtle.heading()

    def استنساخ(self):
        return self.turtle.clone()

    def درجة(self, num=360):
        self.turtle.degrees(num)

    def بدء_مضلع(self):
        self.turtle.begin_poly()

    def إنهاء_المضلع(self):
        self.turtle.end_poly()

    def هل_يملأ(self):
        return self.turtle.filling()

    def إحضار_المضلع(self):
        return self.turtle.get_poly()

    def إحضار_القلم(self):
        return self.turtle.getpen()

    def إحضار_الشاشة(self):
        return self.turtle.getscreen()

    def تعريف_شكل_المضلع(self):
        return self.turtle.get_shapepoly()

    def إحضار_السلحفاة(self):
        return self.turtle.getturtle()

    def إخفاء_السلحفاة(self):
        self.turtle.hideturtle

    def إخفاء(self):
        self.turtle.ht()

    def هل_ظاهر(self):
        return self.turtle.isvisible()

    def عند_الضغط(self, fun):
        self.turtle.onclick(fun)

    def عند_السحب(self, fun):
        self.turtle.ondrag(fun)

    def عند_الترك(self, fun):
        self.turtle.onrelease(fun)

    def صفات_القلم(self):
        return self.turtle.pen()

    def راديان(self):
        self.turtle.radians()

    def وضع_إعادة_التوسيع(self, rmode=None):
        if rmode is not None:
            self.turtle.resizemode(rmode)
        else:
            return self.turtle.resizemode()

    def زاوية_الانحراف_ضبط(self, angle):
        self.turtle.settiltangle(angle)

    def إلغاء_العملية_السابقة(self):
        self.turtle.undo()

    def تعريف_الشكل(self):
        self.turtle.shapetransform()

    def إظهار_السلحفاة(self):
        self.turtle.showturtle()

    def إنحراف(self, angle):
        self.turtle.tilt(angle)

    def زاوية_الإنحراف(self, angle):
        if angle is not None:
            self.turtle.tiltangle(angle)
        else:
            return self.turtle.tiltangle()

    def حجم_السلحفاة(self, w=None, h=None, o=None):
        if w is not None and h is not None and o is not None:
            self.turtle.turtlesize(w, h, o)
        else:
            return self.turtle.turtlesize()

    def عرض(self, w):
        if w is not None:
            self.turtle.width(w)
        else:
            return self.turtle.width()

    def كتابة(self, par="", move=False, align="left", font=("Arial", 8, "normal")):
        self.turtle.write(par, move, align, font)


class شاشة:
    def __init__(self):
        self.screen = turtle.Screen()

    def إضافة_شكل(self, sname):
        self.screen.addshape(sname)

    def تسجيل_شكل(self, sname, coords):
        self.screen.register_shape(sname, coords)

    def اعداد(self, width, height):
        self.screen.setup(int(width), int(height))

    def خروج_عند_الضغط(self):
        self.screen.exitonclick()

    def الحلقة_الأساسية(self):
        self.screen.mainloop()

    def تحديث(self):
        self.screen.update()

    def لون_الخلفية(self, color):
        self.screen.bgcolor(color)

    def صورة_الخلفية(self, color):
        self.screen.bgpic(color)

    def السلام_عليكم(self):
        self.screen.bye()

    def مسح_الشاشة(self):
        self.screen.clearscreen()

    def وضع_اللون(self, cmode=None):
        if cmode is not None:
            self.screen.colormode(cmode)
        else:
            return self.screen.colormode()

    def تأخير(self, sec=None):
        if sec is not None:
            self.screen.delay(sec)
        else:
            return self.screen.delay()

    def إحضار_اللوحة(self):
        return self.screen.getcanvas()

    def إحضار_الأشكال(self):
        return self.screen.getshapes()

    def إستماع(self):
        self.screen.listen()

    def وضع(self, mode=None):
        if mode is not None:
            self.screen.mode(mode)
        else:
            return self.screen.mode()

    def ىمدخل_رقم(self, title, prompt, default=None, minval=None, maxval=None):
        return self.screen.numinput(title, prompt, default, minval, maxval)

    def عند_مفتاح(self, fun, key):
        self.screen.onkey(fun, key)

    def عند_ضغط_مفتاح(self, fun, key):
        self.screen.onkeypress(fun, key)

    def عند_ترك_مفتاح(self, fun, key):
        self.screen.onkeyrelease(fun, key)

    def عند_ضغط_الشاشة(self, fun):
        self.screen.onscreenclick(fun)

    def عند_انتهاء_المؤقت(self, fun, t):
        self.screen.ontimer(fun, t)

    def إعادة_ضبط_الشاشة(self):
        self.screen.resetscreen()

    def حجم_الشاشة(self, width=None, height=None, background=None):
        if width is not None and height is not None and background is not None:
            self.screen.screensize(width, height, background)
        else:
            return self.screen.screensize()

    def إحداثيات_العالم(self, llx, lly, urx, ury):
        self.screen.setworldcoordinates(llx, lly, urx, ury)

    def مدخل_نصي(self, title, prompt):
        return self.screen.textinput(title, prompt)

    def عنوان_النافذة(self,title):
        self.screen.title(title)
    
    def مخطط(self, n, delay=None):
        if delay is None:
            self.screen.tracer(n)
        else:
            self.screen.tracer(n, delay)
    
    def إحضار_السلاحف(self):
        return self.screen.turtles()
    
    def عرض_النافذة(self):
        return self.screen.window_width()

    def طول_النافذة(self):
        return self.screen.window_height()