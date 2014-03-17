import numpy as siffror

def stenosv(sten,sax,pase):
	
	sten=sten*siffror.random.normal(10)
	sax=sax*siffror.random.normal(10)
	pase=pase*siffror.random.normal(10)
	
	siffror.floor(sten)
	siffror.floor(sax)
	siffror.floor(pase)

	if(sten<sax):
		if(sten<pase):
			return "sten" 
		else:
			return "pase" 
	if(sax<sten):
		if(sax<pase):
			return "sax" 
		else: 
			return "pase" 
	if(pase<sten):
		if(pase<sax):
			return "pase" 
		else:
			return "sax" 


print stenosv(100,100,100)
