from tf_corpus import *
import random
import os

import spacy
nlp = spacy.load("pt_core_news_md")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def dicionario_kx_pt(texto_kx, texto_pt):
    limpar_tela()
    palavras_kx = texto_kx.lower().split()
    palavras_pt = texto_pt.lower().split()

    dicionario = (dict(zip(palavras_kx, palavras_pt)))
 
    
    for palavra, traducao in sorted(dicionario.items()):
        print(f"{palavra} = {traducao}")
   
    
    while True:
        resposta = input(' \n Selecione uma opção \n1: Desafio \n2: Tradutor  \n3: Sair \n>')
    
        if resposta == '1':
            desafio() 
            break
		
        elif resposta == '2':
            iniciar_tradutor()
            break
	
        elif resposta == '3':
            print("Ynatekié! Até outra hora")
            break
	    
        else:
            limpar_tela()
            print('Opção inválida\n')
    
    
    return inspetor(dicionario)
    
def inspetor(dicionario):
	 
	mapeamento = {
		'da': 'de a',
		'do': 'de o',
		'na': 'em a',
		'no': 'em o',
		'pelo': 'por o',
		'pela': 'por a'
		}
	novo_dic = {}
	for palavra, traducao in dicionario.items():
		nova = mapeamento.get(palavra, palavra)
		novo_dic[nova] = traducao
	
	return novo_dic


    
    
def dicionario_pt_kx(texto_pt, texto_kx):
    limpar_tela()
    palavras_kx = texto_kx.lower().split()
    palavras_pt = texto_pt.lower().split()

    dicionario = dict(zip(palavras_pt, palavras_kx))
    

    return inspetor(dicionario)

def desafio():
	limpar_tela()
	
	
	print('Pronto para um desafio? Escreva o significado das frases para ganhar pontos!')
	print('Traduza do Kariri-Xocó para o Português os nomes desses animais:')
	pontos = 0
	
	for rodada in range(3):
		print(f'\nPergunta {rodada + 1} de 3')

		animal = random.choice(animais)
		print(f"Traduza: {animal}")
	
		resposta = input('Sua resposta:')
	
		if resposta.strip().lower() == resposta_certa_animais[animal]:
			print('Parabéns! Resposta correta!✅ ')
			pontos += 1
		else:
			print(f'Que pena! Resposta errada :(\n  A resposta era "{resposta_certa_animais[animal]}"')
			
	print(f'Você está com {pontos} pontos!')
	print('Traduza do Kariri-Xocó para o Português os nomes dessas partes do corpo humano:')
	for rodada in range(3):
		print(f'\nPergunta {rodada + 1} de 3')

		parte = random.choice(pch)
		print(f"Traduza: {parte}")
	
		resposta = input('Sua resposta:')
	
		if resposta.strip().lower() == resposta_certa_pch[parte]:
			print('Parabéns! Resposta correta!✅ ')
			pontos += 1
		else:
			print(f'Que pena! Resposta errada :(\n  A resposta era "{resposta_certa_pch[parte]}"')
	print(f'Você está com {pontos} pontos!')
	
	print('Vamos dificultar! Traduza do Kariri-Xocó para o Português as frases a seguir:')
	for rodada in range(4):
		print(f'\nPergunta {rodada + 1} de 4')

		frase = random.choice(frases)
		print(f"Traduza: {frase}")
	
		resposta = input('Sua resposta:')
	
		if resposta.strip().lower() == resposta_certa_frases[frase]:
			print('Parabéns! Resposta correta!✅ ')
			pontos += 1
		else:
			print(f'Que pena! Resposta errada :(\n  A resposta era "{resposta_certa_frases[frase]}"')
			
	if pontos == 10:
		print(f'UAU!!🥳 Você acertou tudo!')
	elif pontos >= 5:
		print(f'Você fez {pontos} pontos. Parabéns!!')
	elif pontos <= 4:
		print(f'Você fez  {pontos} pontos. Vamos continuar estudando, eu sei que você consegue ir melhor na próxima!')
			
			
	while True:
		resposta = input(' \n Selecione uma opção \n1: Dicionário Kariri-Xocó → Português \n2: Tradutor  \n3: Sair \n>')
    
		if resposta == '1':
			dicionario_kx_pt(texto_kx, texto_pt)
			break
		
		elif resposta == '2':
			iniciar_tradutor()
			break
	
		elif resposta == '3':
			print("Ynatekié! Até outra hora")
			break
	    
		else:
			limpar_tela()
			print('Opção inválida\n')


def iniciar_tradutor():
	limpar_tela()
	dic_pt_kx = dicionario_pt_kx(texto_pt, texto_kx)
	tradutor_pt_kx(dic_pt_kx)
			


def tradutor_pt_kx(dic_pt_kx):
	while True:
		limpar_tela()
		texto = input('Digite um texto em português que gostaria de traduzir: \n>')
		tokens = nlp(texto)
		traducao = []
		for token in tokens:
			lemma = token.lemma_.lower()
			print("=> ", token, lemma, lemma in dic_pt_kx)
			if lemma in dic_pt_kx:
				traducao.append(dic_pt_kx[lemma])
			else:
		 		traducao.append(f"[{token.text}]")
		
		print('Tradução:')
		print(" ".join(traducao))



		repetir = input('\nDeseja fazer outra tradução? (sim/não): ').strip().lower()
		if repetir == 'sim':
			continue
		elif repetir == 'não':
			escolha = input('Qual modo deseja utilizar? \n1: Dicionário Kariri-Xocó → Português \n2: Desafio \n3: Tradutor \n4: Sair \n>')
			
			if escolha == '1':
				dicionario_kx_pt(texto_kx, texto_pt)
				break
				
			elif escolha == '2':
				desafio()
				break
			
			elif escolha == '3':
				iniciar_tradutor()
				break
				
			elif escolha == '4':
				print("Ynatekié! Até outra hora")
				break
			
			else:
				limpar_tela()
				print('Opção inválida\n')
		
		else:
			limpar_tela()
			print('Opção inválida\n')




limpar_tela()

while True:
	escolha = input('Qual modo deseja utilizar? \n1: Dicionário Kariri-Xocó → Português \n2: Desafio \n3: Tradutor \n>')
	
	if escolha == '1':
		dicionario_kx_pt(texto_kx, texto_pt)
		break
		
	elif escolha == '2':
		desafio()
		break
	
	elif escolha == '3':
		iniciar_tradutor()
		break
	else:
		limpar_tela()
		print('Opção inválida\n')
