# Caesar Cipher Tool
==================

A simple Python implementation of the Caesar cipher with encrypt/decrypt functions and an interactive CLI menu for easy use. [web:10]

Features
- Encrypts/decrypts messages with configurable shift (1-25).
- Handles both uppercase and lowercase letters.
- Preserves spaces and punctuation.
- Interactive loop menu for repeated operations.
- Input validation and error handling. [web:14]

# Usage
-----
(In terminal)
python caesar_cipher.py

# Installation
------------
1. Open this repo in GitHub Codespaces.
2. In the terminal, run: python caesar_cipher.py

# How it Works
------------
A Caesar Cipher works by shifting the each letter in a message by a fixed number of positions in the alphabet to create a simple code. 
Named after Julius Caesar, who used it for secret messages, it wraps around the alphabet so Z shifts to A if needed. 
For example, with a shift of 3, "A" becomes "D," "B" becomes "E," and "XYZ" becomes "ABC.

# Functions
---------
- caesar_encrypt(text: str, shift: int) -> str
- caesar_decrypt(text: str, shift: int) -> str

# License
---------
Python Caesar Cipher © 2025 by The-R34per is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/
