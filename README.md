# WHO_Mortality_Database

## Projektübersicht
In unserem Projekt analysieren wir Daten aus der WHO Mortality Database, um Unterschiede in der Sterblichkeit zwischen Ländern zu untersuchen. Zunächst haben wir den Datensatz aufbereitet. Dies beinhaltete Zusammenführen mehrerer CSV-Dateien, Entfernen irrelevanter Zeilen, Ergänzen von Spaltennamen und Mapping von Länder-Codes zu Ländernamen und prüfen die Datenqualität (Missingness, Konsistenz/Merging, Outlier-Analyse).

In der Analyse liegt der Fokus auf vorzeitiger Mortalität (Anteil der Todesfälle unter 65 Jahren) sowie auf allgemeinen Sterberaten pro 100'000 Einwohner. Wir haben globale Muster in einer Weltkarte visualisiert. Dabei lag der Fokus stets auf dem Jahr 2017, da dieses über alle Länder hinweg am meisten Daten aufwies. Zudem führten wir eine Auswertung für Europa durch für das Jahr 2009. Daneben untersuchten wir auch Zusammenhänge mit Lebenserwartung und sozioökonomischen Faktoren wie dem BIP pro Kopf mit Hilfe der Korrelationen, Effektstärken und Regressionsmodellen. Ergänzend werden Häufigkeiten von Todesursachen pro Land ausgewertet.

## Projektstruktur

Die Analyse ist in mehrere Jupyter Notebooks unterteilt, die in logischer Reihenfolge aufgebaut sind:

- 01_Datenaufbereitung.ipynp:  Zusammenführung, Bereinigung und Aufbereitung der Rohdaten  
- 02_Datenexploration_und_Übersicht.ipynb: Erste statistische Auswertungen, Datenqualität und Verteilungen  
- 03_Vorzeitige_Mortalität_Weltweit.ipynb: Analyse der vorzeitigen Mortalität (< 65 Jahre) inklusive Weltkarte  
- 04_Sterberaten_Europa.ipynb: Regionale Analyse der Sterberaten in Europa  
- 05_Todesursachen_Analyse.ipynb: Auswertung und Vergleich von Todesursachen pro Land
- karte.ipynb: Hilfsnotebook zur Erstellung einer animierten Karte

## Datengrundlage

Unsere Analyse basiert auf mehreren CSV-Dateien aus der WHO Mortality Database, welche Sterbefälle nach Land, Alter und Todesursache enthalten. Wir haben die Daten aus mehreren Teildateien zusammengeführt und mithilfe von Lookup-Tabellen (Ländercodes, Todesursachen Codes) aufbereitet. Ergänzend brauchten wir auch externe Daten aus der World Bank Database (BIP, Lebenserwartung und Bevölkerungszahlen). Die Auswertung bezieht sich hauptsächlich auf das Jahr 2017. In einzelnen Analysen haben wir auch andere Jahre gebraucht wie 2009.

## Vorgehen und Methoden

Unsere Analyse begann mit der Aufbereitung der Rohdaten aus der WHO Mortality Database durch Zusammenführen mehrerer Teildateien und Vereinheitlichung von Länder- und Causes-Code. 

Anschliessend haben wir eine explorative Datenanalyse durchgeführt, bei der Datenabdeckung, Verteilungen und Ausreisser untersucht wurden. Bereits in diesem Schritt haben wir die Sterberaten pro Land berechnet, sowie Zusammenhangsanalysen mit Pearson und Spearman-Korrelationen durchgeführt.

Darauf aufbauen haben wir eine vertiefte Analyse zur vorzeitigen Mortalität durchgeführt. Darin bezogen wir uns auf den Anteil der Todesfälle unter 65 Jahren pro Land im Jahr 2017. Diese Ergebnisse haben wir sowohl statistisch ausgewertet als auch visuell (Weltkarte) dargestellt. Zur Untersuchung von Gruppenunterschieden und Zusammenhängen brauchten wir Cohen’s d, Kruskal-Wallis-Test sowie multiple lineare Regressionsmodelle zum Einsatz. 

In einem weiteren Schritt führten wir ein regionale Vertiefungen für Europa durch und betrachteten Sterberaten pro 100000 Einwohner in den verschiedenen Ländern.

Ergänzend haben wir auch die Todesursachen untersucht, um Unterschiede zwischen Ländern zu finden.

## Contributions

| Name     | Beitrag |
|----------|--------|
| Kristian | Analyse der Todesursachen sowie Erstellung der animierten Karte |
| Linus    | Explorative Datenanalyse, Korrelationsanalysen und untersuchen der Todesraten |
| Nevio    | Analyse der vorzeitigen Mortalität und die regionale Analyse für Europa |
| Alle     | Gemeinsame Datenaufbereitung und Zusammenführung der Rohdaten |

