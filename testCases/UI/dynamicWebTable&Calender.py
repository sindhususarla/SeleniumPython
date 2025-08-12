#Choosing date from a calender
#Has table tag in the DOM
#tr is table row; td is table data ir column

select_date = "20-Dec-2022"

dates = select_date.split('-')

driver.find_element(By.ID, "onward_calender").click()

td = driver.find_elements(By.XPATH, "//div[@id='rb-calendar_onward_cal']//td")

for ele in td:
    if ele.text == dates[0]:
        ele.click()
        break


from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Calculate the date two days from today
future_date = today + timedelta(days=2)

# Format the date as a string (optional)
formatted_date = future_date.strftime('%Y-%m-%d')

print("Date two days from today:", formatted_date)
