mydict = {}     # 빈 딕셔너리 생성
mydict["홍길동"] = "010-1234-5678"
mydict["이순신"] = "010-9999-4445"
print(mydict)

#del
del mydict["이순신"]
print(mydict)

mydict.clear()
print(mydict)

mydict = {"kim":2021001, "lee":"2021122", "park":"232323"}
print(mydict)

print(mydict.get("lee"))
print(mydict.pop("lee"))
print(mydict)
print(mydict.get('han'))













# 전체 항목 삭제 - 딕셔너리명.clear()