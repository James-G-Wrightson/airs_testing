# Criteria 1: Prompts
# %% Background
criteria_1_background = """
You must assess the Risk of Confounding Biases in the study. This criterion is concerned with biases due to one or more uncontrolled (or inappropriately controlled) variables (confounders) that influence both the intervention/exposure and the outcome. Confounding is the presence of an unblocked ‘backdoor path’ that affects both the intervention/exposure and the outcome. If there is confounding, a confounder (also known as a concomitant or covariate) will distort the association between an intervention/exposure and an outcome. More technically, if the assumption of exchangeability between groups does not hold because the intervention/exposure and the outcome share common causes, effect estimates will be biased by confounding. When a confounder is controlled for, such as through stratification, conditional exchangeability between groups may hold (i.e., the assumption of randomness may not be violated within a stratum or strata of the confounder variable), and thus a valid effect estimate may be provided within a stratum or strata. Awareness of potential confounders (i.e., hypothetical candidates) may be gained by trying to understand variability in effect. When such a factor is not controlled (or inappropriately controlled) before intervention/exposure, the resulting effect estimates may be biased if confounding is not adjusted for. Note that such baseline confounding is sometimes referred to as ‘selection bias’. Baseline confounding due to the selection of subjects or areas into studies can be dealt with before intervention or exposure (e.g., stratified sampling in which the population of inference is divided into subpopulations), and thus it needs to be assessed as baseline confounding in this criterion. Assessment of risk of confounding biases requires subject knowledge for determining potential confounders of the addressed causal structure
"""
# %% Standard criteria prompts
## Criterion 1.1 Prompt
criteria_1_1_prompt = """
# Answer the following question
"Question 1.1: Is it possible for the impact of the exposure or the effectiveness of the intervention to be confounded in this study?"
"""
## Criterion 1.2 Prompt
criteria_1_2_prompt = """
# Answer the following question
"Question 1.2: Did the author(s) control for all the potential confounders?"
"""
## Criterion 1.3 Prompt
criteria_1_3_prompt = """
# Answer the following question
"Question 1.3: Is there any justifiable reason for not controlling for all the potential confounders (so that omission of some of the potential confounders is unlikely to influence the assessment of the effectiveness or impact)?"
"""
## Criterion 1.4 Prompt
criteria_1_4_prompt = """
# Answer the following question
"Question 1.4: Were the potential confounders, that were controlled for, (and/or the instrumental variable used if applicable) likely to be measured accurately and precisely enough?"
"""
## Criterion 1.5 Prompt
criteria_1_5_prompt = """
# Answer the following question
"Question 1.5: Did the author(s) analyse the effect appropriately by taking into account the potential confounders, as well as the issue of accuracy and precision of the measurements of the potential confounders (and the instrumental variable if applicable)?"
"""
### Criterion 1.6 Prompt
criteria_1_6_prompt = """
# Answer the following question
"Question 1.6: What are the predicted magnitude and the direction of biases due to confounding?"
"""

# %% Combined prompt with all criteria
criteria_1_all_prompt = """
# Answer the following questions

Question 1.1: Is it possible for the impact of the exposure or the effectiveness of the intervention to be confounded in this study?

Question 1.2: Did the author(s) control for all the potential confounders?

Question 1.3: Is there any justifiable reason for not controlling for all the potential confounders (so that omission of some of the potential confounders is unlikely to influence the assessment of the effectiveness or impact)?

Question 1.4: Were the potential confounders, that were controlled for, (and/or the instrumental variable used if applicable) likely to be measured accurately and precisely enough?

Question 1.5: Did the author(s) analyse the effect appropriately by taking into account the potential confounders, as well as the issue of accuracy and precision of the measurements of the potential confounders (and the instrumental variable if applicable)?

Question 1.6: What are the predicted magnitude and the direction of biases due to confounding?
"""