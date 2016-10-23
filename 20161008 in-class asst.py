#!/usr/bin/python3

"""
10-08 in-class assignment

1. implement a test case with 5+ assertEqual() calls verifying that a method in re or os.path works properly

2. write a program whose user specifies the path to a pickle file containing a positive integer, implement a test case which causes & catches 3+ kinds of exceptions.

"""
##################################################################

import unittest
import os.path
import os


class test_OSpath(unittest.TestCase):
    def test_split(self):
        filepath = os.path.realpath(__file__) # we make an assumption that os.path.realpath works correctly
        filename = os.path.basename(__file__) # we make an assumption that os.path.basename works correctly
        
        cwd = os.getcwd()
        self.assertEqual(os.path.split(filepath)[0], cwd)
        
        dirname = os.path.dirname(filepath)
        self.assertEqual(os.path.split(filepath)[0], dirname)
        
        self.assertEqual(len(os.path.split(filepath)), 2)
        self.assertEqual(os.path.split(filepath)[1], filename)
        
        fakepath = '/something/else/does/not/exist.fml'
        self.assertEqual(len(os.path.split(fakepath)), 2)
        self.assertEqual(os.path.split(fakepath)[0], '/something/else/does/not')
        self.assertEqual(os.path.split(fakepath)[1], 'exist.fml')
           
           
##################################################################

import pickle

picklefile = 'filename.pickle'
goodvar = 3

def setup():
    a = goodvar
    with open(picklefile, 'wb') as handle:
        pickle.dump(a, handle)
        
def badsetup():
    a = 'pickled string'
    with open(picklefile, 'wb') as handle:
        pickle.dump(a, handle)
        
#setup()

def validate(picklefile):
    with open(picklefile, 'rb') as handle:
        b = pickle.load(handle)
        print(goodvar == b)


class test_Pickle(unittest.TestCase):
    def test_filenotfound(self):
        setup()
        wrongname = input("Please enter filename: ")
        with self.assertRaises(FileNotFoundError):
            validate(wrongname)
            
    def test_wrongcontenttype(self):
        setup()
        with self.assertRaises(TypeError):
            with open(picklefile, 'rb') as handle:
                b = pickle.load(handle)
                print(b + 'abc')
                
    def test_tamperedfile(self):
        setup()
        with open(picklefile, 'w') as handle:
            handle.write("some bogus text")
        with self.assertRaises(pickle.UnpicklingError):
            validate(picklefile)
            
    def test_wrongcontent(self):
        badsetup()
        with self.assertRaises(TypeError):
            validate(picklefile)
            
        
        




        
unittest.main(verbosity=2)