from datetime import datetime
import lyricsgenius as lg
import os

def login_genius(key = 'h5ZhFryULh_gum-tPES8CR9ovkkJKJHuOXy2WfoebApbBxsfJmjbyRGekOMHmczw', skip = True, exclude = [], remove_headers = True):
  """
  Args:

  <key> => llave única para acceder a Genius como desarrollador (se obtiene del registro en genius.com)
  <skip> => salta cualquier contenido que no sean lyrics
  <exclude> => términos que deben ser excluidos del nombre de cada canción, recomendado [('Remix'),('Live')]
  <remove_headers> => quita la descripción de la canción

  Description:

  Esta función toma un <key> del usuario (tiene una por defecto) y el usuario puede escoger si desea saltar elementos que no sean letras de canciones.
  Retorna un objeto de clase Genius que permite la consulta de canciones.

  """
  genius = lg.Genius(key, skip_non_songs = skip, excluded_terms = exclude, remove_section_headers = remove_headers)
  return genius

def default_artist():
  """
  Description:

  Lista por defecto para minar los datos
  """
  artist_list = ['MGMT','Motionless In White','Mistki','The Offspring','Architects','Incubus','Bad Omens','Hollywood Undead','Blink-182','My Chemical Romance','As I Lay Dying','Avenged Sevenfold',
                    'Bon Jovi','Cave town','Disturbed','Foo Fighters','Grimes','In Flames','Judas Priest','Korn', 'Nine Inch Nails','The Word Alive','Thirty Seconds To Mars','All Time Low',
                    'Thousand FootKrutch','Falling In Reverse','Red','Bring Me The Horizon','Whitechapel','In This Moment','Halestorm','The Amity Affliction','We Came As Romans','Our last night',
                    'Icon for hire','Panic At The Disco','Fall Out Boy','Imagine Dragons','Pink Floyd','Def Leppard','Deep Purple','Motley crue','Radiohead','Muse','Bob Dylan','Arctic Monkeys',
                    'Beach House','Vampire Weekend','Gorillaz','Interpol','The Strokes','The Killers','Japanese Breakfast','Tame Impala','Metronomy','alt-J','Franz Ferdinand','The Smiths',
                    'Future Islands','David Bowie','The Rolling Stones','Angel Olsen','Simon Garfunkel','Eminem','The vaccines','The lumineers','Aurora','Depeche Mode','The Drums',
                    'Nick Cave the Bad Seeds','Bob Marley', 'Mr. Kitty','Lacuna Coil','The Neighbourhood','Ice Nine Kills']
  return artist_list

def get_lyrics(geniusSession:lg.Genius, arr:list, k:int):
    """
    Args:

    <geniusSession> => Objeto tipo Genius que permite la consulta.
    <arr> => lista de artistas para minar (recomendado que todos sean del mismo idioma).
    <k> => int, número de canciones por artista.

    Description:

    Toma un contador desde cero que permite llevar la cuenta de canciones por artista.
    Luego, comienza a buscar por artista, la cantidad de canciones deseadas ordenadas por popularidad y las escribe en lyrics.txt, que es la base de datos usada.
    Retorna una lista.
    """
    c = 0
    lyrics_list = []
    for name in arr:
        try:
            songs = (geniusSession.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [f"Artist:{name}, \n {song.lyrics} \n \n  <|endoftext|>   \n \n" for song in songs]
            lyrics_list.append(s)
            c += 1
            print(f"Songs grabbed:{len(s)}\n")
        except:
            print(f"some exception at {name}: {c}")
    return [''.join(x) for x in lyrics_list]

def create_file(name='lyrics', final_lyrics=[]):
  """
  Args:

  <name> => nombre del archivo+extensión, por defecto es lyrics.txt.
  <lyrics_list> => lista con los artistas y sus respectivas canciones.

  Description:

  Crea un archivo <name> donde se guardarán las canciones descargadas.
  """
  filename = name +'-'+ datetime.now().strftime("%Y_%m_%d")
  lyrics = open(filename+'.txt',"w")
  lyrics.write(' '.join(map(str, final_lyrics)))
  lyrics.close()

"""
genius = login_genius(exclude=['(Remix)', '(Live)'])

artists = default_artist()

final_lyrics = get_lyrics(arr = artists, k = 25)

create_file('lyrics.txt', final_lyrics)
"""
