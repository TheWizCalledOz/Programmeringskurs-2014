class Pistol():
	def __init__(self):
		print "You picked up a gun!"
		self.bullets=0

	def shoot(self):
		if self.bullets>0:
			self.bullets=self.bullets-1
			print "BANG!"
		else:
			print "You have no bullets left"


	def reload(self):
		self.bullets=0
		self.bullets=self.bullets+8
		print "RELOADING!"

	def show(self):
		return self.bullets

minpistol=Pistol()

minpistol.reload()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.reload()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.shoot()
minpistol.show()

print "You have", minpistol.bullets, "bullets left"
