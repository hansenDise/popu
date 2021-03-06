﻿from django.db import models

# Create your models here.

#职业表
class Occupation(models.Model):
	occupationid = models.AutoField(primary_key=True)
	occupationname = models.CharField(max_length=20,null=True)
	
	def __unicode__(self):
		return self.occupationname
	
	class Meta():
		db_table = "Occupation"
	
#类别
class Category(models.Model):
	categoryid = models.AutoField(primary_key=True)
	categoryname = models.CharField(max_length=50,null=True)
	
	def __unicode__(self):
		return self.categoryname
	
	class Meta():
		db_table = "Category"
		
#类型
class Genres(models.Model):
	genresid = models.AutoField(primary_key=True)
	genresname = models.CharField(max_length=20,null=True)
	
	def __unicode__(self):
		return self.genresname
	
	class Meta():
		db_table = "Genres"
		
#电影
class Movie(models.Model):
	movieid = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	cn_title = models.CharField(max_length=200,null=True)
	year = models.IntegerField(null=True)
	imdburl = models.CharField(max_length=200,null=True)
	posterurl = models.CharField(max_length=300,null=True)
	runtime = models.IntegerField(null=True)
	plot = models.TextField(null=True)
	
	def __unicode__(self):
		return self.title
	
	class Meta():
		db_table = "Movie"
		
#人物
class People(models.Model):
	peopleid = models.AutoField(primary_key=True)
	occupationid = models.ForeignKey(Occupation,db_column='occupationid')
	firstname_en = models.CharField(max_length=30,null=True)
	middlename_en = models.CharField(max_length=30,null=True)
	lastname_en = models.CharField(max_length=30,null=True)
	# firstname_cn = models.CharField(max_length=30)
	# middlename_cn = models.CharField(max_length=30)
	# lastname_cn = models.CharField(max_length=30)
	borndate = models.DateField(null=True)
	summary = models.TextField(null=True)
	
	def __unicode__(self):
		return self.firstname_en
	
	class Meta():
		db_table = "People"
		
#种子
class Torrent(models.Model):
	torrentid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	categoryid = models.ForeignKey(Category,db_column='categoryid')
	name = models.CharField(max_length=200)
	shacode = models.CharField(max_length=40)
	torrenturl = models.CharField(max_length=300,null=True)
	magneturl = models.CharField(max_length=300,null=True)
	filesize = models.CharField(max_length=20,null=True)
	addedtime = models.DateTimeField()
	seeds = models.IntegerField(null=True)
	downloadcount = models.IntegerField(null=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta():
		db_table = "Torrent"

#截屏
class ScreenShot(models.Model):
	screenshotid = models.AutoField(primary_key=True)
	torrentid = models.ForeignKey(Torrent,db_column='torrentid')
	picurl = models.CharField(max_length=300,null=True)
	
	def __unicode__(self):
		return self.picurl
	
	class Meta():
		db_table="ScreenShot"

#字幕
class Subtitle(models.Model):
	subtitleid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	fileurl = models.CharField(max_length=300,null=True)
	
	class Meta():
		db_table = "Subtitle"

#预告片
class Trailer(models.Model):
	trailerid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	trailerurl = models.CharField(max_length=300,null=True)
	
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

class Movie_Torrent(models.Model):
	Movie_Torrentid = models.AutoField(primary_key=True)
	movieid = models.ForeignKey(Movie,db_column='movieid')
	torrentid = models.ForeignKey(Torrent,db_column='torrentid')
	
	class Meta():
		db_table = 'Movie_Torrent'


