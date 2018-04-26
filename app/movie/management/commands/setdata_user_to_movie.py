import random

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, CommandError

from ...models import Movie, UserToMovie

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_list = [
            [True, False, None, '', ],
            [False, True, '1.0', 'Never see this movie.', ],
            [False, True, '1.5', '그냥 재미 없어요!!', ],
            [False, True, '2.0', 'not bad', ],
            [False, True, '2.5', '다시 보고 싶지 않아요 ㅋ', ],
            [False, True, '3.0', '그저 그런 영화입니다.~', ],
            [False, True, '3.5', '배우의 연기력만 좋아요', ],
            [False, True, '4.0', 'great movie~', ],
            [False, True, '4.5', '최고의 영화입니다.', ],
            [False, True, '5.0', '인생영화! 내일 또 봐야지 ㅎㅎ', ],
        ]
        movie_list = Movie.objects.all()

        user_list = [14, 13, 12]
        # user_list = User.objects.all().order_by('-pk')[:3]

        for user in user_list:
            set_user = User.objects.get(pk=user)
            for movie in movie_list:
                print('-' * 70)
                print(f'movie >> {movie}')
                data = random.choice(data_list)
                print(f'data >> {data}')
                obj, created = UserToMovie.objects.get_or_create(
                    user=set_user,
                    movie=movie,
                    defaults={
                        'user_want_movie': data[0],
                        'user_watched_movie': data[1],
                        'rating': data[2],
                        'comment': data[3],
                    },
                )
                Movie.objects.update_rating_avg(id=movie.pk)
                print(f'obj >> {obj}')
                print(f'created >> {created}')
                print('-'*70)

        self.stdout.write(self.style.SUCCESS('Success: setdata_user_to_movie command'))
