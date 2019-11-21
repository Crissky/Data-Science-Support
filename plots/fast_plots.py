def groupPlotBar(data_values, legends, label_groups, x_name="X Axis", y_name="Y Axis", title='title', legend_loc='lower left', barWidth=0.25):
  import numpy as np
  import matplotlib.pyplot as plt

  num_plot = len( data_values[0] )
  num_bar = len( data_values )

  step = (num_bar+1) * barWidth
  end = step * num_plot
  first_x_bar_loc = np.arange(0, end, step)
  x_bar_locs = [first_x_bar_loc]

  # Set position of bar on X axis
  for index in range(0, num_bar-1):
    x_bar_locs.append( [x + barWidth for x in x_bar_locs[index]])
  
  # Make the plot
  for index in range(num_bar):
    x_bar_loc = x_bar_locs[index]
    data_value = data_values[index]
    legend = legends[index]

    plt.bar(x_bar_loc, data_value, width=barWidth, edgecolor='white', label=legend)

  plt.xlabel(x_name, fontweight='bold')
  plt.ylabel(y_name, fontweight='bold')
  plt.title(title)
  
  # Add xticks on the middle of the group bars
  if(num_bar%2 != 0):
    plt.xticks([r + barWidth for r in range(num_plot)], label_groups)
  else:
    pos_label_groups = x_bar_locs[(num_bar//2)]
    plt.xticks([r-(barWidth/2) for r in pos_label_groups ], label_groups)

  plt.legend(loc=legend_loc)
  plt.show()

if(__name__ == '__main__'):
  data = ( [0.82, 0.88], [0.89, 0.95], [0.88, 0.93], [0.96, 0.99] )
  legends = ['Imagem normal', 'Imagem sem fundo', 'Imagem Escala de Cinza', 'Imagem Escala de Cinza sem fundo']
  labels = ['Sem Peso', 'Com Peso']

  groupPlotBar(data_values=data, legends=legends, label_groups=labels, y_name='Macro AVG', x_name="", title='Images Grey Scale')
