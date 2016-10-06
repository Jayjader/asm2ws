#! /usr/bin/python

import sys

# commands
'''
cmds_stack = ('push', 'duplicate', 'swap', 'discard')
cmds_arith = ('add', 'sub', 'multiply', 'divide', 'mod')
cmds_heap = ('store', 'retrieve')
cmds_flow = ('label', 'call', 'jump', 'jumpz', 'jumpn', 'endcall', 'endprog')
cmds_io = ('writec', 'writen', 'readc', 'readn')
'''
imps = {
        'stack' :       ' ',
        'arithmetic' :  '\t ',
        'heap'       :  '\t\t',
        'flow'       :  '\n',
        'io'         :  '\t\n',
        }
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

asm_file = open(sys.argv[1], 'r')
asm = asm_file.read()
# Decode to unicode and split into words
asm = asm.decode().split()

ws = ''
line = 0

while len(asm) > 0:
    word = asm.pop(0)
    line += 1
    # Parse for Instruction Modification Parameter (IMP), then Command,
    # then (if relevant) Parameter
    try:
        command = commands[word]
        ws += imps[command]
        ws += command['cmd']

        if word == 'push':
            pass
    except KeyError:
        print('Error! {0} is not a valid command (line {1})'.format([word, line]))
        sys.exit(1)


ws_file = open(sys.argv[1][:-6], 'wb')
