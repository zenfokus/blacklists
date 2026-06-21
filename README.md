# IP Threat Intelligence Lists

> [!WARNING]
> **IMPORTANT: BRANCH CHANGE**
> To prevent massive repository bloat, all generated blocklists are now published to the `release` branch instead of `main`. 
> If you are using raw GitHub URLs in your firewalls or scripts, **you must update your URLs** to point to the `release` branch.

A collection of freely available, regularly updated IP blacklists for use in firewalls, bunkerweb, apache waf, fail2ban, IDS/IPS, network security solutions, or threat hunting.

## Overview of sources

| File                                  | Description                                         | Source |
|---------------------------------------|-----------------------------------------------------|--------|
| `blocklist_net_ua.list`               | Malicious IPs according to blocklist.net.ua         | [Link](https://iplists.firehol.org/?ipset=blocklist_net_ua) |
| `dm_tor.list`                         | Active TOR exit and relay nodes                     | [Link](https://iplists.firehol.org/?ipset=dm_tor) |
| `et_block.list`                       | Known malicious IPs from Emerging Threats           | [Link](https://iplists.firehol.org/?ipset=et_block) |
| `firehol-level4.list`                 | General malicious IPs – low risk                    | [Link](http://iplists.firehol.org/?ipset=firehol_level4) |
| `firehol_webserver.list`              | Compromised or dangerous web servers                | [Link](https://iplists.firehol.org/?ipset=firehol_webserver) |
| `greensnow.list`                      | Attackers with suspicious behavior                  | [Link](https://iplists.firehol.org/?ipset=greensnow) |
| `iblocklist_ciarmy_malicious.list`    | IPs with confirmed malicious behavior               | [Link](https://iplists.firehol.org/?ipset=iblocklist_ciarmy_malicious) |
| `spamhaus_drop.list`                  | Spamhaus DROP – known cybercrime networks           | [Link](https://iplists.firehol.org/?ipset=spamhaus_drop) |
| `spamhaus_edrop.list`                 | Spamhaus eDROP – extended cybercrime IP list        | [Link](https://iplists.firehol.org/?ipset=spamhaus_edrop) |
| `stopforumspam.list`                  | IPs that have been flagged for forum spam           | [Link](https://iplists.firehol.org/?ipset=stopforumspam) |

## All-in-One List (AIO)

For easy integration into firewalls or network analyses, a consolidated blacklist is available that combines all of the above sources:

**AIO blacklist:**  
[https://raw.githubusercontent.com/zenfokus/blacklists/refs/heads/release/aio/aio_blacklist.list](https://raw.githubusercontent.com/zenfokus/blacklists/refs/heads/release/aio/aio_blacklist.list)

This list is updated regularly and is ideal for productive use if only one central file is to be used.

---

## License / Use

All lists come from publicly available sources. Please note the respective terms of use of the original sources. This collection is intended solely for research and security analysis.
