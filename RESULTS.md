# Homework 1 results

Your name:
Alexander Pegot-Ogier (ap9283)
Nikolaos Prasinos (np3106)
Kyeongmo Kang (kk5739)

## Part 1
Paste the results of your queries for each question given in the README below:

1.
ID: 22344, Track Title: Outburst
ID: 66084, Track Title: Got My Modem Working
ID: 66096, Track Title: Mistress Song

2.
track_explicit values: None
track_explicit values: Radio-Safe
track_explicit values: Radio-Unsafe
track_explicit values: Adults-Only

3.
Track Title: Siesta, Listens: 356588

4.
Artists with related projects: 453

5.
Track Language: de, Number of Tracks: 4
Track Language: ru, Number of Tracks: 4

6.
Number of Tracks: 34

7.
Artist Name: U Can Unlearn Guitar, Number of Distinct Producers: 6
Artist Name: Ars Sonor, Number of Distinct Producers: 6
Artist Name: Disco Missile, Number of Distinct Producers: 5

8.
ID: 76008, Track Title: JessicaBD, Artist Name: Cody Goss

## Part 2

- Execution time before optimization: 
Mean time: 0.043 [seconds/query]
Best time: 0.008 [seconds/query]

- Execution time after optimization:
Mean time: 0.032 [seconds/query]
Best time   : 0.006 [seconds/query]

- Briefly describe how you optimized for this query:

To optimize this query, we focused on improving the efficiency of joins and aggregations, as they are the most computationally expensive operations. Since the query retrieves artists and their albums by joining the artist, track, and album tables, we added indexes that directly support these relationships. The best-performing index was idx_track_artist_album ON track(artist_id, album_id), which allows SQLite to quickly locate tracks for a given artist and efficiently join them with albums. Additionally, we tested indexes on artist.id, album.id, and album.album_listens, but they did not yield significant improvements, as they do not directly optimize the join-heavy structure of the query. This approach ensured that the database could process grouping and aggregation (MIN(album.album_listens)) faster, leading to noticeable performance gains.

- Did you try anything other approaches?  How did they compare to your final answer?

Yes, we experimented with several different indexing strategies to compare their impact on query performance. First, we tested an index on artist.id, but since it is already the primary key and inherently indexed, the improvement was minimal. Then, we tried an index on album.id, but this had no effect, as the query does not perform direct lookups on albums—it only aggregates album_listens. Finally, we tested an index on album_listens, expecting it to speed up filtering with the HAVING clause, but it provided no benefit because SQLite processes MIN(album.album_listens) after grouping, making an index on individual listens ineffective. Ultimately, the best performance was achieved with a composite index on track(artist_id, album_id), as it optimized the core join operations, significantly reducing query execution time.
