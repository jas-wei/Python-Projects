import doctest

DANCEABLE = 0.5
POPULAR = 50

# represents the characteristic score of a song as:
# (tempo, popularity score, danceability score, energy score)
# where all values are >=0
Scores = tuple[float, int, float, float]
TEMPO = 0
POPULARITY = 1
DANCEABILITY = 2
ENERGY = 3

# represents a music track as:
# (track id, name, artist, duration (in ms), genre tags, scores)
# where id, name, artist != '', duration>0, and genre tags can be empty
MusicTrack = tuple[str, str, str, int, list[str], Scores]
TRACK_ID = 0
TITLE = 1
ARTIST = 2
DURATION = 3
GENRES = 4
SCORES = 5


# column numbers of data within input csv file
INPUT_TRACK_ID = 0
INPUT_TITLE = 3
INPUT_ARTIST = 2
INPUT_DURATION = 7
INPUT_GENRE = 1
INPUT_POPULARITY = 4
INPUT_TEMPO = 15
INPUT_DANCEABILITY = 6
INPUT_ENERGY = 8

#helper 1
def create_scores (tempo:float, popularity:int, dancibility:float, 
                   energy:float) -> Scores:
    '''
    This function will returns the values as a tuple in Track_score
    
    Precondition: the type of these values will match those described in 
    Track_score
    
    >>> create_scores (4, 0, 23, 12)
    (4, 0, 23, 12)
    >>> create_scores (79.124, 5, 0.518, 0.805)
    (79.124, 5, 0.518, 0.805)
    '''
    return (tempo, popularity, dancibility, energy)

#helper 2
def create_music_track (unique_id:str, title:str, artist:str, 
                        duration:int, genre_tag:list[str], 
                        score:Scores) -> MusicTrack:
    '''
    >>> create_music_track ('12qwegsdf', 'he', 'lee', 3, '',\
    (222, 34, 555, 234)) # doctest: +NORMALIZE_WHITESPACE
    ('12qwegsdf', 'he', 'lee', 3, [], (222, 34, 555, 234))
    
    >>> create_music_track('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', \
    'The Carters', 285200, 'R&B:Rap:Pop', \
    (135.414, 55, 0.592, 0.569)) # doctest: +NORMALIZE_WHITESPACE
    ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    
    >>> create_music_track ('007reLkuOQhAJypiC5sVyX', 'Power and the Glory', \
    'Jimmy Cliff', 311333, 'Reggae:Ska', \
    (89.336, 30, 0.683, 0.423)) #doctest: +NORMALIZE_WHITESPACE
    ('007reLkuOQhAJypiC5sVyX', 'Power and the Glory', \
    'Jimmy Cliff', 311333, ['Reggae', 'Ska'], (89.336, 30, 0.683, 0.423))
    '''
    if genre_tag != '':
        genre_list = genre_tag.split (':')
    else:
        genre_list = []
        
    return (unique_id, title, artist, duration, genre_list, score)

#helper 3
def get_highest_danceability_score (track_list:list[MusicTrack])->int:
    '''
    The function returns the highest danceability score of all 
    those music track tuples in the list.
    
    >>> t=[]
    >>> get_highest_danceability_score(t)
    0
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.826, 0.729))
    
    >>> get_highest_danceability_score([t1, t2, t3, t4])
    0.826
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 1.232, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.826, 0.729))
    
    >>> get_highest_danceability_score([t1, t2, t3, t4])
    1.232
    '''
    if track_list == []:
        return 0
    
    num_elements = len(track_list)
    index = 1
    
    highest = track_list[0][SCORES][DANCEABILITY]
    while index < num_elements:
        if track_list[index][SCORES][DANCEABILITY] > highest:
            highest = track_list[index][SCORES][DANCEABILITY]
        index += 1
    
    return highest

#1
def read_file(filename: str) -> list[MusicTrack]:
    """
    Reads file into a list of MusicTrack tuples and returns the list.

    Precondition: file is csv with data in expected columns
    and contains a header row with column titles.

    >>> read_file('0lines_data.csv')
    []

    >>> read_file('10lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    [('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme',
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862)),
    ('000CzNKC8PEt1yC3L8dqwV', 'Coeur Brise √† Prendre - Remastered',
    'Henri Salvador', 130653, ['Movie'], (79.124, 5, 0.518, 0.805)),
    ('000DfZJww8KiixTKuk9usJ', 'Earthlings',
    'Mike Love', 357573, ['Reggae'], (120.365, 30, 0.631, 0.513)),
    ('000EWWBkYaREzsBplYjUag', 'Fewerdolr',
    'Don Philippe', 104924, ['Jazz'], (76.43, 39, 0.768, 0.137)),
    ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time',
    'ZAYN', 188491, ['Dance', 'Pop'], (120.963, 70, 0.748, 0.627)),
    ('0017XiMkqbTfF2AUOzlhj6', 'Thanksgiving Chicken',
    'Chad Daniels', 127040, [], (173.912, 27, 0.536, 0.78)),
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me',
    'Taj Mahal', 160107, ['Blues'], (90.048, 31, 0.826, 0.679)),
    ('52TDNHSeWey4NFAfLDgfjL',
    'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
    'Bob Marley & The Wailers', 278987, ['Reggae'],
    (180.043, 31, 0.675, 0.808)),
    ('001VMKfkHZrlyj7JlQbQFL',
    '"Await The Kings Justice - From The ""Game Of Thrones"" Soundtrack"',
    'Ramin Djawadi', 120840, ['Soundtrack'], (113.655, 41, 0.168, 0.0354)),
    ('001YQlnDSduXd5LgBd66gT', 'El Tiempo Es Dinero - Remasterizado 2007',
    'Soda Stereo', 177267, ['Ska'], (183.571, 38, 0.554, 0.921))]
    """
    # TODO: complete this function body
    file_handle = open(filename, 'r', encoding="utf8")
    
    result_list = []
    
    file_handle.readline()
    
    for line in file_handle:
        line = line.strip()
        track = line.split(',')
        
        popularity = int(track[INPUT_POPULARITY])
        tempo = float(track[INPUT_TEMPO])
        danceability = float(track[INPUT_DANCEABILITY])
        energy = float(track[INPUT_ENERGY])
        
        score = create_scores(tempo, popularity, danceability, energy) 
        
        unique_id = track[INPUT_TRACK_ID]
        title = track[INPUT_TITLE]
        artist = track[INPUT_ARTIST]
        duration = int(track[INPUT_DURATION])
        genre_tag = track[INPUT_GENRE]    
        
        music_track = create_music_track (unique_id, title, artist, 
                                          duration, genre_tag, score)
        result_list.append(music_track)
    
    file_handle.close()
    return result_list

#2
def get_most_danceable_song_titles(lotracks: list[MusicTrack]) -> list[str]:
    """ return list of titles of the most danceable MusicTracks in lotracks

    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.826, 0.729))

    >>> tracks = [t4, t2, t3, t1]

    >>> get_most_danceable_song_titles([])
    []
    
    >>> get_most_danceable_song_titles([t3])
    ['SUMMER']
    
    >>> get_most_danceable_song_titles([t1, t3])
    ['Zangiefs Theme']

    >>> get_most_danceable_song_titles([t2, t1, t3, t4])
    ['She Knows How To Rock Me', 'Get It Together']

    >>> get_most_danceable_song_titles([t1, t2, t3, t4])
    ['She Knows How To Rock Me', 'Get It Together']

    >>> get_most_danceable_song_titles([t1, t2, t4, t3])
    ['She Knows How To Rock Me', 'Get It Together']

    >>> get_most_danceable_song_titles([t1, t4, t3, t2])
    ['Get It Together', 'She Knows How To Rock Me']
    """
    # TODO: complete this function body
    result_list = []
    
    if lotracks != []:
        danceability_score = get_highest_danceability_score(lotracks)
        
        for track in lotracks:
            if danceability_score in track[SCORES]:
                result_list.append(track[TITLE])
        
    return result_list

#3
def get_most_danceable_tracks_by_artist(track_data: list[MusicTrack],
                                        artist: str) -> list[str]:
    """
    returns a list of the title(s) of MusicTrack(s) in track_data with the
    highest danceability score from given artist ignoring case.
    >>> some_tracks = [\
    ('53hNzjDClsnsdYpLIwqXvn', 'Video Phone', 'Beyonce', \
    215440, ['Dance', 'R&B'], (84.769, 51, 0.479, 0.763)),\
    ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time', 'ZAYN', \
    188491, ['Dance', 'Pop'], (120.963, 70, 0.748, 0.627)),\
    ('5BkHkyO9PFXs1m7vSMnXp4', 'Ring The Alarm', 'Beyonce', \
    203347, ['Dance', 'R&B'], (169.673, 52, 0.458, 0.751)),\
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', \
    160107, ['Blues'], (90.048, 31, 0.826, 0.679)),\
    ('5IVuqXILoxVWvWEPm82Jxr', 'Crazy In Love', 'Beyonce', \
    236133, ['Dance', 'Pop', 'R&B'], (99.165, 78, 0.646, 0.77))\
    ]

    >>> some_equally_danceable = [\
    ('53hNzjDClsnsdYpLIwqXvn', 'Video Phone', 'Beyonce', \
    215440, ['Dance', 'R&B'], (84.769, 51, 0.479, 0.763)),\
    ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time', 'ZAYN', \
    188491, ['Dance', 'Pop'], (120.963, 70, 0.748, 0.627)),\
    ('5BkHkyO9PFXs1m7vSMnXp4', 'Ring The Alarm', 'Beyonce', \
    203347, ['Dance', 'R&B'], (169.673, 52, 0.646, 0.751)),\
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', \
    160107, ['Blues'], (90.048, 31, 0.826, 0.679)),\
    ('5IVuqXILoxVWvWEPm82Jxr', 'Crazy In Love', 'Beyonce', \
    236133, ['Dance', 'Pop', 'R&B'], (99.165, 78, 0.646, 0.77))\
    ]

    >>> get_most_danceable_tracks_by_artist([], 'Beyonce')
    []

    >>> get_most_danceable_tracks_by_artist(some_tracks, '')
    []

    >>> get_most_danceable_tracks_by_artist(some_tracks, 'Radiohead')
    []

    >>> get_most_danceable_tracks_by_artist(some_tracks, 'ZAYNE')
    []

    >>> get_most_danceable_tracks_by_artist(some_tracks, 'ZAYN')
    ['Still Got Time']

    >>> get_most_danceable_tracks_by_artist(some_tracks, 'zaYN')
    ['Still Got Time']

    >>> get_most_danceable_tracks_by_artist(some_tracks, 'Beyonce')
    ['Crazy In Love']

    >>> get_most_danceable_tracks_by_artist(some_equally_danceable, 'Beyonce')
    ['Ring The Alarm', 'Crazy In Love']

    """
    result_list = []
    if track_data != [] or artist != '': 
        lower_artist = str.lower(artist)
        max_danceability = 0
        
        for track in track_data:
            current = track[SCORES][DANCEABILITY]
            lower_track_artist = str.lower(track[ARTIST])
            
            if (lower_artist == lower_track_artist
                and current > max_danceability):
                max_danceability = current

        if (max_danceability > 0):
            for track in track_data:
                current_title = track[TITLE]
                current = track[SCORES][DANCEABILITY]
                lower_track_artist = str.lower(track[ARTIST])
                
                if (max_danceability == current
                    and lower_artist == lower_track_artist
                    and current_title not in result_list):
                    result_list.append(current_title)
                    
        return result_list

#4 
def get_genres_by_artist(track_data: list[MusicTrack],
                         artist: str) -> list[str]:
    """
    returns a sorted list of the all genre(s)
    in track_data associated with given artist (matches ignore case)

    >>> some_tracks = [\
    ('53hNzjDClsnsdYpLIwqXvn', 'Video Phone', 'Beyonce', \
    215440, ['Dance', 'R&B'], (84.769, 51, 0.479, 0.763)),\
    ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time', 'ZAYN', \
    188491, ['Dance', 'Pop'], (120.963, 70, 0.748, 0.627)),\
    ('5BkHkyO9PFXs1m7vSMnXp4', 'Ring The Alarm', 'Beyonce', \
    203347, ['Dance', 'R&B'], (169.673, 52, 0.458, 0.751)),\
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', \
    160107, ['Blues'], (90.048, 31, 0.826, 0.679)),\
    ('5IVuqXILoxVWvWEPm82Jxr', 'Crazy In Love', 'Beyonce', \
    236133, ['Dance', 'Pop', 'R&B'], (99.165, 78, 0.646, 0.77))\
    ]

    >>> get_genres_by_artist([], 'Beyonce')
    []

    >>> get_genres_by_artist(some_tracks, '')
    []

    >>> get_genres_by_artist(some_tracks, 'Radiohead')
    []

    >>> get_genres_by_artist(some_tracks, 'ZAYNE')
    []

    >>> get_genres_by_artist(some_tracks, 'ZAYN')
    ['Dance', 'Pop']

    >>> get_genres_by_artist(some_tracks, 'zaYN')
    ['Dance', 'Pop']

    >>> get_genres_by_artist(some_tracks, 'Beyonce')
    ['Dance', 'Pop', 'R&B']

    """
    # TODO: complete this function body
    result_list = []
    
    if track_data != [] or artist != '':
        lower_artist = str.lower(artist)
        
        for track in track_data:
            lower_track_artist = str.lower(track[ARTIST])
            
            if lower_artist == lower_track_artist:
                for genre in track[GENRES]:
                    if genre not in result_list:
                        result_list.append(genre)
        result_list.sort()
        
    return result_list

#5
def make_party_playlist(track_data: list[MusicTrack]) -> list[str]:
    """
    returns a sorted list of the title(s) in track_data that:
    - have 'Dance' as a tag genre
    - have a 'Danceability' score above 0.5
    - have 'Popularity' score above 50

    >>> some_tracks = [\
    ('53hNzjDClsnsdYpLIwqXvn', 'Video Phone', 'Beyonce', \
    215440, ['Dance', 'R&B'], (84.769, 51, 0.479, 0.763)),\
    ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time', 'ZAYN', \
    188491, ['Dance', 'Pop'], (120.963, 70, 0.748, 0.627)),\
    ('5BkHkyO9PFXs1m7vSMnXp4', 'Ring The Alarm', 'Beyonce', \
    203347, ['Dance', 'R&B'], (169.673, 52, 0.458, 0.751)),\
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', \
    160107, ['Blues'], (90.048, 31, 0.826, 0.679)),\
    ('5IVuqXILoxVWvWEPm82Jxr', 'Crazy In Love', 'Beyonce', \
    236133, ['Dance', 'Pop', 'R&B'], (99.165, 78, 0.646, 0.77)),\
    ('7ywzEdEuVG1lsjsRCGJfLy', 'When I Look At You', 'Miley Cyrus', \
    248587, ['Dance', 'Pop'], (137.87, 64, 0.465, 0.569)),\
    ('7ytES33eLYS9WaZLKqWfYM', 'My Life', 'Mary J. Blige', \
    257427, ['Dance', 'R&B', 'Soul'], (150.904, 50, 0.546, 0.612)),\
    ('7z0JDE4w67HXt5lEWsU2Hj', 'Strawberry Bubblegum', 'Justin Timberlake', \
    479747, ['Dance', 'Rap'], (104.96, 54, 0.798, 0.465)),\
    ('7z38bideBRvGAgjXe2SECm', 'Opposites Attract', 'Paula Abdul', \
    263779, ['Dance'], (117.79, 52, 0.783, 0.842))\
    ]
    
    >>> other_tracks = [\
    ('53hNzjDClsnsdYpLIwqXvn', 'Video Phone', 'Beyonce', \
    215440, ['R&B'], (84.769, 51, 0.479, 0.763)),\
    ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time', 'ZAYN', \
    188491, ['Pop'], (120.963, 70, 0.748, 0.627)),\
    ('5BkHkyO9PFXs1m7vSMnXp4', 'Ring The Alarm', 'Beyonce', \
    203347, ['R&B'], (169.673, 52, 0.458, 0.751)),\
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', \
    160107, ['Blues'], (90.048, 31, 0.826, 0.679)),\
    ('5IVuqXILoxVWvWEPm82Jxr', 'Crazy In Love', 'Beyonce', \
    236133, ['Pop', 'R&B'], (99.165, 78, 0.646, 0.77)),\
    ('7ywzEdEuVG1lsjsRCGJfLy', 'When I Look At You', 'Miley Cyrus', \
    248587, ['Pop'], (137.87, 64, 0.465, 0.569)),\
    ('7ytES33eLYS9WaZLKqWfYM', 'My Life', 'Mary J. Blige', \
    257427, ['R&B', 'Soul'], (150.904, 50, 0.546, 0.612)),\
    ('7z0JDE4w67HXt5lEWsU2Hj', 'Strawberry Bubblegum', 'Justin Timberlake', \
    479747, ['Rap'], (104.96, 54, 0.798, 0.465)),\
    ]

    >>> make_party_playlist([])
    []

    >>> make_party_playlist(some_tracks) # doctest: +NORMALIZE_WHITESPACE
    ['Crazy In Love', 'Opposites Attract',
    'Still Got Time', 'Strawberry Bubblegum']
    
    >>> make_party_playlist(other_tracks) # doctest: +NORMALIZE_WHITESPACE
    []
    """
    # TODO: complete this function body
    title_list = []
    
    if track_data != []:
        for track in track_data:
            if (track[SCORES][POPULARITY] > POPULAR
                and track[SCORES][DANCEABILITY] > DANCEABLE):
                for genre in track[GENRES]:
                    if 'dance' == str.lower(genre):
                        title_list.append(track[TITLE])
        
        if title_list != []:
            title_list.sort()
            
    return title_list