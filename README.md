# IP Threat Intelligence Lists

Eine Sammlung frei verfügbarer, regelmäßig aktualisierter IP-Blacklists zur Verwendung in Firewalls, IDS/IPS, Netzwerksicherheitslösungen oder beim Threat Hunting.

## Übersicht der Quellen

| Datei                                  | Beschreibung                                        | Quelle |
|---------------------------------------|-----------------------------------------------------|--------|
| `blocklist_net_ua.list`               | Bösartige IPs laut blocklist.net.ua              | [Link](https://iplists.firehol.org/?ipset=blocklist_net_ua) |
| `dm_tor.list`                         | Aktive TOR-Exit- und -Relay-Nodes                | [Link](https://iplists.firehol.org/?ipset=dm_tor) |
| `et_block.list`                       | Bekannte bösartige IPs von Emerging Threats      | [Link](https://iplists.firehol.org/?ipset=et_block) |
| `firehol-level1.list`                 | Allgemeine bösartige IPs – niedriges Risiko      | [Link](https://iplists.firehol.org/?ipset=firehol-level1) |
| `firehol_proxies.list`                | Offene Proxy-Server                              | [Link](https://iplists.firehol.org/?ipset=firehol_proxies) |
| `firehol_webserver.list`              | Kompromittierte oder gefährliche Webserver       | [Link](https://iplists.firehol.org/?ipset=firehol_webserver) |
| `greensnow.list`                      | Angreifer mit verdächtigem Verhalten             | [Link](https://iplists.firehol.org/?ipset=greensnow) |
| `iblocklist_ciarmy_malicious.list`    | IPs mit bestätigtem bösartigem Verhalten         | [Link](https://iplists.firehol.org/?ipset=iblocklist_ciarmy_malicious) |
| `spamhaus_drop.list`                  | Spamhaus DROP – bekannte Cybercrime-Netze        | [Link](https://iplists.firehol.org/?ipset=spamhaus_drop) |
| `spamhaus_edrop.list`                 | Spamhaus eDROP – erweiterte Cybercrime-IP-Liste  | [Link](https://iplists.firehol.org/?ipset=spamhaus_edrop) |
| `stopforumspam.list`                  | IPs, die bei Forenspam aufgefallen sind          | [Link](https://iplists.firehol.org/?ipset=stopforumspam) |

## All-in-One Liste (AIO)

Für eine einfache Integration in Firewalls oder Netzwerkanalysen steht eine konsolidierte Blacklist zur Verfügung, die alle oben genannten Quellen vereint:

**AIO-Blacklist:**  
[https://raw.githubusercontent.com/zenfokus/blacklists/refs/heads/main/aio/aio_blacklist.list](https://raw.githubusercontent.com/zenfokus/blacklists/refs/heads/main/aio/aio_blacklist.list)

Diese Liste wird regelmäßig aktualisiert und eignet sich ideal für den produktiven Einsatz, wenn nur eine zentrale Datei verwendet werden soll.

---

## Lizenz / Nutzung

Alle Listen stammen aus öffentlich zugänglichen Quellen. Bitte beachte die jeweiligen Nutzungsbedingungen der Originalquellen. Diese Sammlung dient ausschließlich der Forschungs- und Sicherheitsanalyse.
