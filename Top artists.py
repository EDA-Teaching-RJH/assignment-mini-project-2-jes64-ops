import re
import csv

Artist_pattern = r"^([A-Za-z\s]+)\s(\d+)$" #this is a pattern for names and digits for artist name and number of awards

input_file = 'artist.txt' #input data 
output_file = 'upcoming_artist.csv' # outputiing to a csv file

with open(output_file, "a", newline='') as file: # this will keep output file open in append automaitcally to overwrite data  when hading data row 
    names = ['artist_name', 'awards']
    writer = csv.DictWriter(file, fieldnames=names) # creates a dicrwriter tp write in the csv file
    
    with open(input_file, "r") as file: # when input file is open it may read the txt
        for line in file:
                artist = line.rstrip() # removes and stores artists names line by line with no extra meterial 
                match = re.search(Artist_pattern, artist) # artist name must match line pattern 
                if match:
                    artist_name = match.group(1).strip() # removes and sortes artist name from the pattern group 1
                    awards = int(match.group(2))# removes and sortes artist awarrds from the pattern group 2
                    if awards < 10: # if awards interger is less than 10 then it writes to output_file and stores in upcoming artists
                        writer.writerow({"artist_name": artist_name, "awards": awards})
                    else:
                        print(f"Artist name: {artist_name}, Awards: {awards}")# within this application is outputs the top artists that have more than 10 awards
                else: 
                    print(f"Invalid artist: {artist}")
        
