import sys

input = sys.stdin.readline

no_hear = []
no_see  = []

h_num, s_num = map(int, input().split())

for i in range(h_num) :
    no_hear.append( input().strip() )
    
for i in range(s_num) :
    no_see.append( input().strip() )
    
    
sort_list = sorted( set(no_hear) & set(no_see) )

print( len(sort_list) )

for name in sort_list :
    print( name )