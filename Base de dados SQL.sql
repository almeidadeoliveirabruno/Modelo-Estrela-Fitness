create database FitnessTracker
use FitnessTracker

DELETE FROM DIM_local
CREATE TABLE DIM_local(
	IDlocal INT PRIMARY KEY,
	weather_conditions VARCHAR(10),
	location VARCHAR(10)
)

DELETE FROM DIM_pessoa
CREATE TABLE DIM_pessoa(
	IDpessoa INT PRIMARY KEY,
	workout_type VARCHAR(15),
	mood VARCHAR(15)
)


DELETE FROM DIM_DATE
CREATE TABLE DIM_DATE(
	DATE DATE PRIMARY KEY,
	YEAR INT NOT NULL,            
    MONTH TINYINT NOT NULL,       
    DAY TINYINT NOT NULL,         
    QUARTER TINYINT NOT NULL      
)

delete from FATO
CREATE TABLE FATO(
	SK INT PRIMARY KEY,
	user_id INT ,
	DATE DATE,
	STEPS INT,
	calories_burned DECIMAL(7,2),
	distance_km DECIMAL(5,2),
	active_minutes INT,
	sleep_hours DECIMAL(5,2),
	heart_rate_avg DECIMAL(6,2),
	IDpessoa INT,
	IDlocal INT,
	FOREIGN KEY (IDpessoa) REFERENCES DIM_pessoa,
	FOREIGN KEY (IDlocal) REFERENCES DIM_local,
	FOREIGN KEY (DATE) REFERENCES DIM_date
)

select * from DIM_DATE
SELECT * FROM DIM_pessoa
SELECT * FROM FATO
SELECT * FROM DIM_local

select mood, COUNT(FATO.SK) from DIM_pessoa
join FATO on DIM_pessoa.IDpessoa = FATO.IDpessoa
GROUP BY mood 
ORDER BY COUNT(FATO.SK) DESC

select avg(calories_burned), DIM_pessoa.workout_type FROM FATO
JOIN DIM_pessoa ON FATO.IDpessoa = DIM_pessoa.IDpessoa
GROUP BY workout_type ORDER BY avg(calories_burned) desc