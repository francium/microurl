create table if not exists Micros (
    id int auto_increment primary key,
    micro_link text not null,
    real_link text not null,
    creation int not null,
    expiration int not null
);
