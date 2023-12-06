# RPG-Monster-Linker

Este projeto é uma ferramenta que visa linkar diferentes obras de RPG, utilizando como base os sistemas Tagmar, Pathfinder e Dungeons & Dragons (D&D). A ideia central é criar um banco de dados unificado que contenha informações sobre monstros presentes em Tagmar, e encontrar monstros similares ou relacionados nos sistemas Pathfinder e D&D.

Equipe
Desenvolvedores:

Erick Ramos Coutinho

Victor Matheus Araújo Oliveira

Orientação:

Professor Artur de Oliveira da Rocha Franco
## Arquivos
Bd_bestas: dataset final
interface_pesquisador_besta: Código da construção da interface de pesquisa.
análise_descritiva: análise dos datasets de modo separado e de forma conjunta.

Funcionalidades Principais
Banco de Dados Unificado: O projeto conta com um banco de dados central, chamado bd_bestas, que inclui 81 monstros de Tagmar. Cada entrada contém informações detalhadas, como descrição e atributos específicos para Tagmar, Pathfinder e D&D.

Pesquisa de Monstros: Utilizando scripts em Python, é possível realizar pesquisas no banco de dados para obter informações sobre monstros específicos. Ao inserir o nome de um monstro, o sistema retorna sua descrição e atributos em cada um dos sistemas RPG.

Estrutura do Banco de Dados
ADD descrição de cada atributo das colunas de cada sistema

O banco de dados bd_bestas possui as seguintes colunas:

## Tagmar:
Os 7 atributos podem basicamente assumir valores entre -4 e 6. (obs: alguns seres celestiais podem atigir valores superiores a 13 pontos.)

Atributos:

INT(tagmar): Intelecto - Capacidade de raciocínio, memória. O Intelecto é importante para o estudo de magia arcana e Habilidades como Navegação, Medicina, etc.

AUR(tagmar): Aura - Todos os seres são envolvidos por um tipo de energia mística que os conecta com outros planos de existência. Esta energia é chamada Aura, e ela permite a interação do personagem com a magia. (mais capacidade mágica, resistência contra magias, etc.)

CAR(tagmar): Carisma - Corresponde à voz de comando, a força de vontade, e a auto-estima. Define a força da personalidade do personagem. Desta característica dependem Habilidades como Persuasão e Liderança.

FOR(tagmar): Força - A Força é muito importante em combate, pois, além de aumentar o dano, permite o uso de armas mais pesadas ou maiores. Além do combate, serve para levantar mais peso.

FIS(tagmar): Físico - Resistência ao esforço e à dor; saúde e vigor. Ajuda a resistir à fadiga do combate e, em caso de ferimentos, a sobreviver aos golpes recebidos.

AGI(tagmar): Agilidade - São os reflexos, a rapidez e a coordenação. Esta característica é especialmente importante para o Subterfúgio e para as Manobras; além de tornar o personagem mais difícil de ser acertado em combate.

PER(tagmar): Percepção - Capacidade do indivíduo de perceber o ambiente em que está. Inclui a atenção e a capacidade de concentração. É de extrema importância para Rastreadores e no uso de Habilidades como Manusear Armadilhas, Observar e Escutar.

## Pathfinder:
Os valores de atributos de pessoas comuns variam de 3 a 18, porém personagens de nível elevado podem ter valores de atributo muito acima de 18.

Atributos:

Str (Path): Representa a força física e a capacidade de um personagem para lidar com tarefas que exigem poder bruto.

Dex (Path): Reflete a agilidade, velocidade, equilíbrio e coordenação do personagem. Afeta a capacidade de esquiva, a precisão em ataques à distância e a habilidade em realizar atividades que exigem destreza manual.

Con (Path): Representa a saúde, resistência e vitalidade do personagem. Afeta a quantidade de pontos de vida, a resistência a doenças e venenos, e a habilidade de suportar condições adversas.

Int (Path): Reflete a astúcia, raciocínio lógico e conhecimento do personagem. Afeta a quantidade de pontos de perícia que o personagem recebe ao subir de nível, além de influenciar testes de conhecimento e a capacidade de aprender novas habilidades.

Wis (Path): Representa a intuição, percepção e força de vontade do personagem. Afeta testes de resistência contra magias e efeitos mentais, bem como a habilidade de perceber detalhes e situações sutis.

Cha (Path): Reflete o magnetismo pessoal, capacidade de liderança e habilidade social do personagem. Afeta testes de diplomacia, intimidação e blefe, além de influenciar a reação de outras criaturas em relação ao personagem.

## D&D:
A pontuação máxima de um atributo é geralmente 20, isso significa que um personagem, em condições normais, não pode ter um atributo superior a 20 sem o auxílio de efeitos mágicos, itens mágicos, ou outras circunstâncias especiais.

Atributos:

Str (D&D): Refere-se à força física do personagem, sua capacidade de levantar objetos pesados, causar dano corpo a corpo e realizar tarefas que exigem força bruta.

Dex (D&D): Representa a agilidade, coordenação e reflexos do personagem. Afeta a precisão em ataques à distância, a capacidade de evitar ataques e a realização de tarefas que requerem habilidade manual e movimentos ágeis.

Con (D&D): Reflete a resistência física e a saúde do personagem. Uma alta constituição ajuda na resistência a doenças, venenos e na capacidade de resistir a danos.

Int (D&D): Representa a capacidade mental do personagem, incluindo o raciocínio lógico, memória e conhecimento. Personagens com alta inteligência são muitas vezes bons em magias e habilidades que envolvem pensamento crítico.

Wis (D&D): Reflete a percepção, intuição e senso comum do personagem. Afeta a capacidade de perceber ameaças, discernir motivações e resistir a magias que afetam a mente.

Cha (D&D): Representa a personalidade, carisma e poder de persuasão do personagem. Pode influenciar a interação social, a capacidade de liderança e a habilidade de convencer os outros.

## Contribuição
Sinta-se à vontade para contribuir com novos monstros, correções ou melhorias.
