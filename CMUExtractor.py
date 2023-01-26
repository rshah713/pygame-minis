#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Convert CMU colors to RGB values using https://academy.cs.cmu.edu/docs/builtInColors
- Parse the CSV to extract color -> rgb
- Parse inputted code segment to identify all the colors
- Output in Python-friendly format



========================================================
Directions:
- Plug CMU CS colors into code.py
- Run & copy output into python program
"""

import csv

COLORS = {}
with open('CMUColors.csv', 'r') as CMUColors:
    reader = csv.reader(CMUColors)
    for row in reader:
        if row[0] != '':
            continue
        COLORS[row[1]] = row[3]

inp_f = open('code.py')
inp = inp_f.read()
inp_f.close()

colors_needed = {}

def parse_str(keyword):
    global colors_needed
    """
    keyword: either 'fill' or 'border'
    representing the keyword to parse based on
    CMU CS code
    """
    prev = 0
    for i in range(inp.count(keyword)):
        ind = inp.find(keyword, prev+1)
        if keyword == 'app.background =':
            # we know there's only 1 app.bg
            # we know it's at the top
            ind = inp.find(keyword, prev)
        prev = ind
        """
        the first char after 'fill=' or 'border='
        starting_char:
            -  ' representing raw color
            - 'r' representing rgb
            - 'N' representing None
            - 'g' representing gradient
        """
        starting_char = inp[ind+len(keyword)+1]
        if starting_char == "'":
            color = inp[ind+len(keyword)+2:inp.find(starting_char, ind+len(keyword)+2)]
            rgb = COLORS[color]
            colors_needed[color] = rgb
        elif starting_char == 'N':
            pass # None
        elif starting_char == 'r':
            pass # choosing not to process if its alr in rgb() form
        elif starting_char == 'g':
            gradient_ind = ind+len(keyword)+1
            close_paren_ind = inp.find(')', ind)
            substring = inp[gradient_ind:close_paren_ind+1]
            while substring.count('(') != substring.count(')'):
                # gradient(rgb(.., .., ..))
                # means ')' isn't ending gradient but rather rgb
                close_paren_ind = inp.find(')', close_paren_ind+1)
                substring = inp[gradient_ind:close_paren_ind+1]
            if substring.find('start') != -1:
                # if there's a start= arg, chop it off
                substring = substring.replace(substring[substring.find('start')-2:-1], '')
            substring = substring[len('gradient'):]
            if substring.find('rgb') != -1:
                # if rgb vals are nested in there
                # eval() fails
                return
            for color in eval(substring):
                rgb = COLORS[color]
                colors_needed[color] = rgb

parse_str('border')
parse_str('fill')
parse_str('app.background =')

"""
Format into Python variables for easy copy-paste
"""
for k, v in colors_needed.items():
    print("{} = ({})".format(k.upper(), v))
