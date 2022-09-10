# YCDB
----

Yahoo Column-aware DB

Data is partitioned into multiple database (hashcode%n), in each database, keys can be continuously partitioned into windows (1byte), tables and rows.
Each row contains at most 16 slots, which keep the conflicted key-values, linear scan to locate the slot, a bloom filter in each slot for quick check.

Window/Table/Row is multiple layers hashing mechanism.

![[Archive/工作资料/Gemini/_resources/YCDB.resources/unknown_filename.2.png]]

![[Archive/工作资料/Gemini/_resources/YCDB.resources/unknown_filename.png]]

![[Archive/工作资料/Gemini/_resources/YCDB.resources/unknown_filename.1.png]]



\-bash-4.1$ hostname
[mds3.cbs.cb.bf1.yahoo.com](http://mds3.cbs.cb.bf1.yahoo.com)
\-bash-4.1$ pwd
/home/y/var/curveball\_segment\_gds
\-bash-4.1$ ls
segment\_p26.ycdb  segment\_p27.ycdb  segment\_p28.ycdb  segment\_p29.ycdb  segment\_p30.ycdb  segment\_p31.ycdb  segment\_p32.ycdb  segment\_p33.ycdb  segment\_p34.ycdb  segment\_p35.ycdb  segment\_p36.ycdb  segment\_p37.ycdb  segment\_p38.ycdb
\-bash-4.1$ ls segment\_p26.ycdb
db.master     window\_00000  window\_00001  window\_00002  ... (256 windows)

\-bash-4.1$ ll segment\_p26.ycdb/window\_00\*/\*
\-rwxr-xr-x 1 root root 3174400 Jan 17 01:18 segment\_p26.ycdb/window\_00000/table.0000
\-rwxr-xr-x 1 root root 3174400 Jan 17 01:18 segment\_p26.ycdb/window\_00001/table.0000
\-rwxr-xr-x 1 root root 3174400 Jan 17 01:18 segment\_p26.ycdb/window\_00002/table.0000
... (each window directory contains one table file, all tables are in size 3174400)

\-bash-4.1$ ycdb\_stat -d segment\_p27.ycdb -p .
Tables      =     256                      Disk Usage =  815931452 (778.1M)
Defrags     =       0                  User Data Size =   32114666 (30.6M)
Splits      =       0                    Storage Size =   61256814 (58.4M)
Expansions  =       0                 Fragmented Size =          0 (0)
Keys        =  341389            Key Size (sum / avg) =    8199660 / 24
Utilization =    3.94%         Value Size (sum / avg) =   23915006 / 70
Writable    =   92.49%                  Writable Size =  754654098 (719.7M)
Overhead    =    3.57%                  Overhead Size =   29162688 (27.8M)
Hash        = YCDB\_MurmurHash3\_128 (seed = 12345)
Windows     =     256                  Max Tables/Win =       2048
Inserts     =  341389                           Reads =          0
Updates     =       0                         Deletes =          0
Table COWs  =       0
Schema:
  col1                 =\> YCDB\_BYTES\_T

----

- Date: 2019-03-21
- Tags: #Interview/Gemini 



