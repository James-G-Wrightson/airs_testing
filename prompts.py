# Intro prompt #
## V1 ##
# intro_prompt = """
# # Introduction and Role Setting:
# You are a systematic reviewer who is an expert in risk of bias assessment of papers in environmental policies. You are particularly good at learning evaluation criteria, and closely following it to assess the risk of bias of climate and energy studies. 
# You can fully understand and follow the evaluation guidelines and evaluate the studies I have provided to you. Make sure all your judgments are based on the facts reported in the article and not on any extrapolation or speculation of your own.
# ## Guidelines for Evaluation:
# **Note:** The examples provided do not cover all possible scenarios in real-world applications. So, use your expert judgment to evaluate each item based on the information provided in the study, and do not rely solely on the examples.
# ### Important:
# - If there is too little information to support the judgment, do not speculate positively.
# - Reply with **ONLY** one of **Yes** or **No**. You provide reasoning behind each decision.
# """

# output_format = """
# # Output Format

# Please output the result STRICTLY in the format below:

# {
#   "explanation": str,
#   "Result": str
# }

# where explanation is a detailed reasoning that supports the decision, based on evidence from the document, and result is the overall decision for this item, respond only with one of ['**Yes**', '**No**'].
# """

## V2 ##
intro_prompt = """
# Introduction and Role Setting:
You are a systematic reviewer who is an expert in risk of bias assessment of papers in environmental policies. You are particularly good at learning evaluation criteria, and closely following them to assess the risk of bias of climate and energy studies. 
You can fully understand and follow the evaluation criteria and evaluate the studies I have provided to you. Make sure all your judgments are based on the facts reported in the article and not on any extrapolation or speculation of your own.
## Guidelines for Evaluation:
### Important:
- If there is too little information to support the judgment, do not speculate positively.
- Reply with ONLY one of "**Yes**" or "**No**" and provide an explanation.
"""

output_format = """
# Output Format

Please output the result STRICTLY in the format below:

{
  "Explanation": str,
  "Reply": str
}

where Explanation is the detailed reasoning that supports the Reply, based on evidence from the document, and Reply is the overall judgement (respond only with one of ['**Yes**', '**No**']).
"""

# Criteria prompts #

## Criteria 1

### 1.2
#### V1
criteria_prompt12 = """
# Risk of Bias Assessment Criteria
### 1.2) Confounder All: 
Did the authors control for all the potential confounders?
Consider the following:
- If any potential confounder was unmeasured, unadjusted, or found irrelevant but plausibly related to the outcome, respond **No**.
- If all potential confounders were measured, respond **yes**.
- Respond **Yes** if the study used randomization and/or statistical adjustment for the main known confounders (e.g., demographics, household characteristics, baseline outcomes, weather, etc.).
- Respond **Yes** if minor pretreatment imbalances exist but were adjusted for, or are expected due to chance in randomized designs.
- Respond **Yes** if authors acknowledged potential confounders and showed steps to account for them.
###
"""
#### V2
criteria_prompt12_v2= """
# Risk of Bias Assessment Criteria:
Did the authors control for all the potential confounders?
"""
#### V3
criteria_prompt12_v3= """
# Risk of Bias Assessment Criteria:
Did the authors control for all the potential confounders?
## Guidance:
Identify whether the authors controlled for all potential confounders that may affect both the intervention/exposure and the outcome. Use causal reasoning where possible. List any confounders explicitly mentioned or implied, describe how (if at all) they were controlled for (e.g., stratification, statistical adjustment, randomization), and provide a final judgment on whether control for confounding was sufficient according to causal inference principles.
"""

### 1.3
#### V1
criteria_prompt13 = """
# Risk of Bias Assessment Criteria
### 1.3) Confounder Justified Omission:
Is there any justifiable reason for not controlling for all the potential confounders (so that omission of some of the potential confounders is unlikely to influence the assessment of the effectiveness or impact)?

Consider the following:
- Step 1: Were any plausible confounders (e.g., demographics, building characteristics, behavioral traits) omitted or not discussed in the analysis? Do not assume RCT or fixed effects alone means all confounders were handled. If yes, continue to Step 2.
- Step 2: Did the authors clearly justify the omission? Acceptable reasons include: RCT, DiD, or fixed effects used **and explained**, **or** clearly stated use of randomization (RCT) that reasonably implies balance between groups, even if not accompanied by a detailed discussion of confounder handling, Fixed effects at a sufficiently granular level (e.g., household, individual, firm), Balance shown between groups, Homogeneous samples, Practical or methodological constraints common in the field (e.g., voluntary participation, lack of a control group, lack of data on non-participants, gradual phase-in designs, limited data, privacy or data protection restrictions, small sample sizes due to technology adoption limits or intrusive measurement methods, recognized limitations of certain designs such as DiD’s inability to fully control for all confounders), Concern for overadjustment, Norms in the field , An **instrumental variable** used appropriately (i.e., not associated with the confounder(s), associated with the intervention/exposure, and does not directly influence the outcome — enabling valid estimation)
- **Step 3:** Was the justification valid and reasonable? If plausible confounders were omitted **and** at least one acceptable reason from Step 2 is present, you must select **Yes** — even if the authors do not explicitly frame it as a justification or provide additional discussion.
- Recognized methodological limitations (e.g., DiD’s inability to fully control for all confounders) and practical constraints common in the field (e.g., voluntary participation, lack of control group, privacy restrictions, small sample sizes from intrusive technology) are sufficient for a **yes** when they are unavoidable and align with accepted norms in the literature.
- Constraints (small N, privacy, feasibility) should only be reported as contextual limitations, not as justification, unless the authors clearly argue why due to the limits, confounders were not controlled for.
"""
#### V2
criteria_prompt13_v2 = """
# Risk of Bias Assessment Criteria
Confounder Justified Omission: Is there any justifiable reason for not controlling for all the potential confounders (so that omission of some of the potential confounders is unlikely to influence the assessment of the effectiveness or impact)?
Consider the following:
Answer **Yes** when there is evidence that omission of some of the potential confounders does not affect the assessment of effectiveness or impact. This may be the case if adjusting all potential confounders will lead to overadjustment, or an ‘instrumental variable’ is used for estimating the effectiveness or impact, etc. Instrumental variable is a variable that (1) is not associated with the confounder(s), (2) is associated with the intervention/exposure but (3) does not directly influence the outcome. If used appropriately, it enables valid estimation. 
"""
#### V3
criteria_prompt13_v3 = """
# Risk of Bias Assessment Criteria
Confounder Justified Omission: Is there any justifiable reason for not controlling for all the potential confounders (so that omission of some of the potential confounders is unlikely to influence the assessment of the effectiveness or impact)?
Consider the following:
Evaluate whether the study provides a justifiable reason for not controlling for certain potential confounders, such that their omission is unlikely to bias the assessment of the intervention or exposure's effect.
Where applicable, infer the underlying causal structure and determine whether any uncontrolled backdoor paths are present. Identify any variables that could plausibly act as confounders but were not controlled for, and assess whether their omission is defensible based on causal reasoning, study design, or domain-specific justification.
Consider whether the remaining adjustment set sufficiently blocks all major sources of bias, and conclude whether the residual risk of confounding is low and unlikely to affect the study's internal validity.
"""

## Criteria 2

### 2.3
#### V1
criteria_prompt23 = """
# Risk of Bias Assessment Criteria

### 2.3) Sample Exclusion
After the start of the intervention/exposure or during the analysis, were any subjects or areas excluded or lost from the study or analysis? When some subjects or areas, or collected data are excluded, it might increase the risk of post-intervention/exposure selection bias.
Consider the following:
- If the final participated sample is lower than the total potential participation sample, then respond with **yes**. 
- If the final participated sample is the same as the total potential participation sample, then respond with **no**.
"""