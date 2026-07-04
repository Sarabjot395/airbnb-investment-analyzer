{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "debe0aba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"../data/raw/AB_US_2020.csv\", low_memory=False)\n",
    "\n",
    "# Work on a copy, keep df as your \"checkpoint\" if needed\n",
    "df_clean = df.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b55a6b5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             id                                               name    host_id  \\\n",
      "15434  43806155  Beautiful 14th floor view mins from MGH - Evonify  212359760   \n",
      "27734  43806155  Beautiful 14th floor view mins from MGH - Evonify  212359760   \n",
      "\n",
      "      host_name neighbourhood_group   neighbourhood  latitude  longitude  \\\n",
      "15434   Evonify                 NaN        West End  42.36461  -71.06792   \n",
      "27734   Evonify                 NaN  East Cambridge  42.36461  -71.06792   \n",
      "\n",
      "             room_type  price  minimum_nights  number_of_reviews last_review  \\\n",
      "15434  Entire home/apt    222              13                  0         NaN   \n",
      "27734  Entire home/apt    299              13                  0         NaN   \n",
      "\n",
      "       reviews_per_month  calculated_host_listings_count  availability_365  \\\n",
      "15434                NaN                              45               150   \n",
      "27734                NaN                               1                 0   \n",
      "\n",
      "            city  \n",
      "15434     Boston  \n",
      "27734  Cambridge  \n"
     ]
    }
   ],
   "source": [
    "dup_id = df_clean[df_clean['id'].duplicated(keep=False)]\n",
    "print(dup_id)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "be1a3c43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows before: 226030, Rows after: 226029\n"
     ]
    }
   ],
   "source": [
    "# If they're essentially identical, keep the first occurrence\n",
    "df_clean = df_clean.drop_duplicates(subset='id', keep='first')\n",
    "\n",
    "print(f\"Rows before: {len(df)}, Rows after: {len(df_clean)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6aecc423",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "196520    100000000\n",
       "121846         1250\n",
       "196514         1125\n",
       "98220          1125\n",
       "45259          1125\n",
       "46094          1125\n",
       "178099         1125\n",
       "47771          1125\n",
       "45561          1124\n",
       "44590          1124\n",
       "120716         1124\n",
       "90377          1123\n",
       "178711         1000\n",
       "88138          1000\n",
       "88146          1000\n",
       "44445          1000\n",
       "89345          1000\n",
       "119475         1000\n",
       "181110         1000\n",
       "97515          1000\n",
       "Name: minimum_nights, dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_clean['minimum_nights'].sort_values(ascending=False).head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ae41947d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows after minimum_nights fix: 225964\n"
     ]
    }
   ],
   "source": [
    "df_clean = df_clean[df_clean['minimum_nights'] <= 365]\n",
    "print(f\"Rows after minimum_nights fix: {len(df_clean)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8c7d8e91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "99th percentile price: 1700.0\n",
      "Rows after price cleaning: 223667\n"
     ]
    }
   ],
   "source": [
    "# Remove $0 listings — not real bookable prices\n",
    "df_clean = df_clean[df_clean['price'] > 0]\n",
    "\n",
    "# Use percentile-based capping rather than an arbitrary number\n",
    "upper_limit = df_clean['price'].quantile(0.99)\n",
    "print(f\"99th percentile price: {upper_limit}\")\n",
    "\n",
    "df_clean = df_clean[df_clean['price'] <= upper_limit]\n",
    "print(f\"Rows after price cleaning: {len(df_clean)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4503b612",
   "metadata": {},
   "outputs": [],
   "source": [
    "# neighbourhood_group: structural, not random — don't fabricate it, just label it clearly\n",
    "df_clean['neighbourhood_group'] = df_clean['neighbourhood_group'].fillna('Not Reported')\n",
    "\n",
    "# last_review / reviews_per_month: missing because zero reviews exist — 0 is the correct fill, not \"unknown\"\n",
    "df_clean['reviews_per_month'] = df_clean['reviews_per_month'].fillna(0)\n",
    "# last_review stays missing — there's no fake date that would make sense here; we'll just remember why when we use it later\n",
    "\n",
    "# name / host_name: negligible, safe to drop those few rows\n",
    "df_clean = df_clean.dropna(subset=['name', 'host_name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a2d73032",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/xy/kfvm92f11z3481brx08h09mm0000gn/T/ipykernel_55157/1051192382.py:1: UserWarning: Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.\n",
      "  df_clean['last_review'] = pd.to_datetime(df_clean['last_review'], errors='coerce')\n"
     ]
    }
   ],
   "source": [
    "df_clean['last_review'] = pd.to_datetime(df_clean['last_review'], errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7dae9139",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final cleaned shape: (223610, 17)\n"
     ]
    }
   ],
   "source": [
    "df_clean.to_csv(\"../data/processed/AB_US_2020_cleaned.csv\", index=False)\n",
    "print(f\"Final cleaned shape: {df_clean.shape}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9718afc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv (3.12.13)",
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
   "version": "3.12.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
