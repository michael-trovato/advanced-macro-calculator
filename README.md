# Advanced Macro Calculator

[![PyPI version](https://badge.fury.io/py/advanced-macro-calculator.svg)](https://pypi.org/project/advanced-macro-calculator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Website

A website version of this calculator is available at [Advanced Macro Calculator](https://www.advancedmacrocalculator.com/).

## Description

This calculator helps
you optimize your nutritional intake and body composition by recommending targeted macros and calories tailored to you.

With the tool being diet agnostic, it fits into any individual's diet preference.

It is built on reliable scientific evidence and provides you with personalized advice based on your specific input.

This calculator requires [Python 3](https://www.python.org/downloads/) to run.

## Installation

```
pip install advanced-macro-calculator
```

## Usage

```
advanced_macro_calculator
```

## Prompts

Please answer the prompts with the required information.

This calculator fully supports imperial and metric units.

Users can choose to lose or gain weight based on percentage of body weight or fixed values (lbs or kg).

This is useful when wanting to lose as a percentage of body weight per week while in a fat loss phase,
and gaining at a fixed value (lbs or kg) during a muscle gain phase.

## Calculating Body Fat Percentage
Your Body Fat Percentage plays a vital role in assessing your overall health status.

If you have greater than average muscle mass for your weight and height,
then it would be wise to test your body fat percentage using an accurate method,
such as [DEXA](https://health.ucdavis.edu/sports-medicine/resources/dxa-info#:~:text=The%20DXA%2C%20or%20%22Dual%20X,table%20that%20you%20lay%20on.),
and entering your body fat percentage.

An accurate body fat percentage will ensure a proper protein target per day as it is calculated based on lean body mass.

The default protein target is set to **2.2 g/kg<sub>LBM</sub>/day**.<sup>[[1]](https://pubmed.ncbi.nlm.nih.gov/28698222/)</sup>

### Known Body Fat Percentage
If you know your body fat percentage through reliable testing methods,
this percentage should be used to calculate your lean body mass.

### Unknown Body Fat Percentage
If your body fat percentage is unknown, a default estimate will be calculated.
This calculation involves determining your Body Mass Index (BMI) using your weight and height.
Following this, your body fat percentage is identified
using the [Deurenberg formula](https://en.wikipedia.org/wiki/Body_fat_percentage#From_BMI).
Finally, lean body mass is computed based on total body weight and the ascertained body fat percentage.

#### Other Methods

##### Reference Photos

You can find reference photos of individuals at different body fat percentages
and choose the body fat percentage that is closest to you.

##### US Navy Body Fat Calculator

The [US Navy Body Fat Calculator](https://www.calculator.net/body-fat-calculator.html) is used by the US Navy
to determine body fat percentage.

Note, neck circumference will have a large impact on the results.

## Safety Thresholds for Weight Change
Implementing safety thresholds ensures
your health is not compromised due to excessively quick weight change or extremely low caloric intake. 

### Weight Loss Measures
- **Maximum Weekly Weight Loss:** 2 lbs (0.907 kg)
- **Lowest Daily Caloric Intake:** 80% Basal Metabolic Rate (BMR)

### Weight Gain Measures
- **Maximum Weekly Weight Gain:** 2 lbs (0.907 kg)
- **Recommended Weekly Weight Gain:** 0.25 lbs (0.113 kg) and 0.5 lbs (0.226 kg)

### Understanding Dietary Fat Requirements for Optimal Health
To maintain good health and proper bodily functions, it's crucial to consume a minimum amount of fat every day.
However, the scientific consensus regarding the precise amount required is yet to be reached.
Thus, an estimated value with a 10% safety margin is used to ensure an adequate fat intake.

#### Essential Fatty Acids: The Daily Requirement

One key aspect of dietary fats is
to maintain the required level of essential fatty acids in our bodies
to prevent deficiencies and related health issues. 

Below are the daily requirements of essential fatty acids:

- **Omega-3 EPA & DHA:** Ideally, an adult should consume between 2 and 6 grams per day for optimal health.<sup>[[2]](https://www.foundmyfitness.com/topics/omega-3#optimal-omega-3-intake-for-most-adults) [[3]](https://biolayne.com/articles/nutrition/fat-facts-fat-source-matters/)</sup>

- **Linoleic Acid:** The [recommended intake](https://en.wikipedia.org/wiki/Essential_fatty_acid#Reference_intake_values) is between 11 and 17 grams per day.<sup>[[4]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3650500/)</sup>

##### Omega-3 EPA & DHA

This calculator specifically measures **EPA & DHA**, which are crucial types of Omega-3,
despite **alpha-linolenic acid** also being recognized as an essential Omega-3 fatty acid.
The reason for this lies in the observed inconsistencies within the individuals'
processes that convert ALA into EPA & DHA.<sup>[[5]](https://pubs.rsc.org/en/content/articlelanding/2018/FO/C7FO01809F)

There's a note of particular importance to those with the **APOE-4** SNP.
It's suggested they place a higher precedence on the intake of Omega-3 from fish.<sup>[[2]](https://www.foundmyfitness.com/topics/omega-3#apoe-4-and-alzheimer-39-s-disease)</sup>

Studies prove that maintaining an **Omega-3 Index of 8–11%** yields the greatest health benefits.<sup>[[2]](https://www.foundmyfitness.com/topics/omega-3#long-term-measure-of-omega-3-intake)</sup>
The consistent inclusion of these essential fatty acids in your diet plays a pivotal role in preserving the state of your overall health.

#### Minimum Dietary Fat

To ensure that optimal hormonal health is maintained,
the minimum dietary fat intake is set at **0.75 g/kg<sub>LBM</sub>/day**.
This guideline is informed by scientific research and navigates the shortcomings
associated with the more traditional methods of calculating fat intake: *percentage of total daily calories* and *percentage of total body weight*.

- **Percentage of Total Daily Calories**:
While this method is widely used, it can inadvertently underestimate the necessary fat intake during periods of caloric deficit,
potentially compromising hormonal balance and overall health.

- **Percentage of Total Body Weight**:
This approach might lead to an overestimation of fat needs for individuals with a higher body fat percentage.
It fails to account for the fact that adipose tissue does not directly increase dietary fat requirements
for maintaining essential physiological functions, including hormonal health.

The approach of focusing on **lean body mass (LBM)**, offers a more individualized strategy.
It ensures that all individuals, regardless of their total body weight or caloric intake,
receive a foundational amount of dietary fat essential for hormone production and other critical bodily functions.
This method acknowledges that while body composition varies greatly among individuals,
the fundamental need for dietary fats to support health and well-being does not.

##### Saturated Fat

While saturated fat is not considered essential,
consuming some saturated fat per day is known to enhance hormonal health.

The default minimum recommended intake of saturated fat is set to **0.15 g/kg<sub>LBM</sub>/day**.

## Managing your Caloric Intake
The calculator meticulously ensures that your optimal protein and fat goals are met according to your dietary needs.
Given the remaining calories, you select your macro targets.
This flexibility comes in handy when you want to modulate the macros according to your specific dietary regime.

### Available Options
1. **Favor Protein:** Assign all remaining calories towards protein.
2. **Favor Carbohydrates:** Allocate all remaining calories to carbs.
3. **Favor Fat:** Direct all remaining calories towards fats.
4. **Blend of Carbohydrates & Fats:** Distribute remaining calories evenly between carbohydrates and fats.
5. **Blend of Fat & Protein:** Split remaining calories evenly between fats and proteins.
6. **Blend of Carbohydrates & Protein:** Evenly divide remaining calories between carbohydrates and proteins.
7. **Blend of Carbohydrates, Fats, & Protein:** Distribute remaining calories amongst carbohydrates, fats, and proteins equally.

The distribution in mixed categories is done considering the caloric value per gram of each macro.

## Practical Application

### General Principles

When it comes to following a diet, certain general principles are universally acknowledged,
irrespective of the specific dietary choice. Here are the key points to remember:

- **Protein should be your top priority:** Protein is essential as it helps build and repair body tissues. Prioritize its consumption to ensure that your body gets an adequate supply every day.

- **Maximize Muscle Protein Synthesis (MPS):** MPS is a repair process that remodels and strengthens our muscles. You should strive to maximize this process.

- **Consider meal frequency:** Consuming four meals a day, evenly spaced will help maintain a steady supply of amino acids in the bloodstream throughout the day.
Nonetheless, at a practical level, consuming two to four meals per day is acceptable and more feasible for most.

- **Pay attention to the first and last meals:** The first and last meals of the day play a vital role in providing the body with enough amino acids to prevent catabolism (the breakdown of muscle tissue).
It's particularly important to ensure adequate protein intake after resistance training sessions.

- **Optimal protein quantity for MPS stimulation:** Research suggests that an intake of 20–40 grams of protein can optimally stimulate MPS.<sup>[[6]](https://physoc.onlinelibrary.wiley.com/doi/10.14814/phy2.12893)</sup> <sup>[[7]](https://pubmed.ncbi.nlm.nih.gov/33300582/)</sup>
This will depend on the leucine content of the protein.<sup>[[16]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6248570/)

Remember, every individual's dietary needs and responses can vary. Always consult with a healthcare professional before making significant changes to your diet.

#### Weight Loss

To optimize your diet for weight loss, choose foods with high satiety per calorie, lower caloric density.
Ideally, aim for lean protein-rich options that also contain good fats.
Remember to meet your daily protein and fat targets!

##### Protein Intake Optimization

Raising protein intake beyond **2.2 g/kg<sub>LBM</sub>/day** while maintaining a calorie deficit may provide several benefits such as:

1. Enhanced Satiety

2. Greater Caloric Expenditure through Thermic Effect of Food (TEF)

However, it's advisable to cap protein intake at **3.0 g/kg<sub>LBM</sub>/day**. Consuming protein beyond this limit is unlikely to offer further improvements in satiety. 

According to a hypercaloric protein overfeeding study,
healthy resistance-trained individuals can safely consume up to **4.4 g/kg/day** of protein.<sup>[[7]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4022420/)</sup>

##### TEF Breakdown<sup>[[17]](https://pubmed.ncbi.nlm.nih.gov/8878356/)</sup>

- **Protein:** 20–30%
- **Carbs:** 5–10%
- **Fat:** 0–3%

##### Age-related Anabolic Resistance

To account for the effects of age-related anabolic resistance,
a protein bonus is factored into the daily protein recommendation.
This adjustment ensures that older individuals receive an optimal protein intake to support muscle protein synthesis (MPS) and maintain muscle health.

**Protein Bonus by Age**:

- Ages 50–65: **+0.01 g/kg<sub>LBM</sub>/day**
- Ages 65+: **+0.02 g/kg<sub>LBM</sub>/day**

These increments help counteract the reduced efficiency of muscle protein synthesis that occurs with aging.

**Why This Matters**:

As we age, our bodies become less responsive to dietary protein,
requiring slightly higher intakes to achieve the same anabolic response. Factoring in these age-related adjustments ensures personalized, science-backed recommendations for optimal health.


##### Examples (Non-Exhaustive)
- Lean Meats
  - 93% Ground Beef
  - Turkey
  - Chicken
- Wild Caught Fish
  - Salmon
  - Sardines
  - Mackerel
- Non-Fat Yogurt
- Steamed Vegetables
- Tubers
- Fruits (Especially Berries)
- Carbonated Water with Meals

#### Weight Gain

Targeting a lower satiety per calorie,
higher caloric density foods will help you to consume more calories for easier weight gain.

##### Examples (Non-Exhaustive)
- Fattier Meats
- Whole Fat Yogurt
- Sauteed Vegetables
- Whole Grains

### Waist-to-Height Ratio

One of the cheapest and yet powerful methods
of determining your health risk is the [Waist-to-height Ratio (WHtR)](https://en.wikipedia.org/wiki/Waist-to-height_ratio).

Measure your waist circumference around the naval, then divide that number by your height (in the same units).

Your WHtR should be less than 0.5 for optimal health.<sup>[[8]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4157748/)</sup>

#### Boundary Values
- 0.4–0.49: Healthy
- 0.5–0.59: Increased Central Adiposity
- 0.6+: High Central Adiposity

#### Example

Height: 5' 10" (70 inches)

Waist: 40 inches

40 inches / 70 inches = 0.57 (Elevated Health Risk)

### Exercise Recommendations

#### Resistence Training

- **Frequency:** It is advised to work each muscle group at least once per week. This frequency aids in preventing muscle atrophy.
- **For Muscle Gain:** If your goal is hypertrophy, consider engaging each muscle group twice-weekly. This frequency is often recommended to optimize muscle growth.
- **Recovery and Training:** To maximize hypertrophy, it would be ideal to schedule your training routine in such a way that you rework each muscle group as soon as it recovers.
- **Volume:** The volume of training (total number of sets and repetitions) is important for muscle growth and should be adjusted according to individual factors such as training experience, muscle mass, and recovery capacity.
Typically, more experienced lifters might need a higher volume to continue making gains due to adaptations in muscle endurance and strength.

**Benefits:**

- Increased Hypertrophy
- Strengthened Muscles & Bones
- Fall Prevention<sup>[[9]](https://www.cdc.gov/falls/facts.html)</sup>
- Increased BMR<sup>[[10]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3661116/)</sup>

#### Cardiovascular Training

Not only great to increase total daily energy expenditure,
cardio has been linked to increased life span.<sup>[[11]](https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm)

**Benefits:**
- Increased VO2 max
- Increased BDNF<sup>[[12]](https://www.foundmyfitness.com/topics/bdnf#bdnf-provides-a-possible-link-between-exercise-and-improved-brain-health)</sup>
- Lower Risk of Cardiovascular Disease
- Lower Risk of Certain Cancers<sup>[[13]](https://www.cancer.gov/about-cancer/causes-prevention/risk/obesity/physical-activity-fact-sheet#what-is-known-about-the-relationship-between-physical-activity-and-cancer-risk)</sup>
- Improved Outcomes with Infectious Diseases<sup>[[14]](https://www.cdc.gov/coronavirus/2019-ncov/downloads/Brief-Summary-of-Findings-on-the-Association-Between-Physical-Inactivity-and-Severe-COVID-19-Outcomes.pdf)</sup>
<sup>[[15]](https://bjsm.bmj.com/content/57/19/1231)</sup>

### Lab Tests

These are generally recommended lab tests.

- HbA1c
- CBC
- CMP
- Fasting Lipids (9–12 Hours)
- Thyroid Panel
- Sex Hormones

## Special Thanks

The following doctors have contributed greatly to my understanding of nutritional science.

- Mike Israetel, PhD
- Theodore (Ted) Naiman, MD
- Gabrielle Lyon, MD
- Layne Norton, PhD
- Rhonda Patrick, PhD

## Constants

- **Minimum Protein Intake:** 2.2 g/kg<sub>LBM</sub>/day<sup>[[1]](https://pubmed.ncbi.nlm.nih.gov/28698222/)</sup>
- **Maximum Protein Intake:** 3.0 g/kg<sub>LBM</sub>/day
- **Minimum Total Fat Grams:** 0.75 g/kg<sub>LBM</sub>/day
- **Minimum Saturated Fat Grams:** 0.15 g/kg<sub>LBM</sub>/day
- **Minimum Fat Grams Safety Factor:** 10%
- **Maximum Caloric Deficit Below BMR:** 20%

## Disclaimers
This calculator is designed to provide general guidance and informational content only.
It is not a substitute for professional medical advice or for the care
that patients receive from their healthcare professionals. 

### Medical Disclaimer
Please consult with healthcare professionals for advice
pertaining to your individual health conditions and requirements.
Reliance on any information provided by this calculator is solely at your own risk.

### Fitness Disclaimer
The health and fitness advice provided is for general informational and educational purposes only.
It is not a substitute for professional advice,
and we strongly encourage you to consult with fitness professionals before implementing any fitness program.

## References

1. Morton RW, Murphy KT, McKellar SR, Schoenfeld BJ, Henselmans M, Helms E, Aragon AA, Devries MC, Banfield L, Krieger JW, Phillips SM. A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength in healthy adults. Br J Sports Med. 2018 Mar;52(6):376-384. doi: 10.1136/bjsports-2017-097608. Epub 2017 Jul 11. Erratum in: Br J Sports Med. 2020 Oct;54(19):e7. PMID: 28698222; PMCID: PMC5867436.
2. "Optimal Omega-3 Intake for Most Adults." FoundMyFitness: Omega-3, n.d., https://www.foundmyfitness.com/topics/omega-3#optimal-omega-3-intake-for-most-adults.
3. Norton, Layne. "Fat Facts: Fat Source Matters." BioLayne, no publication date, https://biolayne.com/articles/nutrition/fat-facts-fat-source-matters/.
4. Whelan J, Fritsche K. Linoleic acid. Adv Nutr. 2013 May 1;4(3):311-2. doi: 10.3945/an.113.003772. PMID: 23674797; PMCID: PMC3650500.
5. T. Greupner , L. Kutzner , F. Nolte , A. Strangmann , H. Kohrs , A. Hahn , N. H. Schebb and J. P. Schuchardt , Food Funct., 2018, 9 , 1587 —1600
6. Macnaughton, L.S.; Wardle, S.L.; Witard, O.C.; McGlory, C.; Hamilton, D.L.; Jeromson, S.; Lawrence, C.E.; Wallis, G.A.; Tipton,
K.D. The response of muscle protein synthesis following whole-body resistance exercise is greater following 40 g than 20 g of
ingested whey protein. Physiol. Rep. 2016, 4, e12893
7. Tagawa R, Watanabe D, Ito K, Ueda K, Nakayama K, Sanbongi C, Miyachi M. Dose-response relationship between protein intake and muscle mass increase: a systematic review and meta-analysis of randomized controlled trials. Nutr Rev. 2020 Nov 4;79(1):66–75. doi: 10.1093/nutrit/nuaa104. Epub ahead of print. PMID: 33300582; PMCID: PMC7727026.
8. Ashwell M, Mayhew L, Richardson J, Rickayzen B. Waist-to-height ratio is more predictive of years of life lost than body mass index. PLoS One. 2014 Sep 8;9(9):e103483. doi: 10.1371/journal.pone.0103483. PMID: 25198730; PMCID: PMC4157748.
9. "Facts about Falls." Centers for Disease Control and Prevention, n.d., https://www.cdc.gov/falls/facts.html.
10. McPherron AC, Guo T, Bond ND, Gavrilova O. Increasing muscle mass to improve metabolism. Adipocyte. 2013 Apr 1;2(2):92-8. doi: 10.4161/adip.22500. PMID: 23805405; PMCID: PMC3661116.
11. "Health Benefits of Physical Activity." Centers for Disease Control and Prevention, n.d., https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm.
12. "BDNF Provides a Possible Link Between Exercise and Improved Brain Health." FoundMyFitness: BDNF, n.d., https://www.foundmyfitness.com/topics/bdnf#bdnf-provides-a-possible-link-between-exercise-and-improved-brain-health.
13. "What Is Known About the Relationship Between Physical Activity and Cancer Risk." National Cancer Institute: Physical Activity and Cancer, n.d., https://www.cancer.gov/about-cancer/causes-prevention/risk/obesity/physical-activity-fact-sheet#what-is-known-about-the-relationship-between-physical-activity-and-cancer-risk.
14. "Brief Summary of Findings on the Association Between Physical Inactivity and Severe COVID-19 Outcomes." Centers for Disease Control and Prevention, n.d., PDF file, https://www.cdc.gov/coronavirus/2019-ncov/downloads/Brief-Summary-of-Findings-on-the-Association-Between-Physical-Inactivity-and-Severe-COVID-19-Outcomes.pdf.
15. Webber BJ, Yun HC, Whitfield GP Leisure-time physical activity and mortality from influenza and pneumonia: a cohort study of 577 909 US adults British Journal of Sports Medicine 2023;57:1231-1237.
16. Volpi E. Is leucine content in dietary protein the key to muscle preservation in older women? Am J Clin Nutr. 2018 Feb 1;107(2):143-144. doi: 10.1093/ajcn/nqy009. PMID: 29529164; PMCID: PMC6248570.
17. Tappy L. Thermic effect of food and sympathetic nervous system activity in humans. Reprod Nutr Dev. 1996;36(4):391-7. doi: 10.1051/rnd:19960405. PMID: 8878356.
