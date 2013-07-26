from matplotlib import pyplot
import logging
logging.basicConfig(level=logging.INFO)

def refresh():
    pyplot.figure()
    pyplot.axis('off')
    pyplot.axis('equal')

    from pattern.utils import grid
    pointsx = []
    pointsy = []
    for point in grid.points():
        pointsx.append(point[0])
        pointsy.append(point[1])
    pyplot.scatter(pointsx, pointsy)

def getPathName(path):
    return ''.join(['%d%d' % point for point in path])

def drawOne(path, outDir=None):
    refresh()
    for i in xrange(1, len(path)):
        x = path[i-1][0]
        y = path[i-1][1]
        dx = path[i][0] - x
        dy = path[i][1] - y
        pyplot.arrow(x, y, dx, dy, head_width=0.05, head_length=0.1, length_includes_head=True)
    endpointsx = [path[0][0], path[-1][0]]
    endpointsy = [path[0][1], path[-1][1]]
    pyplot.scatter(endpointsx, endpointsy, c='r')
    save(outDir=outDir, name=getPathName(path))

def drawMany(paths, outDir=None):
    for path in paths:
        drawOne(path, outDir)

def generateTest():
    path = [
        (1, 3),
        (2, 2),
        (3, 3),
        (3, 2),
        (2, 3),
        (1, 2),
        (2, 1),
        (3, 1),
        ]
    return path

def generateOne():
    #return generateTest()
    import pattern.random
    randomPath = pattern.random.generateOne()
    return randomPath

def generateMany(n=1):
    for i in xrange(n):
        yield generateOne()

def save(outDir=None, name=None):
    if outDir is None:
        outDir = '.'
    if name is None:
        import datetime
        name = datetime.datetime.today().strftime('%Y%m%d%H%M%S.%f')
    import os
    name = os.path.join(outDir, '%s.png' % name)
    logging.info('saving %s...' % name)
    if os.path.isfile(name):
        logging.info('already there')
    else:
        pyplot.savefig(name)
        logging.info('done')

def main():
    import optparse

    op = optparse.OptionParser()
    op.add_option('-n', dest='n', type='int', help='how many to generate')
    op.add_option('--outdir', dest='outdir', help='path to directory to save in')
    options, args = op.parse_args()

    drawMany(paths=generateMany(options.n), outDir=options.outdir)

if __name__ == '__main__':
    main()
