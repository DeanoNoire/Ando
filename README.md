# Ando
Raspberry based Flask local website receiving data from Resthooks from Home Assistant, Android App and 433MHz RF receiver


Pinout:
GPIO 27 - Relay In1 (Garage Switch)
GPIO 14 - D0 (433)
GPIO 15 - D1 (433)
GPIO 18 - D2 (433)
GPIO 23 - D4 (433)
GPIO 20 - Display DIO
GPIO 21 - Display CLK

States:
0 - closed
1 - open
50 - garageChanging - open
100 gateChanging - open
500 garageChanging - close
1000 gateChanging - close

monžé stavy
0 0     = 0
0 1     = 1
1 0     = 1
1 1     = 2
50 0    = 50      Changing garage - opening
50 1    = 51      Changing garage - opening
0 100   = 100     Changing gate - opening
1 100   = 101     Changing gate - opening
50 100  = 150     Changing both - opening
500 0  = 500       Changing garage - close
500 1 = 501       Changing garage - close
0 1000 = 1000     Changing gate - close
1 1000 = 1001     Changing gate - close 
500 100 = 600     garage close / gate open
50 1000 = 1050    garage open / gate close
500 1000 = 1500   changing both - close

