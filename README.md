# heilbrigðiseftirlitið, crawler
Í spjalli yfir kaffibolla sagðist einhver vilja getað skoðað gögnin um niðurstöður heilbrigðiseftirlitsins  
reykjavík er með síðu fyrir sín gögn, þar sem er bara hægt að leita eftir stöðum, ekki skoða gögnin sjálf  
Mig langaði að skoða gögnin, þannig ég scrape-aði þau  


### Gögn í repo-inu
- Actual skrifturnar 
- tmp gögnin sem voru scraped 2024.03.13, ef einhver vill prófa parserinn án þess að bomba næstum 3000 requests á reykjavik.is
- data/results.json - Parsed gögnin

### Smáa letrið
- Þessi scraper er eeeeeeeeeekki fallegur, þetta eru 4 aðskildar skriftur  
- Þessi scraper er ekki hraður, hann sækjir kennitölu lista yfir öll fyrirtæki með starfsleyfi hjá heilbrigiseftirlitinu og leitar eftir hverri einustu  
- Ég er ekki viss um áreiðanleika output gagnanna, ég gerði stikk prufur og þær stemmdu en ég lofa engu um að gögnin séu alveg rétt hjá mér   
- Ef þú ákveður að scrape-a þetta, ekki fjarlægja time.sleep(1), við skulum ekkert reyna að drekkja þessum servers þeirra.
