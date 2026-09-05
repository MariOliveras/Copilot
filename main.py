def calcular_media(notas):
   
    if not notas: 
        return 0
    return sum(notas) / len(notas)

def verificar_situacao(media):  
    if media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"  

def main():
    print("----Sistema de Análise de Notas----")
    try:
        notas_aluno = [8.0, 7.0, 9.0, 6.5]
        
        media = calcular_media(notas_aluno)
        
        situacao = verificar_situacao(media) 
        
        print(f"Notas: {notas_aluno}")
        print(f"Média Final: {media:.2f}")
        print(f"Situação: {situacao}")
        
    except Exception as e:  
        print(f"Ocorreu um erro no processamento: {e}") 

if __name__ == "__main__":
    main()
