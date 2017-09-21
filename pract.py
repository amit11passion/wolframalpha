import wolframalpha

app_id="ALYU56-4KLQTPY8WJ"
ques=input("please eneter your question: ")
client =wolframalpha.Client(app_id)
res = client.query(ques)

for rs in res.pods:
    print("-"*50)
    print(rs.text)
#answer=next(res.results)
#print(answer)