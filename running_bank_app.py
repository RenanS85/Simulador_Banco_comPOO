from random import randint
from time import sleep
from classes import *

def layout_A(txt):
    print('-=' * 40)
    print(txt.upper().center(80))
    print('-=' * 40)
    print('')
    sleep(0.7)

def layout_for_insert(inset_txt):
    print('--' * 30)
    txt = input(inset_txt)
    sleep(0.7)
    return txt

def loading():
    ansi_number = str(randint(41,46))
    c=0
    print ('CARREGANDO'.center(80))
    while c != 80:
        sleep(0.012)
        print (f'\033[{ansi_number}m ', end='')
        c+=1
    print ('\033[m\n ')
    sleep(0.7)


#####################################################################################################

layout_A('Olá sou um simulador de transfências e depósitos bancários escrito com poo')
layout_A('vamos incluir um cliente na simulação')
loading()
name = layout_for_insert('NOME: ')
age = layout_for_insert('IDADE: ')
client = Client(name,age)
loading()
layout_A('escolha seu banco\n1 - Banco Safe Money\n2 - Banco Money no Bolso\n3 - Banco Dim Dim Aqui')
bank_code = layout_for_insert('NUMERO DO BANCO: ')
if bank_code == '1':
    bank = Bank(client, '1')
elif bank_code == '2':
    bank = Bank(client, '2')
elif bank_code == '3':
    bank = Bank(client, '3')
loading()
layout_A('escolha a categoria')
choose_category = layout_for_insert('1 - Regular\n2 - VIP\n3 - Premium\nDGITE A OPÇÂO: ')
if choose_category == '1':
    bank.insert_client_category(regular=True)
elif choose_category == '2':
    bank.insert_client_category(vip=True)
elif choose_category == '3':
    bank.insert_client_category(premium=True)
print ('cadastrando cliente...')
loading()
layout_A('escolha o tipo de conta')
choose_account = layout_for_insert('1 - Poupança\n2 - Corrente \nDGITE A OPÇÂO: ')
agency = layout_for_insert('Digite um número fictício para a agência: ')
acc_number = layout_for_insert('Digite um número fictício para o número da conta: ')
balance = float(layout_for_insert('Digite um saldo para simular as transações: '))
layout_A('lembre de guardar seus números de agência e conta!\n'
         'eles serão utilizados nas ações de simulação')
if choose_account == '1':
    bank.insert_account(agency, acc_number, balance, saving_acc=True)
elif choose_account == '2':
    bank.insert_account(agency, acc_number, balance, current_acc=True)
print('cadastrando tipo de conta...')
loading()
layout_A('tudo pronto!')
layout_A('1 - Depósito em sua conta\n2 - Transferir de sua conta')
do_what = layout_for_insert('DIGITE A OPÇÂO:')
while True:
    try:
        client_bank = layout_for_insert('Código do Banco do Cliente: ')
    except client_bank != bank.bank_code:
        print('OPS, banco errado!')
        continue
    else:
        break
while True:
    try:
        client_agency = layout_for_insert('Agência do Cliente: ')
    except client_agency != bank.client.account.agency:
        print('OPS, agência errada!')
        continue
    else:
        break
while True:
    try:
        client_acc_number = layout_for_insert('Número da conta do Cliente: ')
    except client_acc_number != bank.client.account.acc_number:
        print('OPS, conta errada!')
        continue
    else:
        break
if do_what == '1':
    client.account.deposit()
elif do_what == '2':
    client.account.withdraw()


















