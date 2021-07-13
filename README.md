# Celular Abstrato em Python
 Uma exemplificação do conceito de abstração e herança em python
Ecrito em ```pyhon versão 3.9```

O Programa tem a finalidade de estudar e analisar uma cadeia de abstrações e herança em python, afim de poder transcrever o que entendemos do mundo real, simulando pequenos problemas, propriedades e eventos de um celular.

A Classe PAI Abstrata

![image](https://user-images.githubusercontent.com/18727307/125477687-e289d1b7-0489-4801-9d6e-babb67b2d67a.png)

Através de uma classe PAI abstrata, podemos representar e abstrair métodos genéricos e comum a todos os tipos e modelos de celulares que venham a abstrair da classe PAI.

# A Classe Celular Android
![image](https://user-images.githubusercontent.com/18727307/125477936-c5aa3925-db94-4d52-986d-8f0c82fba6b0.png)

Afim de simular e abstrair o problema em celulares com o sistema operacional Android , criamos a classe AndroidCelular(AbstractCelular) que Herda de AbstractCelular.
Os métodos básicos não precisam ser sobrecarregados ou sobrescritos pois eles podem ser acionados pela classe base abstrata por se tratar de métodos comuns a todos tipos de celulares.


# A Classe Celular Motorola MotoV8 
![image](https://user-images.githubusercontent.com/18727307/125478371-5841566c-d37d-435a-bff8-e0221e441fcf.png)

A Classe herda da classe Celulares Android.


# O Artefato de exemplo para um MotorolaV8
![image](https://user-images.githubusercontent.com/18727307/125478582-6eb85ffc-ba20-4005-bb34-25308b581456.png)

# A Saída 
![image](https://user-images.githubusercontent.com/18727307/125479480-e6f2a129-5504-4941-90a7-bbd459aedfaa.png)


A pai vamos exemplificar a criação d exceptions que serão invocadas através do artefato no qual não são implementadas nas classes filhas e será acionada através da classe abstrata ponto.

![image](https://user-images.githubusercontent.com/18727307/125486921-47698659-be34-498c-a6bd-6eed522a11e8.png)

Criamos então a unidade de código para representar e desacoplar as exceptions que será diparadas na aplicação.

 class EENotMessagetextTecnology(Exception):
  def __init__(self, message):
    self.message = message


class EENotCallVoice(Exception):
  def __init__(self, message):
    self.message = message 

![image](https://user-images.githubusercontent.com/18727307/125487125-e586abeb-b204-4067-a4b4-e7b1f3085572.png)

Vamos invocar o método chamadastelefonicas()  

![image](https://user-images.githubusercontent.com/18727307/125487218-7ef26bea-a8a5-464e-a5af-6ce2cdd0a024.png)

E teremos a Raise exception levantada pela aplicaçao.



