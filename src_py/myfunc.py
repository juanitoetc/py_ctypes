import ctypes
import os
from _ctypes import addressof

_sum = ctypes.CDLL('/home/juani/EclipseWorkspace/myClibrary/Debug/libmyClibrary.so')
_sum.our_function.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_sum.square_array.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
_sum.structFill.argtype = (ctypes.c_void_p)

class polarXY(ctypes.Structure):
     _fields_ = [("intX", ctypes.c_int),
                ("intY", ctypes.c_int)]

def our_function(numbers):
    global _sum
    num_numbers = len(numbers)
    array_type = ctypes.c_int * num_numbers
    result = _sum.our_function(ctypes.c_int(num_numbers), array_type(*numbers))
    return int(result)
     
def square_list(liInput):
    global _sum
     
    list_len = len(liInput)
    listZeros = [0] * list_len
     
    dArrayIn = ctypes.c_double * list_len      #Input: array of "ctype specific object" and size "len"
    dArrayOut = ctypes.c_double * list_len     #Returned value
     
    #unpacking arguments, so the elements can be pass as different parameters
    dInput = dArrayIn(*liInput)
    dOutput = dArrayOut(*listZeros)
     
    #call C function
    _sum.square_array(ctypes.c_int(list_len), dInput, dOutput)
    return dOutput

#Funtion which recibes a list of two elements and fill the fields of the structure
def vpGetNumber(lsXY):
    #Generate the empty structure
    varPolar = polarXY()
    varPolar.intX = 10
    varPolar.intY= 12
    ptPolar = ctypes.pointer(varPolar)
    #Casting it using addressof as a void pointer
    #vpStruct = ctypes.cast(ptPolar, ctypes.c_void_p)
    #Call the C function for filling
    _sum.structFill(ptPolar)
    print("Hello")
    
    