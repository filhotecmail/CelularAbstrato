from pip._vendor.distlib.compat import raw_input

print("..........................................................")
print("PROGRAMA DECOMPOSIÇÃO DE VALORES MONETÁRIOS")
print("ANALISTA.: DIGITE O NOME DO ANALISTA DO SISTEMA")
print("DATA.: ----/----/---- ")
print("OBJETIVO.: CALCULAR QUANTAS CÉDULAS DE 50,10,5 E 1")
print("O SISTEMA PRECISA CALCULAR DE ACORDO COM O VALOR INFORMADO")
print("TODO.: [1]-> PEDIR ENTRADA DE DADOS ")
print("       [2]-> ANALISAR DADOS, PERSISTINDO SOMENTE EM NÚMEROS INTEIROS NATURAIS ")
print("       [3]-> ARMAZENAR VALOR INFORMADO EM UMA VARIÁVEL ")
print("       [4]-> CRIAR UM VETOR DE TAMANHO 4 COM VALORES 50,10,5,1 ")
print("       [5]-> CRIAR UM VETOR PARA A SAIDA ARMAZENADA E FORMATADA EM STRING");
print("       [6]-> INICIALIAZAR VARIAVEL SALDO COM O VALOR DIGITADO");
print("       [6]-> O SALDO PARA 0");
print("       [8]-> ANALISAR VALOR IMPUTYADOS, O PROGRAMA DEVERA REPORTAR UMA EXCEPTION PARA");
print("            : NAO PERMITIR ENTRAR COM CHAR DIFERENTE DE 1 2 3 4 5 6 7 8 9 0");
print("            : NAO PERMITIR 0 ZERO OU VALORES MENORES E NEGATIVOS A ZERO");
print("            : A CONDIÇÃO ASSERTIVA LEVANTA UMA EXCEPTION PARA COM A LOGICA ANALISADA");
print("            PREVININDO O PROGRAMA DE CONTINUAR ");
print("      [9]-> INICIO DO PROCESSAMENTO ");
print("         -> ENQUANDO RESTO > 0 FAÇA ");
print("         -> PERCORRE E FAZ UMA ITERAÇÃO COM VETOR DE NOTAS CONFIGURADAS ");
print("         -> ANALISA UMA CONDIÇÃO COM 2 DESVIOS, SE RESTO >= QUE NOTAS[I] ITERADO PELO FOR ");
print("            CALCULA O RESTO ENTRE RESTO DIVISION BY NOTAS[ I  ] ITERADO ");
print("            A SAIDA TERÁ UM ALEMENTO ADICIONADO E UTILIZANDO FORMAT PARA CONCATENAÇÃO ");
print("            O SALDO SERÁ AUMENTADO DE SEU VALOR PARA SER VALOR SUM INT(RESTO) O CAST É ")
print("            NECESSARIO DEVIDO A PONTO FLUTUANTE * NOTAS[ I ] ");
print("            SUBTRAI DO RESTO O VALOR QUE FOI DIGITADO PELO USUARIO - O SALDO CALCULADO ");
print("            CASO RESTO NÃO SEJA MAIOR QUE NOTAS[ ITERATOR ] ");
print("            RESTO TERÁ A SUA DIVISION BY 1 ");
print("            PRINTA A SAÍDA ");
print("..........................................................")


mark = raw_input("Digite um valor válido  :")
notas = [50, 10, 5, 1]
saida = []
saldo=0;
assert (int(mark)),"O programa só aceita numeros inteiros ";
assert (int(mark) > 0),"O valor tem que ser maior que zero para ser analisado ";

resto =int(mark);

while (resto > 0):
  for nota in range(len(notas)):
    if (resto >= notas[nota]):
        resto = (resto / notas[nota]);
        saida = saida+["{} Cédula de {}".format(int(resto),notas[nota])];
        saldo = saldo + (int(resto)*notas[nota]);
        resto = int(mark) - saldo;

    else:
        resto= (resto / 1);

print("{}".format(saida))