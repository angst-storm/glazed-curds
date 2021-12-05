create table fvf_not_active_cams as
select grz, camera, date
from fvf
where camera not in (
    select camera
    from (select distinct camera, lat, lon from fvf) c
    group by camera
    having count(lat) > 1
        or count(lon) > 1);

create table autos_starts_and_ends_time as
select grz, min(date), max(date)
from fvf_not_active_cams
group by grz;

create table autos_starts as
select grz, min(camera) as camera, min(date) as date
from (select fvf.grz, fvf.camera, sae.min as date
      from autos_starts_and_ends_time sae
               join fvf_not_active_cams fvf
                    on sae.grz = fvf.grz and sae.min = fvf.date) starts
group by grz;

create table autos_ends as
select grz, max(camera) as camera, max(date) as date
from (select fvf.grz, fvf.camera, sae.max as date
      from autos_starts_and_ends_time sae
               join fvf_not_active_cams fvf
                    on sae.grz = fvf.grz and sae.max = fvf.date) starts
group by grz;

create table autos_starts_and_ends as
select starts.grz    as grz,
       starts.camera as start_cam,
       starts.date   as start_time,
       ends.camera   as end_cam,
       ends.date     as end_time
from autos_starts starts
         left outer join autos_ends ends
                         on starts.grz = ends.grz;

create table not_active_cameras as
select distinct fnac.camera, fvf.lat, fvf.lon
from fvf_not_active_cams fnac
         left outer join (select distinct camera, lat, lon from fvf) fvf
                         on fnac.camera = fvf.camera;
