#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# USAGE:
#   python lab1_part1.py music_small.db

import sys
import sqlite3


# The database file should be given as the first argument on the command line
# Please do not hard code the database file!
db_file = sys.argv[1]
print(db_file)
# We connect to the database using
with sqlite3.connect(db_file) as conn:
    # This query counts the number of artists who became active in 1990
    year = (1990,)
    for row in conn.execute('SELECT count(*) FROM artist WHERE artist_active_year_begin=?', year):
        # Since there is no grouping here, the aggregation is over all rows
        # and there will only be one output row from the query, which we can
        # print as follows:
        print('Tracks from {}: {}'.format(year[0], row[0]))

        # The [0] bits here tell us to pull the first column out of the 'year' tuple
        # and query results, respectively.

    # ADD YOUR CODE STARTING HERE

    # Question 1
    print('Question 1:')

    # implement your solution to q1
    for row in conn.execute("SELECT id,track_title FROM track WHERE track_lyricist LIKE 'W%'"):
        print(f"ID: {row[0]}, Track Title: {row[1]}")

    print('---')
    # Question 2
    print('Question 2:')

    # implement your solution to q2
    for row in conn.execute("SELECT DISTINCT track_explicit FROM track"):
        print(f"track_explicit values: {row[0]}")

    print('---')

    # Question 3
    print('Question 3:')

    # implement your solution to q3
    for row in conn.execute("SELECT track_title, SUM(track_listens) AS listen FROM track GROUP By track_title ORDER By listen DESC LIMIT 1"):
        print(f"Track Title: {row[0]}, Listens: {row[1]}")

    print('---')

    # Question 4
    print('Question 4:')

    # implement your solution to q4
    for row in conn.execute("SELECT COUNT(*) FROM artist WHERE artist_related_projects IS NOT NULL;"):
        print(f"Artists with related projects: {row[0]}")

    print('---')

    # Question 5
    print('Question 5:')

    # implement your solution to q5
    for row in conn.execute("""select track_language_code,count(id) as number_of_tracks
                            from track group by track_language_code
                            HAVING number_of_tracks = 4"""):
        print(f"Track Language: {row[0]}, Number of Tracks: {row[1]}")
    print('---')
    # Question 6
    print('Question 6: ')
    for row in conn.execute("""
        SELECT COUNT(t.id)
        FROM track t
        JOIN artist a ON t.artist_id = a.id
        WHERE a.artist_active_year_begin >= 1990
        AND a.artist_active_year_end <= 1999
        AND artist_active_year_end >= artist_active_year_begin
                                """):
        print(f"Number of Tracks: {row[0]}")
    # implement your solution to q6

    print('---')

    # Question 7
    print('Question 7:')

    # implement your solution to q7
    for row in conn.execute("""SELECT a.id, artist_name, COUNT(DISTINCT(album_producer)) as number_of_distinct_prod
            FROM artist as a
            INNER JOIN track as t
            on a.id = t.artist_id
            INNER JOIN album as al
            ON t.album_id = al.id
            GROUP BY artist_name
            ORDER BY number_of_distinct_prod DESC
            LIMIT 3;"""):
        print(f"Artist Name: {row[1]} with ID {row[0]} Number of Distinct Producers: {row[2]}")
    print('---')

    # Question 8
    print('Question 8:')

    # implement your solution to q8
    for row in conn.execute("""SELECT t.id, track_title ,artist_name
        FROM artist as a
        LEFT JOIN track as t
        on a.id = t.artist_id
        LEFT JOIN album as al
        ON t.album_id = al.id
        ORDER BY (al.album_listens - t.track_listens) DESC
        LIMIT 1;"""):
        print(f"ID: {row[0]}, Track Title: {row[1]}, Artist Name: {row[2]}")
    print('---')
