# coding: utf-8


import textdistance as td 
import pandas as pd

def HammingDistance(str1, str2):
    h1 = td.hamming(str1, str2)
    h2 = td.hamming.distance(str1, str2)
    h3 = td.hamming.similarity(str1, str2)
    h4 = td.hamming.normalized_distance(str1, str2)
    h5 = td.hamming.normalized_similarity(str1, str2)
    h6 = td.Hamming(qval=2).distance(str1, str2)
#     print("Hamming Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def LevenshteinDistance(str1, str2):
    h1 = td.levenshtein(str1, str2)
    h2 = td.levenshtein.distance(str1, str2)
    h3 = td.levenshtein.similarity(str1, str2)
    h4 = td.levenshtein.normalized_distance(str1, str2)
    h5 = td.levenshtein.normalized_similarity(str1, str2)
    h6 = td.Levenshtein(qval=2).distance(str1, str2)
#     print("Levenshtein Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def NeddlemanWunschDistance(str1, str2):
    h1 = td.needleman_wunsch(str1, str2)
    h2 = td.needleman_wunsch.distance(str1, str2)
    h3 = td.needleman_wunsch.similarity(str1, str2)
    h4 = td.needleman_wunsch.normalized_distance(str1, str2)
    h5 = td.needleman_wunsch.normalized_similarity(str1, str2)
    h6 = td.NeedlemanWunsch(qval=2).distance(str1, str2)
#     print("Neddleman Wunsch Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def MnlinsDistance(str1, str2):
    h1 = td.mlipns(str1, str2)
    h2 = td.mlipns.distance(str1, str2)
    h3 = td.mlipns.similarity(str1, str2)
    h4 = td.mlipns.normalized_distance(str1, str2)
    h5 = td.mlipns.normalized_similarity(str1, str2)
    # h6 = td.Mlipns(qval=2).distance(str1, str2)
#     print("MNLINS Distance:")
#     print (h1, h2, h3, h4, h5)
    return (h1, h2, h3, h4, h5)

def DamerauLevenshteinDistance(str1, str2):  
    h1 = td.damerau_levenshtein(str1, str2)
    h2 = td.damerau_levenshtein.distance(str1, str2)
    h3 = td.damerau_levenshtein.similarity(str1, str2)
    h4 = td.damerau_levenshtein.normalized_distance(str1, str2)
    h5 = td.damerau_levenshtein.normalized_similarity(str1, str2)
    h6 = td.DamerauLevenshtein(qval=2).distance(str1, str2)
#     print("Damerau Levenshtein Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def JaroWinklerDistance(str1, str2):
    h1 = td.jaro_winkler(str1, str2)
    h2 = td.jaro_winkler.distance(str1, str2)
    h3 = td.jaro_winkler.similarity(str1, str2)
    h4 = td.jaro_winkler.normalized_distance(str1, str2)
    h5 = td.jaro_winkler.normalized_similarity(str1, str2)
    h6 = td.JaroWinkler(qval=2).distance(str1, str2)
#     print("Jaro Winkler Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def GotohDistance(str1, str2):
    h1 = td.gotoh(str1, str2)
    h2 = td.gotoh.distance(str1, str2)
    h3 = td.gotoh.similarity(str1, str2)
    h4 = td.gotoh.normalized_distance(str1, str2)
    h5 = td.gotoh.normalized_similarity(str1, str2)
    h6 = td.Gotoh(qval=2).distance(str1, str2)
#     print("Gotoh Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def SmithWatermanDistance(str1, str2):
    h1 = td.smith_waterman(str1, str2)
    h2 = td.smith_waterman.distance(str1, str2)
    h3 = td.smith_waterman.similarity(str1, str2)
    h4 = td.smith_waterman.normalized_distance(str1, str2)
    h5 = td.smith_waterman.normalized_similarity(str1, str2)
    h6 = td.SmithWaterman(qval=2).distance(str1, str2)
#     print("Smith Waterman Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def JaccardDistance(str1, str2):
    h1 = td.jaccard(str1, str2)
    h2 = td.jaccard.distance(str1, str2)
    h3 = td.jaccard.similarity(str1, str2)
    h4 = td.jaccard.normalized_distance(str1, str2)
    h5 = td.jaccard.normalized_similarity(str1, str2)
    h6 = td.Jaccard(qval=2).distance(str1, str2)
#     print("Jaccard Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def SorensenDistance(str1, str2):
    h1 = td.sorensen(str1, str2)
    h2 = td.sorensen.distance(str1, str2)
    h3 = td.sorensen.similarity(str1, str2)
    h4 = td.sorensen.normalized_distance(str1, str2)
    h5 = td.sorensen.normalized_similarity(str1, str2)
    h6 = td.Sorensen(qval=2).distance(str1, str2)
#     print("Sorensen Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def TverskyDistance(str1, str2):
    h1 = td.tversky(str1, str2)
    h2 = td.tversky.distance(str1, str2)
    h3 = td.tversky.similarity(str1, str2)
    h4 = td.tversky.normalized_distance(str1, str2)
    h5 = td.tversky.normalized_similarity(str1, str2)
    h6 = td.Tversky(qval=2).distance(str1, str2)
#     print("Tversky Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def OverlapDistance(str1, str2):
    h1 = td.overlap(str1, str2)
    h2 = td.overlap.distance(str1, str2)
    h3 = td.overlap.similarity(str1, str2)
    h4 = td.overlap.normalized_distance(str1, str2)
    h5 = td.overlap.normalized_similarity(str1, str2)
    h6 = td.Overlap(qval=2).distance(str1, str2)
#     print("Overlap Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def TanimotoDistance(str1, str2):
    h1 = td.tanimoto(str1, str2)
    h2 = td.tanimoto.distance(str1, str2)
    h3 = td.tanimoto.similarity(str1, str2)
    h4 = td.tanimoto.normalized_distance(str1, str2)
    h5 = td.tanimoto.normalized_similarity(str1, str2)
    h6 = td.Tanimoto(qval=2).distance(str1, str2)
#     print("Tanimoto Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def CosineDistance(str1, str2):
    h1 = td.cosine(str1, str2)
    h2 = td.cosine.distance(str1, str2)
    h3 = td.cosine.similarity(str1, str2)
    h4 = td.cosine.normalized_distance(str1, str2)
    h5 = td.cosine.normalized_similarity(str1, str2)
    h6 = td.Cosine(qval=2).distance(str1, str2)
#     print("Cosine Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def MongeElkanDistance(str1, str2):
    h1 = td.monge_elkan(str1, str2)
    h2 = td.monge_elkan.distance(str1, str2)
    h3 = td.monge_elkan.similarity(str1, str2)
    h4 = td.monge_elkan.normalized_distance(str1, str2)
    h5 = td.monge_elkan.normalized_similarity(str1, str2)
    h6 = td.MongeElkan(qval=2).distance(str1, str2)
#     print("MongeElkan Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)

def BagDistance(str1, str2):
    h1 = td.bag(str1, str2)
    h2 = td.bag.distance(str1, str2)
    h3 = td.bag.similarity(str1, str2)
    h4 = td.bag.normalized_distance(str1, str2)
    h5 = td.bag.normalized_similarity(str1, str2)
    h6 = td.Bag(qval=2).distance(str1, str2)
#     print("Bag Distance:")
#     print (h1, h2, h3, h4, h5, h6)
    return (h1, h2, h3, h4, h5, h6)


normalized_distance = pd.DataFrame(columns=['str1', 'str2', 'Hamming', 'Levenshtein', 'NeedlemanWunsch', 'MNLINS', 
                           'DamerauLevenshtein', 'JaroWinkler', 'Gotoh', 'SmithWaterman', 'Jaccard', 
                           'Sorensen', 'Tversky', 'Overlap', 'Cosine', 'MongeElkan', 'Bag' ])

normalized_similarity = pd.DataFrame(columns=['str1', 'str2', 'Hamming', 'Levenshtein', 'NeedlemanWunsch', 'MNLINS', 
                           'DamerauLevenshtein', 'JaroWinkler', 'Gotoh', 'SmithWaterman', 'Jaccard', 
                           'Sorensen', 'Tversky', 'Overlap', 'Cosine', 'MongeElkan', 'Bag' ])

similarity = pd.DataFrame(columns=['str1', 'str2', 'Hamming', 'Levenshtein', 'NeedlemanWunsch', 'MNLINS', 
                           'DamerauLevenshtein', 'JaroWinkler', 'Gotoh', 'SmithWaterman', 'Jaccard', 
                           'Sorensen', 'Tversky', 'Overlap', 'Cosine', 'MongeElkan', 'Bag' ])

distance = pd.DataFrame(columns=['str1', 'str2', 'Hamming', 'Levenshtein', 'NeedlemanWunsch', 'MNLINS', 
                           'DamerauLevenshtein', 'JaroWinkler', 'Gotoh', 'SmithWaterman', 'Jaccard', 
                           'Sorensen', 'Tversky', 'Overlap', 'Cosine', 'MongeElkan', 'Bag' ])

df = pd.DataFrame(columns=['str1', 'str2', 'Hamming', 'Levenshtein', 'NeedlemanWunsch', 'MNLINS', 
                           'DamerauLevenshtein', 'JaroWinkler', 'Gotoh', 'SmithWaterman', 'Jaccard', 
                           'Sorensen', 'Tversky', 'Overlap', 'Cosine', 'MongeElkan', 'Bag' ])

answers = ["you are a horse.", "are you a horse", "  ", "we are horses.", "you are a rising sun", "house of a rising sun the"]
ref = "a horse is a monkey"
a = "you are a horse."


for idx, item in enumerate(answers):
    h1, h2, h3, h4, h5, h6 = HammingDistance(item, ref)
    l1, l2, l3, l4, l5, l6 = LevenshteinDistance(item, ref)
    nw1, nw2, nw3, nw4, nw5, nw6 = NeddlemanWunschDistance(item, ref)
    m1, m2, m3, m4, m5 = MnlinsDistance(item, ref)
    dl1, dl2, dl3, dl4, dl5, dl6 = DamerauLevenshteinDistance(item, ref)
    jw1, jw2, jw3, jw4, jw5, jw6 = JaroWinklerDistance(item, ref)
    g1, g2, g3, g4, g5, g6 = GotohDistance(item, ref)
    sw1, sw2, sw3, sw4, sw5, sw6 = SmithWatermanDistance(item, ref)
    j1, j2, j3, j4, j5, j6 = JaccardDistance(item, ref)
    s1, s2, s3, s4, s5, s6 = SorensenDistance(item, ref)
    t1, t2, t3, t4, t5, t6 = TverskyDistance(item, ref)
    o1, o2, o3, o4, o5, o6 = OverlapDistance(item, ref)
#     ta1, ta2, ta3, ta4, ta5, ta6 = TanimotoDistance(item, ref)
    c1, c2, c3, c4, c5, c6 = CosineDistance(item, ref)
    me1, me2, me3, me4, me5, me6 = MongeElkanDistance(item, ref)
    b1, b2, b3, b4, b5, b6 = BagDistance(item, ref)
    
    normalized_similarity = normalized_similarity.append({'str1':item,'str2':ref,'Hamming':h5,'Levenshtein':l5,
                    'NeedlemanWunsch':nw5,'MNLINS':m5,'DamerauLevenshtein':dl5,
                    'JaroWinkler':jw5,'Gotoh':g5,'SmithWaterman':sw5,'Jaccard':j5,
                    'Sorensen':s5,'Tversky':t5,'Overlap':o5,'Cosine':c5,
                    'MongeElkan':me5,'Bag':b5}, ignore_index=True)
    
    normalized_distance = normalized_distance.append({'str1':item,'str2':ref,'Hamming':h4,'Levenshtein':l4,
                    'NeedlemanWunsch':nw4,'MNLINS':m4,'DamerauLevenshtein':dl4,
                    'JaroWinkler':jw4,'Gotoh':g4,'SmithWaterman':sw4,'Jaccard':j4,
                    'Sorensen':s4,'Tversky':t4,'Overlap':o4,'Cosine':c4,
                    'MongeElkan':me4,'Bag':b4}, ignore_index=True)
    
    similarity = similarity.append({'str1':item,'str2':ref,'Hamming':h3,'Levenshtein':l3,
                    'NeedlemanWunsch':nw3,'MNLINS':m3,'DamerauLevenshtein':dl3,
                    'JaroWinkler':jw3,'Gotoh':g3,'SmithWaterman':sw3,'Jaccard':j3,
                    'Sorensen':s3,'Tversky':t3,'Overlap':o3,'Cosine':c3,
                    'MongeElkan':me3,'Bag':b3}, ignore_index=True)
    
    distance = distance.append({'str1':item,'str2':ref,'Hamming':h2,'Levenshtein':l2,
                    'NeedlemanWunsch':nw2,'MNLINS':m2,'DamerauLevenshtein':dl2,
                    'JaroWinkler':jw2,'Gotoh':g2,'SmithWaterman':sw2,'Jaccard':j2,
                    'Sorensen':s2,'Tversky':t2,'Overlap':o2,'Cosine':c2,
                    'MongeElkan':me2,'Bag':b2}, ignore_index=True)
    
    df = df.append({'str1':item,'str2':ref,'Hamming':h1,'Levenshtein':l1,
                    'NeedlemanWunsch':nw1,'MNLINS':m1,'DamerauLevenshtein':dl1,
                    'JaroWinkler':jw1,'Gotoh':g1,'SmithWaterman':sw1,'Jaccard':j1,
                    'Sorensen':s1,'Tversky':t1,'Overlap':o1,'Cosine':c1,
                    'MongeElkan':me1,'Bag':b1}, ignore_index=True)


print(normalized_distance)

print(normalized_similarity)

print(distance)

print(similarity)

print(df)
