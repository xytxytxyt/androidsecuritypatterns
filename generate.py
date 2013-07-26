from matplotlib import pyplot

def refresh():
    pyplot.figure()
    pyplot.axis('off')
    pyplot.axis('equal')

    pointsx = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    pointsy = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    pyplot.scatter(pointsx, pointsy)

def arrow(x, y, dx, dy):
    pyplot.arrow(x, y, dx, dy, head_width=0.05, head_length=0.1, length_includes_head=True)

def generatetest():
    arrow(1, 3, 1, -1)
    arrow(2, 2, 1, 1)
    arrow(3, 3, 0, -1)
    arrow(3, 2, -1, 1)
    arrow(2, 3, -1, -1)
    arrow(1, 2, 1, -1)
    arrow(2, 1, 1, 0)

def generateone():
    generatetest()

def generate(n=1):
    for i in xrange(n):
        refresh()
        generateone()
        save()

def save(outdir='.'):
    import os, datetime
    pyplot.savefig(os.path.join(outdir, '%s.png' % datetime.datetime.today().strftime('%Y%m%d%H%M%S.%f')))

def main():
    import optparse

    op = optparse.OptionParser()
    op.add_option('-n', dest='n', type='int', help='how many to generate')
    options, args = op.parse_args()

    generate(options.n)

if __name__ == '__main__':
    main()
