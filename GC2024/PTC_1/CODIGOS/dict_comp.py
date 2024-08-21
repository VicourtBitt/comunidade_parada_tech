
produtos = [
    {"nome" : "Garrafa Termica", "preco" : 24.99},
    {"nome" : "Televisao 32' Smart", "preco" : 1299.99}
]

prod_desc = [
            # RESULTADO
            {**produto, "preco": round(produto["preco"] * 0.95, 2)}
            # SE
            if produto['preco'] > 150.00 
            # SENAO
            else {**produto}
            # PARA
            for produto in produtos
            ]