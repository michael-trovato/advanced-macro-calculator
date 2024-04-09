# Simple Macro Calculator

## How to Use:

### Running:

[Python 3](https://www.python.org/downloads/) is required to run this calculator. The most recent version is recommended.

### Prompts:

Please answer the prompts with the required information.
If your body fat percentage isn't known,
then an average ideal body weight based on height will be used to estimate lean body mass.

If you have greater than average muscle mass for your weight and height, then it would be wise to find (DEXA, Bod Pod),
and enter your body fat percentage.

An accurate body fat percentage will ensure a proper protein target.

The default protein target is set to 2.2 grams per kg of lean body mass.

## Body Fat Percentage:

### Known:

If your body fat percentage is known through a reliable method of testing (DEXA, Bod Pod), then it will be used to calculate your lean body mass.

### Unknown:

If your body fat percentage is unknown, then an estimate will be calculated the following way. 

The initial weight and height is used to find ideal body weight.

For each inch from 5 feet, a 5 lb change is adjusted to the initial weight.

Then, lean body fat is calculated.

#### Male:

The initial weight is 110 lbs.

The ideal body fat percentage is set to 12.5%.

##### Example:

Height: 5' 10"

160 lbs = 110 lbs + (10 inches * 5 lbs)

#### Female:

The initial weight is 100 lbs.

The ideal body fat percentage is set to 22.5%.

##### Example:

Height: 5' 5"

125 lbs = 100 lbs + (5 inches * 5 lbs)

## Safety:

For practical purposes, certain hard stops have been implemented.

### Weight Loss Per Week:

A hard stop of 2 lbs per week has been implemented to prevent daily calories from dropping too low.

### Weight Gain Per Week:

A maximum gain of 1 lb per week is implemented.
However, it is recommended to target 0.25 lbs to 0.5 lbs per week to minimize fat gain.

### Optimal Dietary Fat Intake:

To maintain proper health status, a minimum daily amount of fat must be consumed.

Due to lack of scientific understanding,
the best effort approach is made for determining fat grams with a safety factor (20%).

It is important to maintain essential fatty acid status to avoid deficiencies.

#### Essential Fatty Acids:
- [Optimal Omega 3 DHA & EPA (1.75 to 2.5 grams daily)](https://www.foundmyfitness.com/topics/omega-3#optimal-omega-3-intake-for-most-adults)
- [Linoleic Acid (11 to 17 grams daily)](https://en.wikipedia.org/wiki/Essential_fatty_acid#Reference_intake_values)

## Special Thanks:

The following doctors have contributed greatly to my understanding of nutritional science.

- Mike Israetel, PhD
- Theodore (Ted) Naiman, MD
- Layne Norton, PhD
- Rhonda Patrick, PhD

## Disclaimers:

### Medical Disclaimer:

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

### Fitness Disclaimer:

The site cannot and does not contain fitness advice.
The fitness information is provided for general informational and educational purposes
only and is not a substitute for professional advice.
Before taking any actions based upon such information, we encourage you to consult with the appropriate professionals.
The use of any information provided on this site is solely at your own risk.