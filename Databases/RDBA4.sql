
SELECT * FROM BRANCH;
SELECT * FROM STAFF;
SELECT * FROM PROPERTY;
SELECT * FROM RENTER;
SELECT * FROM OWNER;
SELECT * FROM VIEWING;

SELECT * FROM RENTER;
SELECT * FROM STAFF;
SELECT * FROM OWNER;


--q1

--staff name that is a renter and an owner (same name, same person)
--staff renter owner

SELECT STAFF.FName, STAFF.LName

FROM STAFF,RENTER,OWNER

WHERE ((STAFF.FName = RENTER.FName) AND (STAFF.FName = OWNER.FName)) AND ((STAFF.LName = RENTER.LName) AND (STAFF.LName = OWNER.LName));




--q2

--all staff names living in cork and working in dublin
--Staff Renter Branch

-- STAFF names from STAFF where the staff numbers 

SELECT STAFF.FName, STAFF.LName, BRANCH.City, PROPERTY.City

FROM STAFF, PROPERTY, BRANCH

WHERE BRANCH.City ='Dublin' AND PROPERTY.City = 'Cork' AND ((STAFF.BranchNo = PROPERTY.BranchNo) AND (STAFF.BranchNo = BRANCH.BranchNo));



--q3

--names and numbers of renters living in the same property (Different names, same address)

--RENTER names and numbers
--WHERE address is the same 

SELECT RENTER1.FName, RENTER1.LName, RENTER1.TelNo
FROM RENTER AS RENTER1, RENTER AS RENTER2
WHERE RENTER1.Address=RENTER2.Address AND RENTER1.FName<RENTER2.FName;


--q4

--find telephone numbers of renters who used damp when viewing a property PA3

SELECT RENTER.TelNo
FROM RENTER,VIEWING
WHERE (RENTER.RenterNo = VIEWING.RenterNo) AND (VIEWING.Comment LIKE'%damp%') AND (VIEWING.PropertyNo = 'PA3');


--q5

--find telephone numbers of any renter any property in cork 

SELECT RENTER.TelNo, VIEWING.Comment
FROM RENTER,VIEWING,PROPERTY
WHERE (VIEWING.PropertyNo = PROPERTY.PropertyNo) AND (VIEWING.Comment LIKE'%damp%') AND (PROPERTY.City = 'Cork');


--q6

--all names of owners who own more than one property

SELECT OWNER.FName, OWNER.LName
FROM OWNER,PROPERTY
WHERE OWNER.OwnerNo = PROPERTY.OwnerNo 
AND NOT (SELECT DISTINCT PROPERTY.OwnerNo 
        FROM PROPERTY);
