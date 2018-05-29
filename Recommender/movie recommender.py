import os
import pandas as pd
from collections import defaultdict
import sys

def find_frequent_items(fav_rev_users, k_itemsets, min_support):
    counts = defaultdict(int)
    for user, reviews in fav_rev_users.items():
        for itemset in k_itemsets:
            if itemset.issubset(reviews):
                for other_rev_movie in reviews - itemset:
                    current_superset = itemset | frozenset((other_rev_movie,))
                    counts[current_superset] += 1
    return dict([(itemset, frequency) for itemset, frequency in counts.items() if frequency >= min_support])

def get_movie_name(movie_id):
    title_object = movie_names_data[movie_names_data["MovieID"]==movie_id  ]["Title"]
    title= title_object.values[0]
    return title


data_folder = "E:\Study\Python\Recommender\ml-100k"
data_file = os.path.join(data_folder, "u.data")
movie_names = os.path.join(data_folder, "u.item")
movie_names_data = pd.read_csv(movie_names , delimiter="|", header = None, encoding = "mac-roman")
movie_names_data.columns = ["MovieID", "Title", "Release Date",
"Video Release", "IMDB", "<UNK>", "Action", "Adventure",
"Animation", "Children's", "Comedy", "Crime", "Documentary",
"Drama", "Fantasy", "Film-Noir",
"Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller",
"War", "Western"]

all_ratings = pd.read_csv(data_file, delimiter = "\t", header=None, names = ["UserID","MovieID","Ratings","Datetime"])
all_ratings["Datetime"] = pd.to_datetime(all_ratings['Datetime'], unit = 's')

all_ratings["Favorable"] = all_ratings["Ratings"]>3

#getting the first 200 users and all those favourable users from the ratings dataset
ratings = all_ratings[all_ratings['UserID'].isin(range(200))]
favorable_ratings = ratings[ratings["Favorable"]]

favorable_reviews = dict((k, frozenset(v.values)) for k, v in favorable_ratings.groupby("UserID")["MovieID"])
# frozen set allowing us to check if a movie has been rated by a user or not
num_fav_movie = ratings[["MovieID","Favorable"]].groupby("MovieID").sum()
# how frequently a movie is reviewed by the user
print(num_fav_movie.sort_values("Favorable", ascending = False)[:5])
# sorting the movies according to how favorable they are

# finding the frequently occuring data items and also setting minimum support value
frequent_itemsets = {}
min_support = 50

frequent_itemsets[1] = dict((frozenset((mvid,)),row["Favorable"]) for mvid, row in num_fav_movie.iterrows() if row["Favorable"]>min_support)

for k in range(2,20):
    cur_freq_item = find_frequent_items(favorable_reviews, frequent_itemsets[k-1], min_support)
    frequent_itemsets[k] = cur_freq_item
    if len(cur_freq_item)==0:
        print("Did not find itemsets of length {}".format(k))
        sys.stdout.flush()
        break
    else:
        print("I found {} frequent itemsets of length {}".format(len(cur_freq_item),k))
        sys.stdout.flush()

del frequent_itemsets[1]

candidate_rules = []
for itemset_length, itemset_counts in frequent_itemsets.items():
    for itemset in itemset_counts.keys():
        for conclusion in itemset:
            premise = itemset - set((conclusion,))
            candidate_rules.append((premise,conclusion))

print(candidate_rules[:5])

correct_count = defaultdict(int)
incorrect_count = defaultdict(int)

for users, reviews in favorable_reviews.items():
    for candidate_rule in candidate_rules:
        premise, conclusion = candidate_rule
        if premise.issubset(reviews):
            if conclusion in reviews:
                correct_count[candidate_rule] += 1
            else:
                incorrect_count[candidate_rule] += 1

rule_confidence = {candidate_rule: correct_count[candidate_rule]/float(correct_count[candidate_rule]+incorrect_count[candidate_rule]) for candidate_rule in candidate_rules}

from operator import itemgetter
sorted_confidence = sorted(rule_confidence.items(), key = itemgetter(1), reverse = True)
for index in range(5):
    print("Rule {}:".format(index+1))
    premise, conclusion = sorted_confidence[index][0]
    premise_name = ", ".join(get_movie_name(idx) for idx in premise)
    conclusion_name = get_movie_name(conclusion)
    print("if a person recommends {}, they will also recommend {}".format(premise_name, conclusion_name))
    print("Confidence: {:.2f}%".format(rule_confidence[(premise, conclusion)]*100))
    print("")

# evaluating the whole process
test_dataset = all_ratings[~all_ratings["UserID"].isin(range(200))]
test_favorable =  test_dataset[test_dataset["Favorable"]]
test_favorable_user = dict((k, frozenset(v.values)) for k,v in test_favorable.groupby("UserID")["MovieID"])
correct_counts = defaultdict(int)
incorrect_counts = defaultdict(int)
for user, reviews in test_favorable_user.items():
    for candidate_rule in candidate_rules:
        premise, conclusion = candidate_rule
        if premise.issubset(reviews):
            if conclusion in reviews:
                correct_counts[candidate_rule] += 1
            else:
                incorrect_counts[candidate_rule] += 1

test_confidence = {candidate_rule: correct_counts[candidate_rule]/ float(correct_counts[candidate_rule] + incorrect_counts[candidate_rule]) for candidate_rule in rule_confidence}

for index in range(5):
    print("Rule {0}:".format(index + 1))
    (premise, conclusion) = sorted_confidence[index][0]
    premise_names = ", ".join(get_movie_name(idx) for idx in premise)
    conclusion_name = get_movie_name(conclusion)
    print("Rule: If a person recommends {0} they will also recommend {1}".format(premise_names, conclusion_name))
    print(" - Train Confidence: {0:.3f}".format(rule_confidence.get((premise, conclusion), -1)))
    print(" - Test Confidence: {0:.3f}".format(test_confidence.get((premise, conclusion),-1)))
    print("")
    






    















        




