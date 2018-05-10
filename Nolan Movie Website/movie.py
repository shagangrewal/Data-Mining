import media
import webpage

a = media.Movie("Momento","A man suffering from memory disorder",
                "C:\\Users\\Shagan Grewal\\Downloads\\Python\\Website\\images\\Memento_poster.jpg",
                "https://www.youtube.com/watch?v=0vS0E9bBSL0")
b = media.Movie("The Prestige","Story of two magicians striving to be the best",
                "C:\\Users\\Shagan Grewal\\Downloads\\Python\\Website\\images\\11297657.jpg",
                "https://www.youtube.com/watch?v=o4gHCmTQDVI")
c = media.Movie("The Dark Knoight","Batman up against his greatest foe, The Joker",
                "C:\\Users\\Shagan Grewal\\Downloads\\Python\\Website\\images\\Dark_Knight.jpg",
                "https://www.youtube.com/watch?v=EXeTwQWrcwY")
d = media.Movie("Inception","Story of man caught in his past and manufactured dreams",
                "C:\\Users\\Shagan Grewal\\Downloads\\Python\\Website\\images\\inception.jpg",
                "https://www.youtube.com/watch?v=YoHD9XEInc0")
e = media.Movie("Interstellar","Man on a space mission to save human race",
                "C:\\Users\\Shagan Grewal\\Downloads\\Python\\Website\\images\\Interstellar.jpg",
                "https://www.youtube.com/watch?v=zSWdZVtXT7E")
f = media.Movie("Dunkirk","Famous rescue mission on Dunkirk during World War-2",
                "C:\\Users\\Shagan Grewal\\Downloads\\Python\\Website\\images\\Dunkirk.jpg",
                "https://www.youtube.com/watch?v=F-eMt3SrfFU")

movie_list = [a,b,c,d,e,f]
webpage.open_movies_page(movie_list)

