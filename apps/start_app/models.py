from django.db import models

class new_a:
	key = models.IntegerField(max_length = 255)
	name = models.CharField(max_length = 255)
	age = models.IntegerField(max_length = 11)
	sex = models.CharField(max_length = 255)

	class Meta:
		db_table = "new_a"

class user:
	name = models.CharField(max_length = 255)
	id = models.IntegerField(max_length = 11)
	age = models.IntegerField(max_length = 11)
	json = models.CharField(max_length = 255)
	delete_time = models.CharField(max_length = 12)

	class Meta:
		db_table = "user"
