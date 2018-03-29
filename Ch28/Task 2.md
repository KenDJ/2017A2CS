###
IF A <> 0       	LDD A
    THEN		CMP #0
	B <- A		JPE ELSE
    ELSE		THEN: STO B
	B <- B ?C 1	JMP ENDIF
ENDIF			ELSE: LDD B
			DEC ACC
			STO B
			ENDIF:??????