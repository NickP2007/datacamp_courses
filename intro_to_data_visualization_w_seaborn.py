# MAKING A SCATTER PLOT WITH LISTS
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

# MAKING A COUNT PLOT WITH A LIST
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt 
import seaborn as sns


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

# TIDY vs. UNTIDY DATA
# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())

# MAKING A COUNT PLOT WITH A DATAFRAME
# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt 
import pandas  as pd 
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()

# HUE AND SCATTER PLOTS
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=['Rural','Urban'])

# Show plot
plt.show()

# HUE AND COUNT PLOTS
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school',data=student_data,hue='location',palette=palette_colors)



# Display plot
plt.show()

# CREATING SUBPLOTS WITH COL AND ROW
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row='study_time')

# Show plot
plt.show()

# CREATING TWO-FACTOR SUBPLOTS
# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col='schoolsup',
            col_order=["yes", "no"],
            row="famsup",
            row_order=['yes','no']
            )

# Show plot
plt.show()

# CHANGING THE SIZE OF SCATTER PLOT POINTS
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",hue='cylinders')

# Show plot
plt.show()

# CHANGING THE STYLE OF SCATTER PLOT POINTS
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration',y='mpg',data=mpg,kind='scatter',hue='origin',size='origin',style='origin')



# Show plot
plt.show()

# VISUALIZING STANDARD DEVIATION WITH LINE PLOTS
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",ci='sd')

# Show plot
plt.show()

# PLOTTING SUBGROUPS IN LINE PLOTS
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",dashes=False,markers=True)

# Show plot
plt.show()

# COUNT PLOTS
# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")

# Show plot
plt.show()

# BAR PLOTS WITH PERCENTAGES
# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender',y='Interested in Math',data=survey_data,kind='bar')


# Show plot
plt.show()

# CUSTOMIZING BAR PLOTS
# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            ci=None)

# Show plot
plt.show()

# CREATE AND INTERPRET A BOX PLOT
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(data=student_data,kind='box',x='study_time',y='G3',order=study_time_order)




# Show plot
plt.show()

# OMITTING OUTLIERS
# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet',y='G3',data=student_data,col='location',kind='box',sym='',hue='location')

# Show plot
plt.show()

# ADJUSTING THE WHISKERS
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0,100])

# Show plot
plt.show()

# CUSTOMIZING POINT PLOTS
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join=False)
            
# Show plot
plt.show()

# POINT PLOTS WITH SUBGROUPS
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()

# CHANGING STYLE AND PALETTE
# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

# CHANGING THE SCALE
# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# USING A CUSTOM PALETTE
# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
sns.set_palette(['#39A7D0','#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()

# FACETGRIDS VS AXESSUBPLOTS
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)

# ADDING A TITLE TO A FACETGRID OBJECT
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle('Car Weight vs. Horsepower')

# Show plot
plt.show()

# ADDING A TITLE AND AXIS LABELS
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel='Car Model Year',ylabel='Average MPG')


# Show plot
plt.show()

# ROATATING X-TICKS AND LABELS
# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()

# BOX PLOT WITH SUBGROUPS
# Set palette to "Blues"
sns.set_palette('Blues')

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue='Interested in Pets')

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle('Age of Those Interested in Pets vs. Not')

# Show plot
plt.show()

# BAR PLOT WITH SUBGROUPS AND SUBPLOTS
# Set the figure style to "dark"
sns.set_style('dark')

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col='Gender')

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()

