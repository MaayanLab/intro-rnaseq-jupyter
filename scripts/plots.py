import plotly.graph_objs as go
from plotly.offline import iplot

def plot_3d_scatter(x,y,z,text='', title='', xlab='x', ylab='y', zlab='z'):

    # Plot it
    trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        text=text,
        marker=dict(
            size=12,
            opacity=0.8
        )
    )

    data = [trace]
    go.layout = go.Layout(
        title=title,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        ),
        scene = dict(
            xaxis = dict(
                title = xlab
            ),
            yaxis = dict(
                title = ylab
            ),
            zaxis = dict(
                title = zlab
            )
        )
    )
    fig = go.Figure(data=data, layout=go.layout)
    return iplot(fig)


def plot_2d_scatter(x,y,text='', title='', xlab='x', ylab='y'):

    # Plot it
    trace = go.Scattergl(
        x=x,
        y=y,
        mode='markers',
        text=text,
        marker=dict(
            size=12,
            opacity=0.8
        )
    )

    data = [trace]
    go.layout = go.Layout(
        title=title,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        ),
        scene = dict(
            xaxis = dict(
                title = xlab
            ),
            yaxis = dict(
                title = ylab
            )
        )
    )
    fig = go.Figure(data=data, layout=go.layout)
    return iplot(fig)