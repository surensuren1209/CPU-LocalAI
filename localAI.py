import ollama

while True:
    question = input("Ask Something...I am Loacl🤖 : ")

    if question.lower() in ['exit', 'quit']:
        print("Goodbye...✌️")
        break

    try:
        response = ollama.generate(model='mistral', prompt=question)
        print("Answer:", response['response'])
    except Exception as e:
        print(f"An error occurred: {e}")