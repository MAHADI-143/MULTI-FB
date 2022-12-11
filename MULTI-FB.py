import os, sys
try:
    __import__("MULTI").login()
except Exception as e:
    exit(str(e))
