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
### 1.1
#### V1
criteria_prompt11 = """
# Risk of Bias Assessment Criteria
### 1.1) Confounder Possibility: 
Could any variable that is not appropriately controlled affect both the assignment (or uptake) of the intervention and the outcome?
Consider the following:
- Some examples of confounders are Electricity use, Energy prices, Environmental attitudes, HH variables (e.g. Age, Gender, education level, income), Residence variables (e.g. Location, Size, Ownership; Seasonality etc.), Weather etc.
- If the intervention was implemented only by self-selected partner organizations, agencies, utilities, or regions, respond with **yes**.
- If statistically significant differences existed in pretreatment variables between control and treatment group(s), then respond with **no**.
- If there are any structural, organizational, or contextual factors that affect both participation in the intervention and the outcome, respond **yes**.
- If randomization occurred within units (e.g., within utilities), but the units themselves were not randomly selected, respond with **yes**.
###
"""
#### V2
criteria_prompt11_v2= """
# Risk of Bias Assessment Criteria:
 Is it possible for the impact of the exposure or the effectiveness of the intervention to be confounded in this study?
"""
#### V3
criteria_prompt11_v3= """
# Risk of Bias Assessment Criteria:
Is it possible for the impact of the exposure or the effectiveness of the intervention to be confounded in this study?
## Guidance:
Determine whether the observed impact of the exposure or the effectiveness of the intervention could be confounded. Use causal reasoning principles and, if possible, infer the underlying causal structure. Identify any variables that could plausibly act as common causes of both the exposure/intervention and the outcome. Evaluate whether any unblocked backdoor paths exist that may introduce confounding. Based on this, provide a judgment on whether there is a risk that the observed effect could be confounded.
"""
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
# Risk of Bias Assessment Criteria:
Is there any justifiable reason for not controlling for all the potential confounders (so that omission of some of the potential confounders is unlikely to influence the assessment of the effectiveness or impact)?
"""
#### V3
criteria_prompt13_v3 = """
# Risk of Bias Assessment Criteria:
Is there any justifiable reason for not controlling for all the potential confounders (so that omission of some of the potential confounders is unlikely to influence the assessment of the effectiveness or impact)?
## Guidance:
Evaluate whether the study provides a justifiable reason for not controlling for certain potential confounders, such that their omission is unlikely to bias the assessment of the intervention or exposure's effect.
Where applicable, infer the underlying causal structure and determine whether any uncontrolled backdoor paths are present. Identify any variables that could plausibly act as confounders but were not controlled for, and assess whether their omission is defensible based on causal reasoning, study design, or domain-specific justification.
Consider whether the remaining adjustment set sufficiently blocks all major sources of bias, and conclude whether the residual risk of confounding is low and unlikely to affect the study's internal validity.
"""

## Criteria 6
### 6.1
#### V1
criteria_prompt61 = """
### 6.1) DataSelective: 
Are the reported effect estimate likely to only represent a part of measurements of the outcome, i.e. only a part of measured outcomes is reported. E.g., only 80 measured outcomes are reported when there are 100, or the effect estimate is based on 80 measured outcomes when there are 100. 
Consider the following:  
- Assume there is always enough information to make a judgment.  
- Do not require the study to state selective reporting explicitly.  
- Respond **Yes** if:  
  - Some measured outcomes are described but not reported in results.  
  - Only significant results are presented while nonsignificant ones are missing.  
  - Subgroups, time points, or measured variables are mentioned but omitted from the analysis.  
- Respond **No** if:  
  - All outcomes the study describes as measured are reported.  
  - Subgroup breakdowns or appliance-level data are simply disaggregations of the main outcome, not separate outcomes.  
  - Engagement metrics, demographics, or qualitative focus groups are presented only as background or controls, not as prespecified outcomes.  
###
"""
#### V2
criteria_prompt61_v2  = """
# Risk of Bias Assessment Criteria:
Are the reported relevant outcome data (or effect estimate) likely to be of (or based on) selected measurements of the outcome?
"""
#### V3
criteria_prompt61_v3 = """
# Risk of Bias Assessment Criteria:
Are the reported relevant outcome data (or effect estimate) likely to be of (or based on) selected measurements of the outcome?
## Guidance:
Examine the outcomes described in the study. First, determine whether multiple ways of measuring the same outcome were available (e.g., different scales, time points, or instruments). 
Next, check whether only a subset of these was reported. 
Finally, assess whether this selective reporting could bias the overall interpretation of the findings.
"""
### 6.2
#### V1
criteria_prompt62 = """
# Risk of Bias Assessment Criteria:
### 6.1) Data Subgroups:
Are relevant outcome data likely to be unreported for some subgroup(s)? I.e., only outcome data on certain subjects or areas with certain characteristic(s) (e.g., taxonomic group) or in certain conditions (e.g., intervention intensity) are available.
Consider the following:
- Is there selective disclosure of findings from multiple subgroups or subpopulations? 
###
"""
#### V2
criteria_prompt62_v2 = """
# Risk of Bias Assessment Criteria:
Are relevant outcome data likely to be unreported for some subgroup(s)? 
"""
#### V3
criteria_prompt62_v3 = """
# Risk of Bias Assessment Criteria:
Are relevant outcome data likely to be unreported for some subgroup(s)? 
## Guidance:
Begin by identifying all subgroups mentioned in the study design or population description. Next, match these against the subgroups for which outcomes are actually reported. If any subgroups are omitted from the outcome reporting, reason whether this could reflect selective disclosure aimed at supporting a specific conclusion.
"""
### 6.3
#### V1
criteria_prompt63 = """
# Risk of Bias Assessment Criteria
### 6.3) Data Causal:
Is/are the analysis/analyses of the causal relationship of interest (intervention-outcome or exposure-outcome) likely to be partially reported?  
Consider the following:
- If there is selective disclosure of findings from multiple analyses, respond **yes**.
- Otherwise, respond **no**. 
###
"""
#### V2
criteria_prompt63_v2 = """
# Risk of Bias Assessment Criteria:
Is/are the analysis/analyses of the causal relationship of interest (intervention-outcome or exposure-outcome) likely to be partially reported?
"""
#### V3
criteria_prompt63_v3 = """
# Risk of Bias Assessment Criteria:
Is/are the analysis/analyses of the causal relationship of interest (intervention-outcome or exposure-outcome) likely to be partially reported?
## Guidance:
Identify the main causal question(s) the study aimed to answer. Then, review the statistical analyses used to evaluate those questions. Were multiple analytic approaches or models possible? Determine whether the reporting appears comprehensive or whether certain results were omitted, potentially due to non-significant or contradictory findings.
"""