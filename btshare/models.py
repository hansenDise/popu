from django.db import models

# Create your models here.

#职业表
class Occupation(models.Modle):
	occupationid = models.AutoField(primary_key=True)
	occupationname = models.CharField(max_length=20)
	
	class Meta():
		db_table = "Occupation"
	
#类别
class Category(models.Model):
	categoryid = models.AutoField(primary_key=True)
	categoryname = models.CharField(max_length=50)
	
	class Meta():
		db_table = "Category"
		
#类型
class Genres(models.Model):
	genresid = models.AutoField(primary_key=True)
	genresname = models.CharField(max_length=20)
	
	class Meta():
		db_table = "Genres"
		
#电影
class Movie(models.Model):
	movieid = models.AutoField(primary_key=True)
	categoryid = models.ForeignKey(Category)
	title = models.CharField(max_length=200)
	year = models.IntegerField()
	imdburl = models.CharField(max_length=200)
	posterurl = models.CharField(max_length=300)
	runtime = models.IntegerField()
	plot = models.TextField()
	
	class Meta():
		db_table = "Movie"
		
#人物
class People(models.Model):
	peopleid = models.AutoField(primary_key=True)
	occupationid = models.ForeignKey(Occupation)
	firstname_en = models.CharField(30)
	middlename_en = models.CharField(30)
	lastname_en = models.CharField(30)
	borndate = models.DateField()
	summary = models.TextField()
	
	class Meta():
		db_table = "People"
		
#种子
class Torrent(models.Model):
	torrentid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie)
	name = models.CharField(max_length=200)
	filesize = models.CharField(20)
	addedtime = models.DateTimeField()
	seeds = models.IntegerField()
	downloadcount = models.IntegerField()
	
	class Meta():
		db_table = "Torrent"

#截屏
class ScreenShot(models.Model):
	screenshotid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie)
	picurl = models.CharField(max_length=300)
	
	class Meta():
		db_table="ScreenShot"

#字幕
class Subtitle(models.Model):
	subtitleid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie)
	fileurl = models.CharField(max_length=300)
	
	class Meta():
		db_table = "Subtitle"

#预告片
class Trailer(models.Model):
	trailerid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie)
	trailerurl = models.CharField(max_length=300)
	
	class Meta():
		db_table = "Trailer"

#
class Movie_Genres(models.Model):
	movie_genresid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie)
	genresid = models.ForeignKey(Genres)
	
	class Meta():
		db_table = "Movie_Genres"
		
#
class Movie_People(models.Model):
	movie_peopleid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie)
	peopleid = models.ForeignKey(People)
	
	class Meta():
		db_table = "Movie_People"
		