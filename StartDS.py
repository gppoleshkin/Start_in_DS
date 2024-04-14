import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_excel('stds.xlsx')
df = df.rename(columns={'Unnamed: 0': 'год'})

# Выводим сообщение
st.write("АНАЛИЗ ЗАРПЛАТ ПО РОССИИ")
st.write("Для начала, ознакомимся с нашими данными:")
st.write("Наш датасет состоит из несколькиз колонок: средняя зарплата по экономике в целом и отдельным секторам, а также темпы инфляции и роста ВВП")
df

df['Прирост % Всего по  экономике'] = df['Всего по  экономике'].pct_change()* 100
df['Прирост % Производство кокса и нефтепродуктов'] = df['Производство кокса и нефтепродуктов'].pct_change()* 100
df['Прирост % Финансовая деятельность'] = df['Финансовая деятельность'].pct_change()* 100
df['Прирост % Образование'] = df['Образование'].pct_change()* 100

# вычисляем средний прирост по каждой колонке
mean_growth_total = df['Прирост % Всего по  экономике'].mean()
mean_growth_coke = df['Прирост % Производство кокса и нефтепродуктов'].mean()
mean_growth_finance = df['Прирост % Финансовая деятельность'].mean()
mean_growth_education = df['Прирост % Образование'].mean()
mean_inflation = df['Инфляция'].mean()
mean_gdp = df['Прирост ВВП'].mean()

# вычисляем средний прирост по каждой колонке
mean_growth_total = df['Прирост % Всего по  экономике'].mean()
mean_growth_coke = df['Прирост % Производство кокса и нефтепродуктов'].mean()
mean_growth_finance = df['Прирост % Финансовая деятельность'].mean()
mean_growth_education = df['Прирост % Образование'].mean()
mean_inflation = df['Инфляция'].mean()
mean_gdp = df['Прирост ВВП'].mean()

# Создаем новую колонку 'Всего по экономике с учетом инфляции'
df['Всего по  экономике с учетом инфляции'] = df['Всего по  экономике'].copy()

# Пересчитываем среднюю зарплату 'Всего по  экономике' с учетом инфляции начиная с 2001 года
for i in range(1, len(df)):
    df.at[i, 'Всего по  экономике с учетом инфляции'] = df.at[i, 'Всего по  экономике'] * (1 + df.at[i, 'Инфляция']/100)

# Пересчитываем среднюю зарплату для сектора 'Производство кокса и нефтепродуктов' с учетом инфляции
df['Производство кокса и нефтепродуктов с учетом инфляции'] = df['Производство кокса и нефтепродуктов'].copy()
for i in range(1, len(df)):
    df.at[i, 'Производство кокса и нефтепродуктов с учетом инфляции'] = df.at[i, 'Производство кокса и нефтепродуктов'] * (1 + df.at[i, 'Инфляция']/100)

# Пересчитываем среднюю зарплату для сектора 'Финансовая деятельность' с учетом инфляции
df['Финансовая деятельность с учетом инфляции'] = df['Финансовая деятельность'].copy()
for i in range(1, len(df)):
    df.at[i, 'Финансовая деятельность с учетом инфляции'] = df.at[i, 'Финансовая деятельность'] * (1 + df.at[i, 'Инфляция']/100)

# Пересчитываем среднюю зарплату для сектора 'Образование' с учетом инфляции
df['Образование с учетом инфляции'] = df['Образование'].copy()
for i in range(1, len(df)):
    df.at[i, 'Образование с учетом инфляции'] = df.at[i, 'Образование'] * (1 + df.at[i, 'Инфляция']/100)


##################


# Создаем новую колонку 'Всего по экономике с учетом роста ВВП'
df['Всего по  экономике с учетом роста ВВП'] = df['Всего по  экономике'].copy()

# Пересчитываем среднюю зарплату 'Всего по  экономике' с учетом роста ВВП начиная с 2001 года
for i in range(1, len(df)):
    df.at[i, 'Всего по  экономике с учетом прироста ВВП'] = df.at[i, 'Всего по  экономике'] * (1 + df.at[i, 'Прирост ВВП']/100)

# Пересчитываем среднюю зарплату для сектора 'Производство кокса и нефтепродуктов' с учетом роста ВВП
df['Производство кокса и нефтепродуктов с учетом прироста ВВП'] = df['Производство кокса и нефтепродуктов'].copy()
for i in range(1, len(df)):
    df.at[i, 'Производство кокса и нефтепродуктов с учетом прироста ВВП'] = df.at[i, 'Производство кокса и нефтепродуктов'] * (1 + df.at[i, 'Прирост ВВП']/100)

# Пересчитываем среднюю зарплату для сектора 'Финансовая деятельность' с учетом роста ВВП
df['Финансовая деятельность с роста ВВП'] = df['Финансовая деятельность'].copy()
for i in range(1, len(df)):
    df.at[i, 'Финансовая деятельность с учетом прироста ВВП'] = df.at[i, 'Финансовая деятельность'] * (1 + df.at[i, 'Прирост ВВП']/100)

# Пересчитываем среднюю зарплату для сектора 'Образование' с учетом роста ВВП
df['Образование с учетом роста прироста ВВП'] = df['Образование'].copy()
for i in range(1, len(df)):
    df.at[i, 'Образование с учетом прироста ВВП'] = df.at[i, 'Образование'] * (1 + df.at[i, 'Прирост ВВП']/100)

st.write("Наибольшие значения прироста прироста зарплат и инфляции соответствует началу нулевых")

# Строим графики для каждой колонки с процентным приростом и задаем каждому свой цвет
fig, ax = plt.subplots()
ax.plot(df['год'], df['Прирост % Всего по  экономике'], marker='o', color='r', label='Прирост % Всего по экономике')
ax.plot(df['год'], df['Прирост % Производство кокса и нефтепродуктов'], marker='o', color='g', label='Прирост % Производство кокса и нефтепродуктов')
ax.plot(df['год'], df['Прирост % Финансовая деятельность'], marker='o', color='b', label='Прирост % Финансовая деятельность')
ax.plot(df['год'], df['Прирост % Образование'], marker='o', color='c', label='Прирост % Образование')
ax.plot(df['год'], df['Инфляция'], marker='o', color='y', label='Инфляция')
plt.title('Сравнение приростов по годам')
plt.xlabel('год')
plt.ylabel('Прирост, %')
plt.legend()
plt.grid(True)

# Отображаем график в Streamlit
st.pyplot(fig)

# Создаем график для отображения среднего прироста как столбиков
fig1, ax1 = plt.subplots(figsize=(14, 10))
ax1.bar(['Всего по экономике', 'Производство кокса и н/п', 'Фин. деятельность', 'Образование', 'Инфляция', 'ВВП'],
        [mean_growth_total, mean_growth_coke, mean_growth_finance, mean_growth_education, mean_inflation, mean_gdp],
        color=['r', 'g', 'b', 'c','y', 'brown'])
plt.title('Средний прирост по секторам')
plt.xlabel('Сектор')
plt.ylabel('Средний прирост, %')


# Создаем график для отображения среднего прироста как столбиков
fig1, ax1 = plt.subplots(figsize=(14, 10))
ax1.bar(['Всего по экономике', 'Производство кокса и н/п', 'Фин. деятельность', 'Образование', 'Инфляция', 'ВВП'],
        [mean_growth_total, mean_growth_coke, mean_growth_finance, mean_growth_education, mean_inflation, mean_gdp],
        color=['r', 'g', 'b', 'c','y', 'brown'])
plt.title('Средний прирост по секторам')
plt.xlabel('Сектор')
plt.ylabel('Средний прирост, %')

# Отображаем график среднего прироста в Streamlit
st.pyplot(fig1)

# Вычисляем корреляцию прироста по каждому сектору с приростом 'Прирост % Всего по экономике'
correlation_1 = df['Прирост % Всего по  экономике'].corr(df['Прирост % Производство кокса и нефтепродуктов'])
correlation_2 = df['Прирост % Всего по  экономике'].corr(df['Прирост % Финансовая деятельность'])
correlation_3 = df['Прирост % Всего по  экономике'].corr(df['Прирост % Образование'])

# Выводим сообщение
st.write("Рост зарплат в конкрентных секторах отлично коррелирует общим приростом")
# Создаем график для отображения корреляции как столбиков
fig2, ax2 = plt.subplots(figsize=(14, 9))
ax2.bar(['Производство кокса и нефтепродуктов', 'Финансовая деятельность', 'Образование'],
        [correlation_1, correlation_2, correlation_3],
        color=['r', 'g', 'b'])
plt.title('Корреляция прироста по секторам с приростом по экономике')
plt.xlabel('Сектор')
plt.ylabel('Корреляция')

# Отображаем график корреляции в Streamlit
st.pyplot(fig2)

# Создаем фигуру
fig3, axs = plt.subplots(2, 2, figsize=(16, 8))

# График для 'Всего по экономике' и 'Всего по экономике с учетом инфляции'
axs[0, 0].plot(df['год'], df['Всего по  экономике'], marker='o', label='Всего по экономике')
axs[0, 0].plot(df['год'], df['Всего по  экономике с учетом инфляции'], marker='o', label='Всего по экономике с учетом инфляции')
axs[0, 0].plot(df['год'], df['Всего по  экономике с учетом прироста ВВП'], marker='o', label='Всего по  экономике с учетом прироста ВВП')
axs[0, 0].set_title('Зарплата в экономике с учетом инфляции и роста ВВП')
axs[0, 0].set(xlabel='год', ylabel='Средняя Зарплата')
axs[0, 0].legend()

# График для 'Производство кокса и нефтепродуктов' и 'Производство кокса и нефтепродуктов с учетом инфляции'
axs[0, 1].plot(df['год'], df['Производство кокса и нефтепродуктов'], marker='o', label='Производство кокса и нефтепродуктов')
axs[0, 1].plot(df['год'], df['Производство кокса и нефтепродуктов с учетом инфляции'], marker='o', label='Производство кокса и нефтепродуктов с учетом инфляции')
axs[0, 1].plot(df['год'], df['Производство кокса и нефтепродуктов с учетом прироста ВВП'], marker='o', label='Производство кокса и нефтепродуктов с учетом прироста ВВП')
axs[0, 1].set_title('Зарплата в секторе "Производство кокса и нефтепродуктов" с учетом инфляции и роста ВВП')
axs[0, 1].set(xlabel='год', ylabel='Средняя Зарплата')
axs[0, 1].legend()

# График для 'Финансовая деятельность' и 'Финансовая деятельность с учетом инфляции'
axs[1, 0].plot(df['год'], df['Финансовая деятельность'], marker='o', label='Финансовая деятельность')
axs[1, 0].plot(df['год'], df['Финансовая деятельность с учетом инфляции'], marker='o', label='Финансовая деятельность с учетом инфляции')
axs[1, 0].plot(df['год'], df['Финансовая деятельность с учетом прироста ВВП'], marker='o', label='Финансовая деятельность с учетом прироста ВВП')
axs[1, 0].set_title('Зарплата в секторе "Финансовая деятельность" с учетом инфляции и роста ВВП')
axs[1, 0].set(xlabel='год', ylabel='Средняя Зарплата')
axs[1, 0].legend()

# График для 'Образование' и 'Образование с учетом инфляции'
axs[1, 1].plot(df['год'], df['Образование'], marker='o', label='Образование')
axs[1, 1].plot(df['год'], df['Образование с учетом инфляции'], marker='o', label='Образование с учетом инфляции')
axs[1, 1].plot(df['год'], df['Образование с учетом прироста ВВП'], marker='o', label='Образование с учетом роста прироста ВВП')
axs[1, 1].set_title('Зарплата в секторе "Образование" с учетом инфляции и роста ВВП')
axs[1, 1].set(xlabel='год', ylabel='Средняя Зарплата')
axs[1, 1].legend()

plt.tight_layout()

# Отображаем графики в Streamlit
st.pyplot(fig3)

#Последний график

years = df['год'].unique()
salaries_total = df['Всего по  экономике']
salaries_inflation = df['Всего по  экономике с учетом инфляции']
salaries_gdp_growth = df['Всего по  экономике с учетом прироста ВВП']

plt.figure(figsize=(14, 7))
bar_width = 0.3
bar_positions_total = np.arange(len(years))
bar_positions_inflation = bar_positions_total + bar_width
bar_positions_growth = bar_positions_inflation + bar_width

plt.bar(bar_positions_total, salaries_total, bar_width, label='Всего по экономике', color='r')
plt.bar(bar_positions_inflation, salaries_inflation, bar_width, label='Всего по экономике с учетом инфляции', color='g')
plt.bar(bar_positions_growth, salaries_gdp_growth, bar_width, label='Всего по экономике с учетом прироста ВВП', color='b')

plt.xlabel('Год')
plt.ylabel('Средняя зарплата в России')
plt.title('Зарплаты по годам в разных условиях')
plt.xticks(bar_positions_inflation, years)
plt.legend()

# Отображаем график в Streamlit
st.pyplot()

# Выводим сообщение
st.write("Вывод:")
st.write("На основании анализа данных можно сказать, что рост номинальной зарплаты отстает от инфляции и роста ВВП, но это отставание некритичное и достаточно мало")