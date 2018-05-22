# House Price Calculator

Pakiet umożliwiający wycenę domów/mieszkań w Polsce na podstawie wprowadzonych
parametrów, takich jak: metraż, rodzaj zabudowy, rynek, rok budowy, 
materiał budynku. Dodatkowo biblioteka uwzględnia lokalizację, tzn. położenie
względem największych miast w Polsce (geolokalizacja Google Maps Api) oraz
pozwala na zaprezentowanie położenia wycenianego mieszkania oraz miasta
odniesienia na mapie poprzez informacje dot. zgeokodowanych adresów (wsp. 
geograficzne).

Przydatnymi funkcjami są też m.in. typowanie dokładnych adresów na podstawie 
danych adresowych domu/mieszkania oraz możliwość uwzględnianie kosztów 
atrybutów dodatkowych przy wycenie, np. balkon, ogródek, winda, strzeżone 
osiedle itp.

### Autor:

- Kamil Cieślik <br />

### Hierarchia zawartości biblioteki:
```
house_price_calculator
|
|
|__ calculator
|     |
|     |__ exception
|     |     |
|     |     |__ __init__.py
|     |     |
|     |     |__ construction_year_violation_exception.py
|     |     |
|     |     |__ flat_parameter_mismatch_exception.py
|     |
|     |__ util
|     |     |
|     |     |__ __init__.py
|     |     |
|     |     |__ address.py
|     |     |
|     |     |__ calculator_result.py
|     |     |
|     |     |__ reference_city.py
|     |     
|     |__ __init__.py
|     |__ prices_calculator.py
|
|__ tests
|     |__ calculations_test.py
|
|__ LICENSE
|
|__ MANIFEST.in
|
|__ README.md
|
|__ setup.py
```

### Przykłady użycia:
```
TODO:
```

- Kamil Cieślik <br />

### Wykorzystane technologie i dodatkowe API:

- Python 3.6 <br /> 

- Google Maps API <br /> 

- Python Client for Google Maps Services <br /> 

### Wykorzystane narzędzia:

- PyCharm Professional IDEA 2018.1.1 <br />
