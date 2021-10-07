# Kulki

Projekt badawczy mający na celu sprawdzenie wpływu różnego rodzaju kar i nagród na zachowanie użytkownika

## Spis treści

- [Zasady gry](#zasady)
- [Zasady commitowania](#commits)
- [Technologie](#technologie)

## Zasady gry

- Gra polegać będzie na ustawianiu kulek w zadanym obszarze poprzez wybór kolumny przy pomocy wpisywania numeru kolumny
- Za ułożenie kulek o jednakowym kolorze w sąsiadujących polach użytkownik dostawać będzie nagrodę
- Za ułożenie kulek o niejednakowym kolorze w sąsiadujących polach użytkownik dostawać będzie karę
- W grze obowiązują dwa warianty kar i nagród, a celem badania jest sprawdzenie jak użyta opcja wpływa na wyniki uzyskiwane przez użytkownika
- Użytkownik na starcie nie zna obowiązujących zasad

## Zasady commitowania

### Poniższe polecenia przeznaczone są do wykorzystania w aplikacji konsolowej (np. GIT CMD)

- Do sklonowania repozytorium do wybranego folderu

```
git clone https://github.com/jwieckowski/kulki.git
```

- Do pobrania zmian ze zdalnego repozytorium - wykonywać kiedy lokalnie nie mamy zmian i chcemy uaktualnić stan repozytorium ze stanem panującym globalnie

```
git pull
```

- Po napisaniu kodu o danej funkcjonalności i sprawdzeniu jego poprawności (w zalezności czy dodajemy wszystkie pliki, w których są zmiany czy tylko konkretny plik)

```
git add . / konkretny_plik.py
```

- Następnie commitujemy zmiany

```
git commit -m "treść commita, czyli co on wprowadza, jakie nowe funkcjonalności, co zmieniono"
```

- Kolejny krok to umieszczenie lokalnego commita na zdalnym repozytorium

```
git push -u origin
```

- W celu sprawdzenia statusu commitów

```
git status
```

- Natomiast w celu wyświetlenia historii commitów

```
git log
```

## Technologie

- Python - jako środowisko uruchomieniowe i język programowania
- PyGame - framework do stworzenia aplikacji okienkowej
- GazeRecorder - aplikacja do badania obszarów skupienia wzroku przez użytkownika w trakcie gry
