# Music Metadata Analysis (SQLite + Python)

## Overview

This project explores a normalized music metadata database using SQL and Python. It was originally submitted as Homework 2 for NYU’s DSGA1004 - Big Data course. The goal is to extract insights, optimize queries, and interact with a structured SQLite database programmatically and analytically.

## Objectives

- Write precise SQL queries for information retrieval and aggregation.
- Execute and validate queries using Python scripts.
- Optimize database performance via indexing.
- Document performance improvements and query logic.

## Database

- **File**: `music-small.db`
- **Schema**: 3 relational tables: `track`, `album`, `artist`
- **Source**: Derived from [Free Music Archive](https://freemusicarchive.org/)
- **Caveats**: Contains real-world issues like missing fields, explicit metadata, etc.

## Project Files

```
music-small-data-analysis/
├── hw2_part1.py           # SQL query execution for part 1
├── hw2_part2.py           # Query benchmarking and index optimization
├── music-small.db         # Main SQLite database
├── music-small-original.db# Backup DB file
├── RESULTS.md             # Query results, insights, and performance benchmarks
├── README.md              # Project instructions (original)
```

## Key Tasks

### Part 1: Querying with SQL

- Find tracks by lyricists whose name begins with "W"
- Enumerate values in `track.track_explicit`
- Identify the most listened track
- Count artists with related projects
- Analyze language codes used by tracks
- Count tracks by 1990s-only artists
- Rank artists by number of album producers
- Find largest gap between track listens and album listens

### Part 2: Indexing & Performance Optimization

- Applied benchmarking to measure query performance
- Designed and tested multiple indexing strategies
- Identified optimal composite index:
  ```sql
  CREATE INDEX idx_track_artist_album ON track(artist_id, album_id);
  ```
- Achieved runtime improvement (mean: 0.043s → 0.032s)

## Performance Summary

| Metric                | Before | After |
| --------------------- | ------ | ----- |
| Mean Time (sec/query) | 0.043  | 0.032 |
| Best Time (sec/query) | 0.008  | 0.006 |

See `RESULTS.md` for full breakdown and reasoning.

## Technologies Used

- Python 3.10+
- SQLite3
- SQL

## Getting Started

1. Clone the repo:

```bash
git clone https://github.com/yourusername/music-small-data-analysis.git
```

2. Run Part 1:

```bash
python hw2_part1.py music-small.db
```

3. Run Part 2 Benchmark:

```bash
python hw2_part2.py music-small.db
```

## Contributors

- Kyeongmo Kang 
- Nikolaos Prasinos 
- Alexander Pegot-Ogier 

## License

Academic use only. Created for DSGA1004 - Fall 2024.

