# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 6/1/2022
# Description: Enter a movie on the list. Returns title, year, and streaming service.
#

class Movie:
    """class for defining a list of movies"""
    def __init__(self, title: str, genre: str, director: str, year: int):
        """assigns values for movie list's elements"""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

        """get methods for elements within movie list"""
    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year


class StreamingService:
    """class for creating streaming service list"""
    def __init__(self, name):
        """assigns values within the streaming service list"""
        self._name = name
        self._catalog = {}

        """get methods for elements in steaming service list"""
    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie):
        """adds a move to streaming service list"""
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, movie_title):
        """removes movie from streaming service list"""
        if movie_title in self._catalog:
            del self._catalog[movie_title]


class StreamingGuide:
    """Class for creating a streaming guide"""
    def __init__(self):
        """assigns values of a list called streaming service"""
        self._streaming_services = []

    def add_streaming_service(self, streaming_service):
        """adds streaming service to streaming guide"""
        self._streaming_services.append(streaming_service)

    def delete_streaming_service(self, streaming_service_name):
        """removes streaming service from streaming guide"""
        streaming_service_names = [service.get_name() for service in self._streaming_services]

        if streaming_service_name in streaming_service_names:
            service_index = streaming_service_names.index(streaming_service_name)
            self._streaming_services.pop(service_index)

    def where_to_watch(self, movie_title):
        """final function gathers title and year of requested movie and returns the with streaming service"""
        output = []

        for service in self._streaming_services:
            catalog = service.get_catalog()

            if movie_title in catalog:
                movie_title_year = f"{movie_title} ({catalog.get(movie_title).get_year()})"

                if movie_title_year not in output:
                    output.append(movie_title_year)

                output.append(service.get_name())

        if len(output) > 0:
            return output

        return None


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

print(search_results)
