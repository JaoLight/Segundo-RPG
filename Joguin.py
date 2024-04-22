import random
import sys
import math

BOLD = '\033[1m'
END = '\033[0m'
NEG = '\033[7m'
AZUL = '\033[1;36m'
VERM = '\033[1;31m'
AMAR = '\033[1;33m'
VERD = '\033[1;32m'


class Player:
    def __init__(self, classe, nome):
        self.classe = classe
        self.nome = nome
        self.hp = 0
        self.lvl = 1
        self.almas = 0
        self.xp = 50
        self.xp_ganho = 0
        self.atk = 0
        self.energia = 0
        self.crit = 0
        self.df = 0
        self.mana = 0
        self.hp_definido = 0

    def atributos(self):
        self.forca = 0
        self.determinacao = 0
        self.inteligencia = 0
        self.bravura = 0
        self.sorte = 0
        self.pontos = 0

    def perfil(self):
        self.p_hp_def = self.determinacao * 5 + (self.hp_definido + 50) * self.lvl + self.hp_definido
        self.p_hp = self.p_hp_def
        self.p_mana = self.inteligencia * 5 + (self.atk + 50) * self.lvl + self.mana
        self.p_crit = self.sorte / 5 + 3 + self.crit
        self.s_crit = random.randint(1, 3)
        if self.s_crit == 2:
            self.d_crit = random.randint(0, self.p_crit)
        else:
            self.d_crit = 0
        self.p_atk = self.forca * 5 + self.bravura * 2 + self.sorte  + self.atk
        self.p_df = self.bravura * 5 + self.lvl * 5 + self.df

    def experience(self, xp_recebido):
        self.xp_ganho += xp_recebido
        while self.xp_ganho >= self.xp:
            self.xp_ganho -= self.xp
            self.lvl += 1
            input(f'{VERD}[VOCÊ SUBIU DE NÍVEL]{END}')
            if self.lvl % 10 == 0:
                self.xp += 100
            else:
                self.xp += 10


nn = 'a'
player = Player('h', nn)
while True:
    escolher_classe = input('''[Digite "ajuda" para ver as classes disponíveis.]
Digite qual classe você deseja: ''')
    match escolher_classe:
        case 'ajuda':
            print(f'''{VERM}==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}
{BOLD}                                        Classes disponíveis:{END}

{BOLD}Guerreiro{END}                      {BOLD}Tanker{END}                      {BOLD}Bruto{END}
{VERD}Usuário de Espada{END}              {VERD}Alta Defesa{END}                 {VERD}Grande Lutador{END}
Dano: 60                       Dano: 50                    Dano: 60
Vida: 170                      Vida: 250                   Vida: 170
Crit: 10                       Crit: 10                    Crit: 20
Def: 10                        Def: 20                     Def: 15
Mana: 100                      Mana: 50                    Mana: 70

{BOLD}Assassino{END}                      {BOLD}Piromante{END}                   {BOLD}Criomante{END}
{VERD}Furtividade{END}                    {VERD}Magia de Fogo{END}               {VERD}Magia de Gelo{END}
Dano: 75                       Dano: 70                    Dano: 60
Vida: 100                      Vida: 120                   Vida: 120
Crit: 10                       Crit: 20                    Crit: 25
Def: 10                        Def: 10                     Def: 10
Mana: 150                      Mana: 200                   Mana: 200
 
{BOLD}Geomante{END}                       {BOLD}Necromante{END}                  {BOLD}Electromante{END}
{VERD}Magia da Terra{END}                 {VERD}Invocador{END}                   {VERD}Magia Elétrica{END}
Dano: 65                       Dano: 40                    Dano: 55 
Vida: 150                      Vida: 150                   Vida: 165
Crit: 20                       Crit: 10                    Crit: 20
Def: 5                         Def: 0                      Def: 5
Mana: 200                      Mana: 200                   Mana: 200

{VERM}==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
        case 'guerreiro':
            player.classe = 'Guerreiro'
            player.atk = 60
            player.hp = 170
            player.crit = 10
            player.df = 10
            player.mana = 100
            player.hp_definido = 150
            break
        case 'tanker':
            player.classe = 'Tanker'
            player.atk = 50
            player.hp = 250
            player.crit = 10
            player.df = 20
            player.mana = 50
            player.hp_definido = 250
            break
        case 'bruto':
            player.classe = 'Bruto'
            player.atk = 60
            player.hp = 170
            player.crit = 20
            player.df = 15
            player.mana = 70
            player.hp_definido = 170
            break
        case 'assassino':
            player.classe = 'Assassino'
            player.atk = 75
            player.hp = 100
            player.crit = 10
            player.df = 10
            player.mana = 150
            player.hp_definido = 100
            break
        case 'piromante':
            player.classe = 'Piromante'
            player.atk = 70
            player.hp = 120
            player.crit = 20
            player.df = 10
            player.mana = 200
            player.hp_definido = 120
            break
        case 'criomante':
            player.classe = 'Criomante'
            player.atk = 60
            player.hp = 120
            player.crit = 25
            player.df = 10
            player.mana = 200
            player.hp_definido = 120
            break
        case 'geomante':
            player.classe = 'Geomante'
            player.atk = 65
            player.hp = 175
            player.crit = 15
            player.df = 10
            player.mana = 200
            player.hp_definido = 175
            break
        case 'necromante':
            player.classe = 'Necromante'
            player.atk = 40
            player.hp = 150
            player.crit = 10
            player.df = 0
            player.mana = 200
            player.hp_definido = 150
            break
        case 'electromante':
            player.classe = 'Electromante'
            player.atk = 55
            player.hp = 165
            player.crit = 20
            player.df = 5
            player.mana = 200
            player.hp_definido = 165
            break
        case _:
            input('[Digite um valor válido]')
            continue


class Menus:
    def __init__(self):
        self.inv_armor = []
        self.inv_sword = []
        self.inv_key = []
        self.inv_artefatos = []

    def menu(self):
        while True:
            player.atributos()
            player.perfil()
            print(f'''{AMAR}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}
{BOLD}                O que deseja?{END}
    
[1] Inventário
[2] Atributos
[3] Perfil
[4] Habilidades
------------------
[5] Sair
    
{AMAR}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
            msg = int(input(''))

            match msg:
                case 1:
                    while True:
                        print(f'''
{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}
{BOLD}             ~~__INVENTÁRIO__~~{END}

{BOLD}A)Armas:{END}
{list(self.inv_sword)}
                        
{BOLD}B)Armaduras:{END}
{list(self.inv_armor)}
                        
{BOLD}C)Artefatos:{END}
{list(self.inv_artefatos)}
                        
{BOLD}D)Chaves:{END}
{list(self.inv_key)}
                        
[Digite "ajuda" para saber como funciona]
[Digite "sair" para sair]
{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
                        inv_msg = input(':')
                        match inv_msg:
                            case 'ajuda':
                                print('''Para usar ou equipar um item, primeiro digite a letra.
Logo depois irá perguntar o número do item e basta digitar o número''')
                                input('[Aperte Enter para continuar...]')
                            case 'a':
                                print('[Deseja equipar qual arma?]')
                                arm = input('')
                                continue
                            case 'b':
                                print('[Deseja equipar qual armadura?]')
                                armd = input('')
                                continue
                            case 'c':
                                print('[Deseja usar qual artefato?]')
                                armd = input('')
                                continue
                            case 'd':
                                print('[Deseja usar qual chave?]')
                                armd = input('')
                                continue
                            case 'sair':
                                break
                            case _:
                                print('[Digite um valor válido]')
                                continue

                case 2:
                    while True:
                        print(f'''
{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}
{BOLD}        ~~__ATRIBUTOS DO JOGADOR__~~{END}

Força: {player.forca}
Determinação: {player.determinacao}
Inteligência: {player.inteligencia}
Bravura: {player.bravura}
Sorte: {player.sorte}

{BOLD}Pontos disponíveis:{END} {player.pontos}
[Digite (sair) para sair]
{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
                        at = input('')
                        match at:
                            case 'sair':
                                break
                            case _:
                                input('[Digite um valor válido]')
                                continue

                case 3:
                    while True:
                        print(f'''
{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}
{BOLD}         ~~__PERFIL DO JOGADOR__~~

{VERM}Nível:{END} {player.lvl}     {AMAR}XP:{END} {player.xp_ganho}/{player.xp}     {VERD}Classe:{END} {player.classe}
{VERD}{player.nome}{END}             {AZUL}Almas: {player.almas}{END}

{BOLD}Vida:{END} {player.p_hp}/{player.p_hp_def}
{BOLD}Dano:{END} {player.p_atk}
{BOLD}Crítico:{END} {player.p_crit}
{BOLD}Mana:{END} {player.p_mana}
{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
                        prf = input('')
                        match prf:
                            case 'sair':
                                break
                            case _:
                                continue
                                
                case 4:
                    while True:
                        print(f'''{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}
{BOLD}        ~~__MENU DE HABILIDADES__~~{END}

{BOLD}Habilidade 1:{END}


{AZUL}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
                        hab = input('')
                        match hab:
                            case 'sair':
                                break

                case 5:
                    break
                        
                case _:
                    input('Digite uma opção válida')


class Habilidades:
    def __init__(self):
        self.feg = 1
    
    def habilidade1(self):
        print(f'''{AMAR}Fúria:{END}    Qualquer classe

Permite que ataque duas vezes no mesmo turno
e cause 10% a mais de dano.

{BOLD}Preço:{END} 150 Almas
{VERM}{self.hab1}{END} ''')


class Loja:
    def __init__(self):
        self.almas = 0
        self.hab1 = ''
        self.hab2 = ''
        self.hab3 = ''
        self.hab4 = ''
        self.hab5 = ''
        self.habilidades = {
            'mão forte': {
                'nome': 'Mão Forte';
                'preço': 250;
                'texto': 'Aumenta seu dano com arma em 20%, caso esteja sem arma, aumenta em 30%. Usado uma vez por batalha.'
            }
        }

    def perg_loja(self):
        print('[Você tem certeza que quer comprar?]')
        a1 = input(':')
        if a1 == 'sim':
            input('[Item adquirido]')
            input('[Enviado para o inventário]')
            return 'ADQUIRIDO'
        else:
            input('[Compra cancelada!!]')
            return ''
        
    def loja(self):
        while True:
            print(f'''{AMAR}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}
{BOLD}          ~~__LOJINHA DO TONHO__~~{END}

[1] Habilidades
[2] Armas
[3] Armaduras
[4] Sair

{AMAR}==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
            lj = int(input(':'))

            match lj:
                case 4:
                    break
                case 1:
                    while True:
                        print(f'''{VERM}==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}

{AZUL}ALMAS:{END} {player.almas}

{BOLD}---------------------------------------------------{END}

{BOLD}---------------------------------------------------{END}

{BOLD}---------------------------------------------------{END}

{BOLD}---------------------------------------------------{END}

[Para comprar um item basta digitar o nome. Ex: "mão forte"]
[Digite "sair" para sair ou "próximo" para ir à próxima página]

{VERM}==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=={END}''')
                        habi = input(':')
                        match habi:
                            case 'sair':
                                break
                            case 'fúria':
                                if self.hab1 != 'ADQUIRIDO':
                                    self.hab1 = self.perg_loja()
                                    continue
                                else:
                                    input('[Você já tem essa habilidade]')
                            case 'mão forte':
                                if self.hab2 != 'ADQUIRIDO':
                                    self.hab2 = self.perg_loja()
                                    continue
                                else:
                                    input('[Você já tem essa habilidade]')
                            case 'grito de provocação':
                                if self.hab3 != 'ADQUIRIDO':
                                    self.hab3 = self.perg_loja()
                                    continue
                                else:
                                    input('[Você já tem essa habilidade]')
                            case 'próximo':

                          

loja = Loja()
print(loja.loja())

menu = Menus()
print(menu.menu())

while True:
    nn = str(input('Escolha um nome: '))
    if nn == '':
        input('[Digite um Nome Válido]')
        continue
    else:
        break