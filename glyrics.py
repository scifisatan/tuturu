import lyricsgenius as lg
client_access_token = "9hPqYJZrPuKjD_yGIsqgPfQ8_QlTxnuFsTwCifdnXFDsRiBLcp8Zx51DDnokiJkj"

genius = lg.Genius(client_access_token)
    
# Turn off status messages
genius.verbose = True
# Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.remove_section_headers = True
# Include hits thought to be non-songs (e.g. track lists)
genius.skip_non_songs = False
# Exclude songs with these words in their title
genius.excluded_terms = ["(Remix)", "(Live)"]



def lyric(keyword):
    songs = genius.search_songs(keyword)
    for song in songs['hits']:
        title = song['result']['title']
        artist = song['result']['primary_artist']['name']
        url = song['result']['url']
        song_lyrics = genius.lyrics(song_url=url)
        song_lyrics = song_lyrics.replace('EmbedShare URLCopyEmbedCopy', '')
        return [title,artist,song_lyrics]
        break



