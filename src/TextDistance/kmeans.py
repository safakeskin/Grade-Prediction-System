def main():
    # from sklearn.cluster import KMeans
    import pandas as pd
    import sys
    # from sklearn.cluster import KMeans
    from TextDistance import TextDistance as textd
    # import matplotlib.pyplot as plt

    args = sys.argv
    data = pd.read_csv(args[1], delimiter=";").to_numpy()[:,1]
    ref = "There are 131 false labels out of 400. 116 of them are labeled as 0 but they should be labeled as 1. Therefore; errors are mostly belongs to class 1. Classifier is better at classifying class 0 data."
    
    feature_df = textd.constructTrainingData(data, ref, 13)
    # training_data = feature_df.to_numpy()[:,2:].astype(float)
    # print(training_data)

    # kmeans = KMeans(n_clusters=2)
    # kmeans.fit(training_data)

    # y_km = kmeans.fit_predict(training_data)
    # print(y_km)
    # plt.scatter(training_data[y_km ==0,0], training_data[y_km == 0,1], s=100, c='red')
    # plt.scatter(training_data[y_km ==1,0], training_data[y_km == 1,1], s=100, c='black')
    # plt.show()
    print(feature_df)

if __name__ == "__main__":
    main()