class Movie():

    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_director(self):
        return self._year

class StreamingService():

    def __init__(self, name, catalog):
        self._name = name
        self._catalog = catalog

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie

    def del_movie




class StreamingGuide():

    def __init__(self, add_streaming_service, delete_streaming_service, where_to_watch):
        self._add_steaming_service = add_streaming_service
        self._delete_streaming_service = delete_streaming_service
        self._where_to_watch = where_to_watch

    def get_add_streaming_service(self):
        return self._add_steaming_service

    def get_delete_streaming_service(self):
        return self._delete_streaming_service

    def get_where_to_watch(self):
        return self._where_to_watch






movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch('Little Women')
