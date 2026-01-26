# zoomcamp-module-one-homework

Data-engineering-zoomcamp module 1 homework: Docker & SQL



Question 1. Understanding Docker images

Commands used:
    docker run -it --rm --entrypoint=bash python:3.13
    pip -V

Answer:
    pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)



Question 2. Understanding Docker networking and docker-compose

Answer:
    db:5432 Because cotainer name 'db' is also hostname and thanks to docker-compose both containers are in the same docker network, which bypasess traffic on external port 5433 and makes the traffic possible on the internal port 5432.

Question 3.

    SELECT COUNT(1) FROM public."green_tripdata_2025-11"
    WHERE  lpep_pickup_datetime >= '2025-11-01' AND lpep_pickup_datetime < '2025-12-01' AND trip_distance <= 1

Answer: 8007

Question 4.

    SELECT DATE(lpep_pickup_datetime), trip_distance FROM public."green_tripdata_2025-11"
    WHERE trip_distance < 100
    ORDER BY trip_distance DESC
    LIMIT 1

Answer: 2025-11-14

Question 5.

    SELECT "Zone", COUNT(*) as "trips_count" FROM public."green_tripdata_2025-11" as trip_data
    JOIN public.taxi_zone_lookup as zone_lookup ON zone_lookup."LocationID" = trip_data."PULocationID"
    WHERE DATE(lpep_pickup_datetime) = '2025-11-18'
    GROUP BY "Zone"
    ORDER BY "trips_count" DESC
    LIMIT 1

Answer: "East Harlem North"	434

Question 6.

    SELECT 
	    (SELECT "Zone" FROM public.taxi_zone_lookup as drop_lookup WHERE drop_lookup."LocationID" = trip_data."DOLocationID"), tip_amount
    FROM public."green_tripdata_2025-11" as trip_data
    JOIN public.taxi_zone_lookup as zone_lookup ON zone_lookup."LocationID" = trip_data."PULocationID"
    WHERE "Zone" = 'East Harlem North' AND DATE(lpep_pickup_datetime) BETWEEN '2025-11-01' AND '2025-11-30'
    ORDER BY tip_amount DESC
    LIMIT 1

Answer: "Yorkville West"	81.89
 