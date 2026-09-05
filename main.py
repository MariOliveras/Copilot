def calcular_media(notas):
 if notas:
  return 0
 return sum(notas) /len(notas)

def verificar_situação(media):
 if media >= 7.0:
  return "Aprovado"
 elif 5.0 <= media<7.0:
  return"Recuperação"
 else:
  return "Repovado"

 def main():
  print ("----Sistema de Análise de Notas----")
  try:
   notas_aluno = [8.0,7.0,9.0,6.5]
   media = calcular_media(notas_aluno)
   situação = verificar_situação

   print(f"Notas:{}