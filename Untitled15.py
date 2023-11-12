#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


from pandasql import sqldf


# In[32]:


covid_deaths=pd.read_excel(r'/Users/macuser/Documents/Projects/CovidDeaths.xlsx')
covid_deaths


# In[34]:


covid_vaccinations = pd.read_excel(r'/Users/macuser/Documents/Projects/CovidVaccinations.xlsx')
covid_vaccinations


# In[55]:


query ='select * from covid_deaths where continent is not null order by 3,4'
sqldf(query)


# In[39]:


query ='select location, date, total_cases, new_cases, total_deaths, population from covid_deaths order by 1,2'
sqldf(query)


# In[49]:


#total cases vs total deaths(shows the likelihood of dying if you contract covid in your country)
query ='select location, date, total_cases, total_deaths,(total_deaths/total_cases)*100 as death_percentage from covid_deaths where location like "%states%" order by 1,2'
sqldf(query)


# In[53]:


#looking at the total cases vs population
#shows what percentage of population got covid
query ='select location,max(total_cases) as highestinfectioncount, population,max((total_cases/population))*100 as percentpopulationinfected from covid_deaths group by location, population order by percentpopulationinfected desc'
sqldf(query)


# In[57]:


#showing countries with highest death count per population
query ='select location,max(total_deaths) as totaldeathcount from covid_deaths where continent is not null group by location order by totaldeathcount desc'
sqldf(query)


# In[60]:


#let's break things down by continent
query ='select continent,max(total_deaths) as totaldeathcount from covid_deaths where continent is not null group by continent order by totaldeathcount desc'
sqldf(query)


# In[66]:


#global numbers
query ='select date,sum(new_cases) as total cases, sum(cast(new_deaths as int)) as total deaths,sum(cast(new_deaths as int))/sum(new_cases)*100 as death_percentage from covid_deaths where continent is not null group by date order by 1,2'
sqldf(query)


# In[67]:


#looking at total population vs vaccinations
query ='select * from covid_deaths dea join covid_vaccinations vac on dea.location = vac.location and dea.date = vac.date'
sqldf(query)


# In[79]:


#looking at total population vs vaccinations
query ='select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,sum(vac.new_vaccinations) over (partition by dea.location order by dea.location, dea.date) as Rollingpeoplevaccinated, from covid_deaths dea join covid_vaccinations vac on dea.location = vac.location and dea.date = vac.date where dea.continent is not null order by 2,3'
sqldf(query)


# In[85]:


#Use temp table

query ='create table (continent nvarchar(255),date datetime, population numeric,new_vaccinations numeric, rollingpeoplevaccinated) insert into select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,sum(vac.new_vaccinations) over (partition by dea.location order by dea.location, dea.date) as Rollingpeoplevaccinated, from covid_deaths dea join covid_vaccinations vac on dea.location = vac.location and dea.date = vac.date where dea.continent is not null)'
sqldf(query)


# In[ ]:





# In[ ]:




