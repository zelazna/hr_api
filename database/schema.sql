create table jobs
(
	id serial not null
		constraint jobs_pkey
			primary key,
	date date default CURRENT_DATE not null,
	text text,
	url varchar(400) not null,
	email varchar(400),
	ref varchar(200)
);

alter table jobs owner to constantinguidon;

create index ix_jobs_id
	on jobs (id);

create unique index ix_jobs_url
	on jobs (url);

create table users
(
	id serial not null
		constraint users_pkey
			primary key,
	email varchar(255) not null
		constraint users_email_key
			unique,
	password varchar(255) not null,
	registered_on timestamp not null,
	admin boolean not null
);

alter table users owner to constantinguidon;

create table matchs
(
	id serial not null
		constraint matchs_pkey
			primary key,
	user_id integer not null
		constraint matchs_user_id_fkey
			references users,
	job_id integer not null
		constraint matchs_job_id_fkey
			references jobs,
	interest boolean,
	constraint unique_match
		unique (user_id, job_id)
);

alter table matchs owner to constantinguidon;

create index ix_matchs_id
	on matchs (id);

