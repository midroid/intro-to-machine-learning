#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    predError = []
    errd = 0
    erra = []
    indexa = []
    ind = 0

    for i in range(len(ages)):
        erra.append(abs( predictions[i][0] - net_worths[i][0] ))
    for j in range(9):
        ind = erra.index(max(erra))
        indexa.append(erra.index(max(erra)))
        erra[ind] = 0

    for i in range(len(ages)):
        if ( i in indexa ):
            pass
        else:
            errd = predictions[i][0] - net_worths[i][0]
            cleaned_data.append([ages[i][0], net_worths[i][0], errd])

    return cleaned_data
