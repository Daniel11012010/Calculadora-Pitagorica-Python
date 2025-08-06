import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc,Rectangle
import time
import numpy as np
import sys

def informaçoes():
  global h
  global cO
  global cA
  global a
  global âO
  global âA
  global m
  print("Especifique as informações corretamente para não haver erros(X≠0).")
  m = input("método de contagem(km, m, cm ou etc):")
  h = input("Digite o valor da Hipotenusa, caso não saiba digite h:")
  cO = input("Cateto Oposto, caso não saiba digite cO:")
  cA = input("Cateto Adjacente, caso não saiba digite cA:")
  a = 0
  âO = 0
  âA = 0
  print("Hipotenusa² = cateto Oposto² + cateto Adjacente²")
  print(h,"² =", cO, "² +",cA,"²")
  if(isinstance(h,str)and cO.isdigit() and cA.isdigit()):
      cO = int(cO)
      cA = int(cA)
      h = math.sqrt(cO**2 + cA**2)
      #h = int(h)
      print('1')
  elif(isinstance(cO,str)and h.isdigit() and cA.isdigit()):
      h = int(h)
      cA = int(cA)
      cO = math.sqrt(h**2 - cA**2)
      #cO = int(cO)
      print('2')
  elif(isinstance(cA,str)and cO.isdigit() and h.isdigit()):
      h = int(h)
      cO = int(cO)
      cA = math.sqrt(h**2 - cO**2)
      #cA = int(cA)
      print('3')
  elif(h.isdigit and cO.isdigit() and cA.isdigit()):
      cO = int(cO)
      cA = int(cA)
      h = int(h)
  else:
      print("Informações Erradas, ou operação já está completa.")
      sys.exit()

  print("Hipotenusa =", h)
  print("Cateto Oposto =", cO)
  print("Cateto Adjacente =", cA)
  a = cO * cA / 2
  print(f'Área = {a}{m}²')

  âO = math.degrees(math.atan(cO / cA))
  âA = 90 - âO
  print(f'Ângulo Oposto = {âO:.2f}°')
  print(f'Ângulo Adjacente = {âA:.2f}°')

def exibir_triangulo():
  global h
  global cO
  global cA
  h = (h)
  cO = (cO)
  cA = (cA)

  x = [0, cA, 0, 0]
  y = [0, 0, cO, 0]

  #Desenhando Triangulo
  plt.figure()
  plt.plot(x, y, 'black', linewidth=2)
  plt.fill(x, y, 'skyblue', alpha=0.5)
  plt.xlabel(f'largura({m})')
  plt.ylabel(f'altura({m})')
  plt.title('Triângulo Retângulo')

  #Definindo ângulos externos
  âE = input("Deseja exibir ângulos externos?(s/n):")
  print(f"ângulo externo oposto = {180-âO}")
  print(f"ângulo externo adjacente = {180-âA}")
  tA = âA
  tO = âO*-1
  w= -0.2
  mA = (cA + cO)/2 #media aritimética

  #Desenhando informações
  if(âA>18 and âO>18):
    #Desenhando ângulos externos
    if(âE.strip().lower() in ["sim","s","ss"]):
      plt.text(cA*1.1,cO*0.13, f'{180-âO:.2f}°', ha='center')
      plt.text(cA*0.27,cO, f'{180 -âA :.2f}°', ha='center')
      plt.gca().add_patch(Rectangle((0,0),0,cO+(mA*0.2),color = 'black', linewidth = 2))
      plt.gca().add_patch(Rectangle((0,0),cA+(mA*0.2),0,color = 'black', linewidth = 2))
      tA = 180
      tO = 180
      w= 0.2

    elif(âE.strip().lower() in ["nao","não","n"]):
      tA = âA
      tO = âO*-1
      w= -0.2

    #Desenhando Valor dos ângulos
    plt.text(cA*0.8,cO*0.05, f'{âO:.2f}°', ha='center')
    plt.text(cA*0.1,cO*0.73, f'{âA:.2f}°', ha='center',rotation=âA-90)

    #informaçoes catetos
    plt.text(cA / 2, cO*-0.1, f'Cateto Adjacente = {cA:.2f}', ha='center')
    plt.text(cA*-0.1, cO / 2, f'Cateto Oposto = {cO:.2f}', va='center', rotation=90)
    plt.text(cA / 2, cO / 2, f'Hipotenusa = {h:.2f}', ha='center', rotation=-np.degrees(np.arctan(cO/cA)))
    plt.text(cA, cO, f'Área = {a:.2f}{m}²', ha='center')

  if(âA>13 or âO>13):
    #DESENHANDO OS ANGULOS
    anguloReto = Rectangle((0,0),mA/10,mA/10, color = 'black', fill = False, linewidth = 1.5)
    plt.gca().add_patch(anguloReto)
    arcA = Arc((0,cO),angle=270,width=mA*0.2,height=mA*0.2,theta1=0, theta2=tA)
    plt.gca().add_patch(arcA)
    arcO = Arc((cA,0),angle=0,width=mA*w,height=mA*0.2,theta1=0, theta2=tO)
    plt.gca().add_patch(arcO)

  #Definindo gráfico e limites
  plt.xlim(cA*-0.2, cA * 1.4)
  plt.ylim(cO*-0.2, cO *1.4)
  plt.gca().set_aspect('equal')
  plt.grid(True, linestyle="--", alpha=0.6)

  plt.show()
informaçoes()
exibir_triangulo()
time.sleep(1)
repeat = input("Deseja comparar com outro triângulo?")
while (repeat.strip().lower() in ["sim","s","ss"]):
    informaçoes()
    exibir_triangulo()
  #  repeat = input("Deseja comparar com outro triângulo?",'\n',"Obs: todos os triângulos devem estar no mesmo método de contagem.")

else:
  print("Obrigado por usar o programa!")
