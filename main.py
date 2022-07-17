# Project Fenaverat by Alex Arbuckle #


# import <
from os import path
from github import Github
from discord import Intents
from discord.ext import commands
from lxRbckl import jsonLoad, jsonDump, githubSet

# >


# global <
gPath = path.realpath(__file__).split('/')
gDirectory = '/'.join(gPath[:(len(gPath) - 1)])
githubToken = ''
fenaverat = commands.Bot(command_prefix = '', intents = Intents.all())
discordToken = ''

# >


async def setFunction(ctx, pKey: str, pAction: str, pValue: str, pData: dict):
    '''  '''

    pass


async def getFunction(ctx, pKey: str, pAction: str, pValue: str, pData: dict):
    '''  '''

    pass


async def delFunction(ctx, pKey: str, pAction: str, pValue: str, pData: dict):
    '''  '''

    pass


@commands.has_permissions(administrator = True)
@fenaverat.command(aliases = jsonLoad(pFile = f'{gDirectory}/setting.json')['aliases'])
async def commandFunction(ctx):
    '''  '''

    await {

        'set' : setFunction,
        'get' : getFunction,
        'delete' : deleteFunction

    }[ctx.invoked_with.lower()](

        ctx

    )


# main <
if (__name__ == '__main__'):

    pass

# >
