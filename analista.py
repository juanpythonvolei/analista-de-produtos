import requests 
from bs4 import BeautifulSoup
from analisador import analisar
from time import sleep
import streamlit as st
def pesquisar_produto(produto):
        url_base =  f"https://www.bing.com/search?q="
        pesquisa = produto.split(" ")
        for item in pesquisa:
                url_base += f"+{item}"
        pesquisa2 = produto.split("")
        url = f"https://www.bing.com/search?q={produto2[0]}+{produto2[1]}"
        #url_ia = analisar(f"Por favor, crie uma url de pesquisa para o navegador bing, a qual contenha o conteudo desse input: {produto}.Retorne apenas o link, sem aspas, ou outros caracteres." )
        #url = url_ia.replace("```",'').strip()
        response = requests.get(url_base)
        soup = BeautifulSoup(response.content, "html.parser")

        lista_links = (analisar(f"Por favor me retorne uma lista com os links desse html, que levem a sites de compra como: tudocelular,amazon,mercadolivre etc... . Retorne apenas a lista python, sem as aspas externa e com os links separados por virgulas.Apenas retorne os links que estejam relacionados com o produto {produto}",str(soup)))
        links = lista_links.split(',')
        return links
def acessar_links(links):
    lista_paginas = []
    for item in links:
        try:
            url = f"{item}"
            response = requests.get(url)

            pagina_item= BeautifulSoup(response.content, "html.parser")
            lista_paginas.append(pagina_item)
        except:
            print('não foi possível acessar esse link')
    st.write(lista_paginas)   
    return lista_paginas
def resposta(lista_paginas):
    lista_infos = []   
    for pagina in lista_paginas:
        try:
            resposta_infos = analisar(f'''
            Por favor, analise esse html referente a um produto em um site e me retorne as seguintes informações: Preço do produto mais vantajoso, vendedor, nome do produto, resumo das informaões técnicas,link do produto e nome do site em que está o item.Apenas o necessário mesmo. Me retorne essas informações em um texto, no quais os tópicos que te mostrei devem estar saparados por esse caracter"....//".Se você não puder indentificar esses tópicos no html por conta de resticões de acesso, por favor, não o analise''',str(pagina)
        
            )
            lista_infos.append(f'{resposta_infos}')
            sleep(1.5)
        except:
            pass
    
    try:
        return analisar(f"Você é um analisador de produtos e sua função é me ajudar a selecionar o melhor local de compra e o melhor produto a ser selecionado. Te apresentarei uma lista de informações referentes a um produto, vindas de sites e vendedores diferentes. Por favor, retorne para mim a sua avaliação  de qual é o produto mais vantajoso o vendedor desses produto e o site no qual ele está hospedado bem como seu link de acesso. Além disso, elabore uma tabela com os demais produtos e vendedores, elencando-os do mais barato para o mais caro.",str(lista_infos))
    except:
        print("Não foi possível realizar a análise dos produtos")
