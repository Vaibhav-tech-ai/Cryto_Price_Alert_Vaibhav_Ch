# Kryto_Task_Vaibhav_Ch
Basically there are 3 endpoints.

The first one being a create endpoint here the user could create an alert by his username and by inputting the crypto name and the price for which he is creating an alert. As soon as the values are entered the record in stored in the MongoDB. There are two tables one being the users and the other being the Alerts which stores everything along with the status. As soon as the create API is called first the user is added in the Users table and then the values are added in the Alerts table. One thing to be noticed is as soon as the create api is called the status is updated as created and pushed in the DB.

The second being a delete endpoint it basically searches for the alert on the basis of the user input and then updates its status to deleted.

The third one is used to fetch the alerts either by the username or by the status if the filter is being used by the user. So there can be two scenarios where the user is searching by using a filter on status hence only the selected status records will be shown to the user. Or else if the user wants all the alerts then he can simply search by his username then all the alerts irrespective of the status is shown. Along with that all the returned records are pageinated and is displayed in a JSON format.

The next thing is the main functionality where the email is triggered once the target price becomes same as the current price. So I used the external api where the prices of crypto is present then I am pushing those API values into a dictionary where the key is the crypto symbol and the value is it's current price and this process is going on all the time hence the values in the dictionary are getting updated and are checked paralelly with the values in our Database so that whenever the target price is reached a trigger is printed to the screen and also it's status is updated as triggered. Here I didn't use RabbitMQ instead used a script which would do the same functionality.

# How to run it
There are two files "app.py" and "externalapi.py" which have to be run paralelly to get the desired results. externalapi.py makes sure to update the dictionary with the recent price of the crypto symbol so that it can match with the alerts existing in the database. Hence two split terminals can be opened so that both the scripts can be run at the same time. functions.py contains all the used functions.

# Solution for sending alerts
Here I used a dictionary to store the values from the API so as to get the current price for each crypto symbol and later I matched it with my existing alerts from my database. Also I used a threshold value as the crypto market is very fickle hence as soon as it enters the range a trigger is generated and the message is printed on the screen. I couldn't use RabbitMQ because of the time but surely that would have been an efficient solution compared to this. 

# Things I learnt
Frankly this is the first time I tried to create API routes and thanks to KRYPTO I could learn whatever I could in these 24 hrs and create something which is functional. The whole learning curve was amazing and the time spent to finish this was invaluable. I tried so much to dockerize it in the end but was facing some errors so couldn't implement it but surely learnt to handle docker as well.

# Improvements
1. Ofcourse the email functionality could have been implemented.
2. RabbitMQ could have been used to trigger the emails.
3. Docker compose could have been implemented.
4. Authorization by JWT could have been implemented.
