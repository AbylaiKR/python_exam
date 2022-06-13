from django import template
from ..models import Comment, Genre,Rating

register = template.Library()


@register.simple_tag()
def get_genre():
    return Genre.objects.all()


@register.simple_tag()
def get_rating_by_id(id):
    ratings = Rating.objects.all()
    score = 0
    count = 0
    for rating in ratings:
        if rating.movie_id == id:
            score = score + rating.rating
            count = count + 1
    if score == 0:
        return 0
    result = score / count
    return round(result, 1)
