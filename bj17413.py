## <와 > 로 스플릿을 하면, 짝수번째 인덱스에는 뒤집어야 하는 문자열이 오고,
## 홀수번째 인덱스에는 태그 안에 들어있는 문자열이 온다.
## 뒤집어야 하는 문자열은, 공백으로 단어를 구분하여 단어별로 뒤집어준다.

s = input()
temp = map(lambda x: x.split('<'), s.split('>'))
s_split = []
for e in temp:
    s_split += e
rev = ''
for i, w in enumerate(s_split):
    if i % 2:
        rev += "<{}>".format(w)
    else:
        rev += ' '.join(map(lambda x: x[::-1], w.split()))
print(rev)