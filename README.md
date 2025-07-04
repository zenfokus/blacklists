# IP Threat Intelligence Lists

Eine Sammlung frei verfügbarer, regelmäßig aktualisierter IP-Blacklists zur Verwendung in Firewalls, IDS/IPS, Netzwerksicherheitslösungen oder beim Threat Hunting.

## Übersicht der Quellen

| Datei                                  | Beschreibung                                        | Quelle |
|---------------------------------------|-----------------------------------------------------|--------|
| `firehol-level1.txt`                  | FireHOL Level 1 – Allgemeine Bedrohungen           | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/firehol_level1.netset) |
| `spamhaus_drop.txt`                   | Spamhaus DROP – Bösartige Netzwerke                | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/spamhaus_drop.netset) |
| `spamhaus_edrop.txt`                  | Spamhaus eDROP – Erweiterte DROP-IPs               | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/spamhaus_edrop.netset) |
| `cruzit_web_attacks.txt`              | CruZit – Web-Angriffe                              | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/cruzit_web_attacks.ipset) |
| `iblocklist_cruzit_web_attacks.txt`   | IBlockList – CruZit Web Attacks (Netset)           | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/iblocklist_cruzit_web_attacks.netset) |
| `iblocklist_ciarmy_malicious.txt`     | IBlockList – CIArmy Malicious (Netset)             | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/iblocklist_ciarmy_malicious.netset) |
| `cybercrime.txt`                      | CyberCrime – IPv4 Blacklist                        | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/cybercrime.ipset) |
| `dm_tor.txt`                          | Tor – Exit Nodes                                   | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/dm_tor.ipset) |
| `et_block.txt`                        | Emerging Threats – Block List                      | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/et_block.netset) |
| `darklist_de.txt`                     | Darklist.de – IP Blacklist                         | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/darklist_de.netset) |
| `ipsum-level-2.txt`                   | Ipsum Level 2 – Aggressives IP-Blocking            | [Link](https://raw.githubusercontent.com/stamparm/ipsum/refs/heads/master/levels/2.txt) |
| `greensnow.txt`                       | GreenSnow – Angreifer-IPs                          | [Link](https://raw.githubusercontent.com/borestad/firehol-mirror/refs/heads/main/greensnow.ipset) |

## All-in-One Liste (AIO)

Für eine einfache Integration in Firewalls oder Netzwerkanalysen steht eine konsolidierte Blacklist zur Verfügung, die alle oben genannten Quellen vereint:

**AIO-Blacklist:**  
[https://raw.githubusercontent.com/zenfokus/blacklists/refs/heads/main/aio/aio_blacklist.list](https://raw.githubusercontent.com/zenfokus/blacklists/refs/heads/main/aio/aio_blacklist.list)

Diese Liste wird regelmäßig aktualisiert und eignet sich ideal für den produktiven Einsatz, wenn nur eine zentrale Datei verwendet werden soll.

---

## Lizenz / Nutzung

Alle Listen stammen aus öffentlich zugänglichen Quellen. Bitte beachte die jeweiligen Nutzungsbedingungen der Originalquellen. Diese Sammlung dient ausschließlich der Forschungs- und Sicherheitsanalyse.
