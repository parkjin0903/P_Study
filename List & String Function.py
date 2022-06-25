#eval('123+323*2') # 유용 but 위험한 함수

'''
s = list()

s.append(x) : 리스트 s의 끝에 x를 추가
s.extend(t) : 리스트 s의 끝에 리스트 t의 내용 전부를 추가
s.clear() : 리스트 s의 내용물 전부 삭제
s.insert(i, x) : s[i]에 x를 저장
s.pop(i) : s[i]를 반환 및 삭제
s.remove(x) : 리스트 s에서 제일 앞에 등장하는 x를 하나만 삭제
s.count(x) : 리스트 s에 등장하는 x의 개수 반환
s.index(x) : 리스트 s에 처음 등장하는 x의 인덱스 값 반환
'''

'''
s = 'str'

s.count(sub) : 문자열 s에 sub가 등장하는 횟수 반환
s.lower() : 문자열 s의 내용을 전부 소문자로 바꾼 문자열 반환
s.upper() : 문자열 s의 내용을 전부 대문자로 바꾼 문자열 반환
s.lstrip() : 문자열 s의 앞에 위치한 공백을 모두 제거한 문자열 반환
s.rstrip() : 문자열 s의 뒤에 위치한 공백을 모두 제거한 문자열 반환
s.strip() : 문자열 s의 앞과 뒤에 위치한 공백을 모두 제거한 문자열 반환
s.replace(old, new) : 문자열 s의 old를 new로 교체한 문자열 반환
s.split() : 문자열 s를 공백을 기준으로 나눠서 리스트에 담아서 반환 -> split(_) 사용시 _ 기준으로 나눔

s.find(sub) : 문자열 s에 sub가 있으면 그 위치의 인덱스 값, 없으면 -1 반환
s.rfind(sub) : s.find는 앞에서부터 sub를 찾는 반면 s.rfind는 뒤에서부터 찾는다

in / not in 로 대체 가능

# bool 반환
s.isdigit()
s.isalpha()
s.startswith(prefix)
s.endswith(suffix)

'''
