-- CREATE TABLE BRANCH (BranchNo, Street, Area, City, TelNo);
-- CREATE TABLE STAFF(StaffNo, FName, LName, Address, TelNo, Job, Gender, Salary, BranchNo);
-- CREATE TABLE PROPERTY(PropertyNo, Street, Area, City, Type, Rooms, Rent, OwnerNo, StaffNo, BranchNo);
-- CREATE TABLE RENTER(RenterNo, FName, LName, Address, TelNo, TypePreference, MaxRent);
-- CREATE TABLE OWNER(OwnerNo, FName, LName, Address, TelNo);
-- CREATE TABLE VIEWING(RenterNo, PropertyNo, Date, Comment);


INSERT INTO BRANCH (BranchNo, Street, Area, City, TelNo) VALUES ('B2', 'South Mall', 'city centre', 'Dublin', '021-123-4567');
INSERT INTO STAFF (StaffNo, FName, LName, Address, TelNo, Job, Gender, Salary, BranchNo) VALUES ('SL33', 'Peter', 'Jones', '10 New St, Ballincollig','021-765-4321', 'Assistant', 'M', 6000, 'Beee2');
INSERT INTO PROPERTY (PropertyNo, Street, Area, City, Type, Rooms, Rent, OwnerNo, StaffNo, BranchNo) VALUES ('PA14', 'Old St', 'Elligyon', 'Cork', 'Apartment', 3, 450,'w00d', 'SL33', 'Beee2');

INSERT INTO RENTER(RenterNo, FName, LName, Address, TelNo, TypePreference, MaxRent) VALUES ('CR76', 'Fart', 'Jones', '8 Barrack St Cork', '021-333-4444','house', 550);
INSERT INTO OWNER(OwnerNo, FName, LName, Address, TelNo) VALUES ('w00d', 'Peter', 'Jones', '1 Main St, Dublin','01-222-3333');
INSERT INTO VIEWING(RenterNo, PropertyNo, Date, Comment) VALUES ('CR76', 'PA14', '10-04-2000', 'real damp');

SELECT * FROM BRANCH;
SELECT * FROM STAFF;
SELECT * FROM PROPERTY;
SELECT * FROM RENTER;
SELECT * FROM OWNER;
SELECT * FROM VIEWING;


-- Assignment 2

--q1

-- SELECT DISTINCT Job 
-- FROM STAFF
-- WHERE Salary>15000;

--q2

-- SELECT Comment, Date
-- FROM VIEWING 
-- WHERE PropertyNo = 'PG28';

--q3

-- SELECT StaffNo,FName,LName
-- FROM STAFF
-- WHERE (Job = 'Manager' or Job='Deputy') AND BranchNo = 'B7'


--q4

-- SELECT PropertyNo, Street, Area, City
-- FROM PROPERTY
-- WHERE (type ='Apartment' OR type='House') AND BranchNo = 'B3' AND Rooms >3;


--q5

-- SELECT FName, LName, BranchNo
-- FROM STAFF
-- WHERE Job='Assistant' AND Salary<10000
-- ORDER BY LName ASC;

--q6


-- SELECT FName, LName, Gender, Job
-- FROM STAFF 
-- WHERE Salary>20000;


--q7

-- SELECT FName AS Forename, LName AS Surname, Job, Salary
-- FROM STAFF 
-- WHERE Gender='M';


--q8 

-- SELECT Street, Area, City, Rent
-- FROM PROPERTY
-- WHERE Rooms = 3 AND Type= 'Apartment' AND BranchNo='B2' AND (Rent BETWEEN 400 AND 500);
