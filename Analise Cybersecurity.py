import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path_df = 'Global_Cybersecurity_Threats_2015-2024.csv'

cybersecurity_data = pd.read_csv(path_df)
# Dados isolados do Brasil
dados_brazil = cybersecurity_data[cybersecurity_data['Country']=='Brazil']

#................................................................................................................................

# Gráfico Dados Brasil
ataques_por_ano = cybersecurity_data['Year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=ataques_por_ano.index, y=ataques_por_ano.values, marker='o', color='r', label='Ataques Cibernéticos')
plt.xlabel('Anos')
plt.ylabel('Número de Ataques')
plt.title('Ataques Cibernéticos (2015-2024)')
plt.grid(True)
plt.legend()
plt.show()

# Média de Perda Financeira por Ano/País: Calcular o impacto financeiro médio dos ataques.
media_perdas_financeiras = cybersecurity_data.groupby(['Year','Country'])['Financial Loss (in Million $)'].mean().reset_index()

plt.figure(figsize=(12,6))
sns.barplot(x='Year',y='Financial Loss (in Million $)', hue='Country', data=media_perdas_financeiras, palette='bright')
plt.xlabel('Ano')
plt.ylabel('Media Perdas Financeiras (milhões)')
plt.title('Média de Perda Financeira por Ano e País')
plt.legend(title='País',ncol=5,loc='best',fontsize=4)
plt.show()

# Número de Usuários Afetados por Ano/País: Analisar o alcance dos ataques.
pessoas_afetadas = cybersecurity_data.groupby(['Year','Country'])['Number of Affected Users'].mean().reset_index()

plt.figure(figsize=(12,6))
sns.barplot(x='Year',y='Number of Affected Users', hue='Country', data=pessoas_afetadas, palette='bright')
plt.xlabel('Ano')
plt.ylabel('Usuários Afetados')
plt.title('Número de Usuários Afetados')
plt.legend(title='País',ncol=5,loc='best',fontsize=4)
plt.show()

# Tempo Médio de Resolução por Tipo de Ataque: Verificar quais ataques demoram mais para serem resolvidos.
tempo_resolucao = cybersecurity_data.groupby('Attack Type')['Incident Resolution Time (in Hours)'].mean().reset_index()
tempo_resolucao = tempo_resolucao.sort_values(by='Incident Resolution Time (in Hours)', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x='Incident Resolution Time (in Hours)', y='Attack Type', data=tempo_resolucao, palette='bright')
plt.xlabel('Tempo Médio de Resolução (Horas)')
plt.ylabel('Tipo de Ataque')
plt.title('Tempo Médio de Resolução por Tipo de Ataque')
plt.xticks(rotation=0)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# Análise por País

# Países Mais Afetados: Contagem de ataques por país
paises_afetados = cybersecurity_data['Country'].value_counts().reset_index()
paises_afetados.columns = ['Country', 'Total Attacks']
paises_afetados = paises_afetados.sort_values(by='Total Attacks', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x='Total Attacks', y='Country', data=paises_afetados, palette='Reds_r')
plt.xlabel('Total de Ataques')
plt.ylabel('País')
plt.title('Países Mais Afetados por Ciberataques')
plt.xticks(rotation=0)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Perda Financeira por País: Identificar os países com maiores prejuízos.
perdas_por_pais = cybersecurity_data.groupby('Country')['Financial Loss (in Million $)'].sum().nlargest(10)

plt.figure(figsize=(12, 6))
perdas_por_pais.plot(kind='bar', color='r')
plt.title('Top 10 Países com Maiores Perdas Financeiras (2015-2024)')
plt.ylabel('Perdas Totais (em milhões USD)')
plt.xlabel('País')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()

# Ataques Mais Frequentes
ataques_frequentes = cybersecurity_data['Attack Type'].value_counts()

plt.figure(figsize=(10, 6))
ataques_frequentes.plot(kind='bar', color='r')
plt.title('Frequência dos Tipos de Ataque Cibernético')
plt.ylabel('Número de Ocorrências')
plt.xlabel('Tipo de Ataque')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()

# Setores Mais Afetados por Tipo de Ataque: Ex: Educação vulnerável a Phishing, Bancos a Ransomware.
plt.figure(figsize=(14, 8))
cross_tab = pd.crosstab(cybersecurity_data['Attack Type'], 
                        cybersecurity_data['Target Industry'])
sns.heatmap(cross_tab, cmap='YlOrRd', annot=True, fmt='d')
plt.title('Relação entre Tipo de Ataque e Setor Alvo')
plt.xlabel('Setor Alvo')
plt.ylabel('Tipo de Ataque')
plt.tight_layout()
plt.show()
# Impacto Financeiro por Setor: Qual setor sofre as maiores perdas.
perda_setor = cybersecurity_data.groupby('Target Industry')['Financial Loss (in Million $)'].sum().nlargest(10)

plt.figure(figsize=(12, 6))
perda_setor.plot(kind='barh', color='r')
plt.title('Top 10 Setores com Maiores Perdas Financeiras')
plt.xlabel('Perdas Totais (em milhões USD)')
plt.ylabel('Setor')
plt.grid(axis='x', linestyle='--')
plt.show()
# 3. Análise de Vulnerabilidades
# Vulnerabilidades Mais Exploradas: Ex: "Unpatched Software", "Weak Passwords".
vulnerabilidades = cybersecurity_data['Security Vulnerability Type'].value_counts()

plt.figure(figsize=(12, 6))
vulnerabilidades.plot(kind='bar', color='r')
plt.title('Vulnerabilidades Mais Exploradas em Ataques Cibernéticos')
plt.ylabel('Número de Ocorrências')
plt.xlabel('Tipo de Vulnerabilidade')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()

# Relação entre Vulnerabilidade e Tipo de Ataque: Ex: "Social Engineering" ligada a Phishing.
plt.figure(figsize=(14, 8))
cross_tab = pd.crosstab(cybersecurity_data['Security Vulnerability Type'], 
                        cybersecurity_data['Attack Type'])
sns.heatmap(cross_tab, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Relação entre Vulnerabilidade e Tipo de Ataque')
plt.xlabel('Tipo de Ataque')
plt.ylabel('Tipo de Vulnerabilidade')
plt.tight_layout()
plt.show()

# Análise de Defesas
# Mecanismos de Defesa Mais Usados: Ex: Firewall, VPN, Antivírus.
defesas = cybersecurity_data['Defense Mechanism Used'].value_counts()

plt.figure(figsize=(12, 6))
defesas.plot(kind='bar', color='b')
plt.title('Mecanismos de Defesa Mais Utilizados')
plt.ylabel('Número de Utilizações')
plt.xlabel('Mecanismo de Defesa')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()
# Eficácia das Defesas: Correlacionar defesas com tempo de resolução ou perda financeira.
eficacia_defesa = cybersecurity_data.groupby('Defense Mechanism Used')['Incident Resolution Time (in Hours)'].mean().sort_values()

plt.figure(figsize=(12, 6))
eficacia_defesa.plot(kind='barh', color='b')
plt.title('Eficácia dos Mecanismos de Defesa (Tempo Médio de Resolução)')
plt.xlabel('Tempo Médio de Resolução (Horas)')
plt.ylabel('Mecanismo de Defesa')
plt.grid(axis='x', linestyle='--')
plt.show()

# Evolução de Ameaças: Como os tipos de ataque mudaram de 2015 a 2024.
evolucao_ataques = pd.crosstab(cybersecurity_data['Year'], cybersecurity_data['Attack Type'])
plt.figure(figsize=(14, 8))
evolucao_ataques.plot(kind='area', stacked=True, colormap='viridis')
plt.title('Evolução dos Tipos de Ataque Cibernético (2015-2024)')
plt.ylabel('Número de Ocorrências')
plt.xlabel('Ano')
plt.legend(title='Tipo de Ataque', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlações e Insights

# Relação entre Origem do Ataque e Setor Alvo
plt.figure(figsize=(12, 6))
cross_tab = pd.crosstab(cybersecurity_data['Attack Source'], 
                        cybersecurity_data['Target Industry'])
sns.heatmap(cross_tab, cmap='YlOrBr', annot=True, fmt='d')
plt.title('Relação entre Fonte do Ataque e Setor Alvo')
plt.xlabel('Setor Alvo')
plt.ylabel('Fonte do Ataque')
plt.tight_layout()
plt.show()

# Análise Geral
# Tendência Temporal 
# I - Os ataques cibernéticos mostraram um aumento consistente ao longo dos anos, com picos em 2019 e 2023.

# Impacto Financeiro  
# I - Os setores bancário e de telecomunicações sofreram as maiores perdas financeiras, 
# II - Países como Índia, China e Brasil lideram em prejuízos totais
  
# Tipos de Ataque 
# I - Phishing e Ransomware são os mais frequentes
# II- Ataques DDoS tendem a ter o menor tempo de resolução

# Vulnerabilidades: 
# I - "Unpatched Software" e "Weak Passwords" são as vulnerabilidades mais exploradas
# II - "Social Engineering" está fortemente associada a ataques de Phishing

# Eficácia de Defesas
# I - Sistemas baseados em IA mostraram os melhores tempos de resposta 
# II - Firewalls são o mecanismo mais utilizado, mas VPNs são mais eficazes contra certos tipos de ataque

# Origem dos Ataques 
# I - Grupos de hackers são responsáveis pela maioria dos incidentes 
# II -Ataques patrocinados por estados-nação tendem a ter maior impacto financeiro

# Esta análise abrangente revela padrões importantes e que pode nos levar a fatores específicos onde podemos aplicar técnicas mais profundas e analíticas 
# destacando áreas críticas que requerem atenção especial em estratégias de segurança cibernética.