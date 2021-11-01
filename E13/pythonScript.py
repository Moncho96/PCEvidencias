# -*- coding: iso-8859-1 -*-
import subprocess, sys

p = subprocess.Popen(["powershell.exe", 
        "C:\\Users\Moncho\Documents\GitHub\PCEvidencias\E13\psScript.ps1"], 
        stdout=sys.stdout)
p.communicate()