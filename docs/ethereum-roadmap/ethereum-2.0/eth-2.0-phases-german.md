title: Ethereum 2.0 Phasen - EthHub

description: Ein Leitfaden der Phasen und Implementierungspläne von Ethereum 2.0, auch Serenity genannt.

# Phasen in Ethereum 2.0

_Da sich Ethereum 2.0 aktuell stark in der Forschungs- und Entwicklungsphase befindet, kann diese Seite kurzfristig veraltet sein. Es wird versucht, sie nach bester Möglichkeit auf dem neuesten Stand zu halten._

## Einführung

Ethereums großes Netzwerk-Upgrade, genannt Ethereum 2.0, Eth2.0 oder auch Serenity, wird Sharding, Proof of Stake, eine neue virtuelle Maschine \(eWASM\) und weitere Neuerungen einführen. Es ist wichtig zu verstehen, dass dieses Upgrade nicht auf einmal stattfinden wird, sondern in verschiedenen Phasen ausgerollt wird. Dieses Dokument versucht, ein Bezugspunkt für diese Phasen und ihre jeweiligen Inhalte zu sein.

## Designziele

Der Ethereum-Forscher Danny Ryan hat 5 verschiedene Designziele für Ethereum 2.0 [festgelegt](https://github.com/ethereum/eth2.0-specs#design-goals):

* **Dezentralisierung:** Damit ein handelsüblicher Laptop mit begrenzten Ressourcen ausreicht, um die Validierung/Verarbeitung von O(1) Shards auszuführen (einschließlich jeder systemischen Validierung wie die der Beacon-Chain).
* **Widerstandsfähigkeit:** Damit das Netzwerk auch bei großen Spaltungen (Forks) oder wenn eine sehr große Anzahl von Nodes offline geht, stabil und funktionsfähig bleibt.
* **Sicherheit:** Sodass Crypto- und Designtechniken verwendet werden, die eine große Anzahl von Validatoren/Nodes insgesamt und per Zeiteinheit ermöglichen.
* **Einfachheit:** Damit die Komplexität minimiert wird, wenn auch auf Kosten einiger Effizienzverluste.
* **Langlebigkeit:** Damit alle Komponenten so ausgewählt werden, dass sie entweder direkt Quantensicherheit besitzen oder einfach ausgetauscht werden können, wenn quantensichere Komponenten verfügbar sind.

## Phase 0 – Beacon-Chain

### **Was beinhaltet sie?**

Phase 0 beinhaltet den Start der sogenannten Beacon-Chain. Die Beacon-Chain verwaltet das „Casper Proof of Stake“-Protokoll für sich selbst und alle Shard-Chains. Wie Ben Edgington [es ausdrückt](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129): „Es gibt eine Reihe an auszuführenden Aufgaben: Die Verwaltung von Validatoren und deren Stakes/Einsätze, die Nominierung des ausgewählten Block-Vorschlagenden für jeden Shard in jedem Schritt, die Organisation von Validatoren in Ausschüssen zum Abstimmen über die vorgeschlagenen Blöcke, die Anwendung der Konsensregeln, die Anwendung von Prämien und Strafen für Validatoren und die Funktion als Ankerpunkt, an dem die Shards ihre Status registrieren, um Shard-übergreifende-Transaktionen (Cross-Shard-Transaktionen) zu ermöglichen.“

Die primäre Quelle der Nutzlast auf der Beacon-Chain werden „Bescheinigungen“ sein. Bescheinigungen sind Verfügbarkeitsabstimmungen für einen Shard-Block und gleichzeitig „Proof of Stake“-Abstimmungen für einen Beacon-Block. Eine ausreichende Anzahl von Bescheinigungen für denselben Shard-Block erzeugt einen „Crosslink“, der das Shard-Segment bis zu diesem Shard-Block in die Beacon-Chain bestätigt.

Phase 0 wird Casper das Friendly Finality Gadget (FFG) für die Endgültigkeit verwenden. Die Endgültigkeit bedeutet einfach ausgedrückt, dass eine bestimmte Operation nach ihrer Durchführung für immer in der Geschichte der Blockchain festgeschrieben ist und nichts diese Operation rückgängig machen kann.

#### **ETH2: Das neue Ether**

Phase 0 führt ETH2 ein, ein neues Asset für Staker \(Validatoren\), das in der Beacon-Chain verwendet wird. Es wird durch zwei Methoden generiert:

* Als Belohnung für die Validierung der Beacon-Chain \(und Shards nach Phase 1\).
* Mit dem Kauf für 1 ETH durch einen ETH1.X-Nutzer über einen [Registrierungsvertrag](https://github.com/ethereum/beacon_chain/blob/master/contracts/validator_registration.v.py). Der Vertrag bezieht sich darauf als Hinterlegung.

Derzeit gibt es keine Möglichkeit, ETH2 in Phase 0 aus der Beacon-Chain abzuheben oder zu übertragen. Nach der Einzahlung im ETH1.x Validator-Vertrag wird das ETH1 Asset effektiv verbrannt. Beacon-Chain-Validatoren beobachten diesen Vertrag und übermitteln Einlageninformationen an die Beacon-Chain, die dann entsprechend ETH2 an die Einleger ausgibt.

Zu guter Letzt wird die Beacon-Chain eine gute Qualität von Zufälligkeit für den Rest des Systems erzeugen \(verteilt, überprüfbar, unvorhersehbar und (angemessen) unparteiisch\). Es wird RANDAO verwenden, womit von vielen Teilnehmern bereitgestellte Beiträge \(individuelle Zufallszahlen\) ganz unkompliziert in einer einzigen Ausgabenummer zusammengefasst werden können.

Dies wird verwendet, um Validatoren in Block-Vorschläger und Ausschüsse für Entscheidungen zu organisieren.

### **Wie wird das Netzwerk aussehen?**

Sobald Phase 0 abgeschlossen ist, wird es zwei aktive Ethereum-Blockchains geben. Der Klarheit halber nennen wir sie die Eth1-Chain \(aktuelle, PoW öffentliche Blockchain\) und die Eth2-Chain \(neue Beacon-Chain\). Während dieser Phase können Benutzer ihr ETH von der Eth1-Chain in die Eth2-Chain eintauschen und die Rolle von Validatoren einnehmen. Allerdings können sie diese ETH (vorläufig) NICHT zur Eth1-Chain zurückmigrieren. Ein Grund für diesen Schritt könnte die Auszahlung von Zinsen in ETH in der Eth2-Chain sein.

Um die Beacon-Chain ausführen zu können, brauchst du einen Beacon-Chain-Client. Dieser wird derzeit getrennt von der bekannten Suite von standardmäßigen Ethereum-Clients (Geth, Parity, Pantheon, etc.) von einer Reihe von [Teams](/ethereum-roadmap/ethereum-2.0/eth2.0-teams/teams-building-eth2.0/) entwickelt. Die meisten Eth2.0-Teams veröffentlichen regelmäßige Updates über ihren Entwicklungsfortschritt der Clients. Einige Teams bieten Beitragenden Belohnungen an, um mehr und mehr Entwickler in den Aufbau der Eth2.0-Architektur einzubinden. Du kannst für Beiträge [hier](https://gitcoin.co/grants/) Gitcoin-Prämien bekommen.

Isoliert ist die Beacon-Chain nicht besonders nützlich. Aber als erste zu realisierende Komponente von Ethereum 2.0 ist es das Fundament des gesamten zukünftigen Systems.

**Wichtige Überlegungen**

* ETH2 ist nach Abschluss der Phase 2 zu und von Shards frei übertragbar (jedoch kann sich dies noch in Zukunft ändern).
* Es wird eine Mindestmenge an ETH-Stakes notwendig sein, um die Beacon-Chain zu Beginn zu starten. Dies ist definiert als `CHAIN_START_FULL_DEPOSIT_THRESHOLD` im [Einlagen-Vertrag, der auf der Eth1.0-Blockchain eingerichtet wird](https://github.com/ethereum/deposit_contract/blob/master/deposit_contract/contracts/validator_registration.v.py#L3).
* Um ein Validator zu werden, musst du 32 ETH2 staken.
* Während der Phase 0 werden alle Transaktionen und Smart-Contract-Berechnungen weiterhin auf der Eth1-Chain laufen.

## Phase 1 - Shard-Chains

### Was beinhalten sie?

Shard-Chains sind der Schlüssel zu zukünftiger Skalierbarkeit, da sie einen parallelen Transaktionsdurchsatz ermöglichen. In Phase 1 werden 64 davon eingesetzt (mit der Option, im Laufe der Zeit mehr hinzuzufügen).

Phase 1 befasst sich in erster Linie mit der Konstruktion, Gültigkeit und dem Konsens der Daten dieser Shard-Chains. Phase 1 gibt weder die Ausführung des Shard-Chain-Zustands noch die Kontostände an. Es erscheint eher wie ein Testlauf für die Sharding-Struktur als ein Versuch, Shards zu skalieren. Die Beacon-Chain behandelt Shard-Chain-Blöcke als einfache Ansammlung von Bits ohne Struktur oder Bedeutung.

**Crosslinks** <br/> Periodisch wird der aktuelle Zustand (die „kombinierte Datenwurzel“) jedes Shards in einem Beacon-Chain-Block als Querverbindung aufgezeichnet. Wenn der Beacon-Chain Block finalisiert wurde, wird auch der entsprechende Shard Block als finalisiert angesehen, und andere Shards wissen, dass sie sich bei Cross-Shard-Transaktionen auf diesen verlassen können. <br/>

Crosslinks sind eine Reihe von Signaturen eines Ausschusses, die für einen Block in einer Shard-Chain bestätigt werden und in die Beacon-Chain aufgenommen werden können. Crosslinks sind die wichtigsten Verbindungen, mit denen die Beacon-Chain den aktualisierten Zustand der Shard-Chains "erlernt". Crosslinks dienen auch als Infrastruktur für asynchrone Cross-Shard Kommunikation.

Shard-Validatoren, die von der Beacon-Chain für jeden Shard an jedem Slot zufällig ausgewählt werden, kommen lediglich zu einer Einigung über den Inhalt jedes Blocks. Sie bestätigen den Inhalt und Status des Shards durch das Erstellen von Crosslinks. Es spielt keine Rolle, welche Informationen in Shard-Blöcken erscheinen, solange alle Ausschüsse einen Konsens erzielen und die Beacon-Chain regelmäßig aktualisieren.

### Wie sieht das Netzwerk aus?

Die Eth1- und Eth2-Chains werden nach Phase 1 weiterhin parallel laufen.

### Wichtige Überlegungen

* In Phase 0, 1 und 2 bleibt die Main PoW-Chain (Eth1) live, während Tests und Übergänge auf der Eth2-Chain stattfinden. Dies bedeutet, dass Belohnungen sowohl an Ethereum 2.0-Validatoren als auch an die normalen PoW-Miner ausgezahlt werden. Daher kann die kombinierte Inflation der beiden Blockchains zunächst steigen, jedoch wird sie danach beginnen, sich in Richtung 0-1% zu bewegen, da auf die alte PoW-Blockchain allmählich weniger Wert gelegt wird.

## Phase 2 - State Execution

### Was beinhaltet sie?

Phase 2 ist der Zeitpunkt, an dem sich die Funktionalität des gesamten Systems vereint. Shard-Chains werden von einfachen Datencontainern in einen strukturierten Kettenzustand überführt und Smart-Contracts werden wieder eingeführt. Jeder Shard verwaltet eine virtuelle Maschine basierend auf [eWASM](https://github.com/ewasm/design) . Phase 2 unterstützt Konten, Verträge, Zustände und andere Abstraktionen, die wir aus Solidity kennen. Wir können erwarten, dass bekannte Werkzeuge wie Truffle, Solc oder Ganache portiert werden, um eWASM vor oder während Phase 2 zu unterstützen.

Phase 2 führt auch das Konzept der Ausführungsumgebungen (Execution Environments, EEs) ein. EEs in einem Shard können auf jede Weise konstruiert werden, die ein Entwickler für passend hält. Es könnte eine EE für eine UTXO-Chain geben, ein System im Libra-Stil, eine EE für einen Gebühren-Markt-Verteiler oder andere. Jeder Shard hat Zugriff auf alle Ausführungsumgebungen und besitzt die Möglichkeit, Transaktionen in diesen zu tätigen sowie Smart-Contracts auszuführen und mit ihnen zu interagieren. Beachte, dass sich das Konzept von Ausführungsumgebungen noch immer in intensiver Forschungs- und Entwicklungsarbeit befindet.

### Wichtige Überlegungen
* Eine dApp muss auswählen, auf welchem Shard sie sich befinden will. Diese Entscheidung ist wichtig, weil die Cross-Shard Kommunikation in Eth2 unterschiedlich ist, da sie nicht synchron ist, was wiederum bedeutet, dass zwischen den Shards eine gewisse Flexibilität verloren geht<br/>
* Eine dApp müsste ziemlich große Datenmengen beinhalten, um alle Ressourcen in einem gegebenen Shard zu verbrauchen und damit das Ausbreiten auf mehrere Shards zu rechtfertigen.<br/>
* Diese Phase stattet Shards mit eWASM als EVM 2.0 aus.
* Es bleibt offen, wann und wie Ethereum 1.0-Konten und -Verträge auf Ethereum 2.0 migriert werden. Es gibt einige [Upgrade-Pläne](https://ethresear.ch/t/the-eth1-eth2-transition/6265)

## Wie geht es weiter?
Die Sharding-Roadmap schlägt nach dem offiziellen Wiki 6 Phasen vor. Ethereum-Forscher Justin Drake ist der festen Überzeugung, dass die Sharding Phase 1 und 2 in den Jahren 2020 und 2021 erfolgen wird \(vorausgesetzt, dass die Beacon-Chain Anfang 2020 startet\). <br/>

Ab Phase 3 ist jede Art der Vorhersage Spekulation, da sich voraussichtlich viel verändern wird. Du kannst dir das [wiki](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#phase-3-light-client-state-protocol) ansehen, um weitere Informationen zu erhalten.

## Ressourcen

* [Ethereum 2.0 Info](https://hackmd.io/e4cNiocFTiS67j6yJ_XHPw?view)
* [Eth 2.0 Specs](https://github.com/ethereum/eth2.0-specs)
* [Phase 0 for Humans](https://notes.ethereum.org/jDcuUp3-T8CeFTv0YpAsHw?view)
* [Sharding Roadmap](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#strongphase-3strong-light-client-state-protocol)
* [State of Ethereum Protocol](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129)
* [Ethereum 2.0 Design Goals](https://media.consensys.net/exploring-the-ethereum-2-0-design-goals-fd2d901b4c01)
* [Q&A Session ETHMagicians](https://medium.com/ethereum-magicians/demystifying-the-road-to-ethereum-2-0-8130ade8d00f)
* [eWASM](https://www.coindesk.com/open-heart-surgery-inside-ethereums-crucial-replacement-of-the-evm)
