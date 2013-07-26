from matplotlib import pyplot

figure = pyplot.figure()
figure.clf()
axes = figure.add_subplot(111)
pyplot.axis('off')
pyplot.axis('equal')

pointsx = [1, 2, 3, 1, 2, 3, 1, 2, 3]
pointsy = [1, 1, 1, 2, 2, 2, 3, 3, 3]
pyplot.scatter(pointsx, pointsy)

pyplot.arrow(1, 1, 1, 1, head_width=0.05, head_length=0.1, length_includes_head=True)
pyplot.arrow(2, 2, -1, 0, head_width=0.05, head_length=0.1, length_includes_head=True)

figure.savefig('lol.png')
