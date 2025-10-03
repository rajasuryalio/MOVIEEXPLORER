from typing import TypedDict

class ActorsResponse(TypedDict):
    id : int
    name : str
    birth_year : int

class MoviesResponse(TypedDict):
    id : int
    title : str
    release_year : int

class GenresResponse(TypedDict):
    id : int
    name : str

class DirectorsResponse(TypedDict):
    id : int
    name : str
    birth_year : int
    