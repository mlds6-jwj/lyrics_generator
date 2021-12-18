import data_acquisition_LyricGeniusAPI as data

if __name__ == '__main__':
    genius = data.login_genius(exclude=['(Remix)', '(Live)'])
    artists = data.default_artist()
    final_lyrics = data.get_lyrics(geniusSession = genius, arr = artists, k = 25)
    data.create_file('lyrics.txt', final_lyrics)
