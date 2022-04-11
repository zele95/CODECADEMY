# %%
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from pybaseball import playerid_lookup
from pybaseball import statcast_batter
import numpy as np
from matplotlib import cm


# import baseball players stats

# print(playerid_lookup('judge', 'aaron'))
# print(playerid_lookup('altuve', 'jose'))
judge_df = statcast_batter('2017-01-01', '2017-12-27', 592450)
altuve_df = statcast_batter('2017-01-01', '2017-12-27', 514888)

# print(judge_df.head())
# print(judge_df.columns)
# print(judge_df.description.unique())
# print(judge_df.type.unique())
# %%
# create a function that performs svm and shows the results
def playerStats(player_df):

    # map type field and drop nans
    # print(aaron_judge.type.unique())
    player_df['type'] = player_df['type'].map({'S':1, 'B':0})
    player_df.dropna(subset = ['type','plate_x','plate_z','strikes'],inplace = True)

    # split data
    training_set, validation_set = train_test_split(player_df, test_size = 0.2,random_state = 1)

    # check for the best parameters
    accuracy = {'gamma':0,'C':0,'value':0}
    accuracyMatrix = []
    i = 4 # can go to 100
    for gamma in range(1,i):
        dim1 = []
        for C in range(1,i):
            classifier = SVC(kernel = 'rbf',gamma = gamma, C = C)
            classifier.fit(training_set[['plate_x','plate_z','strikes']],training_set.type)
            # draw_boundary(ax,classifier)   # for 2 features
            score = classifier.score(validation_set[['plate_x','plate_z','strikes']],validation_set['type'])
            # accuracyMatrix[gamma,C] = score  # for 2 features
            if score > accuracy['value']:
                accuracy['value'] = score
                accuracy['gamma'] = gamma
                accuracy['C'] = C
            dim1.append(score)  # for 3d plot
        accuracyMatrix.append(dim1)  # for 3d plot

    print(accuracy)

    fig, ax = plt.subplots()
    ax = plt.axes(projection ="3d")
    scatter = ax.scatter3D(player_df.plate_x,player_df.plate_z,player_df.strikes, c = player_df.type, cmap = plt.cm.coolwarm, alpha = 0.25)
    classifier = SVC(kernel = 'rbf',gamma = accuracy['gamma'], C = accuracy['C'])
    classifier.fit(training_set[['plate_x','plate_z','strikes']].values,training_set.type)
    # draw_boundary(ax,classifier)
    ax.set_ylim(-2, 6)
    ax.set_xlim(-3, 3)
    plt.legend(handles = scatter.legend_elements()[0],labels = ['Ball','Strike'])
    plt.show()

    # 3D plot of accuracies

    # ax = plt.axes(projection='3d')
    # print(np.array(accuracyMatrix))
    # X, Y = np.meshgrid(np.array(range(1,i)),np.array(range(1,i)))
    # ax.plot_surface(X,Y, np.array(accuracyMatrix),cmap=cm.coolwarm)
    # print(X)
    # plt.show()

# %%

playerStats(judge_df)

playerStats(altuve_df)

# %%
