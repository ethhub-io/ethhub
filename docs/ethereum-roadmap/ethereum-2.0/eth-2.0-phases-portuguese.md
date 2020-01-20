Título: Ethereum 2.0 Fases - EthHub

Descrição: Um guia para as fases e planos de implementação da Ethereum 2.0, que se chama Serenidade.

# Fases da Ethereum 2.0

_Como Ethereum 2.0 está em intensa pesquisa e desenvolvimento, essa página pode se tornar obsoleta a qualquer momento. É mantida atualizada com base nos melhores esforços._

## Introdução

A grande atualização da rede Ethereum, chamada Ethereum 2.0, Eth2 ou Serenity, trará com ela Sharding, Proof Stake, uma nova máquina virtual \(eWASM\) e muito mais. É importante entender que esta atualização não ocorrerá em um único momento - em vez disso, será implantada por fases. Este documento tenta ser um ponto de referência para estas fases e o que cada uma inclui.

## Metas de Design

O pesquisador de Ethereum Danny Ryan tem [estipulado](https://github.com/ethereum/eth2.0-specs#design-goals) 5 objetivos de design distintos para a Ethereum 2.0:

* Descentralização: para permitir um laptop de um usuário típico processar/validar fragmentos (incluindo qualquer validação de nível de sistema de uma cadeia de beacons).
* **Resiliência:** para permanecer online através de grandes partições de rede e mesmo quando partes muito grandes de nós ficam offline.
* **Segurança:** para utilizar técnicas de criptografia e design que permitam uma grande participação de validadores no total e por hora unitária.
* **Simplicidade:** para minimizar a complexidade, mesmo que ao custo de algumas perdas de eficiência.
* **Longevy:** para selecionar todos os componentes como eles são ou quânticos seguros ou podem ser facilmente cambiados para contrapartes quânticas seguras quando disponíveis.

## Fase 0 - Cadeia de Beacon

### **O que está incluído**

Fase 0 é o nome dado para o lançamento da Cadeia de Beacon. A Cadeia de Beacon gerenciará o protocolo de Proof of Stake Casper e todas as suas cadeias de fragmentos. Como Ben Edgington [escreve ](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129), "Há uma série de aspectos para isso: gerenciar validadores e suas participações; nomeando o bloco escolhido proponente para cada fragmento em cada etapa; organizando validadores em comitês para votar nos blocos propostos; aplicação das regras de consenso; aplicação de recompensas e sanções aos validadores; e, ser um ponto de referência em que os fragmentos registam os seus estados para facilitar transações cruzadas.”

A fonte primária de carga na Cadeia de Beacon será "atestações". Atestações são votos disponíveis para um bloco de fragmentos e, simultaneamente, provas de pontos de interesse para um bloco de beacon. Um número suficiente de atestações para o mesmo bloco de fragmentos irá criar um "cruzamento" que confirma o segmento do fragmento até aquele bloco de fragmento na Cadeia de Beacon.

A Fase 0 irá usar o Gadget de Finalidade Amigável (Casper the Friendly Finality Gadget - FFG) para esta finalidade. A finalidade, em termos muito vagos, significa que, uma vez concluída uma determinada operação, esta ficará para sempre gravado na história e nada pode reverter essa operação.

#### **ETH2: O Novo Ether**

Fase 0 irá introduzir o ETH2 que será um novo ativo para acionistas \(validadores\) para ser usado na Cadeia de Beacon. Ele será criado utilizando dois métodos:

* Como recompensa por validar a Cadeia de Beacon \(e fragmentos após a Fase 1\).
* Comprá-lo para 1 ETH por qualquer usuário ETH1.X através de um [contrato de registro](https://github.com/ethereum/beacon_chain/blob/master/contracts/validator_registration.v.py). O contrato refere-se a ele como um depósito.

Atualmente não há nenhuma maneira de retirar ou transferir ETH2 da Cadeia de Sinalizador na Fase 0. Uma vez depositado no contrato de registo de validador ETH1.x, o ETH1 é efetivamente queimado. Os validadores da Cadeia de Beacons assistem a este contrato e enviam informações de depósito à Cadeia de Beacons, que então emitem ETH2 aos depositantes.

Por último, a Cadeia de Beacon irá gerar uma boa qualidade \(distribuída, verificável, imprevisível e (razoavelmente) aleatória) para o resto do sistema. Ela usará RANDAO que é simplesmente uma maneira de combinar contribuições \(números aleatórios individuais\) fornecidas por muitos participantes em um único número de saída.

Isso será usado para organizar validadores em proponentes e comites de blocos.

### **Como será a rede?**

Quando a Fase 0 estiver completa, haverá duas cadeias Ethereum ativas. Por uma questão de clareza, vamos chamá-las de rede ETH1 \(atual, rede principal usando PoW\) e de ETH2 \(a nova rede de Cadeia de Beacons\). Durante esta fase, os usuários poderão migrar seu ETH da rede Eth1 para a rede de Eth2 e tornar-se validadores. No entanto, eles NÃO conseguirão migrar estes ETH de volta (por enquanto). A razão pela qual alguém pode querer fazer isto é porque ele pode ganhar juros pagos pelo ETH na rede de Eth2.

Para executar a Cadeia de Beacons, você vai precisar de um cliente da rede da Cadeia de Beacons. Estes estão sendo desenvolvidos separadamente do conjunto de clientes Ethereum padrão (Geth, Parity, Pantheon, etc) por um número de [equipes](/ethereum-roadmap/ethereum-2.0/eth2.0-teams/teams-building-eth2.0/). A maioria das equipes está publicando atualizações periódicas sobre o progresso do desenvolvimento de seus clientes e algumas das equipes estão oferecendo recompensas aos colaboradores para incluir cada vez mais desenvolvedores na construção do Ethereum 2.0 . Você pode contribuir com doações no Gitcoin [aqui](https://gitcoin.co/grants/)

Por si só, a Cadeia de Beacons pode não parecer particularmente útil. Mas, como primeiro componente da Ethereum 2.0 a ser entregue, é a base de todo o sistema.

**Considerações importantes**

* ETH2 é transferível para e de fragmentos assim que a Fase 2 estiver completa (embora isso possa mudar no futuro).
* Haverá uma quantidade mínima de ETH em depósito necessária para a inicialização inicial da cadeia de sinalizadores. Isto é definido como `CHAIN_START_FUL_DEPOSIT_THRESHOLD` no [contrato de depósito que estará ativo na rede Eth 1.0](https://github.com/ethereum/deposit_contract/blob/master/deposit_contract/contracts/validator_registration.v.py#L3).
* Para se tornar um validador, você precisará depositar 32 ETH2.
* Durante a fase 0, todas as transações de usuário e computação de contratos inteligentes ainda ocorrerão na rede Eth1.

## Fase 1 - Cadeias de Fragmento

### O que está incluído

As cadeias de fragmentos são chave para a futura escalabilidade já que permitem transações em paralelo, e haverá 64 delas implantadas na Fase 1 (com a opção de adicionar mais ao longo do tempo).

A fase 1 está principalmente preocupada com a construção, validade e consenso sobre os dados destas cadeias de fragmentos. Fase 1 não especifica o estado da execução da cadeia de fragmentos ou os saldos da conta. Será como uma execução experimental para a estrutura de compartilhamento ao invés de uma tentativa de usar fragmentos em escala. A Cadeia de Beacon tratará os blocos da cadeia de fragmentos como simples coleções de bits sem estrutura ou significado.

**Crosslinks** <br/> Periodicamente, o estado atual (a "combinação de dados root") de cada fragmento é gravado em um bloco de Cadeia de Beacon como uma ligação cruzada. Quando o bloco de Cadeia de Beacon for finalizado, o bloco de fragmento correspondente é considerado finalizado, e outros fragmentos sabem que podem confiar nisso para transações cruzadas. <br/>

Links cruzados são um conjunto de assinaturas de um comite atestando um bloco em uma cadeia de fragmentos que pode ser incluído na Cadeia de Beacon. Links cruzados são os principais meios pelos quais a Cadeia de Beacon "aprende sobre" o estado atualizado das cadeias de fragmentos. Os Links Cruzados também servem como infraestrutura para uma comunicação assíncrona entre cadeias de fragmentos.

Validadores da cadeia de fragmentos, que são selecionados aleatoriamente pela Cadeia de Beacons para cada fragmento em cada segmento, meramente chegam a um acordo sobre o conteúdo de cada bloco. Eles atestam o conteúdo e o estado através de uma ligação cruzada. Não importa qual informação aparece nos blocos de fragmentos, desde que todas as comissões cheguem a consenso e atualizem a Cadeia de Beacon no fragmento regularmente.

### Como será a rede?

As cadeias Eth1 e Eth2 ainda funcionarão em paralelo após a fase 1.

### Considerações importantes

* Na fase 0, 1 e 2, a rede principal PoW (Eth1) continuará ativa enquanto se realizam testes e a transição estiver ocorrendo para a rede Eth2. Isto significa que as recompensas serão pagas aos validadores do Ethereum 2.0, bem como as recompensas normais de blocos PoW. Por conseguinte, a inflação combinada das duas cadeias pode disparar inicialmente, mas depois começará a ter tendência para a faixa dos 0-1%, à medida que a cadeia PoW for gradualmente "desenfatizada".

## Fase 2 - Execução do estado

### O que está incluído?

A Fase 2 é onde a funcionalidade de todo o sistema começará a reunir-se. A transição de uma cadeia de fragmentos de simples containers de dados para uma cadeia de dados estruturados e com Contratos Inteligentes será reintroduzida. Cada fragmento irá gerenciar uma máquina virtual baseada em [eWASM](https://github.com/ewasm/design). Ele suportará contas, contratos, estado e outras abstrações que estamos familiarizados do Solidity. Podemos esperar ferramentas familiares como truffle, solc, ganache portado para suportar o eWASM antes ou durante a fase 2.

A Fase 2 também introduz o conceito de 'Ambientes de Execução' (EEs). EEs dentro de um fragmento podem ser construídos da forma que um desenvolvedor considerar adequada - pode haver um EE para uma cadeia de estilo UTXO, um sistema ao estilo Libra, um EE para um fornecedor de taxas de mercado e além. Todo fragmento tem acesso a todos os ambientes de execução e tem a capacidade de fazer transações dentro deles, além de executar e interagir com contratos inteligentes. Observe que o conceito de ambiente de execução ainda está em grande análise e desenvolvimento.

### Considerações importantes
* Um dApp terá que escolher em qual fragmento quer estar. Essa decisão é importante porque a comunicação cruzada difere no Eth2, uma vez que não é síncrona, o que significa que se perde alguma composabilidade entre fragmentos<br/>
* Um dApp teria que ter dados bastante grandes para consumir todos os recursos em um dado fragmento para justificar se espalhar por vários deles.<br/>
* Esta fase vai dar fragmentos com eWASM como o EVM 2.0.
* É uma pergunta em aberto quando e como as contas e contratos da Ethereum 1.0 serão migrados para a Ethereum 2.0. Existem alguns [planos de atualização](https://ethresear.ch/t/the-eth1-eth2-transition/6265)

## O que vem depois?
O roteiro da cadeia de fragmentos de acordo com a wiki oficial sugere 6 fases. O pesquisador Justin Drake acredita firmemente que as fases de compartilhamento 1 e 2 virão em 2020 e 2021, respectivamente \(assumindo que a Cadeia do Beacon inicia no começo de 2020\). <br/>

A partir da fase 3, qualquer especulação feita é sujeita a mudanças, você pode ir verificar a [wiki](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#phase-3-light-client-state-protocol) para mais informações sobre a fase.

## Recursos

* [Informações da Ethereum 2.0](https://hackmd.io/e4cNiocFTiS67j6yJ_XHPw?view)
* [Especificações da Ethereum 2.0](https://github.com/ethereum/eth2.0-specs)
* [Fase 0 para Humanos](https://notes.ethereum.org/jDcuUp3-T8CeFTv0YpAsHw?view)
* [Roadmap para a cadeia de fragmentos](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#strongphase-3strong-light-client-state-protocol)
* [Estado do protocolo Ethereum](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129)
* [Objetivos do Ethereum 2.0](https://media.consensys.net/exploring-the-ethereum-2-0-design-goals-fd2d901b4c01)
* [Sessão de perguntas e respostas do ETHMagicians](https://medium.com/ethereum-magicians/demystifying-the-road-to-ethereum-2-0-8130ade8d00f)
* [eWASM](https://www.coindesk.com/open-heart-surgery-inside-ethereums-crucial-replacement-of-the-evm)
