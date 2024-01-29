CREATE TABLE IF NOT EXISTS employee(
	EmployeeId SERIAL PRIMARY KEY NOT NULL,
	FirstName varchar(20) NOT NULL,
	LastName varchar(30) NOT NULL,
	DepartmentId INT NULL REFERENCES department(DepartmentId)
);

CREATE TABLE IF NOT EXISTS department(
	DepartmentId SERIAL PRIMARY KEY NOT NULL,
	DepartmentName varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS income(
    IncomeId SERIAL PRIMARY KEY NOT NULL,
    EmployeeId INT NOT NULL REFERENCES employee(EmployeeId),
    Pay MONEY NOT NULL,
    Frequency VARCHAR(25) NULL
);

CREATE TABLE IF NOT EXISTS contact(
    ContactId SERIAL PRIMARY KEY NOT NULL,
    ContactNumber INT NOT NULL,
    Address VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(2) NOT NULL,
    ZipCode INT NULL,
    EmployeeId INT NOT NULL REFERENCES employee(employeeId)
);