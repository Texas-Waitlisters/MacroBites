# MacroBites

## Inspiration
Two of the members on our team are diabetic, and are supposed to eat foods that have a specific ratio of grams of carbohydrates to grams of protein in order to keep their blood sugar in check. When going to restaurants, it's often tedious and difficult to find nutritional information for foods and be able to compare them in a timely manner. People who have other dietary restrictions, or are on a diet, or are trying to bulk/cut also have similar problems.

## What it does
MacroBites solves this problem by allowing you to search by restaurant or individual food and get specific information about the amount and ratios of macronutrients that the foods have. You can also set your goal macronutrient ratios in your profile, and then get results that rank foods based on how close they are to your goal ratio.

## How we built it
We built the backend with a Python program that queries the Nutritionix API for information, and then used Flask to create endpoints for the different methods we were going to use. The frontend was made with React Native so that the app would be available on as many platforms as possible.

## Challenges we ran into
We had issues interacting with the Nutritionix API between rate limits, confusing documentation, and some features we wish they provided.

## Accomplishments that I'm proud of
We're really proud of how good our app looks! The color scheme, layout and UI are very slick (at least, we think so).

## What's next for MacroBites
We'd like to implement tracking for different types of nutrients (like micronutrients), a function to let you favorite specific foods, and more.

