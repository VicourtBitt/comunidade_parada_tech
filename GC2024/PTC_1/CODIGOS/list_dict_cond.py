victorInfo = {
    "name" : "Victor", # 1
    "age" : 20,        # 2
    "skills" : [       # 3
        "JavaScript",       # 3.0
        "Python",           # 3.1
        "ESP32"             # 3.2
    ],
    "working" : False, # 4
    "role" : "admin",
    "sayHi" : lambda : f"Olá, me chamo {victorInfo['name']}"
}

# LISTAS SÃO UM TIPO DE DADO MUTÁVEL QUE PODE ARMAZENAR DIVERSOS TIPOS DE DADOS
# LISTAS SÃO ITERAVEIS, OU SEJA, ENTRAMOS DE VALOR EM VALOR
# : list

skills = [
    "JavaScript",   # 0
    "Python",       # 1
    "ESP32"         # 2
]

# CONDICIONAIS SÃO AVALIAÇÕES FEITAS AO DECORRER DO SCRIPT
# IF, ELIF, ELSE e o TERNARIO

                     # CONDICAO A VERIFICAR
condicao_tern = victorInfo["name"] == "Victor"
# print(condicao_tern)

            # resultado          # pergunta            # consequencia
condicao_exec = "Victor" if victorInfo["name"] == "Ambos" else "False"
# print(condicao_exec)

condicao_func = victorInfo["sayHi"] if victorInfo["age"] > 18 else lambda : "falsy"