from django.db import models

# Create your models here.

#职业表
class Occupation(models.Model):
	occupationid = models.AutoField(primary_key=True)
	occupationname = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.occupationname
	
	class Meta():
		db_table = "Occupation"
	
#类别
class Category(models.Model):
	categoryid = models.AutoField(primary_key=True)
	categoryname = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.categoryname
	
	class Meta():
		db_table = "Category"
		
#类型
class Genres(models.Model):
	genresid = models.AutoField(primary_key=True)
	genresname = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.genresname
	
	class Meta():
		db_table = "Genres"
		
#电影
class Movie(models.Model):
	movieid = models.AutoField(primary_key=True)
	categoryid = models.ForeignKey(Category,db_column='categoryid')
	title = models.CharField(max_length=200)
	year = models.IntegerField()
	imdburl = models.CharField(max_length=200)
	posterurl = models.CharField(max_length=300)
	runtime = models.IntegerField()
	plot = models.TextField()
	
	def __unicode__(self):
		return self.title
	
	class Meta():
		db_table = "Movie"
		
#人物
class People(models.Model):
	peopleid = models.AutoField(primary_key=True)
	occupationid = models.ForeignKey(Occupation,db_column='occupationid')
	firstname_en = models.CharField(max_length=30)
	middlename_en = models.CharField(max_length=30)
	lastname_en = models.CharField(max_length=30)
	firstname_cn = models.CharField(max_length=30)
	middlename_cn = models.CharField(max_length=30)
	lastname_cn = models.CharField(max_length=30)
	borndate = models.DateField()
	summary = models.TextField()
	
	def __unicode__(self):
		return self.firstname_en
	
	class Meta():
		db_table = "People"
		
#种子
class Torrent(models.Model):
	torrentid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	name = models.CharField(max_length=200)
	torrenturl = models.CharField(max_length=300)
	magneturl = models.CharField(max_length=300)
	filesize = models.CharField(max_length=20)
	addedtime = models.DateTimeField()
	seeds = models.IntegerField()
	downloadcount = models.IntegerField()
	
	def __unicode__(self):
		return self.name
	
	class Meta():
		db_table = "Torrent"

#截屏
class ScreenShot(models.Model):
	screenshotid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	picurl = models.CharField(max_length=300)
	
	class Meta():
		db_table="ScreenShot"

#字幕
class Subtitle(models.Model):
	subtitleid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	fileurl = models.CharField(max_length=300)
	
	class Meta():
		db_table = "Subtitle"

#预告片
class Trailer(models.Model):
	trailerid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	trailerurl = models.CharField(max_length=300)
	
	class Meta():
		db_table = "Trailer"

#
class Movie_Genres(models.Model):
	movie_genresid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	genresid = models.ForeignKey(Genres,db_column='genresid')
	
	class Meta():
		db_table = "Movie_Genres"
		
#
class Movie_People(models.Model):
	movie_peopleid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	peopleid = models.ForeignKey(People,db_column='peopleid')
	
	class Meta():
		db_table = "Movie_People"
		

