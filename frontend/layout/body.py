# import <
from dash import dcc, html
import dash_bootstrap_components as dbc

# >


# global <


# >


def bodyFunction(pData: dict):
    '''  '''

    return dbc.Container(

        fluid = True,
        id = 'bodyContainerId',
        style = dict(

            **pData['bodyStyle']['bodyContainerStyle'],
            backgroundImage = pData['bodyData']['bodyContainerBackgroundImage']

        ),
        children = [

            # header <
            dbc.Row(

                justify = 'center',
                style = dict(

                    **pData['bodyStyle']['headerRowStyle'],
                    border = pData['templateStyle']['gBorderBlack'],
                    borderRadius = pData['templateStyle']['gBorderRadius'],
                    backdropFilter = pData['templateStyle']['gBackdropFilter'],
                    backgroundColor = pData['templateStyle']['gColorTransparentBlack']

                ),
                children = html.Img(

                    src = pData['bodyData']['headerImgSrc'],
                    style = pData['bodyStyle']['headerImgStyle']

                )

            ),

            # >

            # menu <
            dbc.Row(

                align = 'end',
                justify = 'evenly',
                style = dict(

                    **pData['bodyStyle']['menuRowStyle'],
                    border = pData['templateStyle']['gBorderBlack'],
                    borderRadius = pData['templateStyle']['gBorderRadius'],
                    backdropFilter = pData['templateStyle']['gBackdropFilter'],
                    backgroundColor = pData['templateStyle']['gColorTransparentBlack']

                ),
                children = [

                    dbc.Col(

                        width = 'auto',
                        children = dbc.Button(

                            id = k,
                            href = k,
                            children = html.Img(

                                src = v,
                                style = pData['bodyStyle']['menuImgStyle']

                            )

                        )

                    )

                for k, v in pData['bodyData']['menuRowChildren'].items()]

            ),

            # >

            # content <
            dbc.Row(

                justify = 'center',
                id = 'contentRowId'

            ),

            # >

            # footer <
            dbc.Row(

                justify = 'evenly',
                style = dict(

                    **pData['bodyStyle']['footerRowStyle'],
                    border = pData['templateStyle']['gBorderBlack'],
                    borderRadius = pData['templateStyle']['gBorderRadius'],
                    backdropFilter = pData['templateStyle']['gBackdropFilter'],
                    backgroundColor = pData['templateStyle']['gColorTransparentBlack']

                ),
                children = [

                    dbc.Col(

                        width = 'auto',
                        children = html.A(

                            href = k,
                            target = '_blank',
                            children = html.Img(

                                src = v,
                                style = pData['bodyStyle']['footerImgStyle']

                            )

                        )

                    )

                for k, v in pData['bodyData']['footerRowChildren'].items()]

            )

            # >

        ]

    )
