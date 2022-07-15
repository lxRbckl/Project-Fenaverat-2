# import <
from os import path
from dash import Dash
from requests import get
from github import Github
from lxRbckl import jsonLoad # <
from lxRbckl import githubGet
from datetime import datetime as dt
from dash_bootstrap_components import themes

# >


# global <
gPath = path.realpath(__file__)
gDirectory = '/'.join(gPath.split('/')[:-2])
githubToken = ''
application = Dash(

    server = True,
    suppress_callback_exceptions = True,
    external_stylesheets = [themes.GRID]

)
gBootLink = {

    'aboutMeData' : '',
    'myProjectData' : '',
    'myServerData' : '',

    'feedData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/master/backend/data/feed.json',
    'bodyData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/master/backend/data/body.json',
    'boardData' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/master/backend/data/board.json',
    'bodyStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/master/frontend/style/body.json',
    'templateStyle' : 'https://raw.githubusercontent.com/lxRbckl/Project-Fenaverat-2/master/frontend/style/template.json'

}

# >


def hardGetData(): # <
    '''  '''

    return {

        'bodyData' : jsonLoad(pFile = f'{gDirectory}/backend/data/body.json'),
        'feedData' : jsonLoad(pFile = f'{gDirectory}/backend/data/feed.json'),
        'boardData' : jsonLoad(pFile = f'{gDirectory}/backend/data/board.json'),
        'bodyStyle' : jsonLoad(pFile = f'{gDirectory}/frontend/style/body.json'),
        'feedStyle' : jsonLoad(pFile = f'{gDirectory}/frontend/style/feed.json'),
        'boardStyle' : jsonLoad(pFile = f'{gDirectory}/frontend/style/board.json'),
        'templateStyle' : jsonLoad(pFile = f'{gDirectory}/frontend/style/template.json')

    }


def getData(pGithub = Github(githubToken)):
    '''  '''

    return {

        **{k : get(v).json() for k, v in gBootLink.items()},
        **{

            r.full_name : {

                'topic' : r.get_topics(),
                'language' : r.get_languages(),
                'link' : f'https://github.com/{r.full_name}',
                'update' : dt.strptime(str(r.pushed_at).split(' ')[0], '%Y-%m-%d').strftime('%B %d %Y'),
                'about' : githubGet(

                    pGithub = pGithub,
                    pFile = 'about.json',
                    pRepository = r.full_name

                )

            }

        for r in [pGithub.get_user(u).get_repos() for u in get(gBootLink['']).json()['']]}

    }
