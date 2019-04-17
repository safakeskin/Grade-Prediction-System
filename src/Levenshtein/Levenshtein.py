from termcolor import colored


class Levenshtein:
    def __init__(self, str1=None, str2=None):
        if(str1 == None or str2 == None):
            # print(colored("\n\nLevenshtein object is initialized without parameters." +
            # " Use run method with 2 given strings in order to run Levenshtein " +
            # "Distance algorithm with supplied parameters.", "yellow") )
            self.str1 = self.str2 = None
            return
        # print( colored("\n\nLevenshtein object will be initialized with given texts " +
        # "and Levenshtein Distance of texts will be printed in console.", "yellow"))
        self.str1 = str1
        self.str2 = str2
        # lev_dist = self.levenshteinDistance(str1, str2)
#       # print(lev_dist)

    def run(self, str1=None, str2=None):
        try:
            if (str1 == None or str2 == None):
                if(self.str1 == None or self.str2 == None):
                    raise ValueError(
                        "Neither parameters are provided correctly nor object is not initialized with texts.")
                # print(colored("\n\nLevenshtein Distance of the texts that are given while initializing will "
                # + "be printed in console and also will be returned.", "yellow"))
                lev_dist = self.levenshteinDistance(self.str1, self.str2)
                # print(lev_dist)
                return lev_dist
            # print(colored("\n\nLevenshtein Distance of given texts will be printed in console and also will be returned.", "yellow"))
            lev_dist = self.levenshteinDistance(str1, str2)
            # print(lev_dist)
            return lev_dist
        except ValueError as err:
            print(colored("\n\nError: " + repr(err), "red"))

    def levenshteinDistance(self, str1, str2):
        m = len(str1)
        n = len(str2)
        lensum = float(m + n)
        d = []
        for i in range(m+1):
            d.append([i])
        del d[0][0]
        for j in range(n+1):
            d[0].append(j)
        for j in range(1, n+1):
            for i in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    d[i].insert(j, d[i-1][j-1])
                else:
                    minimum = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+2)
                    d[i].insert(j, minimum)
        ldist = d[-1][-1]
        ratio = (lensum - ldist)/lensum
        return {'text1': str1, 'text2': str2, 'distance': ldist, 'ratio': ratio}

    def tfRun(self, str1=None, str2=None):
        try:
            if str1 is None and self.str1 is None or str2 is None and self.str2 is None:
                raise ValueError("First argument is not provided.")
            print("Hello, World!")
        except ValueError as err:
            print(colored("\n\nError: " + repr(err), "red"))


if __name__ == "__main__":
    import tensorflow as tf
    # lev = Levenshtein()
    # lev.run()
    # lev.run("kitten", "sitting")
    lev1 = Levenshtein("kitten", "sitting")
    # lev2 = Levenshtein("rosettacode", "raisethysword")
    print(lev1.run())
    # hypothesis = tf.SparseTensor(
    #     [[0, 0, 0],
    #     [1, 0, 0]],
    #     ["a", "b"],
    #     (2, 1, 1))
    # truth = tf.SparseTensor(
    #     [[0, 1, 0],
    #     [1, 0, 0],
    #     [1, 0, 1],
    #     [1, 1, 0]],
    #     ["a", "b", "c", "a"],
    #     (2, 2, 2))
    hyp = "kitten"
    trt = "sitting"
    hypothesis = tf.SparseTensor(indices=[[0,0,x] for x in range(len(hyp))], values=[h for h in hyp], dense_shape=[1,1,len(hyp)])
    truth = tf.SparseTensor([[0,0,x] for x in range(len(trt))], [t for t in trt], [1,1,len(trt)])
    normalize = True
    output = tf.edit_distance(hypothesis, truth, normalize=normalize)
    print("Hello! \n\n\n")
    sth = tf.Variable(output)
    init_op = tf.initialize_all_variables()
    with tf.Session() as sess:
        sess.run(init_op)
        print(sess.run(sth))