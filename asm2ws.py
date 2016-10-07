#! /usr/bin/python

import sys

# Characters for numbers and labels
characters = {'0' : ' ', '1' : '\t'}

# number -> Whitespace
def number(n):
    n = int(n)
    code = str(int(n<0)) + format(abs(n), 'b')
    word = ''
    for c in code:
        word += characters[c]
    return word

# label -> Whitespace
def label(l):
    assert (set(l) == {'0', '1'}), l
    word = ''
    for c in l:
        word += characters[c]
    return word

# Instruction Modification Parameters
imps = {
        'stack' :       ' ',
        'arithmetic' :  '\t ',
        'heap'       :  '\t\t',
        'flow'       :  '\n',
        'io'         :  '\t\n',
        }
# Commands
commands = {
        'push'      :   {'cmd' : ' ',     'imp' : 'stack'},
        'duplicate' :   {'cmd' : '\n ',   'imp' : 'stack'},
        'swap'      :   {'cmd' : '\n\t',  'imp' : 'stack'},
        'discard'   :   {'cmd' : '\n\n',  'imp' : 'stack'},

        'add'       :   {'cmd' : '  ',    'imp' : 'arithmetic'},
        'sub'       :   {'cmd' : ' \t',   'imp' : 'arithmetic'},
        'multiply'  :   {'cmd' : ' \n',   'imp' : 'arithmetic'},
        'divide'    :   {'cmd' : '\t ',   'imp' : 'arithmetic'},
        'mod'       :   {'cmd' : '\t\t',  'imp' : 'arithmetic'},

        'store'     :   {'cmd' : ' ',     'imp' : 'heap'},
        'retrieve'  :   {'cmd' : '\t',    'imp' : 'heap'},

        'label'     :   {'cmd' : '  ',    'imp' : 'flow'},
        'call'      :   {'cmd' : ' \t',   'imp' : 'flow'},
        'jump'      :   {'cmd' : ' \n',   'imp' : 'flow'},
        'jumpz'     :   {'cmd' : '\t ',   'imp' : 'flow'},
        'jumpn'     :   {'cmd' : '\t\t',  'imp' : 'flow'},
        'endcall'   :   {'cmd' : '\t\n',  'imp' : 'flow'},
        'endprog'   :   {'cmd' : '\n\n',  'imp' : 'flow'},

        'writec'    :   {'cmd' : '  ',    'imp' : 'io'},
        'writen'    :   {'cmd' : ' \t',   'imp' : 'io'},
        'readc'     :   {'cmd' : '\t ',   'imp' : 'io'},
        'readn'     :   {'cmd' : '\t\t',  'imp' : 'io'},
        }

# command -> Whitespace
def command(cmd):
    # Parse for IMP and Command
    cmd = commands[word]
    return imps[cmd['imp']] + cmd['cmd']


if __name__ == '__main__':
    asm_file = open(sys.argv[1], 'r')
    asm = asm_file.read()
    # Split into words
    asm = asm.split()

    ws = ''
    line = 0

    # Parse one by one
    while len(asm) > 0:
        word = asm.pop(0)
        line += 1
        try:
            # Translate command 
            ws += command(word)

            # Push has a number parameter
            if word == 'push':
                word = asm.pop(0)
                ws += number(word) + '\n'
            # Commands that require a label parameter
            elif commands[word]['imp'] == 'flow' and word[:3] != 'end':
                word = asm.pop(0)
                ws += label(word) + '\n'

        except ValueError:
            print('Error! {0} is not a valid number (line {1})'.format(word, line))
            sys.exit(1)
        except KeyError:
            print('Error! {0} is not a valid command (line {1})'.format(word, line))
            sys.exit(1)


    # Write Whitespace code to file
    ws_file = open(sys.argv[1][:-5] + 'ws', 'wb')
    ws_file.write(ws.encode())
    ws_file.close()
