artists = [ 
    "Burna boy 22",
    "Wizkid 31",
    "Davido 29",
    "Rema 12",
    "Asake 3",
    "Samzo 1",
    "UncleKwarmz 0"
] #lists of artists

with open('artist.txt', 'w') as file: # with the input _file open it writes the following lists of artists and creates a new line for each 
    for artist in artists:
        file.write(f"{artist}\n")