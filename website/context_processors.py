from django.urls import reverse

def navbar_context(request):
    user = request.user
    
    def get_nav_items():
        common_items = [
            {'title': 'Home', 'url': reverse('public:index')},
        ]
        
        if user.is_authenticated:
            pass
            # if user.groups.filter(name='Wrestlers').exists():
            #     return common_items + [
            #         {'title': 'Videos', 'url': reverse('wrestling_media:wrestling_media')},
            #     ]
            # elif user.groups.filter(name='Coaches').exists():
            #     return common_items + [
            #         {'title': 'Videos', 'url': reverse('wrestling_media:wrestling_media')},
            #         {'title': 'Upload Videos', 'url': reverse('wrestling_media:create_video')},
            #     ]
            # elif user.groups.filter(name='Staff').exists():
            #     return common_items + [
            #         {'title': 'Videos', 'url': reverse('wrestling_media:wrestling_media')},
            #         {'title': 'Upload', 'url': reverse('wrestling_media:create_video')},
            #         {'title': 'Movies', 'url': reverse('movies:movies')},
            #         {'title': 'Up Movies', 'url': reverse('movies:create_movie')},
            #         {'title': 'Cookbook', 'url': reverse('cookbook:cookbook')},
            #     ]
            # elif user.groups.filter(name='Movies').exists():
            #     return common_items + [
            #         {'title': 'Movies', 'url': reverse('movies:movies')},
            #     ]
        
        # Default items for non-authenticated or non-specific users
        # return common_items + [
        #     {'title': 'Portfolio', 'url': reverse('portfolio:portfolio')},
        #     {'title': 'Videos', 'url': reverse('wrestling_media:wrestling_media')},
        #     {'title': 'Youtube Downloader', 'url': reverse('youtube_downloader:youtube_downloader')},
        #     {'title': 'Cookbook', 'url': reverse('cookbook:cookbook')},
        # ]

    return {
        'nav_items': get_nav_items(),
        'site_name': 'NameDrop',
        'site_name_url': reverse('public:index'),
    }
