import zlib

test = "0000" * 1000

cmpstr = zlib.compress(test.encode('utf-8'))
print(len(cmpstr), "vs " , len(test)) 

to_cmp = test + str(cmpstr)
cmpstr = zlib.compress(to_cmp.encode('utf-8'))

print(len(cmpstr))
