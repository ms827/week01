import sys
sentence = list(sys.stdin.readline().rstrip())

result=''
for st in sentence:
    if st.islower():
        if (ord(st)+13)%ord('z') > 0:
            result+=chr((ord(st)+13)%ord('z')+ord('a'))
        else:   
            result+=chr(ord(st)+13)

    elif st.isupper():
        if (ord(st)+13)%ord('Z') > 0:
            result+=chr((ord(st)+13)%ord('Z')+ord('A'))
        else:   
            result+=chr(ord(st)+13)
    else:
        result+=st
print(result)
