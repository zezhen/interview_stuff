
# download by 940 + 941|942|943|944|972|975|979

ids = map(str, [    777,892,497,528,710,398,519,292,329,382,470,846,478,855,587,319 ])

import sys, os

src = '/Users/zezhen/Dropbox/leetcode/backup/'
dest = '/Users/zezhen/Dropbox/leetcode/next/Other'
for filename in os.listdir(src):
    _id = filename.split('_')[0][1:]

    if _id in ids:
        print os.path.join(src, filename), os.path.join(dest, filename)
        os.rename(os.path.join(src, filename), os.path.join(dest, filename))
        