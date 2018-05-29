import numpy as np
from collections import defaultdict
from operator import itemgetter

def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print('Rule: if a person buys {0}, then the person will also buy {1}.'.format(premise_name,conclusion_name))
    print('- Support: {}'.format(support[(premise, conclusion)]))
    print('- Confidence: {0:.3f}'.format(confidence[(premise, conclusion)]))
    
dataset_file = "affinity_dataset.txt"
X = np.loadtxt(dataset_file)
features = {0:'Milk',1:'Bread',2:'Apple',3:'Juice',4:'Chicken'}
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
total_occur = defaultdict(int)

# premise and conclusion are basically first and second instance combination of events/things

for sample in X:
    for premise in range(5):
        # calculating occurence of each item
        if sample[premise]==1:
            continue
        total_occur[premise]+=1
        for conclusion in range(5):
            # evaluating all the true cmbinations and all the invalid combinations
            if conclusion==premise:
                continue
            if sample[conclusion]==1:
                valid_rules[(premise,conclusion)]+=1
            else:
                invalid_rules[(premise,conclusion)]+=1

support = valid_rules
confidence = defaultdict(float)

# calculating confidence(that is how accurate the support are and how often they can be used)
for premise,coclusion in valid_rules.keys():
    rule = (premise,coclusion)
    confidence[rule] = valid_rules[rule]/total_occur[premise]

sorted_support = sorted(support.items(), key = itemgetter(1), reverse=True)

sorted_confidence = sorted(confidence.items(), key = itemgetter(1), reverse = True)
for index in range(5):
    print('Rule {}:'.format(index+1))
    (premise,conclusion) = sorted_confidence[index][0]
    print_rule(premise, conclusion, support, confidence, features)


    


