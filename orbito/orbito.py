def cria_posicao(col, lin):
    '''cria posicao: str x int → posicao
    cria posicao(col,lin) recebe um caracter e um inteiro correspondentes a coluna
    col e a linha lin e devolve a posicao correspondente. O construtor verifica 
    a validade dos seus argumentos, gerando um ValueError com a mensagem
    'cria_posicao: argumentos invalidos' caso os seus argumentos nao sejam validos.'''
    if type(col) != str or len(col) != 1 or col not in ("abcdefghij") or type(lin) != int or lin not in range(1, 11):
        raise ValueError('cria_posicao: argumentos invalidos')
    return tuple((col, lin))

def obtem_pos_col(pos):
    ''''obtem pos col : posicao → str
    obtem pos col(p) devolve a coluna col da posicao p.'''
    return pos[0]

def obtem_pos_lin(pos):
    '''obtem pos lin: posicao → int
    obtem pos lin(p) devolve a linha lin da posicao p.'''
    return pos[1]

def coluna_max(n):
    '''coluna max: inteiro → str
    coluna max(n) devolve a string com as colunas possiveis para um tabuleiro de
    Orbito-n.'''
    colunas_posiveis = ("abcdefghij")
    return colunas_posiveis[:n*2]

def posicao_para_coordenadas(pos):
    '''posicao para coordenadas: posicao → tuplo
    posicao para coordenadas(p) devolve um tuplo com as coordenadas correspondentes
    a posicao p.'''
    # usa o numero ascii de 'a' para calcular a coluna, e subtraindo 1 da linha para obter as coordenadas em indice 0
    return (ord(obtem_pos_col(pos)) - ord('a'), obtem_pos_lin(pos) - 1)

def coordenadas_para_posicao(coord):
    '''coordenadas para posicao: tuplo → posicao
    coordenadas para posicao(coord) devolve a posicao correspondente as coordenadas
    coord.'''
    return (chr(coord[0] + ord('a')), coord[1] + 1)

def eh_posicao(arg):
    '''eh posicao: universal → booleano
    eh posicao(arg) devolve True caso o seu argumento seja um TAD posicao e
    False caso contrario.'''
    if type(arg) != tuple or len(arg) != 2 or type(arg[0]) != str or len(arg[0]) != 1 or arg[0] not in "abcdefghij" or type(arg[1]) != int or arg[1] not in range(1, 11):
        return False
    return True

def posicoes_iguais(pos1, pos2):
    '''posicoes iguais : universal x universal → booleano
    posicoes iguais(p1, p2) devolve True apenas se p1 e p2 sao posicoes e sao
    iguais, e False caso contrario.'''
    if not eh_posicao(pos1) or not eh_posicao(pos2):
        return False
    if pos1 == pos2:
        return True
    return False

def posicao_para_str(pos):
    '''posicao para str : posicao → str
    posicao para str(p) devolve a cadeia de caracteres que representa o seu argumento, como mostrado nos exemplos'''
    linha = str(obtem_pos_lin(pos))
    return obtem_pos_col(pos) + linha

def str_para_posicao(pos_str):
    '''str para posicao: str → posicao
    str para posicao(s) devolve a posicao representada pelo seu argumento.'''
    return tuple((pos_str[0], int(pos_str[1:])))

def eh_posicao_valida(pos, n):
    '''eh posicao valida: posicao x inteiro → booleano
    eh posicao valida(p, n) devolve True se p e uma posicao valida dentro do tabuleiro
    de Orbito-n e False caso contrario.'''
    if type(n) != int or n < 2 or n > 5 or pos[1] not in range(1, n*2+1):
        return False
    elif pos[0] not in coluna_max(n):
        return False
    return True

def obtem_posicoes_adjacentes(pos, n, d):
    '''obtem posicoes adjacentes : posicao x inteiro x booleano → tuplo
    obtem posicoes adjacentes(p, n, d) devolve um tuplo com as posicoes do tabuleiro
    de Orbito-n adjacentes a posicao p se d e True, ou as posicoes adjacentes ortogonais
    se d e False. As posicoes do tuplo sao ordenadas em sentido horario comecando
    pela posicao acima de p.'''
    
    posicoes_adjacentes = ()
    pos_coord = posicao_para_coordenadas(pos)
    
    # Define movimentos ortogonais e os movimentos ortogonais e diagonais
    movimentos_ortogonais = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    movimentos_todos =  [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1,-1)]
    
    # Escolhe os movimentos com base no booleano d
    if d:
        movimentos = movimentos_todos
    else:
        movimentos = movimentos_ortogonais

    # Calcula as posições adjacentes
    for movimento in movimentos:
        coluna_adjacente = pos_coord[0] + movimento[0]
        linha_adjacente = pos_coord[1] + movimento[1]
        posicao = coordenadas_para_posicao((coluna_adjacente, linha_adjacente))
        if eh_posicao_valida(posicao, n):
            posicoes_adjacentes += (posicao,)

    return posicoes_adjacentes

def posicao_para_orbita(pos, n):
    '''posicao para orbita: posicao x inteiro → int
    posicao para orbita(p, n) devolve o numero da orbita a que a posicao p pertence
    no tabuleiro de Orbito-n.'''
    # Calcula o centro do tabuleiro
    centro = (2*n + 1)/2 -1
    coluna, linha = posicao_para_coordenadas(pos)
    # Calcula a distância máxima da posição ao centro
    distancia = int(max(abs(coluna - centro), abs(linha - centro)))
    return distancia

def ordena_posicoes(posicoes, n):
    '''ordena posicoes: tuplo x inteiro → tuplo
    ordena posicoes(ps, n) devolve um tuplo com as posicoes ps ordenadas de acordo
    com a ordem de leitura do tabuleiro de Orbito-n. As posicoes sao ordenadas
    primeiro por orbita, depois por linha e finalmente por coluna.'''
    
    def posicao_chave(pos):
        '''posicao chave: posicao → tuplo
        posicao chave(p) devolve um tuplo com a chave de ordenacao da posicao p.'''
        # Calcula a orbita da posicao
        orbita = posicao_para_orbita(pos, n)
        # Retorna um tuplo com a orbita, linha e coluna como chave de ordenacao
        return (orbita, obtem_pos_lin(pos), obtem_pos_col(pos))
    
    # Ordena as posicoes usando a chave de ordenacao definida
    return tuple(sorted(posicoes, key=posicao_chave))

def cria_pedra_branca():
    '''cria pedra branca: {} → pedra
    cria pedra branca() devolve uma pedra pertencente ao jogador branco.'''
    return ("Branca")

def cria_pedra_preta():
    '''cria pedra preta: {} → pedra
    cria pedra preta() devolve uma pedra pertencente ao jogador preto.'''
    return("Preta")

def cria_pedra_neutra():
    '''cria pedra neutra: {} → pedra
    cria pedra neutra() devolve uma pedra neutra.'''
    return ("Neutra")

def eh_pedra(arg):
    '''eh pedra: universal → booleano
    eh pedra(arg) devolve True caso o seu argumento seja um TAD pedra e False
    caso contrario.'''
    if type(arg) != str or arg not in (cria_pedra_neutra(),cria_pedra_branca(),cria_pedra_preta()):
        return False
    return True

def eh_pedra_branca(pedra):
    '''eh pedra branca: pedra → booleano
    eh pedra branca(p) devolve True caso a pedra p seja do jogador branco e False
    caso contrario.'''
    if pedra == cria_pedra_branca():
        return True
    return False

def eh_pedra_preta(pedra):
    '''eh pedra preta: pedra → booleano
    eh pedra preta(p) devolve True caso a pedra p seja do jogador preto e False
    caso contrario.'''
    if pedra == cria_pedra_preta():
        return True
    return False

def pedras_iguais(pedra1, pedra2):
    '''pedras iguais : universal x universal → booleano
    pedras iguais(p1, p2) devolve True apenas se p1 e p2 sao pedras e sao iguais.'''
    if pedra1 == pedra2:
        return True
    return False

def pedra_para_str(pedra):
    '''pedra para str : pedra → str
    pedra para str(p) devolve a cadeia de caracteres que representa o jogador dono
    da pedra, isto e, 'O', 'X' ou ' ' para pedras do jogador branco, preto ou
    neutra respetivamente.'''
    if eh_pedra_branca(pedra):
        return "O"
    elif eh_pedra_preta(pedra):
        return "X"
    else:
        return " "

def str_para_pedra(pedra_str):
    '''str para pedra: str → pedra
    str para pedra(s) devolve a pedra representada pelo seu argumento.'''
    if pedra_str == "X":
        return cria_pedra_preta()
    elif pedra_str == "O":
        return cria_pedra_branca()
    else:
        return cria_pedra_neutra()

def eh_pedra_jogador(pedra):
    '''eh pedra jogador : pedra → booleano
    eh pedra jogador(p) devolve True caso a pedra p seja de um jogador e False caso
    contrario.'''
    if pedra not in (cria_pedra_branca(), cria_pedra_preta()):
        return False
    return True

def pedra_para_int(pedra):
    '''pedra para int : pedra → int
    pedra para int(p) devolve um inteiro valor 1, -1 ou 0, dependendo se a pedra e do
    jogador preto, branco ou neutra, respetivamente.'''
    if eh_pedra_preta(pedra):
        return 1
    elif eh_pedra_branca(pedra):
        return -1
    else:
        return 0
    
def cria_tabuleiro_vazio(n):
    '''cria tabuleiro vazio: int → tabuleiro
    cria tabuleiro vazio(n) devolve um tabuleiro de Orbito com n orbitas, sem
    posicoes ocupadas. O construtor verifica a validade do argumento, gerando
    um ValueError com a mensagem 'cria_tabuleiro_vazio: argumento invalido' caso os seu argumento nao seja valido. Considere que o numero
    minimo de orbitas de um tabuleiro de Orbito e 2 e o maximo 5.'''
    
    # Verifica se o número de órbitas é válido
    if type(n) != int or n < 2 or n > 5:
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    
    # Inicializa o tabuleiro como uma lista de listas
    tabuleiro = []
    
    # Preenche o tabuleiro com pedras neutras
    for linha in range(n*2):
        tabuleiro.append([])
        for coluna in range(n*2):
            tabuleiro[linha].append(cria_pedra_neutra())
    
    return tabuleiro

def cria_tabuleiro(n, tuplo_pretas, tuplo_brancas):
    '''cria tabuleiro: int x tuplo x tuplo → tabuleiro
    cria tabuleiro(n, tp, tb) devolve um tabuleiro de Orbito com n orbitas, com as
    posicoes do tuplo tp ocupadas por pedras pretas e as posicoes do tuplo tb ocupadas por pedras brancas. O construtor verifica a validade dos argumentos,
    gerando um ValueError com a mensagem 'cria_tabuleiro: argumentos invalidos' caso os seus argumentos nao sejam validos. Considere que o
    numero minimo de orbitas de um tabuleiro de Orbito e 2 e o maximo 5.'''
    if type(n) != int or n < 2 or n > 5 or type(tuplo_pretas) != tuple or type(tuplo_brancas) != tuple:
        raise ValueError('cria_tabuleiro: argumentos invalidos')

    tabuleiro = cria_tabuleiro_vazio(n)
    
    for pos in tuplo_pretas:
        if not eh_posicao(pos) or not eh_posicao_valida(pos, n) or not pedras_iguais(obtem_pedra(tabuleiro, pos),cria_pedra_neutra()):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        coord = posicao_para_coordenadas(pos)
        tabuleiro[coord[1]][coord[0]] = cria_pedra_preta()

    for pos in tuplo_brancas:
        if not eh_posicao(pos) or not eh_posicao_valida(pos, n) or not pedras_iguais(obtem_pedra(tabuleiro, pos),cria_pedra_neutra()):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        coord = posicao_para_coordenadas(pos)
        tabuleiro[coord[1]][coord[0]] = cria_pedra_branca()

    return tabuleiro

def cria_copia_tabuleiro(tabuleiro):
    '''cria copia tabuleiro: tabuleiro → tabuleiro
    cria copia tabuleiro(t) recebe um tabuleiro e devolve uma copia do tabuleiro.'''
    return [linha.copy() for linha in tabuleiro]

def obtem_numero_orbitas(tabuleiro):
    '''obtem numero orbitas : tabuleiro → int
    obtem numero orbitas(t) devolve o numero de orbitas do tabuleiro t.'''
    return len(tabuleiro) // 2

def obtem_pedra(tabuleiro, pos):
    '''obtem pedra: tabuleiro x posicao → pedra
    obtem pedra(t, p) devolve a pedra na posicao p do tabuleiro t. Se a posicao
    nao estiver ocupada, devolve uma pedra neutra.'''
    coord = posicao_para_coordenadas(pos)
    return tabuleiro[coord[1]][coord[0]]

def obtem_linha_horizontal(tabuleiro, pos):
    '''obtem linha horizontal : tabuleiro x posicao → tuplo
    obtem linha horizontal(t, p) devolve o tuplo formado por tuplos de dois ele-
    mentos correspondentes a posicao e o valor de todas as posicoes da linha
    horizontal que passa pela posicao p, ordenadas de esquerda para a direita.'''
    linha_horizontal = []
    linha = obtem_pos_lin(pos) - 1
    for coluna in range(len(tabuleiro[0])):
        nova_pos = coordenadas_para_posicao((coluna, linha))
        linha_horizontal.append((nova_pos, obtem_pedra(tabuleiro, nova_pos)))
    return tuple(linha_horizontal)

def obtem_linha_vertical(tabuleiro, pos):
    '''obtem linha vertical : tabuleiro x posicao → tuplo
    obtem linha vertical(t, p) devolve o tuplo formado por tuplos de dois elemen-
    tos correspondentes a posicao e o valor de todas as posicoes da linha vertical
    que passa pela posicao p, ordenadas de cima para a baixo.'''
    linha_vertical = []
    coluna = obtem_pos_col(pos)
    for linha in range(len(tabuleiro)):
        nova_pos = cria_posicao(coluna, linha + 1)
        linha_vertical.append((nova_pos, obtem_pedra(tabuleiro, nova_pos)))
    return tuple(linha_vertical)

def obtem_linhas_diagonais(tabuleiro, pos):
    '''obtem linhas diagonais : tabuleiro x posicao → tuplo x tuplo
    obtem linhas diagonais(t, p) devolve dois tuplos formados cada um deles por
    tuplos de dois elementos correspondentes a posicao e o valor de todas as
    posicoes que formam a diagonal (descendente da esquerda para a direita ) e
    antidiagonal (ascendente da esquerda para a direita) que passam pela posicao
    p, respetivamente.'''
    
    n = obtem_numero_orbitas(tabuleiro)
    tuplo_diagonal_descendente = ()
    tuplo_diagonal_ascendente = ()

    pos_coord = posicao_para_coordenadas(pos)
    # No intervalo de tamanho do tabuleiro, calcula as coordenadas da diagonal descendente e ascendente, verificando se são válidas

    for i in range(-n * 2, n * 2):
        nova_coord_desc = (pos_coord[0] + i, pos_coord[1] + i)
        nova_pos_desc = coordenadas_para_posicao(nova_coord_desc)
        if eh_posicao_valida(nova_pos_desc, n):
            pedra = obtem_pedra(tabuleiro, nova_pos_desc)
            tuplo_diagonal_descendente += ((nova_pos_desc, pedra),)

        nova_coord_asc = (pos_coord[0] + i, pos_coord[1] - i)
        nova_pos_asc = coordenadas_para_posicao(nova_coord_asc)
        if eh_posicao_valida(nova_pos_asc, n):
            pedra = obtem_pedra(tabuleiro, nova_pos_asc)
            tuplo_diagonal_ascendente += ((nova_pos_asc, pedra),)

    return tuplo_diagonal_descendente, tuplo_diagonal_ascendente

def obtem_posicoes_pedra(tabuleiro, pedra):
    '''obtem posicoes pedra: tabuleiro x pedra → tuplo
    obtem posicoes pedra(t, j) devolve o tuplo formado por todas as posicoes do
    tabuleiro ocupadas por pedras j (brancas, pretas ou neutras), ordenadas em
    ordem de leitura do tabuleiro.'''
    posicoes_pedras = []
    n = obtem_numero_orbitas(tabuleiro)
    for num_linha, linhas in enumerate(tabuleiro):
        for num_coluna, pedras in enumerate(linhas):
            if pedras_iguais(pedra, pedras):
                posicoes_pedras.append(coordenadas_para_posicao((num_coluna, num_linha)))
    return ordena_posicoes((posicoes_pedras), n)

def coloca_pedra(tabuleiro, pos, pedra):
    '''coloca pedra: tabuleiro x posicao x pedra → tabuleiro
    coloca pedra(t, p, j) modifica destrutivamente o tabuleiro t colocando a pedra
    j na posicao p, e devolve o proprio tabuleiro.'''
    coord = posicao_para_coordenadas(pos)
    tabuleiro[coord[1]][coord[0]] = pedra
    return tabuleiro

def remove_pedra(tabuleiro, pos):
    '''remove pedra: tabuleiro x posicao → tabuleiro
    remove pedra(t, p) modifica destrutivamente o tabuleiro p removendo a pedra
    da posicao p, e devolve o proprio tabuleiro.'''
    return coloca_pedra(tabuleiro, pos, cria_pedra_neutra())

def eh_tabuleiro(arg):
    '''eh tabuleiro: universal → booleano
    eh tabuleiro(arg) devolve True caso o seu argumento seja um TAD tabuleiro
    e False caso contrario.'''
    if type(arg) != list:
        return False
    n = obtem_numero_orbitas(arg)
    if type(n) != int or n < 2 or n > 5 or len(arg) != n*2:
        return False
    for linha in arg:
        if type(linha) != list or len(linha) != len(arg):
            return False
        for pedra in linha:
            if pedra not in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()):
                return False
    return True

def tabuleiros_iguais(tabuleiro1, tabuleiro2):
    '''tabuleiros iguais : universal x universal → booleano
    tabuleiros iguais(t1, t2) devolve True apenas se t1 e t2 forem tabuleiros e
    forem iguais.'''
    if not eh_tabuleiro(tabuleiro1) or not eh_tabuleiro(tabuleiro2):
        return False
    return tabuleiro1 == tabuleiro2

def tabuleiro_para_str(tabuleiro):
    '''tabuleiro para str : tabuleiro → str
    tabuleiro para str(t) devolve a cadeia de caracteres que representa o tabuleiro'''
    n = obtem_numero_orbitas(tabuleiro)  
    # Cria a linha inicial com as letras das colunas, usando o chr para passar de ascii para letra
    tabuleiro_str = "    " + "   ".join(chr(97 + i) for i in range(n * 2)) + '\n'
    for linha in range(n * 2):
        # Adiciona o número da linha e a primeira pedra, usando o 1:02 para garantir que o número tenha 2 dígitos
        tabuleiro_str += f"{linha + 1:02}" + f" [{pedra_para_str(tabuleiro[linha][0])}]"
        for coluna in range(1, n * 2):
            pedra = tabuleiro[linha][coluna]  

            tabuleiro_str += f"-[{pedra_para_str(pedra)}]"
        if linha != n * 2 - 1:
            # Adiciona a linha separadora entre as linhas do tabuleiro, havendo diferença entre a última linha, para não haver espaço extra
            tabuleiro_str += ("\n    |" + "   |" * (n * 2 - 2) + "   |\n")
    return tabuleiro_str

def move_pedra(tabuleiro, pos1, pos2):
    '''move pedra: tabuleiro x posicao x posicao → tabuleiro
    move pedra(t, p1, p2) modifica destrutivamente o tabuleiro t movendo a pedra da
    posicao p1 para a posicao p2, e devolve o proprio tabuleiro.'''
    pedra = obtem_pedra(tabuleiro, pos1)
    tabuleiro = remove_pedra(tabuleiro, pos1)
    tabuleiro = coloca_pedra(tabuleiro, pos2, pedra)
    return tabuleiro

def obtem_posicoes_mesma_orbita(n, pos):
    '''obtem posicoes mesma orbita: int x posicao → lista de posicoes
    obtem posicoes mesma orbita(n, pos) recebe um inteiro n e uma posicao pos, e retorna uma lista de posicoes
    que estao na mesma orbita que a posicao fornecida no tabuleiro de dimensao n.'''
    
    orbita = posicao_para_orbita(pos, n)
    posicoes_mesma_orbita = []

    tab = cria_tabuleiro_vazio(n)
    
    # adiciona todas as posições que pertencem à mesma órbita a uma lista
    for linha in range(n * 2):
        for coluna in range(n * 2):
            posicao_atual = coordenadas_para_posicao((coluna, linha))
            if posicao_para_orbita(posicao_atual, n) == orbita:
                posicoes_mesma_orbita.append(posicao_atual)
    
    # Obtem as posições da linha superior da orbita, seguida da linha da direita, inferior e esquerda
    posicoes_cima = [pos for pos, _ in obtem_linha_horizontal(tab, posicoes_mesma_orbita[1]) if pos in posicoes_mesma_orbita]
    posicoes_baixo = [pos for pos, _ in obtem_linha_horizontal(tab, posicoes_mesma_orbita[-1]) if pos in posicoes_mesma_orbita]
    posicoes_esquerda = [pos for pos, _ in obtem_linha_vertical(tab, posicoes_mesma_orbita[0]) if pos in posicoes_mesma_orbita]
    posicoes_direita = [pos for pos, _ in obtem_linha_vertical(tab, posicoes_mesma_orbita[-1]) if pos in posicoes_mesma_orbita]
    
    # Junta todas as posições em sentido horário, primeiro as posições da linha superior, depois da direita, seguidas da inversa da linha inferior e da inversa da linha da esquerda
    # Usa um dicionário para remover duplicados
    posicoes_mesma_orbita = list(dict.fromkeys(posicoes_cima + posicoes_direita + posicoes_baixo[::-1] + posicoes_esquerda[::-1]))
    
    return posicoes_mesma_orbita

def obtem_posicao_seguinte(tabuleiro, pos, s):
    '''obtem posicao seguinte: tabuleiro x posicao x booleano → posicao
    obtem posicao seguinte(t, p, s) devolve a posicao da mesma orbita que p que se
    encontra a seguir no tabuleiro t em sentido horario se s for True ou anti-horario
    se for False.'''
    n = obtem_numero_orbitas(tabuleiro)
    posicoes_orbita = obtem_posicoes_mesma_orbita(n, pos)
    
    pos_index = posicoes_orbita.index(pos)
    
    if s:
        # Se a posição atual é a última na órbita, retorna a primeira posição
        if pos_index == len(posicoes_orbita) - 1:
            return posicoes_orbita[0]
        # Caso contrário, retorna a próxima posição na órbita
        return posicoes_orbita[pos_index + 1]
    else:
        # Se a posição atual é a primeira na órbita, retorna a última posição
        if pos_index == 0:
            return posicoes_orbita[-1]
        # Caso contrário, retorna a posição anterior na órbita
        return posicoes_orbita[pos_index - 1]
    

def roda_tabuleiro(tabuleiro):
    '''roda tabuleiro: tabuleiro → tabuleiro
    roda tabuleiro(t) modifica destrutivamente o tabuleiro t rodando todas as pedras
    uma posicao em sentido anti-horario, e devolve o proprio tabuleiro.'''
    
    n = obtem_numero_orbitas(tabuleiro)
    novas_posicoes = {}

    # Itera sobre todas as posições do tabuleiro
    for linha in range(n * 2):
        for coluna in range(n * 2):
            pos = coordenadas_para_posicao((coluna, linha))
            pedra = obtem_pedra(tabuleiro, pos)
            # Calcula a nova posição da pedra após a rotação
            nova_pos = obtem_posicao_seguinte(tabuleiro, pos, False)
            novas_posicoes[nova_pos] = pedra

    # Coloca as pedras nas novas posições
    for pos in novas_posicoes:
        coloca_pedra(tabuleiro, pos, novas_posicoes[pos])

    return tabuleiro

def verifica_linha_pedras(tabuleiro, pos, jog, k):
    '''verifica linha pedras : tabuleiro x posicao x pedra x int → booleano
    verifica linha pedras(t, p, j, k) devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal) que contenha a posicao p com k ou mais pedras
    consecutivas do jogador com pedras j, e False caso contrario.'''
    
    # Obtém as linhas horizontal e vertical que passam pela posição
    linhas = [obtem_linha_vertical(tabuleiro, pos), obtem_linha_horizontal(tabuleiro, pos)]
    
    # Obtém as diagonais que passam pela posição
    diagonais = obtem_linhas_diagonais(tabuleiro, pos)
    
    # Adiciona as diagonais às linhas
    linhas.extend(diagonais)

    # Verifica cada linha para ver se há k pedras consecutivas do jogador
    for linha in linhas:
        # Encontra o índice da posição na linha
        indice_posicao = [posicao for posicao, _ in linha].index(pos)
        
        # Verifica segmentos de k posições na linha
        for deslocamento in range(k):
            linha_atual = linha[indice_posicao-deslocamento:indice_posicao+k-deslocamento]
            
            # Verifica se o segmento tem k posições e todas são do jogador
            if len(linha_atual) == k and all(pedras_iguais(jog, pedra) for _, pedra in linha_atual):
                return True
    
    return False

def eh_vencedor(tabuleiro, pedra):
    '''eh vencedor(t, j) e uma funcao auxiliar que recebe um tabuleiro e uma pedra de jogador,
    e devolve True se existe uma linha completa do tabuleiro de pedras do jogador ou False
    caso contrario.'''
    k = obtem_numero_orbitas(tabuleiro) * 2
    posicoes = obtem_posicoes_pedra(tabuleiro, pedra)
    for posicao in posicoes:
        if verifica_linha_pedras(tabuleiro, posicao, pedra, k):
            return True
    return False

def eh_fim_jogo(tabuleiro):
    '''eh fim jogo(t) e uma funcao auxiliar que recebe um tabuleiro e devolve True se o jogo
    ja terminou ou False caso contrario.'''
    Pedra_jog1 = cria_pedra_preta()
    Pedra_jog2 = cria_pedra_branca()
    if eh_vencedor(tabuleiro, Pedra_jog1) or eh_vencedor(tabuleiro, Pedra_jog2):
        return True
    if len(obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra())) == 0:
        return True
    return False

def escolhe_movimento_manual(tabuleiro):
    '''escolhe movimento manual(t) e uma funcao auxiliar que recebe um tabuleiro t e permite
    escolher uma posicao livre do tabuleiro onde colocar uma pedra. A funcao nao modifica
    o seu argumento e devolve a posicao escolhida. A funcao deve apresentar as mensagens
    do exemplo a seguir, repetindo as mensagens ate o jogador introduzir a representacao
    externa de uma jogada valida.'''
    pos_str = input("Escolha uma posicao livre:")
    while True:
        if len(pos_str) not in (2 ,3) or pos_str[0] not in "abcdefghij" or not pos_str[1:].isdigit() or int(pos_str[1:]) not in range(1, 11):
            pos_str = input("Escolha uma posicao livre:")
        else:
            pos = str_para_posicao(pos_str)
            if eh_posicao_valida(pos, obtem_numero_orbitas(tabuleiro)) and pedras_iguais(obtem_pedra(tabuleiro, pos),cria_pedra_neutra()):
                return pos
            else:
                pos_str = input("Escolha uma posicao livre:")

def lvl_facil(tabuleiro, jog):
    '''lvl facil: tabuleiro x pedra → posicao
    lvl facil(t, j) devolve uma posicao escolhida automaticamente de acordo com a estrategia
    facil para o jogador com pedras j.'''

    n = obtem_numero_orbitas(tabuleiro)
    posicoes_livres = obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra())
    posicoes_livres_rodado = []

    # Calcula as posicoes livres dps do tabuleiro ser rotacionado
    for posicoes in posicoes_livres:
        posicoes_livres_rodado.append(obtem_posicao_seguinte(tabuleiro, posicoes, False))

    # Cria uma cópia do tabuleiro e roda-o
    tabuleiro_rodado = roda_tabuleiro(cria_copia_tabuleiro(tabuleiro))

    # Verifica as posições adjacentes para encontrar uma posição com uma pedra igual à do jogador
    for indice_pos, pos in enumerate(posicoes_livres_rodado):
        for pos_adj in obtem_posicoes_adjacentes(pos, n, True):
            if pedras_iguais(obtem_pedra(tabuleiro_rodado, pos_adj), jog):
                return posicoes_livres[indice_pos]
    
    # Se não encontrar essa posição, retorna a primeira posição livre
    return posicoes_livres[0]

def lvl_normal(tabuleiro, jog):
    '''lvl normal: tabuleiro x pedra → posicao
    lvl normal(t, j) devolve uma posicao escolhida automaticamente de acordo com a estrategia
    normal para o jogador com pedras j.'''
    n = obtem_numero_orbitas(tabuleiro)
    pos_livres = obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra())
    pos_livres_rodadas1 = []
    pos_livres_rodadas2 = []
    for indice, posicoes in enumerate(pos_livres):
        pos_livres_rodadas1.append(obtem_posicao_seguinte(tabuleiro, posicoes, False))
        
        pos_livres_rodadas2.append(obtem_posicao_seguinte(tabuleiro, pos_livres_rodadas1[indice], False))
        
    tab_rodado1 = roda_tabuleiro(cria_copia_tabuleiro(tabuleiro))
    tab_rodado2 = roda_tabuleiro(cria_copia_tabuleiro(tab_rodado1))

    bot = cria_pedra_branca() if eh_pedra_preta(jog) else cria_pedra_preta()
    l_jog = l_jog_max = l_bot = l_bot_max = melhor_pos_jog = melhor_pos_bot = 0

    for indice_pos, pos in enumerate(pos_livres_rodadas1):
        coloca_pedra(tab_rodado1, pos, jog)
        for k in range(n * 2, 0, -1):
            if verifica_linha_pedras(tab_rodado1, pos, jog, k):
                l_jog = k
                if l_jog > l_jog_max:
                    l_jog_max = l_jog
                    melhor_pos_jog = indice_pos
                    break
        remove_pedra(tab_rodado1, pos)

    for indice_pos, pos in enumerate(pos_livres_rodadas2):
        coloca_pedra(tab_rodado2, pos, bot)
        for k in range(n * 2, 0, -1):
            if verifica_linha_pedras(tab_rodado2, pos, bot, k):
                l_bot = k
                if l_bot > l_bot_max:
                    l_bot_max = l_bot
                    melhor_pos_bot = indice_pos
                    break
        remove_pedra(tab_rodado2, pos)

    if l_jog_max >= l_bot_max:
        return pos_livres[melhor_pos_jog]
    
    elif l_bot_max > l_jog_max:
        return pos_livres[melhor_pos_bot]
    
    return pos_livres[0]


  

def escolhe_movimento_auto(tabuleiro, jog, lvl):
    '''escolhe movimento auto: tabuleiro x pedra x str → posicao
    escolhe movimento auto(t, j, lvl) e uma funcao auxiliar que recebe um tabuleiro t (em
    que o jogo nao terminou ainda), uma pedra j, e a cadeia de carateres lvl correspondente
    a estrategia, e devolve a posicao escolhida automaticamente de acordo com a estrategia
    selecionada para o jogador com pedras j.'''
    if lvl == "facil":
        return lvl_facil(tabuleiro, jog)
    if lvl == "normal":
        return lvl_normal(tabuleiro, jog)



def orbito(n, modo, jog):
    ''' orbito: int x str x str → int
    orbito(n, modo, jog) e a funcao principal que permite jogar um jogo completo de Orbito-
    n. A funcao recebe o numero de orbitas do tabuleiro, uma cadeia de carateres que
    representa o modo de jogo, e a representacao externa de uma pedra (preta ou branca),
    e devolve um inteiro identificando o jogador vencedor (1 para preto ou -1 para branco),
    ou 0 em caso de empate.'''
    if type(n) != int or n < 2 or n > 5 or modo not in ('facil', 'normal', '2jogadores') or jog not in (pedra_para_str(cria_pedra_preta()), pedra_para_str(cria_pedra_branca())):
        raise ValueError('orbito: argumentos invalidos')
    
    jogador_atual = cria_pedra_preta()
    tabuleiro = cria_tabuleiro_vazio(n)
    if eh_pedra_branca(str_para_pedra(jog)):
        peca_adv = cria_pedra_preta()
    else:
        peca_adv = cria_pedra_branca() 

    print(f"Bem-vindo ao ORBITO-{n}.")
    if modo == '2jogadores':
        print("Jogo para dois jogadores.")
    else:
        print(f"Jogo contra o computador ({modo}).")
        print(f"O jogador joga com '{jog}'.")

    print(tabuleiro_para_str(tabuleiro))

    jog = str_para_pedra(jog)
    while not eh_fim_jogo(tabuleiro):
        if modo == '2jogadores':
            print(f"Turno do jogador '{pedra_para_str(jogador_atual)}'.")
            pos = escolhe_movimento_manual(tabuleiro)
        else:
            if pedras_iguais(jogador_atual, jog):
                print("Turno do jogador.")
                pos = escolhe_movimento_manual(tabuleiro)
            else:
                print(f"Turno do computador ({modo}):")
                pos = escolhe_movimento_auto(tabuleiro, jogador_atual, modo)
        
        tabuleiro = coloca_pedra(tabuleiro, pos, jogador_atual)
        tabuleiro = roda_tabuleiro(tabuleiro)
        print(tabuleiro_para_str(tabuleiro))

        if eh_pedra_preta(jogador_atual):
            jogador_atual = cria_pedra_branca()
        else:
            jogador_atual = cria_pedra_preta()

    if modo == '2jogadores':
        if eh_vencedor(tabuleiro, cria_pedra_preta()):
            print("VITORIA DO JOGADOR 'X'")
            return pedra_para_int(cria_pedra_preta())
        elif eh_vencedor(tabuleiro, cria_pedra_branca()):
            print("VITORIA DO JOGADOR 'O'")
            return pedra_para_int(cria_pedra_branca())
        else:
            print("EMPATE")
            return pedra_para_int(cria_pedra_neutra())
    else:
        if eh_vencedor(tabuleiro, jog) and eh_vencedor(tabuleiro, peca_adv) or not eh_vencedor(tabuleiro, jog) and not eh_vencedor(tabuleiro, peca_adv):
            print("EMPATE")
            return pedra_para_int(cria_pedra_neutra())
        
        elif eh_vencedor(tabuleiro, jog):
            print("VITORIA")
            return pedra_para_int(jog)
            
        elif eh_vencedor(tabuleiro, peca_adv):
            print("DERROTA")
            return pedra_para_int(peca_adv)
        


if __name__ == "__main__":
    print("=== Jogo Orbito ===")
    print("Iniciando tabuleiro 4x4 contra o computador (normal)...")
    try:
        # n = 2 -> grelha 4x4, modo = 'normal', jogador = 'X'
        orbito(2, "normal", "X")
    except KeyboardInterrupt:
        print("\nJogo interrompido.")
