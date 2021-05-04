import lyricsgenius as lg

genius = lg.Genius("")

# Turn off status messages
genius.verbose = True
# Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.remove_section_headers = True
# Include hits thought to be non-songs (e.g. track lists)
genius.skip_non_songs = False
# Exclude songs with these words in their title
genius.excluded_terms = ["(Remix)", "(Live)"]

def lyric(word):
    try:
        song = genius.search_song(word)
        return song.lyrics
    except:
        return "didn't found the lyrics"

def search(artist_name,song_name):
    artist = genius.search_artist(artist_name, max_songs=3, sort="title")
    print(artist.name)
    song = genius.search_song(song_name, artist.name)
  
    return song.lyrics

