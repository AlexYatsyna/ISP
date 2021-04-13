import inspect
import copy
import json
import dis
import opcode
import weakref

from modules.consoleParser import * 
from modules.try1 import t
_extract_code_globals_cache = weakref.WeakKeyDictionary()
STORE_GLOBAL = opcode.opmap['STORE_GLOBAL']
DELETE_GLOBAL = opcode.opmap['DELETE_GLOBAL']
LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']
GLOBAL_OPS = (STORE_GLOBAL, DELETE_GLOBAL, LOAD_GLOBAL)
t = 10
def _extract_code_globals(co):
    out_names = _extract_code_globals_cache.get(co)
    if out_names is None:
        names = co.co_names
        out_names = {names[oparg] for _, oparg in _walk_global_ops(co)}
        if co.co_consts:
            for const in co.co_consts:
                if isinstance(const, types.CodeType):
                    out_names |= _extract_code_globals(const)
        _extract_code_globals_cache[co] = out_names
    return out_names
def _walk_global_ops(code):
    for instr in dis.get_instructions(code):
        op = instr.opcode
        if op in GLOBAL_OPS:
            yield op, instr.arg

class Test:
    address = "Pushkina"

class User:
    name='alex'
    def s(self):
        return self.name

def GGG(a,b):
    return a+t+b

class MySerializer:
    def obj_dic(self,obj):

        if inspect.isclass(obj):

            dic = {'__type__': 'class','__class__': str(obj)}

            for attribute in dir(obj):
                
                if attribute.startswith('__') :
                    continue
                else:
                    value=getattr(obj,attribute)
                if "<class 'type'>" in str(value.__class__):
                    dic[attribute] = self.obj_dic(value)

                elif "<class '__main__." in str(value.__class__):
                    dic[attribute] = self.obj_dic(obj)
                    
                elif callable(value):
                    dic[attribute] = self.obj_dic(value)

                else:
                    dic[attribute] = value

            return dic
                
        elif inspect.isfunction(obj) or inspect.ismethod(obj):
            temp_list=[]
            argumets = {}
            dic = {'__type__': 'function'}

            argumets['co_argcount'] = repr(obj.__code__.co_argcount)
            argumets['co_posonlyargcount'] = repr(obj.__code__.co_posonlyargcount)
            argumets['co_kwonlyargcount'] = repr(obj.__code__.co_kwonlyargcount)
            argumets['co_nlocals'] = repr(obj.__code__.co_nlocals)
            argumets['co_stacksize'] = repr(obj.__code__.co_stacksize)
            argumets['co_flags'] = repr(obj.__code__.co_flags)
            argumets['co_code'] = obj.__code__.co_code.hex()
            argumets['co_consts'] = list(obj.__code__.co_consts)
            argumets['co_names'] = list(obj.__code__.co_names)
            argumets['co_varnames'] = list(obj.__code__.co_varnames) 
            argumets['co_filename'] = repr(obj.__code__.co_filename)
            argumets['co_name'] = repr(obj.__code__.co_name)
            argumets['co_firstlineno'] = repr(obj.__code__.co_firstlineno)
            argumets['co_lnotab'] =obj.__code__.co_lnotab.hex()
            dic['args'] = argumets

            gl = _extract_code_globals(obj.__code__)
            gla = {}
            gla['__builtins__'] = '<module \'builtins\' (built-in)>'

            for glob in gl:
                if glob in globals() :
                    gla[glob] = repr(globals().get(glob))
            dic['globals'] = gla

            return dic
        else:
            dic = {'__type__':'object','__class__':obj.__class__.__name__}
            for attribute in obj.__dir__():
                if attribute.startswith('__'):
                    continue
                else:
                    value=getattr(obj,attribute)
                if callable(value):
                    dic[attribute] = self.obj_dic(value)
                elif "<class '__main__." in str(value.__class__):
                    dic[attribute] = self.obj_dic(value)
                else:
                    dic[attribute]=value
            return dic


 
def SaveToJson(dic):
    stri = "{"

    for key in dic:

        if isinstance (dic[key], dict):

            temp = SaveToJson(dic[key])
            stri+= "\""+key+"\""+": "+temp + ", "
            continue

        elif isinstance(dic[key],list):

            stri+="\""+key+"\""+": ["

            for i in range(len(dic[key])):

                if isinstance(dic[key][i],str):
                    stri+="\""+dic[key][i]+"\", "

            if stri.endswith(", "):
                stri=stri[:len(stri)-2]+"], "
            else:
                stri+="] ,"

        else:
            if isinstance(dic[key],str):
                stri+= "\""+key+"\""+": "+"\""+dic[key]+"\""+", "

    if stri.endswith(", "):
        stri=stri[:(len(stri)-2)]+"}"
    else:
        stri+="}"

    return stri
