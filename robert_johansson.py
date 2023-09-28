import matplotlib.pyplot as plt
import pandas as pd
df_rain2014 = pd.read_csv('rain_2014.csv')
df_rain2015 = pd.read_csv('rain_2015.csv')
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
rain_per_month = []
rain_2014 = []
rain_2015 = []
rain_sum_2015 = df_rain2015.sum()
rain_sum_2014 = df_rain2014.sum()
for month in months:
    rain_per_month.append(rain_sum_2015[month])
    rain_2014.append(rain_sum_2014[month])
    rain_2015.append(rain_sum_2015[month])
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Plot 1
axes[0,0].plot(months, rain_per_month, linestyle="-", label='y1 label')
axes[0,0].set_title('Rainfall per month 2015')

# Plot 2
explode = (0,0,0,0,0,0,0.15,0,0,0,0,0)
axes[0,1].pie(rain_per_month,explode=explode,labels=months,startangle=0,colors=plt.cm.Paired.colors)
axes[0,1].set_title('Rainfall distrubution 2015')

# Plot 3
axes[1,0].bar(months, rain_2014, color='blue')
axes[1,0].bar(months, rain_2015, bottom=rain_2014, color='orange')
axes[1,0].set_title('Rainfall Comparison 2015 and 2014')

# Plot 4
image = plt.imread('umbrella.jpg')
axes[1,1].imshow(image)
axes[1,1].axis('off')

plt.tight_layout()
plt.show()