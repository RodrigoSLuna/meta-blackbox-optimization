#For plotting
import matplotlib.pyplot as plt
from matplotlib import cm
plt.switch_backend("TkAgg")
from mpl_toolkits import mplot3d

#Display function
def display_function(p, lower_bound=-5, upper_bound=5, resolution=50, matlab_plot=True):

    #X, Y and Z
    X = np.linspace(lower_bound, upper_bound, resolution)
    Y = np.linspace(lower_bound, upper_bound, resolution)
    Z = [p((x,y)) for x in X for y in Y]
    Z = np.array(Z)
    Z = -Z.reshape((resolution, resolution))
    X, Y = np.meshgrid(X, Y)

    #Declare fig
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Plot the surface.
    if matlab_plot == True:
        surf = ax.plot_surface(X, Y, Z, cmap=cm.jet_r, linewidth=0, antialiased=False)
    else:
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    ax.view_init(45, 45)

    ax.set_xlabel('x1')
    #ax.set_xlim(lower_bound, upper_bound)
    plt.xticks(np.arange(lower_bound, upper_bound, 2.5))

    ax.set_ylabel('x2')
    #ax.set_ylim(lower_bound, upper_bound)
    plt.yticks(np.arange(lower_bound, upper_bound, 2.5))

    ax.set_zlabel('f')
    name = p.info.split(":")[0]
    plt.title(name)
    plt.show()