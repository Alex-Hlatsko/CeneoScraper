# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|str|
|autor opinii|span.user-post__author-name|author_opinion|str|
|rekomendacja|span.user-post__author-recomendation > em|recomendation|str|
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div[class$="positives"] ~ div.review-feature__item|pros||
|lista wad|div[class$="negatives"] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|span[id^="votes-yes"]|useful||
|dla ilu osób nieprzydatna|span[id^="votes-no"]|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1) ["datetime"]|publish_date||
|data zakupu|span.user-post__published > time:nth-child(2) ["datetime"]|purchase_date||

## Etapy pracy nad projectem
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojedynczej opinii do słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku .json
5. Pobranie wszystkich opinii o pridukcie i zapisanie ich na liście w postaci słowników
6. Dodanie możliwości podanie kodu produktu przez użytkownika 
7. Optymalizacja kodu 
    a. utworzenie funkcji do ekstrakcji elementów 
    b. utworzenie słownika selektorów
    c. użycie dictionary comprehension do pobrania składowych pojedynczycej opinii na podstawie słownika selektorów
8. Analiza pobranych opinii dla konkretnego produktu
    a. wyliczenie podstawowych statystyk:
        - liczba wszystkich opinii
        - liczba opinii dla których podano zalety
        - liczba opinii dla których podano wady
        - średnia opcena produktu 
    b. przygotowanie wykresów:
        - udział poszczególnych rekomendacji w ogólnej liczbie opinii
        - histogram występowania poszczególnych ocen