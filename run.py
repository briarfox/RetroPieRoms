#!/usr/bin/env python
'''
get system url
list - show current roms
get romname - get previously downlaoded rom 
'''
import subprocess
import cmd
from parseroms import get_link, load,parse_roms
system = {'nes': 'nes',
           'snes': 'snes',
           'psx': 'psx'}
           
EmulatorPath = 'RetroPie/roms'

roms = load()

class GetRom(cmd.Cmd):
    
    def do_find(self,line):
        arg = line.split(' ',1)
        if len(arg)< 2:
            print 'usage: find [system] [game]'
            return
        try:
            for name,url in roms[arg[0]].items():
                if arg[1].lower() in name.lower():
                    print name
        except :
            print 'Invalid system Must be:'
            for name in system:
                print name

    
    def do_get(self,line):
        arg = line.split(' ',1)
        if len(arg)< 2:
            print 'usage: get [system] [game]'
            return
        try:
            con = system[arg[0]]
            url = get_link(roms[con][arg[1]])
            print 'Downloading %s - %s' % (con,arg[1])
            print url
            subprocess.call('sudo ./getrom.sh %s %s'% (con,url),shell=True)
        except :
            print 'Game not found'
            return
        
    def do_update(self):
        print 'This may take some time...'
        parse_roms()
        roms = load()
        
    def do_quit(self,line):
        return True
    

GetRom().cmdloop()
