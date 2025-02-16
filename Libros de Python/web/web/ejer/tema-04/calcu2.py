
import pygtk
pygtk.require('2.0')
import gtk

from math import *
import util

safe_list = [
    'math','acos', 'asin', 'atan', 'abs', 'atan2', 'ceil',
    'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs',
    'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
    'log10', 'modf', 'pi', 'pow', 'radians', 'sin',
    'sinh', 'sqrt', 'tan', 'tanh'
    ]

safe_dict = dict (
    [(k, locals ().get (k, None))
     for k in safe_list ])

def handle_operation (entry, label, state):
    inexpr = entry.props.text
    try:
        res = eval (inexpr, state)
        label.props.label = str (res)
    except Exception, err:
        util.show_error_dialog (
            "Error", "Orden incorrecta:\n" +
            str (err))

def calculadora ():
    win = gtk.Window ()
    win.connect ('destroy', gtk.main_quit)
    win.props.title = "Huber calculadora!"
    
    box = gtk.VBox (False, 0)
    win.add (box)

    label = gtk.Label (" = 0")
    entry = gtk.Entry ()
    entry.connect ("activate", handle_operation, label, safe_dict)
    
    box.pack_start (entry)
    box.pack_start (label)

    win.show_all ()
    gtk.main ()

if __name__ == '__main__':
    calculadora ()
