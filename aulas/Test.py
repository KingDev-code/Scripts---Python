def responder(pergunta):
    # Dicionário de perguntas e respostas
    perguntas_respostas = {
        "Como você está?": "Estou bem, obrigado!",
        "Qual é o seu nome?": "Meu nome é PythonBot.",
        "O que você faz?": "Eu sou um programa de conversação simples.",
        "Tchau": "Até mais! Tenha um ótimo dia."
    }

    # Procura a pergunta no dicionário
    resposta = perguntas_respostas.get(pergunta, "Desculpe, eu não entendi essa pergunta.")

    return resposta

def main():
    print("Olá! Eu sou o PythonBot. Você pode digitar 'Tchau' para sair.")

    while True:
        # Recebe uma pergunta do usuário
        pergunta = input("Você: ")

        # Verifica se o usuário deseja sair
        if pergunta.lower() == "tchau":
            print("PythonBot: Até mais! Tenha um ótimo dia.")
            break

        # Obtém a resposta do PythonBot
        resposta = responder(pergunta)
        print("PythonBot:", resposta)

if __name__ == "__main__":
    main()