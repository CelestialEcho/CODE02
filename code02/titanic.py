import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('titanic.csv')

# Приведение типов
df['Sex'] = df['Sex'].astype(str)
df['Pclass'] = df['Pclass'].astype(str)

survival_gender = df.groupby('Sex')['Survived'].mean()


"""
Sen avulla me ymmärämme, että naiset selvisivät huomattavasti useammin kuin miehet.
"""
plt.figure()
survival_gender.plot(kind='bar')
plt.title('Selviytymisaste sukupuolen mukaan')
plt.xlabel('Sukupuoli')
plt.ylabel('Selviytymisaste')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

survival_class = df.groupby('Pclass')['Survived'].mean()


"""
Ensimmäisen luokan matkustajilla oli korkein selviytymisaste.
"""
plt.figure()
survival_class.plot(kind='bar')
plt.title('Selviytymisaste matkustusluokan mukaan')
plt.xlabel('Matkustusluokka')
plt.ylabel('Selviytymisaste')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


"""
Ikäjakauma osoittaa, että suurin osa matkustajista oli nuoria aikuisia.
"""
plt.figure()
df['Age'].dropna().plot(kind='hist', bins=80)
plt.title('Ikäjakauma')
plt.xlabel('Ikä')
plt.ylabel('Matkustajien määrä')
plt.tight_layout()
plt.show()
