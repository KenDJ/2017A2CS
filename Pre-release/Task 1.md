#Ken Su

#Task 1

##1.1

###JSP's initial purpose was to make COBOL batch file processing programs easier to modify and maintain, but the method can be used to design programs for any programming language that has structured control constructs, languages such as C, Java and Perl. 
###JSP structures programs and data using only sequences, iterations and selections, so they essentially create programs that are parsers for regular expressions which simultaneously match the program's input and output data streams. This is claimed to be more straightforward than with other structured programming methods.

##1.2

###
* means repitition - indicating repeated components
¡ãmeans selection, where only one component is chosen

##1.3

###

```pseudocode
WHILE NumberOfStaff >= 0:
	CALL ReadSalary()
	IF Salary > 50:
		THEN
			IF Salary >= 90:
				THEN 
					Role = 'Project Manager'
				ELSE
					Role = 'Lead Developer'
			ENDIF
		ELSE
			Role = 'Manager'
	ENDIF
ENDWHILE
```
##1.4

###
                         Salary > 50
		False				TRUE
		  |                               |
	Assign Manager                     Salary >=90
						|
				False                      TRUE
				  |                          |
		           Salary >=70		     Assign Project Manager
				|
			False       TRUE
			   |          |
		Lead Developer     Consultant

##1.5

###

```pseudocode
IF Salary >= 90:
	THEN
		Role = Project Manager
	ELSE
		IF Salary >= 70:
			THEN
				Role = Consultant
			ELSE
				Role = Lead Developer   
		ENDIF
ENDIF
```

##1.6

```python
def determinerole(salary):
	if salary >= 50:
		if salary >= 70:
			if salary >= 90:
				return("project manager")
			else:
				return("consultant")
		else:
			return("Lead Developer")
	else:
		return("manager")
```

                 
					






