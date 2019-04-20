from TextDistance import TextDistance as textd
import pandas as pd

if __name__ == "__main__":
    model_names = textd.getModels()
    columns = ["str1", "str2"] + model_names

    answers = ["you are a horse.", "are you a horse", "  ", "we are horses.", "you are a rising sun", "house of a rising sun the"]
    ref = "a horse is a monkey"

    normalized_distance     = pd.DataFrame(columns=columns)
    normalized_similarity   = pd.DataFrame(columns=columns)
    similarity              = pd.DataFrame(columns=columns)
    distance                = pd.DataFrame(columns=columns)
    model                   = pd.DataFrame(columns=columns)

    for answer in answers:
        results = {}
        for model_name in model_names:
            results[model_name] = textd.run(model_name, answer, ref)

        model_dict      = textd.getAppendDict(answer,ref, textd.constructAnswerDict(results,0))
        dist_dict       = textd.getAppendDict(answer,ref, textd.constructAnswerDict(results,1))
        sim_dict        = textd.getAppendDict(answer,ref, textd.constructAnswerDict(results,2))
        norm_dist_dict  = textd.getAppendDict(answer,ref, textd.constructAnswerDict(results,3))
        norm_sim_dict   = textd.getAppendDict(answer,ref, textd.constructAnswerDict(results,4))

        model                   = model.append(model_dict, ignore_index=True)
        distance                = distance.append(dist_dict, ignore_index=True)
        similarity              = similarity.append(sim_dict, ignore_index=True)
        normalized_distance     = normalized_distance.append(norm_dist_dict, ignore_index=True)
        normalized_similarity   = normalized_similarity.append(norm_sim_dict, ignore_index=True)
    
    print(normalized_similarity)