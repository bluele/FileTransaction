# Filetransaction
# Copyright 2012 Jun Kimura
# LICENSE MIT
# -*- coding: utf-8 -*-
from os.path import abspath
from shutil import copy2, copyfileobj, copyfile, move
from tempfile import NamedTemporaryFile

def ftopen(*args, **kw):
    return _FopenClass(*args, **kw)

class _FopenClass(object):
    
    def __init__(self, path, mode):
        '''
        @param path: file path
        @param mode: file open mode
        '''
        self.master = {
            'path' : abspath(path),
            'mode' : mode
        }
        
    def __del__(self):
        '''
        @summary: destructor
        '''
        self.ftemp.close()
        
    def __enter__(self):
        ''' 
        @summary: enter with-block
        '''
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        '''
        @summary: exit with-block
        '''
        if exc_type:
            self.rollback()
        else:
            self.commit()
            
    def start(self):
        '''
        @summary: start transaction
        '''
        try:
            self.ftemp = NamedTemporaryFile()
        except:
            raise
    
    def write(self, value):
        '''
        @summary: write temp file.
        '''
        try:
            self.ftemp.write(value)
        except:
            raise
        
    def writelines(self, seq):
        '''
        @summary: write temp file.
        '''
        try:
            self.ftemp.writelines(seq)
        except:
            raise
    
    def rollback(self):
        ''' 
        @summary: rollback
        '''
        try:
            self.ftemp.close()
        except:
            raise
    
    def commit(self):
        '''
        @summary: commit transaction
        '''
        try:
            self.ftemp.flush()
            self.ftemp.seek(0)
            copy2(self.ftemp.name, self.master['path'])
        except:
            raise
