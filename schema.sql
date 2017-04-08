create table if not exists Micros (
    id char(64) primary key,
    micro_link text not null,
    real_link text not null,
    creation int not null,
    expiration int not null,
    hits int default 0,
    public bool not null
);
