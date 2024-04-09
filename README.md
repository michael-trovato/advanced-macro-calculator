# Simple Macro Calculator

## How to Use

### Running

[Python 3](https://www.python.org/downloads/) is required to run this calculator. The most recent version is recommended.

### Prompts

Please answer the prompts with the required information.

The calculator fully supports imperial and metric units.

Users can choose to lose or gain weight based on percentage of body weight or fixed values (lbs or kg).

Useful when wanting to lose as a percentage of body weight per week while in a fat loss phase,
and gaining at fixed values during a muscle gain phase.

If your body fat percentage isn't known,
then an average ideal body weight based on height will be used to estimate lean body mass.

If you have greater than average muscle mass for your weight and height, then it would be wise to find (DEXA, Bod Pod),
and enter your body fat percentage.

An accurate body fat percentage will ensure a proper protein target per day as it is calculated based on lean body mass.

The default protein target is set to 2.2 grams per kg of lean body mass.

## Body Fat Percentage

### Known

If your body fat percentage is known through a reliable method of testing (DEXA, Bod Pod), then it will be used to calculate your lean body mass.

### Unknown

If your body fat percentage is unknown, then an estimate will be calculated the following way. 

First, your bmi is calculated with your weight and height.

Next, using the [Deurenberg formula](https://en.wikipedia.org/wiki/Body_fat_percentage#From_BMI), the body fat percentage is calculated.

Body Fat Percentage = (1.20 × BMI) + (0.23 × Age) − (10.8 × Sex) − 5.4

Lastly, lean body mass is calculated based on total body weight and the calculated body fat percentage.

## Safety Measures for Weight Change
For practical purposes,
hard stops are implemented to dictate the pace of weight change
and to ensure daily caloric intake does not drop too low.

### Weight Loss Measures
- A maximum weight loss limit of 2 lbs per week.
- The lowest daily caloric intake is 20% below the Basal Metabolic Rate (BMR).

### Weight Gain Measures
- A maximum weight gain limit of 2 lbs per week.
- The recommended target for weight gain is between 0.25 lbs (0.113 kg) to 0.5 lbs (0.226 kg) per week to minimize fat gain.

### Optimal Dietary Fat Intake

To maintain proper health status, a minimum daily amount of fat must be consumed.

Due to lack of scientific understanding,
the best effort approach is made for determining fat grams with a safety factor (20%).

It is important to maintain essential fatty acid status to avoid deficiencies.

#### Essential Fatty Acids
- [Optimal Omega 3 DHA & EPA (1.75 to 2.5 grams daily)](https://www.foundmyfitness.com/topics/omega-3#optimal-omega-3-intake-for-most-adults)
- [Linoleic Acid (11 to 17 grams daily)](https://en.wikipedia.org/wiki/Essential_fatty_acid#Reference_intake_values)

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
  - Turkey Breast
  - Wild Caught Salmon
  - Sardines
  - Chicken
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

- Grams Protein per kg LBM = 2.2
- Minimum Grams Fat per kg LBM = 0.75
- Minimum Grams Fat Safety Factor = 0.2

## Disclaimers

### Medical Disclaimer

The information provided by this calculator is for general informational purposes only.
All information on the site is provided in good faith,
however, we make no representation or warranty of any kind, express or implied, regarding the accuracy,
adequacy, validity, reliability, availability, or completeness of any information on the site.

Under no circumstance shall we have any liability to you for any loss or damage of any kind
incurred as a result of the use of the site or reliance on any information provided on the site.
Your use of the site and your reliance on any information on the site is solely at your own risk.

This site cannot and does not contain medical/health advice.
The medical/health information is provided for general informational and educational purposes
only and is not a substitute for professional advice.
Accordingly, before taking any actions based upon such information,
we encourage you to consult with the appropriate professionals.
The use of any information provided on this site is solely at your own risk.

### Fitness Disclaimer

The site cannot and does not contain fitness advice.
The fitness information is provided for general informational and educational purposes
only and is not a substitute for professional advice.
Before taking any actions based upon such information, we encourage you to consult with the appropriate professionals.
The use of any information provided on this site is solely at your own risk.