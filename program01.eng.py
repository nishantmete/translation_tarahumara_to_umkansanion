#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ajeje the librarian, recently found a hidden room
in the Keras Library (a great place located in
Umkansa, the largest village in the White Mountains).
There, she discovered several books, containing
music scores of ancient Tarahumara songs.
So, she invited over a musician friend to have a look
at them, and he informed her that the scores are
written in Tarahumara notation and need to be translated
into a notation familiar to Umkansanian musicians,
so they can play them back.

Tarahumaras used numbers instead of letters for
writing notes:
0 in place of A, 1 in place of B, and so on, until
7 in place of G. Flat (b) and sharp (#) notes
(see note 3 below, if you do not know what flat
and sharp notes are)
were followed by a - and a +, respectively (for example,
0- meant flat A). Moreover, they just repeated the
same number multiple times to represent the note's
duration. For example, 0000 would mean that the
A note had a length of 4, while 0-0-0-0- would mean
that the A flat note had a length of 4.
Pauses were written down
as spaces; for example, twelve spaces represent
a pause of 12. Both notes and pauses could span
different lines of the score (e.g., starting on line
x and continuing on line x + 1, x + 2, and so on).
Finally, music scores were written from right
to left and from top to bottom, and going to a new
line did not mean anything in terms of the music score.
Umkansanians, instead, are used to write down notes using letters,
and each note is followed by its duration (so, the example
above would be written as A4). Flat and sharp notes are
followed by a b or a #, respectively (for example, A flat
is written as Ab, so the example above would be written ad
Ab4). Pauses are written using the letter P, followed by
their duration, and no spaces are used at all.
Finally, they are used to read music from left
to right on a single row.

As Ajeje knows that you are a skilled programmer, she
provides you with a folder containing the transcription
of all the Tarahumara songs she found, organized in
multiple subfolders and files (one song per file).
Also, she prepared an index file in which each row
contains the title of a Tarahumara song (in quotes),
followed by a space and the path of the file containing
that song (in quotes, relative to the root folder).
She would like to translate all the songs listed in
the index and store them into new files, each one
named with the title of the song it contains (.txt),
in a folder structure matching the original one.
Also, she would like to store in the root folder of
the created structure, a file containing on each row
the title of a song (in quotes) and the corresponding
song length, separated by a space. Songs in the index
need to be ordered in descending length and, if the
length of some songs is the same, in ascending alphabetical
order. The length of a song is the sum of the durations
of all notes and pauses it is made of.

Would you be able to help Ajeje out in translating
the Tarahumara songs into Umkansanian ones?

Note 0: below, you are provided with a function to
Umkansanize the Tarahumara songs; after being executed,
it must return a dictionary in which each key is a song
title and the associated value is the song's duration

Note 1: the songs index file index.txt
is stored in the source_root folder

Note 2: the index of the translated songs
index.txt is in the target_root folder

Note 3: flat and sharp notes are just "altered" versions
of regular notes; for example an F# ("F sharp") is the
altered version of an F, that is, an F note which is a
half of a tone higher than a regular F; the same holds for
flat notes, which are a half of a tone lower than regular notes;
from the point of view of the homework, flat and sharp notes
must be treated the same as regular notes (except for their notation).

Note 4: to create the directory structure you can use the 'os' library functions
(e.g. os.makedirs)
'''

import os

def convert_to_umkanian_script(char):
    if char == "+":
        return "#"
    elif char == "-":
        return "b"
    elif char == "0":
        return "A"
    if char == "1":
        return "B"
    elif char == "2":
        return "C"
    elif char == "3":
        return "D"
    elif char == "4":
        return "E"
    elif char == "5":
        return "F"
    elif char == "6":
        return "G"
    else :
        return "P"
    
def convert_to_umkanian_song(a_string):
    umkansanizanion_song_draft = a_string
    umkansanizanion_song_draft_list = []

    """for char, next_char in zip(umkansanizanion_song_draft, umkansanizanion_song_dr [1:]):
        if next_char in ('b', '#'):
            umkansanizanion_song_draft_list.append(char + next_char)
        else:
            if char in ("b", "#"):
                continue
            else:
                umkansanizanion_song_draft_list.append(char)"""
    
    umkansanizanion_song_draft_list = [char + next_char if next_char in ('b', '#') else char for char, next_char in zip(umkansanizanion_song_draft, umkansanizanion_song_draft[1:]) if char not in ("b", "#")]
    umkansanizanion_song_draft_list.append(umkansanizanion_song_draft[-1])

    #nextchar = next_char
    #umkansanizanion_song_draft_list.append(nextchar)
    
    #[umkansanizanion_song_draft_list.remove(element) for element in umkansanizanion_song_draft_list if element in ("b", "#")]
    
    umkansanizanion_song_draft_list = [element for element in umkansanizanion_song_draft_list if element not in ("b", "#")]

    umkansanizanion_song = ""
    previous_char = umkansanizanion_song_draft_list[0]
    repetitions = 1
    for character in umkansanizanion_song_draft_list[1:]:
        if character == previous_char:
            repetitions += 1
        else:
            umkansanizanion_song += previous_char + str(repetitions)
            previous_char = character
            repetitions = 1
    umkansanizanion_song += previous_char + str(repetitions)

    return umkansanizanion_song
    
def get_the_sum(a_string):
    numbers = []
    number = ''
    for character in a_string:
        if character.isnumeric():
            number += character
        else:
            if number.isnumeric():
                numbers.append(int(number))
                number = ''

    if number.isnumeric():
        numbers.append(int(number))

    return sum(numbers)


def make_and_write_the_songs(paths_with_song_names, namers_with_songs, source_root, target_root):
    for keys, values in paths_with_song_names.items():
        directory, file_name = os.path.split(values)
        if len(directory) == 0:
            with open(f"{target_root}/{keys}.txt", "w", encoding="utf-8") as song_files:
                print(namers_with_songs[keys], file=song_files)
        else:
            os.makedirs(f"{target_root}/{directory}", exist_ok=True)
            with open(f"{target_root}/{directory}/{keys}.txt", "w", encoding="utf-8") as song_files:
                print(namers_with_songs[keys], file=song_files)

def make_the_index_file(target_root, sorted_songs):
    os.makedirs(target_root, exist_ok=True)
    with open(f"{target_root}/index.txt", "w", encoding="utf-8") as out_file:
        for a_tuple in sorted_songs:   
            for index, element in enumerate(a_tuple):
                if index == 0:
                    out_file.write(f'"{element}" ')
                else:
                    out_file.write(f"{element}\n")

def open_get_info_index(source_root):
    paths_with_song_names = {}
    with open(f"{source_root}/index.txt", "r", encoding="utf-8") as index_in:
        for line in index_in:
            line_container= line.split('"')
            paths_with_song_names[line_container[1]] = line_container[3]

    return paths_with_song_names

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:

    paths_with_song_names = open_get_info_index(source_root)
    names_with_durations = {}
    namers_with_songs= {}
    for song_name, path in paths_with_song_names.items():    
        with open(f"{source_root}/{path}", "r", encoding="utf-8") as source_file:
            tarahumara_song = ""
            for line in source_file:
                if line[-1] == "\n":
                    line = line[:-1]
                for a_line in line[::-1]:
                    tarahumara_song += a_line
            umkansanizanion_song_draft = ""
            for character in tarahumara_song:
                umkansanizanion_song_draft += convert_to_umkanian_script(character)

            umkansanizanion_song = convert_to_umkanian_song(umkansanizanion_song_draft)
    
            duration = get_the_sum(umkansanizanion_song)
            names_with_durations[song_name] = duration
            namers_with_songs[song_name] = umkansanizanion_song

    
    sorted_songs = sorted(names_with_durations.items(), key=lambda item: (-item[1], item[0]))

    
    write_files = make_the_index_file(target_root, sorted_songs)
    index_file = make_and_write_the_songs(paths_with_song_names, namers_with_songs, source_root, target_root)
    
    return names_with_durations 

if __name__ == "__main__":
    
    #for i in range(0, 18):
    #    print(Umkansanize(f"test01/{i}.txt", "Umkansanian"))
    Umkansanize("test10", "test0010.out")
    pass

