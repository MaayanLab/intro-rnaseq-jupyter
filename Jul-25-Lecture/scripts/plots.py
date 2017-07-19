import plotly.graph_objs as go
from plotly.offline import iplot
import numpy as np

def plot_3d_scatter(x,y,z,text='', title='', color_by=None, xlab='x', ylab='y', zlab='z', colors=["#3366cc", "#dc3912", "#ff9900", "#109618", "#990099", "#0099c6", "#dd4477", "#66aa00", "#b82e2e", "#316395", "#994499", "#22aa99", "#aaaa11", "#6633cc", "#e67300", "#8b0707", "#651067", "#329262", "#5574a6", "#3b3eac"]):

	# Plot it
	if str(color_by) == 'None':
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
	else:
		data = []
		for index, term in enumerate(set(color_by)):
			indices = [i for i,e in enumerate(color_by) if e == term]
			data.append(go.Scatter3d(
				x=[x[i] for i in indices],
				y=[y[i] for i in indices],
				z=[z[i] for i in indices],
				mode='markers',
				text=[text[i] if type(text) == list else '' for i in indices],
				name=term,
				marker=dict(
					size=15,
					opacity=0.8,
					color=colors[index]
				)
			))


	go.layout = go.Layout(
		title=title,
		margin=dict(
			l=0,
			r=0,
			b=0,
			t=50
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


def plot_2d_scatter(x,y,text='', title='', xlab='x', ylab='y',color_by=None,colors=["#3366cc", "#dc3912", "#ff9900", "#109618", "#990099", "#0099c6", "#dd4477", "#66aa00", "#b82e2e", "#316395", "#994499", "#22aa99", "#aaaa11", "#6633cc", "#e67300", "#8b0707", "#651067", "#329262", "#5574a6", "#3b3eac"]):

	if str(color_by) == 'None':
		trace = go.Scattergl(
			x=x,
			y=y,
			mode='markers',
			text=text,
			marker=dict(
				size=12,
				opacity=0.8,
				color='black'
			)
		)
		data = [trace]
	else:
		data = []
		for index, term in enumerate(set(color_by)):
			indices = [i for i,e in enumerate(color_by) if e == term]
			data.append(go.Scatter(
				x=[x[i] for i in indices],
				y=[y[i] for i in indices],
				mode='markers',
				text=[text[i] if type(text) == list else '' for i in indices],
				name=term,
				marker=dict(
					size=15,
					opacity=0.8,
					color=colors[index]
				)
			))

	go.layout = go.Layout(
		title=title,
		hovermode='closest',
		xaxis = dict(
			title = xlab
		),
		yaxis = dict(
			title = ylab
		)
	)
	fig = go.Figure(data=data, layout=go.layout)
	return iplot(fig)

def get_clustergrammer_cats(sample_metadata_dataframe):
	return [{'title': index, 'cats': {value: rowData[rowData==value].index.tolist() for value in set(rowData.values)}} for index, rowData in sample_metadata_dataframe.T.iterrows()]