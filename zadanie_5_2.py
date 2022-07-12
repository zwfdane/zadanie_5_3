""" Wykorzystaj wiedzę na temat programowania obiektowego i napisz program, który spełnia następujące założenia:
    Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie. Każdy film powinien mieć następujące atrybuty:
        Tytuł
        Rok wydania
        Gatunek
        Liczba odtworzeń
    Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:
        Tytuł
        Rok wydania
        Gatunek
        Numer odcinka
        Numer sezonu
        Liczba odtworzeń
    Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
    Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” 
    (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
    Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
    Przechowuje filmy i seriale w jednej liście.

Dodatkowo:
    Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale. 
    Posortuj listę wynikową alfabetycznie.
    Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
    Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
    Napisz funkcję, która uruchomi generate_views 10 razy.
    Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. 
    Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
"""

from webbrowser import get


class Film:
   def __init__(self, title, year, genre, number_plays):
       self.title = title
       self.year = year
       self.genre = genre 
       self.number_plays = number_plays

       # Variables
       self.current_play_number = 0

            
   def __str__(self): 
       return f'{self.title} {self.year} {self.genre} {self.number_plays}' 

   def play(self, play_number=1):
       self.number_plays += play_number
   
   def display(self):
       print(f"{self.title} ({self.year})")


class Series(Film):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode
    
    def __str__(self): 
       super().__init__(*args, **kwargs)
       return f'{self.season} {self.episode}' 

    def display(self):
       print(f"{self.title} S{self.season:02d}E{self.episode:02d}")



def get_movies(m_and_s_list):
        # Czy to jest dobre miejsce na import?
        import operator
        movies_list = []
        for m_and_s in m_and_s_list:
            if isinstance(m_and_s, Series) == False:
                movies_list.append(m_and_s)
        sorted_movies_list = sorted(movies_list, key=operator.attrgetter('title'))
        return sorted_movies_list
def get_series(m_and_s_list):
        import operator
        series_list = []
        for m_and_s in m_and_s_list:
            if isinstance(m_and_s, Series) == True:
                series_list.append(m_and_s)
        sorted_series_list = sorted(series_list, key=operator.attrgetter('title'))
        return sorted_series_list


if __name__ == "__main__":
    # Wyświetlanie instancji klasy Film bez metody display()
    f1 = Film( title="ABC", year=2010, genre="comedy", number_plays=100)
    f1.display()
    # Wyświetlanie instancji klasy Film za pomocą metody display()
    s2 = Series( title="ABC", year=2010, genre="comedy", number_plays=100, season = 4, episode = 11)
    Series.display(s2)
    # Tworzenie wspólnej listy filmów i seriali
    movies_and_series_list =  [Film( title="ABC", year=2010, genre="comedy", number_plays=10)]
    movies_and_series_list.append(Series( title="ABC", year=2019, genre="action", number_plays=100, season = 3, episode = 10))
    movies_and_series_list.append(Film( title="Ucieczka przed słoniem", year=2018, genre="adventure", number_plays=10))
    movies_and_series_list.append(Series( title="Kolorowe bałwanki", year=2021, genre="animated", number_plays=1200, season = 4, episode = 11))
    movies_and_series_list.append(Film( title="Jak przetrwać w dzisiejszych czasach", year=2001, genre="drama", number_plays=150))
    movies_and_series_list.append(Series( title="O podbojach Napoleona", year=2012, genre="historical", number_plays=120, season = 1, episode = 11))
    movies_and_series_list.append(Film( title="Spokój i porządek w Polsce", year=2012, genre="fantasy", number_plays=110))
    movies_and_series_list.append(Film( title="Facet gotuje jajka na miękko", year=2011, genre="horror", number_plays=110))
    movies_and_series_list.append(Series( title="W pogoni za lisem", year=2012, genre="thiller", number_plays=10, season = 4, episode = 12))
    movies_and_series_list.append(Film( title="Stare dobre czasy Dzikiego Zachodu", year=2011, genre="western", number_plays=20))
    movies_and_series_list.append(Series( title="Jak pokonałem MacGeiwera", year=2010, genre="action", number_plays=103, season = 5, episode = 111))
    movies_and_series_list.append(Film( title="W poszukiwaniu Yeti", year=2011, genre="adventure", number_plays=120))
    movies_and_series_list.append(Series( title="Koci patrol", year=2011, genre="animated", number_plays=120, season = 7, episode = 34))
    movies_and_series_list.append(Film( title="Przyjazd teściowej", year=2010, genre="drama", number_plays=34))
    movies_and_series_list.append(Series( title="Cesarz Franciszek i jego podboje", year=2021, genre="historical", number_plays=103, season = 3, episode = 31))
    movies_and_series_list.append(Film( title="Grzeczne dziecko", year=2020, genre="fantasy", number_plays=66))
    movies_and_series_list.append(Film( title="Ojciec sam w domu", year=2010, genre="horror", number_plays=78))
    movies_and_series_list.append(Series( title="ABC kałasznikowa", year=2010, genre="thiller", number_plays=21, season = 4, episode = 24))
    movies_and_series_list.append(Film( title="W sercu dzikiego zachodu", year=2012, genre="western", number_plays=14))


    our_movies = get_movies(movies_and_series_list) 
   
    print("Wyświetlam tylko filmy:")
    for movie in our_movies:
        movie.display()
    
    our_series = get_series(movies_and_series_list) 
   
    print("Wyświetlam tylko seriale:")
    for serie in our_series:
        serie.display()

# Na razie przesyłam część. Bardzo proszę o feedback dotyczący tej części
        

  


    




       