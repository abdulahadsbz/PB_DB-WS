# PB_DB-WS
the name means <b>P</b>rize <b>B</b>ond <b>D</b>ata<b>B</b>ase/<b>W</b>eb<b>S</b>craper  

## How To Run  
### Disclaimer
for now the code is in a early version so i have not yet made a good way to do this  
but that will come with some time  
  
### Steps To Run  
1. download all the files in src to a folder  
2. run PBDB.py first then run PBWS.py  
3. Select which value bonds you want to add to the database  
for example  
0=100rs, 1=200rs, 2=750rs, 3=1500rs, 4=7500rs, 5=15000rs, 6=25000rs, 7=40000rs  
4. wait for all the draws to be added to the database
5. it should be done now, open the database to check or simply check its filesize 

## Why Does The Code Look So Messey
### Why  
the code is in a very early stage i will improve it after im done with my other project

### What You Can Do  
feel free to make a pull request to improve the code or add a feature

## What Does It Do And How  
it scrapes prize bond pages on https://hamariweb.com using the requests library after  
scraping it parses it using bs4 and then it gets all the bond info like PrizeBondNumber,
PrizeBondRank, PrizeBondValue, DrawNumber, DrawDate, DrawLocation to it and then adds all of these to a sqlite3
database
