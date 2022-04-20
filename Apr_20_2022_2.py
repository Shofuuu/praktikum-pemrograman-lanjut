#!/usr/bin/python3

# Exception importing module
try:
    from tkinter import *
    print("Successfully imported tkinter!")
except ImportError:
    print("Tkinter is not installed")
    exit(1)

# Exception missing file while using fopen
try:
    f = open("test.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
    exit(1)