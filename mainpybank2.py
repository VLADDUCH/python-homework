{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "2475d1fa-e3b5-40da-a302-32856d2fd562",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-----------------------------------\n",
      "Total Months:86\n",
      "Total Profits: $38382578\n",
      "Average Change: $-2315.1176470588234  \n",
      "Greatest Increase in Profits: Date               Sep-2016\n",
      "Profit/Losses       1170593\n",
      "shifted_column    1170593.0\n",
      "diffence          1926159.0\n",
      "dtype: object  ($1926159.0)\n",
      "Greatest Decrease in Profits: -2196167.0 ($-2196167.0)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from pathlib import Path\n",
    "#Your task is to create a Python script that analyzes the records to calculate each of the following:\n",
    "#gip= Greatest Increase in ProfitsDecrease in Profits\"\n",
    "#gdp = Greatest decrease in profits\n",
    "#Extract data\n",
    "df = pd.read_csv('pybank.csv')\n",
    "#The total number of months included in the dataset.\n",
    "#use len for months the company records. ie\n",
    "total_months = df[\"Date\"].count()\n",
    "#The net total amount of Profit/Losses over the entire period.\n",
    "df['shifted_column'] = df['Profit/Losses'].shift(1)\n",
    "df['diffence'] = df['Profit/Losses'] - df['shifted_column']\n",
    "average = df['diffence'].mean()\n",
    "gip = df['diffence'].max()\n",
    "gdp = df['diffence'].min()\n",
    "#gip_date = df.loc['diffence'].max()\n",
    "\n",
    "#average = df[\"Profit/Losses\"].mean()\n",
    "#df['Profit/Losses'] = df['Profit/Losses'].shift()\n",
    "#df['difference'] = (df['Profit/Losses'].shift() - df['Profit/Losses'].shift(1)\n",
    "#df['difference'] = df['Profit/Losses'].abs()\n",
    "#average = df['difference'].mean()\n",
    "#gip_date = df['difference'].max()\n",
    "#gdp_date = df['difference'].min()\n",
    "\n",
    "#The greatest increase in profits (date and amount) over the entire period.\n",
    "#gip_date = df.loc[\"difference\"].max()\n",
    "#gip_date= df['difference'].mean()\n",
    "#GreatestIncrease = df[${:.0f}'.format(Bank_pd[\"Amount Changed\"].max())\n",
    "#gdp_date = df[\"Date\"].min()\n",
    "#The greatest decrease in losses (date and amount) over the entire period.\n",
    "#gdp = df[\"Profit/Losses\"]. min ()\n",
    "#print(\"Financial Analysis\")\n",
    "print(\"-----------------------------------\")\n",
    "print(f\"Total Months:{total_months}\")\n",
    "print(f\"Total Profits: ${total_profits}\")\n",
    "print(f\"Average Change: ${average}  \")\n",
    "print(f\"Greatest Increase in Profits: {gip_date}  (${gip})\")\n",
    "print(f\"Greatest Decrease in Profits: {gdp_date} (${gdp})\")\n",
    " \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4e670ab-9f26-48e1-9315-8370c69863fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6b4fd54-5308-483b-aa44-f26bb5b89d7d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f769ac1e-54f8-4217-bee5-524e566b549a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-2315.1176470588234\n"
     ]
    }
   ],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f886a43-b370-41ed-ba01-9c76506e0cf2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}