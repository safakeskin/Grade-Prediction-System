class TextDistance:
    import textdistance as td
    models = {
        "hamming": td.hamming,
        "levenshtein": td.levenshtein,
        "needleman_wunsch": td.needleman_wunsch,
        "mlipns": td.mlipns,
        "damerau_levenshtein": td.damerau_levenshtein,
        "jaro_winkler": td.jaro_winkler,
        "gotoh": td.gotoh,
        "smith_waterman": td.smith_waterman,
        "jaccard": td.jaccard,
        "sorensen": td.sorensen,
        "tversky": td.tversky,
        "overlap": td.overlap,
        # "tanimoto": td.tanimoto,
        "cosine": td.cosine,
        "monge_elkan": td.monge_elkan,
        "bag": td.bag,
    }

    @classmethod
    def getModels(cls):
        return list(cls.models.keys())

    @classmethod
    def run(cls, model_name, str1, str2):
        # func = cls.models[model_name](str1, str2)
        # func_distance   = cls.models[model_name].distance(str1, str2)
        # func_similarity = cls.models[model_name].similarity(str1, str2)
        # func_norm_dist  = cls.models[model_name].normalized_distance(str1, str2)
        func_norm_sim   = cls.models[model_name].normalized_similarity(str1, str2)
        return 0, 0, 0, 0, func_norm_sim
    
    @staticmethod
    def constructAnswerDict(results, index):
        answer_dict = {}
        for model_name in results:
            answer_dict[model_name] = results[model_name][index]
        return answer_dict
    
    @staticmethod
    def getAppendDict(answer,ref,result):
        df_dict = {"str1": answer, "str2":ref}
        z = df_dict.copy()
        z.update(result)
        return z
    
    @classmethod
    def constructTrainingData(cls, answers, truth, algo_num=15):
        import pandas as pd
        model_names = cls.getModels()[:algo_num]
        columns = ["str1", "str2"] + model_names
        ref = truth

        # normalized_distance     = pd.DataFrame(columns=columns)
        normalized_similarity   = pd.DataFrame(columns=columns)
        # similarity              = pd.DataFrame(columns=columns)
        # distance                = pd.DataFrame(columns=columns)
        # model                   = pd.DataFrame(columns=columns)

        for answer in answers:
            results = {}
            for model_name in model_names:
                results[model_name] = cls.run(model_name, answer, ref)

            # model_dict      = cls.getAppendDict(answer,ref, cls.constructAnswerDict(results,0))
            # dist_dict       = cls.getAppendDict(answer,ref, cls.constructAnswerDict(results,1))
            # sim_dict        = cls.getAppendDict(answer,ref, cls.constructAnswerDict(results,2))
            # norm_dist_dict  = cls.getAppendDict(answer,ref, cls.constructAnswerDict(results,3))
            norm_sim_dict   = cls.getAppendDict(answer,ref, cls.constructAnswerDict(results,4))

            # model                   = model.append(model_dict, ignore_index=True)
            # distance                = distance.append(dist_dict, ignore_index=True)
            # similarity              = similarity.append(sim_dict, ignore_index=True)
            # normalized_distance     = normalized_distance.append(norm_dist_dict, ignore_index=True)
            normalized_similarity   = normalized_similarity.append(norm_sim_dict, ignore_index=True)
        return normalized_similarity