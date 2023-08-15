import os,platform,time
 
bitt=platform.architecture()[0]
 
if bitt=="32bit":
    import code32
elif bitt=="64bit":
    import code64
