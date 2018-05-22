# House Price Calculator Library

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
house_price_calculator_library
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
|__ .gitignore
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

#### 1. Moduł prices_calculator.py
Biblioteka spełnia podstawowe funkcjonalności poprzez uruchomienie głównego
modułu poprzez przekazanie argumentów. </b>
Argumenty modułu:
- tryb działania (typowanie adresów, szacowanie wartości mieszkania),
- Google Api Key,
- (1) adres,
- (2) latitude,
- (2) longitude,
- (2) rodzaj zabudowy (blok, kamienica, dom wolnostojący, apartamentowiec),
- (2) rodzaj rynku (wtórny, pierwotny),
- (2) materiał budynku (wielka płyta, pustak, cegła, drewno, żelbeton),
- (2) rok budowy,
- (2) ilość mkw,
- (2) oraz kolejno - atrybuty atrybuty dodatkowe (balkon, piwnica, ogródek,
taras, winda, oddzielna kuchnia, strzeżone osiedle).

##### 1.1. Typowanie i geokodowanie adresów
```
$ python3 -m calculator.prices_calculator y GOOGLE_API_KEY "Zielona 1"
Wynik typowania adresów Google Maps:
Zielona 1, Jastrzębie-Zdrój, Polska, lat: 49.95153, lng: 18.609122
Zielona 1, Gdynia, Polska, lat: 54.549537, lng: 18.530066
Zielona 1, Łódź, Polska, lat: 51.7706658, lng: 19.4555191
Zielona 1, 57-340 Duszniki-Zdrój, Polska, lat: 50.3948124, lng: 16.384597
Zielona 1, 02-913 Warszawa, Polska, lat: 52.1856109, lng: 21.0691659
Zielona 1, Piaseczno, Polska, lat: 52.077273, lng: 21.048627
Zielona 1, 11-015 Olsztynek, Polska, lat: 53.5810419, lng: 20.296602
Zielona 1, 20-082 Lublin, Polska, lat: 51.24814259999999, lng: 22.5642616
Zielona 1, Słupsk, Polska, lat: 54.455675, lng: 17.023571
```

##### 1.2. Szacowanie wartości mieszkania
```
$ python3 -m calculator.prices_calculator no GOOGLE_API_KEY 49.95153 18.609122 
blok pierwotny pustak 2010 32 f f t f t f f
WYNIKI KALKULACJI:
	*miasto odniesiania*
		- nazwa: Katowice,
		- cena za mkw: 4664.0 zł,
		- odległość: 46.96 km.
	*cena mieszkania*
		- podstawowa cena za mkw: 4336.8 zł,
		- ostateczna cena za mkw: 7114.36 zł,
		- cena: 227659.37 zł.
```

### Wykorzystane technologie i dodatkowe API:

- Python 3.6 <br /> 

- Google Maps API <br /> 

- Python Client for Google Maps Services <br /> 

### Wykorzystane narzędzia:

- PyCharm Professional IDEA 2018.1.3 <br />
