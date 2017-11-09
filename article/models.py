from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = "Article"

	Article_author = models.ForeignKey('Author',on_delete=models.SET_NULL, null=True )
	Article_title = models.CharField(max_length = 200, help_text="Enter title")
	Article_text = models.TextField()
	Article_date = models.DateTimeField()
	Article_likes = models.IntegerField(default=0)

	
class Comments(models.Model):
	class Meta():
		db_table = 'Comments'

	Comments_text = models.TextField()
	Comments_article = models.ForeignKey(Article)



class Author(User):
	pass
'''
	Author_First_Name = models.CharField(max_length = 60)
	Author_Last_Name = models.CharField(max_length = 60)
	#Author_Article = models.ForeignKey(Article)
'''
'''
	def get_absolute_url(self):
		"""
        Returns the url to access a particular author instance.
        """
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""
        String for representing the Model object.
        """
		return '%s, %s' % (self.Autohr_Last_Name, self.Author_First_Name)
'''