# Hospital-Database-School
Project in Python

This Project is about the automation of basic Hospital Management. It can be scaled to be used in any hospital, clinic for maintaining patient details and their results. Apart from basic patient’s information, the details include the admission and discharge dates, doctor assigned and the corresponding departments, and follow-up details.
The project Hospital Database Management is for computerizing the working in a hospital from the admission of a patient up to their discharge and further follow-up. The database takes care of all the requirements of an average hospital and is capable to provide easy and effective storage of information related to patients that come up to the hospital.
It can be effectively used by the hospital nurses and receptionists to locate and store patient details with accessibility.

Modules
A module is a python file that has only definitions of variables, functions and classes. A module name is a filename with the .py extension. A module can contain executable statements as well as function definitions.
1.	PICKLE Module
The pickle module implements a fundamental, but also a powerful algorithm for serializing and de-serializing a python object structure. The object structure could be a variable, instance of a class or a list, dictionary or tuple. Pickling is just serialization that is, putting data into a form that can be stored in a file and retrieved later.
●	Pickling- It is a process where a python object hierarchy is converted into a byte stream.
●	Unpickling- It is the inverse operation of pickling, where a byte stream is converted back into an object hierarchy.
o	dump()- This function of pickle module returns the pickled representation of the object as a byte stream, and writes the stream into the file.
o	load()- This function of pickle module reads a pickled object of byte stream of an opened file and returns back into an object hierarchy. The returned object could be a variable, instance of a class, or a list, or tuple.
2.	Os  Module
Python OS module is used to perform task such as finding the name of present working directory , changing current working directory, checking if certain files or directories exist at a location, creating new directories, deleting existing files or directories, walking through a directory and performing operations on every file in the directory that satisfies some user-defined criteria, etc.
o	path.isfile(filename)- This function returns true if the given path is an existing regular file and return false if it doesn’t exist.
3.	Datetime
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation. For related functionality, see also the time and calendar modules.
o	datetime.now()- Returns the current local date and time.

VARIABLES
1.	p_id
o	Datatype: Integer
o	Maintains the uniqueness of every record and stores the admission id of the patients.
2.	p_name
o	Datatype: String
o	Stores the name of the patients.
3.	p_gen
o	Datatype: String
o	Stores the gender of the patients.
4.	p_num
o	Datatype: string
o	Stores the contact number of the patients.
5.	p_dob
o	Datatype: String
o	Stores the date of birth of the patients.

6.	p_rdate
o	Datatype: String
o	Stores the admission date.
7.	p_ddate
o	Datatype: String
o	Stores the tentative discharge date.
8.	p_doc
o	Datatype: String
o	Stores the doctor assigned to the patient
9.	 dept
o	Datatype: String
o	Stores the department involved with the particular patient.

10.	 comments
o	Datatype: String
o	Stores the follow-up comments for the particular patient.

11.	 feedback
o	Datatype: String
o	Stores the feedback given by the particular patient.

METHODS
Class Methods

1.	input(): This method displays a prompt and inputs all the instance variables.

2.	disp(): It returns all the instance variables of the class.

3.	validdate(): It takes a date as an argument and checks for its validity. Used to check the birth, admission and discharge dates of the patients.

4.	doc_assign(): It asks the user for the department involved and shows a list of the available doctors for the corresponding department. It then assigns the doctor as entered from the list.

 

Methods defined outside the Class

5.	create(): This method opens a binary file and calls the method- “input()” and dumps all the entered details into the binary file.

6.	add(): This method opens a binary file and calls the method- “input()” and appends all the entered details into the binary file.

7.	modify(): This method takes ID as input and searches it in the binary file. If the ID exists then it asks for new patient details and changes them according to the details entered by the end user.

8.	follow_up(): This method takes ID as input and searches it in the binary file to display the corresponding Patient’s previous records and details. It is used for the follow up of the patients and asks for special comments on their record, if any from the doctor and the patient’s feedback too.

9.	display(): This method displays all the details of the binary file. 

10.	search(): This method takes ID as input and searches it in the binary file. If the ID exists then it displays the particular patient’s details.

11.	delete(): This method takes name as input and searches it in the binary file. If the name exist then deletes the booking.

12. review(): This method displays all the patients who are to be discharged on the current day and asks whether they have to be discharged yet or not. 
	
Files Generated
Binary Files: Files in python are interpreted as a sequence or stream of bytes stored on some storage media. A file that contains non-readable characters in binary code is called a binary file.

Two binary files are used or generated in this project, which are:
1.	hop.dat: It is a binary file that stores all the patient’s records; namely: ID, Name, Date of Birth, Gender, Admission Date, Discharge Date, Contact Number, Department Involved and the Assigned Doctor for every patient admitted in the Seattle Grace Mercy West Hospital.

2.	temp.dat: It is a binary file generated at the time of modification of any patient’s record or during their discharge. Any changes in the data are made by storing a copy of the records along with the changes done in ‘temp.dat’ which is renamed as ‘hop.dat’ after the latter is deleted.

Text Files Generated
The project also contains one text file.
no.txt: Used for the generation of unique patient ID on each patient admission.
