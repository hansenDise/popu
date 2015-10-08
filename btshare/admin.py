from django.contrib import admin

# Register your models here.

from .models import Occupation
from .models import Category
from .models import Genres
from .models import Movie
from .models import People
from .models import Torrent
from .models import Subtitle
from .models import Trailer
from .models import Movie_Genres
from .models import Movie_People


admin.site.register(Occupation)
admin.site.register(Category)
admin.site.register(Genres)
admin.site.register(Movie)
admin.site.register(People)
admin.site.register(Torrent)
admin.site.register(Subtitle)
admin.site.register(Trailer)
admin.site.register(Movie_Genres)
admin.site.register(Movie_People)