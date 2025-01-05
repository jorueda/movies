from unittest import TestCase
from utils import clean_no_release_date, get_director, clean_related_movies_data


class FormatResults(TestCase):
    def test_clean_no_release_date(self):
        data = {
            "page": 1,
            "results": [
                {
                    "adult": False,
                    "backdrop_path": "/oIwfoUFfWfESn0Y8u8jv9lc8li1.jpg",
                    "genre_ids": [
                        28,
                        53
                    ],
                    "id": 562,
                    "original_language": "en",
                    "original_title": "Die Hard",
                    "overview": "En lo alto de la ciudad de Los Ángeles, un grupo terrorista se ha apoderado de un edificio, tomando a un grupo de personas como rehenes. Sólo un hombre, el policía de Nueva York John McClane, ha conseguido escapar del acoso terrorista. Aunque está solo y fuera de servicio, McClane se enfrentará a los secuestradores. Él es la única esperanza para los rehenes",
                    "popularity": 60.104,
                    "poster_path": "/m54tK4wKjc1w2dp7QInG0munGao.jpg",
                    "release_date": "1988-07-15",
                    "title": "Duro de matar",
                    "video": False,
                    "vote_average": 7.795,
                    "vote_count": 11233
                },
                {
                    "adult": False,
                    "backdrop_path": "/5ftRls3IbR1kXnasqJEJL63LVsc.jpg",
                    "genre_ids": [
                        80,
                        28,
                        35,
                        53
                    ],
                    "id": 33542,
                    "original_language": "cn",
                    "original_title": "紅番區",
                    "overview": "Keong, un policía de Hong Kong, viaja a Nueva York para asistir a la boda de su tío Bill. Bill tiene un supermercado en el Bronx y Keong se ofrece a ayudarle durante su luna de miel, pero de pronto se verá envuelto en una lucha de bandas callejeras cuando una organización criminal hará todo cuanto sea posible por recuperar unos diamantes de gran valor.",
                    "popularity": 24.739,
                    "poster_path": "/zWHpCti0TWpU9g3HkmIShIjnYhW.jpg",
                    "release_date": "",
                    "title": "Masacre en Nueva York",
                    "video": False,
                    "vote_average": 6.817,
                    "vote_count": 1033
                }
            ],
            "total_pages": 1,
            "total_results": 10
        }
        expected_result = {
            "page": 1,
            "results": [
                {
                    "adult": False,
                    "backdrop_path": "/oIwfoUFfWfESn0Y8u8jv9lc8li1.jpg",
                    "genre_ids": [
                        28,
                        53
                    ],
                    "id": 562,
                    "original_language": "en",
                    "original_title": "Die Hard",
                    "overview": "En lo alto de la ciudad de Los Ángeles, un grupo terrorista se ha apoderado de un edificio, tomando a un grupo de personas como rehenes. Sólo un hombre, el policía de Nueva York John McClane, ha conseguido escapar del acoso terrorista. Aunque está solo y fuera de servicio, McClane se enfrentará a los secuestradores. Él es la única esperanza para los rehenes",
                    "popularity": 60.104,
                    "poster_path": "/m54tK4wKjc1w2dp7QInG0munGao.jpg",
                    "release_date": "1988-07-15",
                    "title": "Duro de matar",
                    "video": False,
                    "vote_average": 7.795,
                    "vote_count": 11233
                }
            ],
            "total_pages": 1,
            "total_results": 10
        }
        self.assertEqual(clean_no_release_date(data), expected_result)

    def test_get_director(self):
        data = {
            "id": 4203,
            "cast": [
                {
                    "adult": False,
                    "gender": 1,
                    "id": 2744,
                    "known_for_department": "Acting",
                    "name": "Carmen Maura",
                    "original_name": "Carmen Maura",
                    "popularity": 5.983,
                    "profile_path": "/sXvr7BvxscBkYpGTcYjpqbzkUSH.jpg",
                    "cast_id": 3,
                    "character": "Pepa",
                    "credit_id": "52fe43b2c3a36847f8068787",
                    "order": 0
                },
                {
                    "adult": False,
                    "gender": 2,
                    "id": 3131,
                    "known_for_department": "Acting",
                    "name": "Antonio Banderas",
                    "original_name": "Antonio Banderas",
                    "popularity": 39.118,
                    "profile_path": "/fce7zl6elUzsv7wudHFc7RgFtjD.jpg",
                    "cast_id": 4,
                    "character": "Carlos",
                    "credit_id": "52fe43b2c3a36847f806878b",
                    "order": 1
                },
                {
                    "adult": False,
                    "gender": 1,
                    "id": 25257,
                    "known_for_department": "Acting",
                    "name": "Julieta Serrano",
                    "original_name": "Julieta Serrano",
                    "popularity": 0.945,
                    "profile_path": "/3eVHZ5gieSxNYUJRXaYLDaljDQO.jpg",
                    "cast_id": 5,
                    "character": "Lucía",
                    "credit_id": "52fe43b2c3a36847f806878f",
                    "order": 2
                },
                {
                    "adult": False,
                    "gender": 1,
                    "id": 25025,
                    "known_for_department": "Acting",
                    "name": "María Barranco",
                    "original_name": "María Barranco",
                    "popularity": 2.759,
                    "profile_path": "/47iVJl6a8oOenab7LeYEnBO40xe.jpg",
                    "cast_id": 6,
                    "character": "Candela",
                    "credit_id": "52fe43b2c3a36847f8068793",
                    "order": 3
                },
                {
                    "adult": False,
                    "gender": 1,
                    "id": 25258,
                    "known_for_department": "Acting",
                    "name": "Rossy de Palma",
                    "original_name": "Rossy de Palma",
                    "popularity": 6.946,
                    "profile_path": "/3IH9ZBUcFNwBr8IcS1RZhMKTpeg.jpg",
                    "cast_id": 7,
                    "character": "Marisa",
                    "credit_id": "52fe43b2c3a36847f8068797",
                    "order": 4
                }
            ],
            "crew": [
                {
                    "adult": False,
                    "gender": 2,
                    "id": 309,
                    "known_for_department": "Directing",
                    "name": "Pedro Almodóvar",
                    "original_name": "Pedro Almodóvar",
                    "popularity": 9.367,
                    "profile_path": "/eRgGaVKEftJ0rbZCOPzCSOBZi9.jpg",
                    "credit_id": "52fe43b2c3a36847f806877d",
                    "department": "Directing",
                    "job": "Director"
                },
                {
                    "adult": False,
                    "gender": 0,
                    "id": 27045,
                    "known_for_department": "Sound",
                    "name": "Bernardo Bonezzi",
                    "original_name": "Bernardo Bonezzi",
                    "popularity": 0.055,
                    "profile_path": None,
                    "credit_id": "52fe43b2c3a36847f80687db",
                    "department": "Sound",
                    "job": "Original Music Composer"
                },
                {
                    "adult": False,
                    "gender": 2,
                    "id": 4376,
                    "known_for_department": "Camera",
                    "name": "José Luis Alcaine",
                    "original_name": "José Luis Alcaine",
                    "popularity": 1.572,
                    "profile_path": "/6m3lhxAWoFs2swR1BFdZKwF6GIJ.jpg",
                    "credit_id": "52fe43b2c3a36847f80687e1",
                    "department": "Camera",
                    "job": "Director of Photography"
                },
                {
                    "adult": False,
                    "gender": 2,
                    "id": 952,
                    "known_for_department": "Production",
                    "name": "Agustín Almodóvar",
                    "original_name": "Agustín Almodóvar",
                    "popularity": 2.351,
                    "profile_path": "/ciY5icxyNekGwD3taLvzOprp2w5.jpg",
                    "credit_id": "52fe43b2c3a36847f80687cf",
                    "department": "Production",
                    "job": "Executive Producer"
                },
                {
                    "adult": False,
                    "gender": 2,
                    "id": 309,
                    "known_for_department": "Directing",
                    "name": "Pedro Almodóvar",
                    "original_name": "Pedro Almodóvar",
                    "popularity": 9.367,
                    "profile_path": "/eRgGaVKEftJ0rbZCOPzCSOBZi9.jpg",
                    "credit_id": "52fe43b2c3a36847f80687c9",
                    "department": "Production",
                    "job": "Producer"
                }
            ]
        }
        expected_result = [
            {
                "id": 309,
                "name": "Pedro Almodóvar",
            }
        ]
        self.assertEqual(get_director(data), expected_result)

    def test_clean_related_movies_data(self):
        data = {
            "cast": [
                {
                    "adult": False,
                    "backdrop_path": None,
                    "genre_ids": [
                        99
                    ],
                    "id": 53943,
                    "original_language": "en",
                    "original_title": "Iron and Beyond",
                    "overview": "",
                    "popularity": 3.311,
                    "poster_path": "/790Xm2h0z5CtfVmI7W6jxwut5y.jpg",
                    "release_date": "2002-11-15",
                    "title": "Iron and Beyond",
                    "video": False,
                    "vote_average": 5.3,
                    "vote_count": 3,
                    "character": "Self - Director",
                    "credit_id": "52fe4884c3a36847f816b751",
                    "order": 8
                },
                {
                    "adult": False,
                    "backdrop_path": None,
                    "genre_ids": [
                        10770,
                        99
                    ],
                    "id": 480404,
                    "original_language": "en",
                    "original_title": "A Night to Die For",
                    "overview": "",
                    "popularity": 1.516,
                    "poster_path": "/i1rVhnOgIyGaCU7sixQ9W2KQHoR.jpg",
                    "release_date": "",
                    "title": "A Night to Die For",
                    "video": False,
                    "vote_average": 0,
                    "vote_count": 0,
                    "character": "Self",
                    "credit_id": "657ca6e1176a941737114216",
                    "order": 15
                },
                {
                    "adult": False,
                    "backdrop_path": None,
                    "genre_ids": [],
                    "id": 423192,
                    "original_language": "en",
                    "original_title": "Beneath the Surface: The Making of 'The Hunt for Red October'",
                    "overview": "",
                    "popularity": 1.14,
                    "poster_path": "/yS6c2yf4Ef1721dAFY8VNpdBI33.jpg",
                    "release_date": "2003-05-06",
                    "title": "Beneath the Surface: The Making of 'The Hunt for Red October'",
                    "video": False,
                    "vote_average": 5.4,
                    "vote_count": 4,
                    "character": "",
                    "credit_id": "58134122925141543e025261",
                    "order": 5
                }
            ],
            "crew": [
                {
                    "adult": False,
                    "backdrop_path": "/YL3GPOiDcNraIJOVDCZsoOBoDy.jpg",
                    "genre_ids": [
                        878,
                        28,
                        12,
                        53
                    ],
                    "id": 106,
                    "original_language": "en",
                    "original_title": "Predator",
                    "overview": "Un grupo de mercenarios es contratado por la CIA para rescatar a unos pilotos que han sido apresados por la guerrilla en la selva centroamericana. La misión es un éxito, pero durante el viaje de regreso se dan cuenta de que algo misterioso e invisible está dándoles caza uno a uno. Ese algo resulta ser un cazador alienígena que se queda con las calaveras de sus víctimas como trofeos.",
                    "popularity": 74.286,
                    "poster_path": "/bzLLeqhNBNmO6WImHrrmLNyhMxi.jpg",
                    "release_date": "1987-06-12",
                    "title": "Depredador",
                    "video": False,
                    "vote_average": 7.5,
                    "vote_count": 8137,
                    "credit_id": "52fe4218c3a36847f8003b0d",
                    "department": "Directing",
                    "job": "Director"
                },
                {
                    "adult": False,
                    "backdrop_path": "/oIwfoUFfWfESn0Y8u8jv9lc8li1.jpg",
                    "genre_ids": [
                        28,
                        53
                    ],
                    "id": 562,
                    "original_language": "en",
                    "original_title": "Die Hard",
                    "overview": "En lo alto de la ciudad de Los Ángeles, un grupo terrorista se ha apoderado de un edificio, tomando a un grupo de personas como rehenes. Sólo un hombre, el policía de Nueva York John McClane, ha conseguido escapar del acoso terrorista. Aunque está solo y fuera de servicio, McClane se enfrentará a los secuestradores. Él es la única esperanza para los rehenes",
                    "popularity": 60.104,
                    "poster_path": "/m54tK4wKjc1w2dp7QInG0munGao.jpg",
                    "release_date": "1988-07-15",
                    "title": "Duro de matar",
                    "video": False,
                    "vote_average": 7.795,
                    "vote_count": 11233,
                    "credit_id": "52fe4252c3a36847f8015429",
                    "department": "Directing",
                    "job": "Director"
                },
                {
                    "adult": False,
                    "backdrop_path": "/bMn257wAXIuIDrvtFMxEGSXaRcZ.jpg",
                    "genre_ids": [
                        27,
                        53,
                        10770
                    ],
                    "id": 26215,
                    "original_language": "en",
                    "original_title": "Quicksilver Highway",
                    "overview": "",
                    "popularity": 3.276,
                    "poster_path": "/ktKeyB6yNo81wD60NxZvb7f1nZz.jpg",
                    "release_date": "",
                    "title": "Quicksilver Highway",
                    "video": False,
                    "vote_average": 5.1,
                    "vote_count": 62,
                    "credit_id": "5c6c14690e0a265627a5fe7d",
                    "department": "Production",
                    "job": "Executive Producer"
                },
                {
                    "adult": False,
                    "backdrop_path": "/1yPq4qQ5uFc7G69XcBvyrE695M5.jpg",
                    "genre_ids": [
                        18,
                        80,
                        10770
                    ],
                    "id": 250396,
                    "original_language": "en",
                    "original_title": "The Right to Remain Silent",
                    "overview": "",
                    "popularity": 3.563,
                    "poster_path": "/zsR7M2s4RlRjIsVFXWoXfjFsv9.jpg",
                    "release_date": "1996-01-07",
                    "title": "The Right to Remain Silent",
                    "video": False,
                    "vote_average": 8,
                    "vote_count": 1,
                    "credit_id": "5ec046358e2e00002118c536",
                    "department": "Production",
                    "job": ""
                }
            ],
            "id": 1090
        }
        expected_result = {
            "cast": [
                {
                    "adult": False,
                    "backdrop_path": None,
                    "genre_ids": [
                        99
                    ],
                    "id": 53943,
                    "original_language": "en",
                    "original_title": "Iron and Beyond",
                    "overview": "",
                    "popularity": 3.311,
                    "poster_path": "/790Xm2h0z5CtfVmI7W6jxwut5y.jpg",
                    "release_date": "2002-11-15",
                    "title": "Iron and Beyond",
                    "video": False,
                    "vote_average": 5.3,
                    "vote_count": 3,
                    "character": "Self - Director",
                    "credit_id": "52fe4884c3a36847f816b751",
                    "order": 8
                }
            ],
            "crew": [
                {
                    "adult": False,
                    "backdrop_path": "/YL3GPOiDcNraIJOVDCZsoOBoDy.jpg",
                    "genre_ids": [
                        878,
                        28,
                        12,
                        53
                    ],
                    "id": 106,
                    "original_language": "en",
                    "original_title": "Predator",
                    "overview": "Un grupo de mercenarios es contratado por la CIA para rescatar a unos pilotos que han sido apresados por la guerrilla en la selva centroamericana. La misión es un éxito, pero durante el viaje de regreso se dan cuenta de que algo misterioso e invisible está dándoles caza uno a uno. Ese algo resulta ser un cazador alienígena que se queda con las calaveras de sus víctimas como trofeos.",
                    "popularity": 74.286,
                    "poster_path": "/bzLLeqhNBNmO6WImHrrmLNyhMxi.jpg",
                    "release_date": "1987-06-12",
                    "title": "Depredador",
                    "video": False,
                    "vote_average": 7.5,
                    "vote_count": 8137,
                    "credit_id": "52fe4218c3a36847f8003b0d",
                    "department": "Directing",
                    "job": "Director"
                },
                {
                    "adult": False,
                    "backdrop_path": "/oIwfoUFfWfESn0Y8u8jv9lc8li1.jpg",
                    "genre_ids": [
                        28,
                        53
                    ],
                    "id": 562,
                    "original_language": "en",
                    "original_title": "Die Hard",
                    "overview": "En lo alto de la ciudad de Los Ángeles, un grupo terrorista se ha apoderado de un edificio, tomando a un grupo de personas como rehenes. Sólo un hombre, el policía de Nueva York John McClane, ha conseguido escapar del acoso terrorista. Aunque está solo y fuera de servicio, McClane se enfrentará a los secuestradores. Él es la única esperanza para los rehenes",
                    "popularity": 60.104,
                    "poster_path": "/m54tK4wKjc1w2dp7QInG0munGao.jpg",
                    "release_date": "1988-07-15",
                    "title": "Duro de matar",
                    "video": False,
                    "vote_average": 7.795,
                    "vote_count": 11233,
                    "credit_id": "52fe4252c3a36847f8015429",
                    "department": "Directing",
                    "job": "Director"
                }
            ],
            "id": 1090
        }
        self.assertEqual(clean_related_movies_data(data), expected_result)
