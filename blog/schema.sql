drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    title text not null,
    'subtitle' text not null,
    'date' text not null,
    'path' text not null
);
