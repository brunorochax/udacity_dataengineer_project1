# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays(songplay_id serial primary key, start_time timestamp references time(start_time), \
user_id varchar references users(user_id), level varchar, song_id varchar references songs(song_id), artist_id varchar references artists(artist_id), \
session_id varchar, location varchar, user_agent varchar);""")

user_table_create = ("""create table if not exists users(user_id varchar primary key, first_name varchar, last_name varchar, \
gender varchar, level varchar);""")

song_table_create = ("""create table if not exists songs(song_id varchar primary key, title varchar, artist_id varchar, year int, \
duration float);""")

artist_table_create = ("""create table if not exists artists(artist_id varchar primary key, name varchar, location varchar, \
latitude varchar, longitude varchar);""")

time_table_create = ("""create table if not exists time(start_time timestamp primary key, hour int, day int, week int, month int, \
year int, weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (start_time, user_id, level, song_id, artist_id, \
session_id, location, user_agent) values (%s, %s, %s, %s, %s, %s, %s, %s);""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) values \
(%s, %s, %s, %s, %s);""")

song_table_insert = ("""insert into songs(song_id, title, artist_id, year, duration) values \
(%s, %s, %s, %s, %s);""")

artist_table_insert = ("""insert into artists(artist_id, name, location, latitude, longitude) values \
(%s, %s, %s, %s, %s);""")


time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday) values \
(%s, %s, %s, %s, %s, %s, %s);""")

# FIND SONGS

song_select = ("""select s.song_id, s.artist_id from songs s \
inner join artists a on a.artist_id = s.artist_id \
where s.title = %s and a.name = %s and s.duration = %s \
limit 1
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]