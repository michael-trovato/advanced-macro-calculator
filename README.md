# Advanced Macro Calculator
This calculator helps you optimize your nutritional intake and weight management strategies.
It is built on reliable scientific evidence and provides you with personalized advice based on your specific input.
To use this calculator, any recent version of [Python 3](https://www.python.org/downloads/) should work.

### Prompts

Please answer the prompts with the required information.

The calculator fully supports imperial and metric units.

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

The default protein target is set to 2.2 grams per kg of lean body mass.

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
Implementing hard stops ensures
your health is not compromised due to excessively quick weight change or extremely low caloric intake. 

### Weight Loss Measures
- Maximum weekly weight loss: 2 lbs (0.907 kg)
- Lowest daily caloric intake: 20% below the Basal Metabolic Rate (BMR)

### Weight Gain Measures
- Maximum weekly weight gain: 2 lbs (0.907 kg)
- Recommended weekly weight gain: Between 0.25 lbs (0.113 kg) and 0.5 lbs (0.226 kg) to minimize fat gain

### Understanding Dietary Fat Requirements for Optimal Health
To maintain good health and proper bodily functions, it's crucial to consume a minimum amount of fat every day. However, the scientific consensus regarding the precise amount required is yet to be reached. Thus, an estimated value with a 20% safety margin is commonly considered to ensure an adequate fat intake. 

One key aspect of dietary fats is to maintain the required level of essential fatty acids in our bodies to prevent deficiencies and related health issues. 

#### Essential Fatty Acids: The Daily Requirement
Below are the daily requirements of essential fatty acids:

- [Omega 3 DHA & EPA: Ideally, an adult should consume between 1.75 to 2.5 grams per day for optimal health.](https://www.foundmyfitness.com/topics/omega-3#optimal-omega-3-intake-for-most-adults)

- [Linoleic Acid: The recommended intake is between 11 to 17 grams per day.](https://en.wikipedia.org/wiki/Essential_fatty_acid#Reference_intake_values)

Consistently incorporating these essential fatty acids into your diet will contribute significantly to maintaining your overall health.

## Practical Application

### General Principles

While trying to be diet agnostic, there are certain principles that would be generally accepted.

- Prioritize protein consumption.
- Muscle Protein Synthesis should be maximized.
- Four meals per day (spaced evenly) will keep amino acids elevated in the blood stream throughout the day. However, two to four meals per day are practically acceptable.
- The first and last meals of the day are important to consume enough amino acids to stop catabolism, but getting enough proteins after resistence training is imperative.
- [40 to 50 grams](https://physoc.onlinelibrary.wiley.com/doi/10.14814/phy2.12893) of protein will optimally stimulate MPS. (Work in Progress)

#### Weight Loss

If your goal is to lose weight, then it would be wise to eat foods that have a higher satiety per calorie.

Fat would ideally come with the protein itself.

Be sure to reach your protein and fat targets!

##### Examples
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

Targeting a lower satiety per calorie will help you to consume more calories for weight gain.

##### Examples
- Fattier Meats
- Whole Fat Yogurt
- Sauteed Vegetables
- Whole Grains

### Waist to Height Ratio

One of the cheapest and yet powerful methods
of determining your health risk is the [Waist-to-height Ratio (WHtR)](https://en.wikipedia.org/wiki/Waist-to-height_ratio).

Measure your waist circumference around the naval, then divide that number by your height (in the same units).

Your WHtR should be less than 0.5.

#### Boundary Values
- 0.4 - 0.49: Healthy
- 0.5 - 0.59: Increased Central Adiposity
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
- Thyroid
- Testosterone

## Special Thanks

The following doctors have contributed greatly to my understanding of nutritional science.

- Mike Israetel, PhD
- Theodore (Ted) Naiman, MD
- Layne Norton, PhD
- Rhonda Patrick, PhD

## Constants

- Protein Intake: 2.2 g/kg LBM
- Minimum Fat Grams: 0.75 g/kg LBM
- Minimum Fat Grams Safety Factor: 20%
- Maximum Caloric Deficit Below BMR: 20%

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