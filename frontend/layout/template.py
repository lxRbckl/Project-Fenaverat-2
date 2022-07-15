# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from backend.resource import hardGetData # <
from frontend.layout.body import bodyFunction
from backend.resource import getData, application

# >


# global <
gData = hardGetData()

# >


def templateFunction(pData: dict = gData):
    '''  '''

    return dbc.Container(

         id = 'templateContainerId',
        children = [

            # location <
            # interval <
            dcc.Location(id = 'locationId'),
            dcc.Interval(

                n_intervals = 0,
                id = 'intervalId',
                interval = (60000 * 60)

            ),

            # >

            bodyFunction(pData = gData)

        ]

    )


@application.callback(

    Output('intervalId', 'n_intervals'),
    Input('intervalId', 'n_intervals')

)
def intervalCallback(pInterval: int):
    '''  '''

    # get data <
    # update data <
    global gData
    gData = hardGetData()

    # >

    # return bodyFunction(pData = gData)


# @application.callback(
#
#     Output('contentRowId', 'children'),
#     Input('locationId', 'pathname')
#
# )
# def locationCallback(pPathname: str):
#     '''  '''
#
#     return {
#
#         '/' : 0,
#         '/aboutMe' : 1,
#         '/myServer' : 2,
#         '/myProject' : 3,
#         f'{pPathname[1:]}' : 4
#
#     }[pPathname](gData, pPathname)
