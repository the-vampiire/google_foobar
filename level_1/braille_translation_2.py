def answer(plaintext):
# formats the six-bit binary from the source format to expected format
  def formatBinary(char):
    capital = False
    if char.isupper():
      char = char.lower()
      capital = True

    binary = ascii_to_braile_six_bit_binary[char]

    original = list(binary)
    formatted = []

    conversionDict = { '0':'0', '1':'3', '2':'1', '3':'4', '4':'2', '5':'5' }

    index = 0
    while(index < len(original)):
      newIndex = int(conversionDict[str(index)])

      formatted.insert(newIndex, original[index]) # risky....
      index += 1

    if capital: formatted.insert(0, ascii_to_braile_six_bit_binary[','])
    return formatted

# source braille six-bit binary dictionary
  ascii_to_braile_six_bit_binary = {
    'a': '100000', 'b': '101000', 'c': '110000', 'd': '110100', 'e': '100100',
    'f': '111000', 'g': '111100', 'h': '101100', 'i': '011000', 'j': '011100',
    'k': '100010', 'l': '101010', 'm': '110010', 'n': '110110', 'o': '100110',
    'p': '111010', 'q': '111110', 'r': '101110', 's': '011010', 't': '011110',
    'u': '100011', 'v': '101011', 'w': '011101', 'x': '110011', 'y': '110111',
    'z': '100111', ' ': '000000', '!': '011011', '"': '000100', '#': '010111',
    '$': '111001', '%': '110001', '&': '111011', "'": '000010', '(': '101111',
    ')': '011111', '*': '100001', '+': '010011', ',': '000001', '-': '000011',
    '.': '010001', '/': '010010', '0': '000111', '1': '001000', '2': '001010',
    '3': '001100', '4': '001101', '5': '001001', '6': '001110', '7': '001111',
    '8': '001011', '9': '000110', ':': '100101', ';': '000101', '<': '101001',
    '=': '111111', '>': '010110', '?': '110101', '[': '011001', '\\': '101101',
    ']': '111101', '^': '010100', '_': '010101', '@': '010000'
  }

  formatted = map(lambda char: formatBinary(char), plaintext)
  output = ""
  for sixBit in formatted:
    for bit in sixBit:
      output += bit

  return output


"""
Problem Statement:

Braille Translation
===================

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never 
bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating 
her space station. You figure printing out Braille signs will help them, and - since you'll be promoting efficiency 
at the same time - increase your chances of a promotion. 

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 
grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station 
to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read" 
the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the 
following order:
1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string 
"100100101010100110100010".

"""

"""
Approach:

Letter c (lower) in binary: 01100011
Letter C (upper) in binary: 01000011
Expected output of c:       100100

Letter o (lower) in binary: 01101111
Letter O (upper) in binary: 01001111
Expected output of o:       101010

Letter d (lower) in binary: 01100100
Letter D (upper) in binary: 01000100
Expected output of d:       100110

Letter e (lower) in binary: 01100101
Letter E (upper) in binary: 01000101
Expected output of e:       100010

Input string:                                c     o      d      e
Expected output string (spaces inserted): 100100 101010 100110 100010

Pattern:

  binary representation of ASCII character contains 8 binary bits
  braille expected output contains 6 bits
    No discernable "trimming" pattern emerges
    2 bits are trimmed but the result is still in binary...google "6 digit binary" 
  

"6 digit binary" Results:

  https://en.wikipedia.org/wiki/Six-bit_character_code
    "Braille characters are represented using six dot positions, arranged in a rectangle. Each position may contain a raised dot or not, so Braille can be considered to be a six-bit binary code"
  
  Note: 6-bits can only encode 64 characters 
  Confirmation: Letter C -> https://en.wikipedia.org/wiki/File:Braille_C3.svg -> matches example
    Conclusion: the system is using Earth based braille glyphs 

Resources:
  
  https://en.wikipedia.org/wiki/Braille_ASCII
    used table at bottom of page for ascii_to_six_bit_binary dictionary
    Note 1: only handles lowercase letters 

Approach: write an ASCII to 6-bit binary Braille converter
  Input: ASCII string
  Output: Concatenated 6-bit binary Braille representation for each character in the string
    Note 1: consider the order that is requested
      Irrelevant to the expected concatenated output string (direct order)
    Note 2: what about characters not included in the 6-bit set? 
      Test for ASCII in Python?
    Note 3: only capital alphabet characters are included in the set
      Convert the string to capital letters before conversion
    Note 4: what about capital letters?
      http://6dotbraille.com/
        "There are no capital letters in Braille. A "capital sign" Braille cell (dot 6) is inserted before a lower case letter to produce a "Capital Letter""
          The "capital sign" is represented by a comma or in six-bit binary (from the above dict) "000001"

EDITS:
  Key errors were caused by an incomplete dictionary
  Name error was caused by improper indentation of the ascii_* dictionary
  Note 4 came to fruition and required an adjustment to the code to accomodate for including a "capital sign" 
    
Passed all test cases after edits

"""