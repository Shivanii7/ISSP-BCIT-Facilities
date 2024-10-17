CREATE DATABASE IF NOT EXISTS FileManagement;
USE FileManagement;

CREATE TABLE IF NOT EXISTS Subfolders (
    SubfolderID INT AUTO_INCREMENT PRIMARY KEY,
    SubfolderName VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectName VARCHAR(255) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE
);

CREATE TABLE IF NOT EXISTS Files (
    FileID INT AUTO_INCREMENT PRIMARY KEY,
    FileName VARCHAR(255) NOT NULL,
    FilePath VARCHAR(255) NOT NULL,
    FileType VARCHAR(50) NOT NULL,
    SubfolderID INT,
    ProjectID INT,
    FOREIGN KEY (SubfolderID) REFERENCES Subfolders(SubfolderID) ON DELETE CASCADE,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,
    TagName VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS FileTags (
    FileTagID INT AUTO_INCREMENT PRIMARY KEY,
    FileID INT,
    TagID INT,
    FOREIGN KEY (FileID) REFERENCES Files(FileID) ON DELETE CASCADE,
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE
);

INSERT INTO Subfolders(SubfolderName) VALUES
('Approval for Expenditure (AFE)'),
('Cash Flow Projection'),
('Invoice'),
('Certificate of Substantial Completion'),
('Fire Plan'),
('Lessons Learned'),
('Lien Search'),
('Record CAD Files'),
('Record O&M Manual'),
('Record PDF Files'),
('Consultant Contracts'),
('Contractor Contracts'),
('Drawings'),
('Photos & Videos'),
('Email Correspondence'),
('Stakeholder Registry'),
('Contractor Supplied Items'),
('Owner Supplied Items'),
('Media Files'),
('Construction Meetings'),
('Design Meetings'),
('Kick Off Meeting'),
('Stakeholder Engagement Meetings'),
('Building Permit'),
('Environmental Permit'),
('Inspection Reports'),
('PPA (Permit to Proceed with Application)'),
('Consultant Procurement'),
('Contractor Procurement'),
('FF&E Procurement'),
('Deficiency Reports'),
('Design Team Reports'),
('Field Reviews'),
('Hazmat Reports'),
('Monthly Reports'),
('QS Reports'),
('Move-In Schedule'),
('Permit Schedule'),
('Project Schedule'),
('Access Card Requests'),
('Network Access Requests'),
('Physical Access Requests'),
('Parking Passes'),
('Safety Request Forms'),
('Risk Assessments'),
('Project Charter'),
('Existing As-Built Drawings'),
('Previous Studies'),
('BC Hydro Correspondence'),
('Fortis Correspondence'),
('Municipality Correspondence');

INSERT INTO Tags(TagName) VALUES 
('Geotechnical'),
('Electrical'),
('Masonry'),
('Concrete'),
('Furnishing'),
('Plumbing'),
('Heating, Ventilation, Air Conditioning')
;