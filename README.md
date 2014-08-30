osm-downloader
==============

Narzędzie do pobierania mapek z openstreetmap.org

O programie
===========
Program napisany w pythonie wykorzystuje biblioteki PIL i tkinter.  Archiwum dist zawiera skompilowaną wersje dla systemu MS Windows.

Obsługa
===============
1.Główne okno programu
----------------------
![](https://raw.githubusercontent.com/other019/osm-downloader/master/README/mainwindow.jpg)
![](/README/mainwindow.jpg)

Okno uzupełniamy kolejno adresem lewego górnego kafelka, prawego dolnego kafelka oraz nazwą pliku wynikowego z mapą. Nazwa pliku nie może zawierać polskich znaków. Można podac rozszerzenie (.bmp, gif., .im, .jpeg, .msp, .pcx, .png, .ppm, .spi, .tiff, .xbm, .eps, .palm, .pdf ). Jeśli rozszerzenie nie zostanie podane wtedy zapisany plik bedzie miał format .png.
Program przewidziany tylko dla mapek podstawowych(być może zmienione w kolejnych wersjach). Adres kafelka uzyskujemy na mapce podstawowej klikajac prawym przyciskiem myszy i pokaż obrazek. Kopiujemy URL.

2. Program podczas pracy
----------------------------------
!(https://raw.githubusercontent.com/other019/osm-downloader/master/README/programpodczaspracy.jpg)

Postęp pokazuje pasek znajdujący się poniżej przycisku generuj.

3. Pobieranie zakończone
----------------------------------
!(https://raw.githubusercontent.com/other019/osm-downloader/master/README/sciagnietopomyslnie.jpg)

Program wyswietli okienko o tym, że mapkę pobrano pomyślnie. Można go zamknąć. Przykładowy program oprócz pliku poznan.jpg wygeneruje plik poznan.jpg.log zawierajacy dane o kafelku paczatkowym i koncowym, oraz komunikaty błędów.

Błędy
========================
1.Brak danych
-----------------------
!(https://raw.githubusercontent.com/other019/osm-downloader/master/README/brakdanych.jpg)

2. Złe przybliżenie
----------------------------
!(https://raw.githubusercontent.com/other019/osm-downloader/master/README/brakdanych.jpg)

```
http://b.tile.openstreetmap.org/16/35827/21504.png
                                --
http://a.tile.openstreetmap.org/17/35869/21548.png
                                --
```
Złe przybliżenie może wynikać z tego, że pobraliśmy adres kafelka zanim załadował sie kafelek o poprawnym przybliżeniu.


