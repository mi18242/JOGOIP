# Snake python

Snake python é um jogo baseado em uma experiência 2D, que simula uma cobra que "passeia" pelo Grad5 e se "alimenta" de 3 coletáveis que remetem as questões fáceis, médias e difíceis das listas de IP, além disso, a cobra tenta fugir ao máximo da "bomba"(run time error) - objeto que causa sua morte. Além do mais, o tamanho da cobra cresce à medida que mais se alimenta dos coletáveis e, ademais, a cobra também morre se tocar em si mesma e se bater nas "boradas" do jogo. Vale ressaltar também que:
- HARD: aumenta em dois a pontuação da cobra;
- MEDIUM: aumenta em três a potuação da cobra;
- EASY : aumenta em um a pontuação da cobra;

## Como rodar o jogo:
> 1º - É necessário ter uma IDE instalada, como o visual studio code ou o pycharm.
> >
> 2º - É necessário instalar o pygame e o python em sua máquina.
> >
> 3 º - Rodar o arquivo main.py

## Como jogar o jogo:
Para mover a cobrinha, é necessário usar as seguintes teclas:

   |  **Player** | &#8592; , &#8593; , &#8594; , &#8595;  |

Sendo a primeira delas para mover a cobrinha para o lado, a segunda mover para cima, a terceira mover para o outro lado e a quarta para baixo.

## Equipe:
- Aigo Alana (aacl)
- Ismael Álvaro (ials)
- Milla Rwana (mras)
- Pedro Henrique (phss)
- Rayssa Vitória (rvls)

## Divisão dos trabalhos:
- Aigo Alana: Criação de uma tela de menu e de fim de jogo, implementação de coletáveis com o adicional de uma pontuação diferente para cada coletável.
- Ismael Álvaro: Identificação e armazenamento dos coletáveis, estruturação dos diretórios, desenvolvimento da classe dos objetos coletáveis e atualização das imagens de Spritesheets.
- Milla Rwana: desenvolvimento da base do código, modularização e organização do código, implementação da lógica da movimentação da cobrinha.
- Pedro Henrique: Ajustes para garantir o bom desempenho do jogo, criação da função bomba e ajustes no código principal para integrar essa funcionalidade
- Rayssa Vitória: Aplicação dos sprites e a base do background, correção do tamanho da fonte na tela, testar o jogo para buscar possíveis erros.

## link para acessar o código:
- https://github.com/mi18242/JOGOIP

## Organização do código:
> Como usamos o conceito de modularização do código, o nosso código foi dividido em 4 módulos:

> - O módulo "Bomb.py" foi criado para armazenar informações relativa a bomba(run time error). Além disso, possui:
  
    - Class Bomb: Responsável por criar, posicionar e desenhar uma bomba em um jogo feito com Pygame e, além disso, contém "gerar bomba"- que gera uma posição aleatória para a bomba que não colide com a cobra ou com a comida e "desenhar"- que desenha a bomba na tela na posição bomba_x, bomba_y.

> - O módulo "main.py" é a funcao responsável por rodar o jogo.

> - O módulo "Settings.py" é a funcao que inicializa o Pygame e faz as configurações principais do jogo, além disso define os caminhos para os diretórios principais, de imagens e sons e faz o carregamento de imagens e definição das cores.

> - O módulo "sprites.py" foi criado para armazenar uma classe chamada food e carrega as informações relativas a "comida" e atualiza o sprite da comida :

    - Class comida(): Esta classe utiliza sprites para representar diferentes tipos de comida, cada um com uma cor e um valor em pontos diferentes.

> - O módulo "functions.py" contém funções auxiliares para diferentes aspectos do jogo:

    - "desenhar_cobra": Esta função é responsável por desenhar a cobra na tela.
    
    - "desenhar_pontuacao": Esta função desenha a pontuação atual do jogador na tela.
    
    - "selecionar_velocidade": Controla a direção da cobra com base na tecla pressionada pelo jogador.
    
    - "fim_de_jogo": Esta função é chamada quando o jogo termina e mostra na tela sobre a pontuação e as capturas feitas.

> -  O módulo "Snake_game.py":  Define uma classe SnakeGame, que implementa a lógica principal do jogo. Incluindo o loop do jogo, controle de entrada, lógica de colisão, e a interface do usuário. As classes Food e Bomb são usadas para criar a dinâmica do jogo, fornecendo elementos que a cobra pode interagir. 

    

## Ferramentas e bibliotecas usadas:

- Pygame: Usado pra importar configurações próprias de jogo e, assim, facilitar o trabalho do grupo.
- random : Uma biblioteca nativa do Python que é responsável por facilitar as operações de aleatoriedade, como a geração das frutas e etc.
- os: Um módulo nativo do Python que fornece uma maneira de interagir com o sistema operacional, incluindo funções para manipulação de arquivos, diretórios e processos, bem como para obter informações sobre o ambiente do sistema. Foi usado no código, principalmente, na parte de settings.

## Conceitos apresentados na disciplina que foram aplicados:
  Utilizamos diversos conceitos enquanto estávamos desenvolvendo o jogo, dentre eles:

- Listas: Utilizadas na geração de bombas e na posição da cobra. No código rodar_jogo, por exemplo, a lista pixels armazena as coordenadas dos segmentos da cobra e é usada para evitar que a comida apareça em posições ocupadas pela cobra.
- Tuplas: Usadas para identificar coordenadas, como na definição da posição da comida e da bomba. No código da classe Comida, por exemplo, as tuplas são usadas para armazenar as coordenadas (comida_x, comida_y) e definir a posição da comida.
- Orientação a Objetos: Estruturação completa dos componentes do jogo. Como, por exemplo, a classe food que define objetos de comida e a classe Bomb que é responsável por "desenhar" o run time error no jogo. 
- Condicionais: Importantes para as regras e colisões do jogo. No código rodar_jogo, as condicionais verificam se a cobra colidiu com as paredes ou consigo mesma, ou se a cobra colidiu com a comida ou com a bomba.
- Laços: O jogo ocorre dentro de um laço while not fim_jogo. Esse laço mantém o jogo em execução, atualizando a posição da cobra, desenhando os elementos na tela e verificando eventos de entrada do jogador.

## Desafios e Lições:
No decorrer do processo de criação e aperfeiçoamento do jogo, tivemos alguns desafios com relação ao uso das ferramentas novas apresentadas a serem utilizadas e problemas encontradas que poderiam atrapalhar na jogabilidade, que poderiam atrapalhar na jogabilidade, por exemplo:

- POO: A compreensão de como iríamos usar o POO(programação orientada a objetos) no código nos custou tempo. Conforme fomos entendendo mais sobre seus aspectos, percebemos que precisávamos implementar mais de suas ferramentas no código, principalmente por causa da organização e facilitação as possíveis alterações.
- Problema na colisão: Nossa cobra pode morrer de três formas: Ao se chocar com as bordas da tela, uma colisão com a bomba(run time error) ou ao bater em si mesma. Entretanto, ao fazer o movimento de, por exemplo, ir para a direita e ir para a esquerda, a cobra chocava com si mesma e morria. Esse movimento não poderia acontecer no jogo, visto que poderia confunfir a jogabilidade, posto isto, para resolver o problema, adicionamos mais uma condicional.
- Ajustes na tela: Por termos tomado as medidas da tela cedo, foi necessário revisar tudo novamente para termos um designer melhor e que se encaixasse nos nossos objetivos. Além disso, foi preciso ajustar qual parte a cobra poderia pecorrer, para não "cobrir" a informação da pontuação.
- Reduzido conhecimento em Pygame, git/github: Foi necessário buscar informações sobre essas ferramentas que facilitam muito a elaboração de projetos.
   
Além disso, vale ressaltar que adquirimos um conhecimento muito grande sobre trabalho em equipe e divisão justa de serviços e a importancia de como usar a teoria aprendida nas aulas de maneira eficiente.

## Imagens:












    



    















