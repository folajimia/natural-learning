"""import pandas as pd
#from sk_learn import linear_model
from sk_learn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values=dataframe[['Body']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_value, y_values)

#visualize results
plt.scatter(x_value, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()


from sk_learn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_values. y_values)


>>> print(model.predict([ [127], [248] ]))
[[ 438.94308857, 127.14839521]]"""




# TODO: Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression


# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv("bmi_and_life_expectancy.csv", delimiter=',')
x_values = bmi_life_data[['BMI']]
y_values = bmi_life_data[['Life expectancy']]

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(x_values,y_values)

# Mak a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict(21.07931)
