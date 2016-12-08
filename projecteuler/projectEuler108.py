# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

In the following equation x, y, and n are positive integers.     n*(x+y)=xy

weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module

# test the correction by a small dimension first. 
# test  brute force first, method1

#then, try some smart method! 

#this function is not unidirectional!, 
# it is repeatable, 
def f(n):
    c=0
    for x in range(2*n,n,-1):
        if n*x%(x-n)==0: c=c+1
    return c
    
def test():
    assert "f(4)==3"
    #print f(10**7)  #113

#brute force to too slow, 
def method1(M):
    #
    for i in range(4,2*10**4):
        if i>10000 and i<10300: print("searched to i=",i, f(i))
        if f(i)>M: 
            print("found the solution as: ", i) 
            break
    print("finished the search to i=", i)
    


def problem():
    method1(10**3)
    
if __name__ == "__main__":
    test()
    problem()
    #timeit(func, param)
    
"""
searched to i= 10001 5
searched to i= 10002 14
searched to i= 10003 5
searched to i= 10004 23
searched to i= 10005 41
searched to i= 10006 5
searched to i= 10007 2
searched to i= 10008 53
searched to i= 10009 2
searched to i= 10010 122
searched to i= 10011 14
searched to i= 10012 8
searched to i= 10013 14
searched to i= 10014 14
searched to i= 10015 5
searched to i= 10016 17
searched to i= 10017 32
searched to i= 10018 5
searched to i= 10019 5
searched to i= 10020 68
searched to i= 10021 5
searched to i= 10022 5
searched to i= 10023 14
searched to i= 10024 32
searched to i= 10025 8
searched to i= 10026 23
searched to i= 10027 5
searched to i= 10028 23
searched to i= 10029 5
searched to i= 10030 41
searched to i= 10031 5
searched to i= 10032 122
searched to i= 10033 5
searched to i= 10034 14
searched to i= 10035 23
searched to i= 10036 23
searched to i= 10037 2
searched to i= 10038 41
searched to i= 10039 2
searched to i= 10040 32
searched to i= 10041 5
searched to i= 10042 5
searched to i= 10043 8
searched to i= 10044 68
searched to i= 10045 23
searched to i= 10046 5
searched to i= 10047 14
searched to i= 10048 20
searched to i= 10049 5
searched to i= 10050 68
searched to i= 10051 8
searched to i= 10052 23
searched to i= 10053 8
searched to i= 10054 14
searched to i= 10055 5
searched to i= 10056 32
searched to i= 10057 5
searched to i= 10058 14
searched to i= 10059 14
searched to i= 10060 23
searched to i= 10061 2
searched to i= 10062 68
searched to i= 10063 5
searched to i= 10064 41
searched to i= 10065 41
searched to i= 10066 14
searched to i= 10067 2
searched to i= 10068 23
searched to i= 10069 2
searched to i= 10070 41
searched to i= 10071 11
searched to i= 10072 11
searched to i= 10073 5
searched to i= 10074 41
searched to i= 10075 23
searched to i= 10076 23
searched to i= 10077 5
searched to i= 10078 5
searched to i= 10079 2
searched to i= 10080 248
searched to i= 10081 5
searched to i= 10082 8
searched to i= 10083 5
searched to i= 10084 8
searched to i= 10085 5
searched to i= 10086 23
searched to i= 10087 14
searched to i= 10088 32
searched to i= 10089 23
searched to i= 10090 14
searched to i= 10091 2
searched to i= 10092 38
searched to i= 10093 2
searched to i= 10094 23
searched to i= 10095 14
searched to i= 10096 14
searched to i= 10097 5
searched to i= 10098 95
searched to i= 10099 2
searched to i= 10100 38
searched to i= 10101 41
searched to i= 10102 5
searched to i= 10103 2
searched to i= 10104 32
searched to i= 10105 14
searched to i= 10106 14
searched to i= 10107 8
searched to i= 10108 38
searched to i= 10109 5
searched to i= 10110 41
searched to i= 10111 2
searched to i= 10112 23
searched to i= 10113 5
searched to i= 10114 14
searched to i= 10115 23
searched to i= 10116 38
searched to i= 10117 5
searched to i= 10118 5
searched to i= 10119 5
searched to i= 10120 95
searched to i= 10121 5
searched to i= 10122 41
searched to i= 10123 5
searched to i= 10124 8
searched to i= 10125 32
searched to i= 10126 14
searched to i= 10127 14
searched to i= 10128 41
searched to i= 10129 5
searched to i= 10130 14
searched to i= 10131 14
searched to i= 10132 23
searched to i= 10133 2
searched to i= 10134 23
searched to i= 10135 5
searched to i= 10136 32
searched to i= 10137 14
searched to i= 10138 14
searched to i= 10139 2
searched to i= 10140 113
searched to i= 10141 2
searched to i= 10142 14
searched to i= 10143 38
searched to i= 10144 17
searched to i= 10145 5
searched to i= 10146 41
searched to i= 10147 5
searched to i= 10148 23
searched to i= 10149 14
searched to i= 10150 68
searched to i= 10151 2
searched to i= 10152 74
searched to i= 10153 14
searched to i= 10154 5
searched to i= 10155 14
searched to i= 10156 8
searched to i= 10157 5
searched to i= 10158 14
searched to i= 10159 2
searched to i= 10160 41
searched to i= 10161 8
searched to i= 10162 5
searched to i= 10163 2
searched to i= 10164 113
searched to i= 10165 14
searched to i= 10166 41
searched to i= 10167 5
searched to i= 10168 32
searched to i= 10169 2
searched to i= 10170 68
searched to i= 10171 5
searched to i= 10172 8
searched to i= 10173 5
searched to i= 10174 5
searched to i= 10175 23
searched to i= 10176 59
searched to i= 10177 2
searched to i= 10178 14
searched to i= 10179 32
searched to i= 10180 23
searched to i= 10181 2
searched to i= 10182 14
searched to i= 10183 5
searched to i= 10184 32
searched to i= 10185 41
searched to i= 10186 14
searched to i= 10187 5
searched to i= 10188 38
searched to i= 10189 5
searched to i= 10190 14
searched to i= 10191 14
searched to i= 10192 68
searched to i= 10193 2
searched to i= 10194 14
searched to i= 10195 5
searched to i= 10196 8
searched to i= 10197 23
searched to i= 10198 5
searched to i= 10199 14
searched to i= 10200 158
searched to i= 10201 3
searched to i= 10202 5
searched to i= 10203 14
searched to i= 10204 8
searched to i= 10205 14
searched to i= 10206 59
searched to i= 10207 5
searched to i= 10208 50
searched to i= 10209 14
searched to i= 10210 14
searched to i= 10211 2
searched to i= 10212 68
searched to i= 10213 5
searched to i= 10214 5
searched to i= 10215 23
searched to i= 10216 11
searched to i= 10217 5
searched to i= 10218 41
searched to i= 10219 5
searched to i= 10220 68
searched to i= 10221 5
searched to i= 10222 14
searched to i= 10223 2
searched to i= 10224 68
searched to i= 10225 8
searched to i= 10226 5
searched to i= 10227 14
searched to i= 10228 8
searched to i= 10229 5
searched to i= 10230 122
searched to i= 10231 5
searched to i= 10232 11
searched to i= 10233 11
searched to i= 10234 41
searched to i= 10235 14
searched to i= 10236 23
searched to i= 10237 5
searched to i= 10238 5
searched to i= 10239 5
searched to i= 10240 35
searched to i= 10241 23
searched to i= 10242 23
searched to i= 10243 2
searched to i= 10244 23
searched to i= 10245 14
searched to i= 10246 14
searched to i= 10247 2
searched to i= 10248 95
searched to i= 10249 5
searched to i= 10250 32
searched to i= 10251 23
searched to i= 10252 23
searched to i= 10253 2
searched to i= 10254 14
searched to i= 10255 14
searched to i= 10256 14
searched to i= 10257 14
searched to i= 10258 14
searched to i= 10259 2
searched to i= 10260 158
searched to i= 10261 5
searched to i= 10262 14
searched to i= 10263 14
searched to i= 10264 11
searched to i= 10265 5
searched to i= 10266 41
searched to i= 10267 2
searched to i= 10268 23
searched to i= 10269 23
searched to i= 10270 41
searched to i= 10271 2
searched to i= 10272 50
searched to i= 10273 2
searched to i= 10274 14
searched to i= 10275 23
searched to i= 10276 23
searched to i= 10277 5
searched to i= 10278 23
searched to i= 10279 5
searched to i= 10280 32
searched to i= 10281 14
searched to i= 10282 14
searched to i= 10283 14
searched to i= 10284 23
searched to i= 10285 23
searched to i= 10286 14
searched to i= 10287 14
searched to i= 10288 14
searched to i= 10289 2
searched to i= 10290 95
searched to i= 10291 5
searched to i= 10292 23
searched to i= 10293 14
searched to i= 10294 5
searched to i= 10295 14
searched to i= 10296 158
searched to i= 10297 5
searched to i= 10298 14
searched to i= 10299 5

searched to i= 1000 25
searched to i= 2000 32
searched to i= 3000 74
searched to i= 4000 39
searched to i= 5000 32
searched to i= 6000 95
searched to i= 7000 74
searched to i= 8000 46
searched to i= 9000 123
searched to i= 10000 41
searched to i= 11000 74
searched to i= 12000 116
searched to i= 13000 74
searched to i= 14000 95
searched to i= 15000 95
searched to i= 16000 53
searched to i= 17000 74
searched to i= 18000 158
searched to i= 19000 74
searched to i= 20000 50
searched to i= 21000 221
searched to i= 22000 95
searched to i= 23000 74
searched to i= 24000 137
searched to i= 25000 39
searched to i= 26000 95
searched to i= 27000 172
searched to i= 28000 116
searched to i= 29000 74
searched to i= 30000 122
searched to i= 31000 74
searched to i= 32000 60
searched to i= 33000 221
searched to i= 34000 95
searched to i= 35000 95
searched to i= 36000 193
searched to i= 37000 74
searched to i= 38000 95
searched to i= 39000 221
searched to i= 40000 59
searched to i= 41000 74
searched to i= 42000 284
searched to i= 43000 74
searched to i= 44000 116
searched to i= 45000 158
searched to i= 46000 95
searched to i= 47000 74
searched to i= 48000 158
searched to i= 49000 123
searched to i= 50000 50
searched to i= 51000 221
searched to i= 52000 116
searched to i= 53000 74
searched to i= 54000 221
searched to i= 55000 95

"""