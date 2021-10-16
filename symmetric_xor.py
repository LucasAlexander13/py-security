# declaração da função cifrar e decifrar mensagens utilizando uma chave
def symmetricXor(mensagem, chave):
  '''Retorna a cifra exclusiva entre a mensagem e a chave'''
  pos = 0 # indica o índice inicial ao percorrer a chave
  nova_mensagem = '' # inicia a nova mensagem a ser retornada pela função

  for caracter in mensagem: # para cada caracter na mensagem:
    # armazena o binário OR Exclusivo (^) entre o valor ASCII e a chave atual
    novo_caracter = ord(caracter) ^ int(chave[pos])
    # converte o binário armazenado para o padrão ASCII e adiciona à mensagem
    nova_mensagem += chr(novo_caracter)

    pos += 1 # aumentamos o índice da chave a ser comparado
    if pos >= len(chave): # se o índice for maior que o tamanho da chave:
      pos = 0 # retornamos o índice para a posição inicial

  return nova_mensagem # retorna a mensagem cifrada ou decifrada como string

while True:
  opt = input('Digite 1 para cifrar e 2 para decifrar: ')

  if opt == '1':
    opt = input('Digite 1 para o teste ou 2 para cifrar uma mensagem: ')
    print('')

    if opt == '1':
      msg = 'Serei aprovado nesta disciplina' # mensagem solicitada para impressão
      print(f'A mensagem usada será: {msg}.')
      RU = '3348563' # chave sendo o RU completo com os 7 digitos numéricos
      print(f'A chave usada será o RU: {RU}.')

      print(f'A mensagem foi cifrada: {symmetricXor(msg, RU)}.\n')
      # a mensagem será: Pfvml&bsqk~dbl#ma{qg#gjwklvojme, conforme o algoritmo

    elif opt == '2':
      msg = input('Digite uma mensagem para cifrar: ')
      key = input('Digite uma chave numérica: ')
      print(f'A mensagem foi cifrada: {symmetricXor(msg, key)}.\n')
    
    else:
      print('Comando não reconhecido, tente novamente.\n')

  elif opt == '2':
    opt = input('Digite 1 para o teste ou 2 para decifrar uma mensagem: ')
    print('')

    if opt == '1':
      msg = 'Pfvml&bsqk~dbl#ma{qg#gjwklvojme' # mensagem cifrada para decifrar
      print(f'A mensagem usada será: {msg}.')
      RU = '3348563' # RU utilizado com todos os 7 dígitos numéricos
      print(f'A chave usada será o RU: {RU}.')

      print(f'A mensagem foi decifrada: {symmetricXor(msg, RU)}.\n')
      # a mensagem decifrada será: Serei aprovado nesta disciplina.

    elif opt == '2':
      msg = input('Digite uma mensagem para decifrar: ')
      key = input('Digite uma chave numérica: ')
      print(f'A mensagem foi decifrada: {symmetricXor(msg, key)}.\n')
    
    else:
      print('Comando não reconhecido, tente novamente.\n')
  else:
      print('Comando não reconhecido, tente novamente.\n')