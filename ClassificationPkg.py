from FeatureSpaceRepresentationPkg import FeatureSpaceRepresentation
from PlaylistPkg import getPlaylistMidpoint
from sklearn.neighbors import KNeighborsClassifier
import numpy


def getClassification(playlistId='spotify:playlist:0XgEPjlWTX4g4HjBNhtZIL'):
    midpoint = getPlaylistMidpoint(playlistId)
    model = KNeighborsClassifier(n_neighbors=1)
    representation = FeatureSpaceRepresentation()
    classes = representation.getClasses()
    numpyMatrix = numpy.zeros((0, 7))
    temp = []
    for index in enumerate(classes):
        npArray = classes[index[0]].getNumpyArray()
        temp.append(npArray)
        numpyMatrix = numpy.vstack((numpyMatrix, temp[-1]))
    labels_gt = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    model.fit(numpyMatrix, labels_gt)

    labels = model.predict(midpoint.reshape(1, -1))
    print(labels)
    print(midpoint)


if __name__ == "__main__":
    getClassification()