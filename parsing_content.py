import requests

res=requests.get("https://docs.python.org/3.5/") # получили запрос
print(res.status_code) # вывели статус-код
print(res.headers['Content-Type']) # вывели тип получаемых данных
print(res.content)
print(res.text) #чтение тектового контента

res=requests.get("https://docs.python.org/3.5/_static/py.png")
print(res.status_code)
print(res.headers)
with open("python_file.png", "wb") as f:
    f.write(res.content) # чтение и запись нетекстового контента
