# Sprawozdanie: Architektura Aplikacji w Pythonie — Zestaw Zaliczeniowy

**Jakub Smyrak -  semestr letni 2026**


---

### Lab 1: Dekoratory i obsługa błędów
Pojedyncze wywołanie niestabilnego API ma szansę na sukces wynoszącą 50% (0.5). Zastosowanie dekoratora `@retry` z 5 próbami sprawia, że szansa na to, że **wszystkie próby zawiodą**, spada do zaledwie 3.125% (0.5^5). Oznacza to, że teoretyczne prawdopodobieństwo przynajmniej jednego sukcesu wzrasta do **96.87%**. Eksperyment empiryczny na 100 wywołaniach potwierdza tę skuteczność, niemal całkowicie eliminując niestabilność zewnętrznego interfejsu.

### Lab 2: Współbieżność
Zadanie obliczania sentymentu jest silnie obciążające dla procesora. 
Wyniki eksperymentu jasno pokazują wpływ **GIL** w Pythonie. Użycie (`ThreadPoolExecutor`) nie przyniosło przyspieszenia względem wykonania sekwencyjnego, ponieważ GIL pozwala na wykonanie instrukcji tylko jednemu wątkowi naraz. Prawdziwe przyspieszenie (kilkukrotne) osiągnięto dopiero przy użyciu `multiprocessing.Pool`, który tworzy osobne procesy, z których każdy posiada własny interpreter i własną pamięć, całkowicie omijając blokadę GIL.

### Lab 3: Testowanie i Tokenizacja
Analiza rozmiaru słownika na próbkach testowych ujawnia działanie **Prawa Heapsa** w przetwarzaniu języka naturalnego. 
Na próbce 20 recenzji słownik osiąga około 800–1100 unikalnych tokenów. Przy 100 recenzjach liczba ta rośnie do 2800–3500 tokenów. Słownik rośnie logarytmicznie, a nie liniowo – pierwsze teksty budują bazę o najpopularniejsze słowa (spójniki, popularne przymiotniki), a każda kolejna recenzja wnosi coraz mniej nowych pojęć (głównie rzadsze nazwy własne czy literówki).

### Lab 4: Bazy Danych (SQL vs NoSQL w SQLite)
Zastosowanie struktury JSON w relacyjnej bazie ma swoje koszty. Baza oparta na dokumentach JSON zajmuje zauważalnie więcej miejsca na dysku niż klasyczna tabela, ponieważ w każdym wierszu powiela klucze tekstowe (np. `"stats"`, `"word_count"`). Operacje takie jak filtrowanie są też nieco wolniejsze przez (`json_extract`).
**Wniosek:** Dla tego konkretnego problemu klasyczny schemat SQL (*schema-on-write*) jest lepszy – struktura recenzji jest stała, analizujemy zawsze te same atrybuty, co czyni SQL bardziej efektywnym pamięciowo i wydajnościowo.

### Lab 5: PySpark i przetwarzanie rozproszone
Funkcje okna (`Window`) pozwalają na zaawansowaną analitykę bez utraty szczegółowości danych, w przeciwieństwie do zwykłego `groupBy`. Dzięki nim mogliśmy obliczyć np. różnicę długości konkretnej recenzji względem średniej w jej klasie, bez spłaszczania struktury tabeli. 
Dodatkowo zaobserwowano mechanizm **Lazy Evaluation** – transformacje na Sparku wywoływały się natychmiastowo budując jedynie graf wywołań (DAG). Czasochłonne obliczenia na klastrze uruchomiły się dopiero przy wywołaniu akcji `.toPandas()`.

### Lab 6: Data Quality (Kontrakt Danych)
Oparto mechanizm na twardych i miękkich regułach. Miękkie ostrzeżenia (`warning`) informują o anomaliach w danych (np. skrajne długości recenzji, pozostałości tagów HTML), ale pozwalają danym przejść dalej. Reguły krytyczne (`error`, np. brakujące etykiety) wykorzystują zasadę **Fail-Fast** – zatrzymują cały potok, rzucając wyjątek i chroniąc modele uczenia maszynowego przed wytrenowaniem się na złych danych.