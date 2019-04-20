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
        func = cls.models[model_name](str1, str2)
        func_distance   = cls.models[model_name].distance(str1, str2)
        func_similarity = cls.models[model_name].similarity(str1, str2)
        func_norm_dist  = cls.models[model_name].normalized_distance(str1, str2)
        func_norm_sim   = cls.models[model_name].normalized_similarity(str1, str2)
        return func, func_distance, func_similarity, func_norm_dist, func_norm_sim
    
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