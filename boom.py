import zlib
import zipfile

test = "0000" * 1000

cmpstr = zlib.compress(test.encode('utf-8'))

to_cmp = test + str(cmpstr)
cmpstr = zlib.compress(to_cmp.encode('utf-8'))

zf = zipfile.ZipFile("test.zip" ,mode='w',compression=zipfile.ZIP_DEFLATED)

zf.writestr('a.txt',test)
