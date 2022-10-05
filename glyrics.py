import lyricsgenius as lg
client_id = "f7R4qw8zMe_YJn3WFNWKnNqwPWIrDUZvYjOkwbPkgARCYmDLVTtbQeHj4XYJn9YZ"
client_secret = "U_eOSFxJkp3qBmWpr7in1gDfanywkE6HPrR2EYMYjdnpAAzofms7tVSTXz8A27ru_rbjy7LRQcS4ks6KBMCGQg"
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

def lyric(song_name):
    songs = genius.search_songs(song_name)
    for song in songs['hits']:
        # print(f"{song['result']['title']} by {song['result']['primary_artist']['name']}")
        url = song['result']['url']
        song_lyrics = genius.lyrics(song_url=url)
        # id = song['result']['id']
        # song_lyrics = genius.lyrics(id)
        return [song['result']['title'],song['result']['primary_artist']['name'],song_lyrics]