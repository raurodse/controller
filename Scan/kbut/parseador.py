#!/usr/bin/env python
'''

Left Hand


S0x00 S0x01 S0x02 S0x03 S0x04 S0x05 S0x06
S0x10 S0x11 S0x12 S0x13 S0x14 S0x15 S0x16
S0x20 S0x21 S0x22 S0x23 S0x24 S0x25 S0x26
S0x30 S0x31 S0x32 S0x33 S0x34 S0x35 

				S0x7  S0x17  S0x27 S0x37

Right Hand

S0x4E S0x4D S0x4C S0x4B S0x4A S0x49 S0X48
S0x5E S0x5D S0x5C S0x5B S0x5A S0x59 S0X58
S0x6E S0x6D S0x6C S0x6B S0x6A S0x69 S0X68
      S0x7D S0x7C S0x7B S0x7A S0x79 S0X78

  S0x7F  S0x6F  S0X5F  S0X4F 

'''

lh = [
         '`'   , '1' , '2' , '3' , '4' , '5' , 'f1' ,
	'Tab'  , 'q' , 'w' , 'e' , 'r' , 't' , 'f2' ,
	  ''   , 'a' , 's' , 'd' , 'f' , 'g' , 'f3' ,
	'Esc'  , 'z' , 'x' , 'c' , 'v' , 'b' ,
		   'Alt' , 'Return' , 'Ctrl' , 'function1'
]

lh = [
        'f4' , '6' , '7' , '8' , '9' , '0' , '=' ,
	'f5' , 'y' , 'u' , 'i' , 'o' , 'p' , '' ,
	'f6' , 'h' , 'j' , 'k' , 'l' , ';' , '' ,
	       'n' , 'm' , ',' , '.' , '/' , '' ,
    'Function2' , 'LGui' , 'Space' , 'Backspace'
]

f = open('new_scancode_map.kll','w')
f.write()
f.close()