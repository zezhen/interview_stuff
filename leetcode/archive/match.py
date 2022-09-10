
import sys
import os

srcD = sys.argv[1]
destD = sys.argv[2]

_map = {}
srcfiles = [f for f in os.listdir(srcD) if f.endswith('py')]
for f in srcfiles:
    basename = os.path.basename(f)
    prefix = basename.split('_')[0]
    _map[prefix] = basename

for f in os.listdir(destD):
    basename = os.path.basename(f)
    filename = os.path.splitext(basename)[0]
    if filename.startswith('hard_'):
        filename = filename.replace('hard_', 'h')
    if filename in _map:
        print f
        os.rename(os.path.join(destD,f), os.path.join(destD,_map[filename]))
        os.remove(os.path.join(srcD,_map[filename]))
        
