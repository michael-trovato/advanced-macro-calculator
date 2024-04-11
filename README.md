# Advanced Macro Calculator
This calculator helps
you optimize your nutritional intake and body composition by recommending targeted macros and calories tailored to you.

With the tool being diet agnostic, it fits into any individual's diet preference.

It is built on reliable scientific evidence and provides you with personalized advice based on your specific input.

This calculator requires [Python 3](https://www.python.org/downloads/) to run.

### Prompts

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

The default protein target is set to [2.2 g/kg<sub>LBM</sub>/day](https://pubmed.ncbi.nlm.nih.gov/28698222/).

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

Note that your neck circumference will have a large impact on the results.

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

- **Omega-3 EPA & DHA:** Ideally, an adult should consume between 2 and 6 grams per day for optimal health.<sup>[[1]](https://www.foundmyfitness.com/topics/omega-3#optimal-omega-3-intake-for-most-adults) [[2]](https://biolayne.com/articles/nutrition/fat-facts-fat-source-matters/)</sup>

- **Linoleic Acid:** The recommended intake is between 11 and 17 grams per day.<sup>[[1]](https://en.wikipedia.org/wiki/Essential_fatty_acid#Reference_intake_values)</sup>

##### Omega-3 EPA & DHA

This calculator specifically measures **EPA & DHA**, which are crucial types of Omega-3,
despite **alpha-linolenic acid** also being recognized as an essential Omega-3 fatty acid.
The reason for this lies in the observed inconsistencies within the individuals'
processes that convert ALA into EPA & DHA.<sup>[[1]](https://pubs.rsc.org/en/content/articlelanding/2018/FO/C7FO01809F)

There's a note of particular importance to those with the [APOE-4](https://www.foundmyfitness.com/topics/omega-3#apoe-4-and-alzheimer-39-s-disease) SNP.
It's suggested they place a higher precedence on the intake of Omega-3 from fish.

Studies prove that maintaining an [**Omega-3 Index of 8–11%**](https://www.foundmyfitness.com/topics/omega-3#long-term-measure-of-omega-3-intake) yields the greatest health benefits.
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
The calculator meticulously ensures that your optimal protein and fat goals are met according to your dietary needs. Given the remaining calories, you could customize your macro targets. This flexibility comes in handy when you want to modulate the macros according to your specific dietary regime.

### Available Options
1. **Favor Carbohydrates:** Allocate all remaining calories to carbs.
2. **Favor Fat:** Direct all remaining calories towards fats.
3. **Blend of Carbohydrates & Fats:** Distribute remaining calories evenly between carbohydrates and fats.
4. **Blend of Fat & Protein:** Split remaining calories evenly between fats and proteins.
5. **Blend of Carbohydrates & Protein:** Evenly divide remaining calories between carbohydrates and proteins.
6. **Blend of Carbohydrates, Fats, & Protein:** Distribute remaining calories amongst carbohydrates, fats, and proteins equally.

The distribution in mixed categories is done considering the caloric value per gram of each macro.

## Practical Application

### General Principles

When it comes to following a diet, certain general principles are universally acknowledged,
irrespective of the specific dietary choice. Here are the key points to remember:

- **Protein should be your top priority:** Protein is essential as it helps build and repair body tissues. Prioritize its consumption to ensure that your body gets an adequate supply every day.

- **Maximize Muscle Protein Synthesis (MPS):** MPS is a repair process that remodels and strengthens our muscles. You should strive to maximize this process.

- **Consider meal frequency:** Consuming four meals a day, evenly spaced will help maintain a steady supply of amino acids in the bloodstream throughout the day. Nonetheless, at a practical level, consuming two to four meals per day is acceptable and more feasible for most.

- **Pay attention to the first and last meals:** The first and last meals of the day play a vital role in providing the body with enough amino acids to prevent catabolism (the breakdown of muscle tissue). It's particularly important to ensure adequate protein intake after resistance training sessions.

- **Optimal protein quantity for MPS stimulation:** Research suggests that an intake of 20–40 grams<sup>[[1]](https://physoc.onlinelibrary.wiley.com/doi/10.14814/phy2.12893)</sup> <sup>[[2]](https://pubmed.ncbi.nlm.nih.gov/33300582/)</sup> of protein can optimally stimulate MPS. This will depend on the [leucine content](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6248570/) of the protein.

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

According to [published studies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4022420/), healthy resistance-trained individuals can safely consume up to **4.4 g/kg<sub>LBM</sub>/day** of protein.

###### [TEF Breakdown](https://pubmed.ncbi.nlm.nih.gov/8878356/)

- **Protein:** 20–30%
- **Carbs:** 5–10%
- **Fat:** 0–3%

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

Your WHtR should be less than 0.5 for optimal health.[[1]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4157748/)

#### Boundary Values
- 0.4–0.49: Healthy
- 0.5–0.59: Increased Central Adiposity
- 0.6+: High Central Adiposity

#### Example

Height: 5' 10" (70 inches)

Waist: 40 inches

40 inches / 70 inches = 0.57 (Elevated Health Risk)

### Exercise

#### Resistence Training

Each muscle group should be trained at least once per week to prevent muscle loss.

To gain muscle, training each muscle group twice per week is generally recommended.

Ideally, you would train each muscle group as soon as it is recovered to maximize hypertrophy.

Ensure that adequate volume is reached when training each muscle group.
This will depend on your muscle mass, recovery time, and experience.

#### Cardiovascular Training

Not only great to increase total daily energy expenditure,
cardio has been linked to [increased life span](https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm).

Benefits include:
- Increased VO2 max
- [Increased BDNF](https://www.foundmyfitness.com/topics/bdnf#bdnf-provides-a-possible-link-between-exercise-and-improved-brain-health)
- Lower Risk of Cardiovascular Disease
- Lower Risk of Certain Cancers
- Improved Outcomes with Infectious Diseases

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
- Layne Norton, PhD
- Rhonda Patrick, PhD

## Constants

- **Minimum Protein Intake:** [2.2 g/kg<sub>LBM</sub>/day](https://pubmed.ncbi.nlm.nih.gov/28698222/)
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