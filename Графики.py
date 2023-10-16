def draw_plot():
    import matplotlib.pyplot as plt
    import numpy as np

    # %matplotlib inline

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Plot examples', fontsize=20)
    fig.set_figheight(7)
    fig.set_figwidth(12)

    # The first plot is scatter plot
    means = np.array([20, 10])
    cov = np.array([[1, 0.7], [0.7, 1]])
    points = np.random.multivariate_normal(means, cov, size=500)
    x_1 = points[:, 0]
    y_1 = points[:, 1]
    ax1.scatter(x_1, y_1, c='#2222ff', edgecolors='k', alpha=0.9)
    ax1.set_title('Scatter plot example')

    # The second plot is hist plot
    x_2 = np.random.geometric(p=0.1, size=3000)
    n_bins = 40
    ax2.hist(x_2, bins=n_bins, color='r')
    ax2.set_title('Hist plot example')

    # The third plot is line plot
    x_3 = np.linspace(0.01, 6, 100)
    ax3.plot(x_3, np.log(x_3), c='k', label='$log(x)$')
    ax3.plot(x_3, np.log(2 * x_3), c='r', label='$log(2x)$')
    ax3.set_title('Line plot example')
    ax3.legend(loc='upper left', prop={'size': 9})

    # The fourth plot is bar plot
    x_4 = ['2021-01-0' + str(i) for i in range(1, 10)] + ['2021-01-' + str(i) for i in range(10, 15)]
    y_4 = np.random.normal(loc=5, size=14)
    ax4.bar(x_4, y_4)
    ax4.set_title('Bar plot example')
    ax4.tick_params(axis='x', labelrotation=90)

    fig.set_tight_layout(True)


if __name__ == '__main__':
    draw_plot()
