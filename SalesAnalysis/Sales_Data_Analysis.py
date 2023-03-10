{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c1fbcb55-3a6b-4de6-b391-8073a9b9d01a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Import Necessary Libraries "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "abfe3b7c-9be9-4295-94d5-df78b5d5eb6b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import os \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7d3f085a-44b8-40aa-8bfe-fe0685b107e3",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#TASK 1: Merge 12 months of sale data into single csv file "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2fb482a6-89bc-40f6-95c2-f9c289861aae",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')\n",
    "\n",
    "files = [file for file in os.listdir('./Sales_Data')]\n",
    "\n",
    "all_months_data = pd.DataFrame()\n",
    "\n",
    "for file in files:\n",
    "    df = pd.read_csv('./Sales_Data/'+file)\n",
    "    all_months_data = pd.concat([all_months_data, df])\n",
    "    \n",
    "all_months_data.to_csv('all_month.csv', index = False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c7e8da04-8f0e-4aa9-943b-ffbcbc8fd86d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#read in updated dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0f5c19e8-168e-4644-8fc0-08a288cc3ff0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity Ordered</th>\n",
       "      <th>Price Each</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Purchase Address</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>176558</td>\n",
       "      <td>USB-C Charging Cable</td>\n",
       "      <td>2</td>\n",
       "      <td>11.95</td>\n",
       "      <td>04/19/19 08:46</td>\n",
       "      <td>917 1st St, Dallas, TX 75001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>176559</td>\n",
       "      <td>Bose SoundSport Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>99.99</td>\n",
       "      <td>04/07/19 22:30</td>\n",
       "      <td>682 Chestnut St, Boston, MA 02215</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>176560</td>\n",
       "      <td>Google Phone</td>\n",
       "      <td>1</td>\n",
       "      <td>600</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>176560</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Order ID                     Product Quantity Ordered Price Each  \\\n",
       "0   176558        USB-C Charging Cable                2      11.95   \n",
       "1      NaN                         NaN              NaN        NaN   \n",
       "2   176559  Bose SoundSport Headphones                1      99.99   \n",
       "3   176560                Google Phone                1        600   \n",
       "4   176560            Wired Headphones                1      11.99   \n",
       "\n",
       "       Order Date                      Purchase Address  \n",
       "0  04/19/19 08:46          917 1st St, Dallas, TX 75001  \n",
       "1             NaN                                   NaN  \n",
       "2  04/07/19 22:30     682 Chestnut St, Boston, MA 02215  \n",
       "3  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001  \n",
       "4  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_month = pd.read_csv(\"all_month.csv\")\n",
    "all_month.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "cca74752-9843-4f69-a4f6-abfed4a8d052",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "######Cleam up the data\n",
    "#find rows with NaN Data "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6035c1f5-8592-4e9d-ac23-8140b4556925",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity Ordered</th>\n",
       "      <th>Price Each</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Purchase Address</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>356</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>735</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1433</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1553</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Order ID Product Quantity Ordered Price Each Order Date Purchase Address\n",
       "1         NaN     NaN              NaN        NaN        NaN              NaN\n",
       "356       NaN     NaN              NaN        NaN        NaN              NaN\n",
       "735       NaN     NaN              NaN        NaN        NaN              NaN\n",
       "1433      NaN     NaN              NaN        NaN        NaN              NaN\n",
       "1553      NaN     NaN              NaN        NaN        NaN              NaN"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nan_df = all_month[all_month.isna().any(axis=1)]\n",
    "nan_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1a5461f7-b8a1-4ff1-a651-5c3e48d4c90d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Drop rows of Nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3df4a162-38eb-4862-96ef-1d6396b59f30",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity Ordered</th>\n",
       "      <th>Price Each</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Purchase Address</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>176558</td>\n",
       "      <td>USB-C Charging Cable</td>\n",
       "      <td>2</td>\n",
       "      <td>11.95</td>\n",
       "      <td>04/19/19 08:46</td>\n",
       "      <td>917 1st St, Dallas, TX 75001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>176559</td>\n",
       "      <td>Bose SoundSport Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>99.99</td>\n",
       "      <td>04/07/19 22:30</td>\n",
       "      <td>682 Chestnut St, Boston, MA 02215</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>176560</td>\n",
       "      <td>Google Phone</td>\n",
       "      <td>1</td>\n",
       "      <td>600</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>176560</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>176561</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/30/19 09:27</td>\n",
       "      <td>333 8th St, Los Angeles, CA 90001</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Order ID                     Product Quantity Ordered Price Each  \\\n",
       "0   176558        USB-C Charging Cable                2      11.95   \n",
       "2   176559  Bose SoundSport Headphones                1      99.99   \n",
       "3   176560                Google Phone                1        600   \n",
       "4   176560            Wired Headphones                1      11.99   \n",
       "5   176561            Wired Headphones                1      11.99   \n",
       "\n",
       "       Order Date                      Purchase Address  \n",
       "0  04/19/19 08:46          917 1st St, Dallas, TX 75001  \n",
       "2  04/07/19 22:30     682 Chestnut St, Boston, MA 02215  \n",
       "3  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001  \n",
       "4  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001  \n",
       "5  04/30/19 09:27     333 8th St, Los Angeles, CA 90001  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_month = all_month.dropna(how='all')\n",
    "all_month.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c961e708-5e0b-48d7-b70e-d8c0e9254ebb",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Find \"Or\" and delet it "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d6dc4f8b-6a0f-4792-a9ad-7f57115a679e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "all_month = all_month[all_month['Order Date'].str[0:2] != 'Or']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6dd93f68-b3f9-4021-8899-c59d3c904867",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Convert Columns to the correct type "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "d6a2c351-0791-40e4-a0ff-9061a6d3569b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "all_month['Quantity Ordered'] = pd.to_numeric(all_month['Quantity Ordered'])  # Make int \n",
    "all_month['Price Each'] = pd.to_numeric(all_month['Price Each'])# Make Float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d6af06c7-5e08-48e6-a30f-e321eca0f5f1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Augment data with additional columns \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "808fd25c-c152-435c-95b7-9bfb58de1c80",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#TASK 2: Add Month Column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3e1ac053-9fb0-42ae-aa61-9c5d7139c93e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity Ordered</th>\n",
       "      <th>Price Each</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Purchase Address</th>\n",
       "      <th>Month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>176558</td>\n",
       "      <td>USB-C Charging Cable</td>\n",
       "      <td>2</td>\n",
       "      <td>11.95</td>\n",
       "      <td>04/19/19 08:46</td>\n",
       "      <td>917 1st St, Dallas, TX 75001</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>176559</td>\n",
       "      <td>Bose SoundSport Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>99.99</td>\n",
       "      <td>04/07/19 22:30</td>\n",
       "      <td>682 Chestnut St, Boston, MA 02215</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>176560</td>\n",
       "      <td>Google Phone</td>\n",
       "      <td>1</td>\n",
       "      <td>600.00</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>176560</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>176561</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/30/19 09:27</td>\n",
       "      <td>333 8th St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Order ID                     Product  Quantity Ordered  Price Each  \\\n",
       "0   176558        USB-C Charging Cable                 2       11.95   \n",
       "2   176559  Bose SoundSport Headphones                 1       99.99   \n",
       "3   176560                Google Phone                 1      600.00   \n",
       "4   176560            Wired Headphones                 1       11.99   \n",
       "5   176561            Wired Headphones                 1       11.99   \n",
       "\n",
       "       Order Date                      Purchase Address  Month  \n",
       "0  04/19/19 08:46          917 1st St, Dallas, TX 75001      4  \n",
       "2  04/07/19 22:30     682 Chestnut St, Boston, MA 02215      4  \n",
       "3  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4  \n",
       "4  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4  \n",
       "5  04/30/19 09:27     333 8th St, Los Angeles, CA 90001      4  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_month['Month'] = all_month['Order Date'].str[0:2]\n",
    "all_month['Month'] = all_month['Month'].astype('int32')\n",
    "all_month.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "7221ea05-2f97-4298-86a7-afbb5ea07239",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#TASK 3: Add a sales column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "68b21cf4-d14e-4d89-bcd2-9f5d6002cdd9",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity Ordered</th>\n",
       "      <th>Price Each</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Purchase Address</th>\n",
       "      <th>Month</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>176558</td>\n",
       "      <td>USB-C Charging Cable</td>\n",
       "      <td>2</td>\n",
       "      <td>11.95</td>\n",
       "      <td>04/19/19 08:46</td>\n",
       "      <td>917 1st St, Dallas, TX 75001</td>\n",
       "      <td>4</td>\n",
       "      <td>23.90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>176559</td>\n",
       "      <td>Bose SoundSport Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>99.99</td>\n",
       "      <td>04/07/19 22:30</td>\n",
       "      <td>682 Chestnut St, Boston, MA 02215</td>\n",
       "      <td>4</td>\n",
       "      <td>99.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>176560</td>\n",
       "      <td>Google Phone</td>\n",
       "      <td>1</td>\n",
       "      <td>600.00</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "      <td>600.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>176560</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "      <td>11.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>176561</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/30/19 09:27</td>\n",
       "      <td>333 8th St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "      <td>11.99</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Order ID                     Product  Quantity Ordered  Price Each  \\\n",
       "0   176558        USB-C Charging Cable                 2       11.95   \n",
       "2   176559  Bose SoundSport Headphones                 1       99.99   \n",
       "3   176560                Google Phone                 1      600.00   \n",
       "4   176560            Wired Headphones                 1       11.99   \n",
       "5   176561            Wired Headphones                 1       11.99   \n",
       "\n",
       "       Order Date                      Purchase Address  Month   Sales  \n",
       "0  04/19/19 08:46          917 1st St, Dallas, TX 75001      4   23.90  \n",
       "2  04/07/19 22:30     682 Chestnut St, Boston, MA 02215      4   99.99  \n",
       "3  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4  600.00  \n",
       "4  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4   11.99  \n",
       "5  04/30/19 09:27     333 8th St, Los Angeles, CA 90001      4   11.99  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_month['Sales'] = all_month['Quantity Ordered']*all_month['Price Each']\n",
    "all_month.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "0f1e5562-4e55-4b14-8116-679cf71dfbf0",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#TASK 4: Add a city column "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b7cd9a98-ded3-45df-b176-9c5de0278f9b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Product</th>\n",
       "      <th>Quantity Ordered</th>\n",
       "      <th>Price Each</th>\n",
       "      <th>Order Date</th>\n",
       "      <th>Purchase Address</th>\n",
       "      <th>Month</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Column</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>176558</td>\n",
       "      <td>USB-C Charging Cable</td>\n",
       "      <td>2</td>\n",
       "      <td>11.95</td>\n",
       "      <td>04/19/19 08:46</td>\n",
       "      <td>917 1st St, Dallas, TX 75001</td>\n",
       "      <td>4</td>\n",
       "      <td>23.90</td>\n",
       "      <td>Dallas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>176559</td>\n",
       "      <td>Bose SoundSport Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>99.99</td>\n",
       "      <td>04/07/19 22:30</td>\n",
       "      <td>682 Chestnut St, Boston, MA 02215</td>\n",
       "      <td>4</td>\n",
       "      <td>99.99</td>\n",
       "      <td>Boston</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>176560</td>\n",
       "      <td>Google Phone</td>\n",
       "      <td>1</td>\n",
       "      <td>600.00</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "      <td>600.00</td>\n",
       "      <td>Los Angeles</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>176560</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/12/19 14:38</td>\n",
       "      <td>669 Spruce St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "      <td>11.99</td>\n",
       "      <td>Los Angeles</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>176561</td>\n",
       "      <td>Wired Headphones</td>\n",
       "      <td>1</td>\n",
       "      <td>11.99</td>\n",
       "      <td>04/30/19 09:27</td>\n",
       "      <td>333 8th St, Los Angeles, CA 90001</td>\n",
       "      <td>4</td>\n",
       "      <td>11.99</td>\n",
       "      <td>Los Angeles</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Order ID                     Product  Quantity Ordered  Price Each  \\\n",
       "0   176558        USB-C Charging Cable                 2       11.95   \n",
       "2   176559  Bose SoundSport Headphones                 1       99.99   \n",
       "3   176560                Google Phone                 1      600.00   \n",
       "4   176560            Wired Headphones                 1       11.99   \n",
       "5   176561            Wired Headphones                 1       11.99   \n",
       "\n",
       "       Order Date                      Purchase Address  Month   Sales  \\\n",
       "0  04/19/19 08:46          917 1st St, Dallas, TX 75001      4   23.90   \n",
       "2  04/07/19 22:30     682 Chestnut St, Boston, MA 02215      4   99.99   \n",
       "3  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4  600.00   \n",
       "4  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4   11.99   \n",
       "5  04/30/19 09:27     333 8th St, Los Angeles, CA 90001      4   11.99   \n",
       "\n",
       "         Column  \n",
       "0        Dallas  \n",
       "2        Boston  \n",
       "3   Los Angeles  \n",
       "4   Los Angeles  \n",
       "5   Los Angeles  "
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all_month['Column'] = all_month['Purchase Address'].apply(lambda x: x.split(',')[1])\n",
    "all_month.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "98f1ffd5-8027-4b8b-88b0-4a2921230913",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Question 1: What was the best month for sale? How much was earned that month?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "414833de-0601-4d66-b3c2-f171dc08fd97",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Administrator\\AppData\\Local\\Temp\\ipykernel_11560\\2405799813.py:1: FutureWarning: The default value of numeric_only in DataFrameGroupBy.sum is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.\n",
      "  results = all_month.groupby('Month').sum()\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Quantity Ordered</th>\n",
       "      <th>Price Each</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Month</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10903</td>\n",
       "      <td>1811768.38</td>\n",
       "      <td>1822256.73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13449</td>\n",
       "      <td>2188884.72</td>\n",
       "      <td>2202022.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>17005</td>\n",
       "      <td>2791207.83</td>\n",
       "      <td>2807100.38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>20558</td>\n",
       "      <td>3367671.02</td>\n",
       "      <td>3390670.24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>18667</td>\n",
       "      <td>3135125.13</td>\n",
       "      <td>3152606.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>15253</td>\n",
       "      <td>2562025.61</td>\n",
       "      <td>2577802.26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>16072</td>\n",
       "      <td>2632539.56</td>\n",
       "      <td>2647775.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>13448</td>\n",
       "      <td>2230345.42</td>\n",
       "      <td>2244467.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>13109</td>\n",
       "      <td>2084992.09</td>\n",
       "      <td>2097560.13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>22703</td>\n",
       "      <td>3715554.83</td>\n",
       "      <td>3736726.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>19798</td>\n",
       "      <td>3180600.68</td>\n",
       "      <td>3199603.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>28114</td>\n",
       "      <td>4588415.41</td>\n",
       "      <td>4613443.34</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Quantity Ordered  Price Each       Sales\n",
       "Month                                          \n",
       "1                 10903  1811768.38  1822256.73\n",
       "2                 13449  2188884.72  2202022.42\n",
       "3                 17005  2791207.83  2807100.38\n",
       "4                 20558  3367671.02  3390670.24\n",
       "5                 18667  3135125.13  3152606.75\n",
       "6                 15253  2562025.61  2577802.26\n",
       "7                 16072  2632539.56  2647775.76\n",
       "8                 13448  2230345.42  2244467.88\n",
       "9                 13109  2084992.09  2097560.13\n",
       "10                22703  3715554.83  3736726.88\n",
       "11                19798  3180600.68  3199603.20\n",
       "12                28114  4588415.41  4613443.34"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results = all_month.groupby('Month').sum()\n",
    "results.head(12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "083d0d0d-ef09-4e69-9d32-e9c43333f041",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7a025674-1e33-4a7b-9e2d-b52862365066",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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t7zv27dPUVFRNiUqLDU1VTVq1FBiYqLdUSRdugujTJnCP379/PzkcrlsSlRUUFCQwsPDderUKa1atUq9e/e2O5Jb3bp1VbNmTa1bt849lpubq88//9yYa9xMc7mk7N+/X2vXrlXVqlXtjuQxTv34UF5eXqF/2R48eFCZmZmqUqWK6tSpY1uulJQUzZ07V//6178UEhLiPodbsWJFlS9f3rZcI0eOVEJCgurUqaMzZ85o7ty52rBhg1atWmVbJunSefrfXr8TFBSkqlWr2n5dz3PPPadevXopKipKR48e1dixY+Xn56cBAwbYmuuZZ55RmzZt9OKLL+rhhx/WF198oTfeeENvvPGGrbmkS+U3NTVVSUlJ8vc340der169NGnSJNWpU0fNmjXTl19+qRkzZig5OdnuaFq1apUsy1KjRo104MABPf/882rcuLEGDRp0S3Nc7+fp0KFDNXHiRN1xxx2qW7euRo8erYiICPXp08fWXCdPntT333/vfkbJ5QJfs2bNYj3ac61c4eHh6tu3r7Zv365ly5apoKDA/XugSpUqCggIKLZcPmHzXUclyvr16y1JRaakpCRbc10pkyQrNTXV1lzJyclWVFSUFRAQYFWvXt3q0qWLtXr1alszXY0ptyf379/fCg8PtwICAqxatWpZ/fv3tw4cOGB3LMuyLGvp0qVW8+bNrcDAQKtx48bWG2+8YXcky7Isa9WqVZYka+/evXZHccvNzbWGDBli1alTxypXrpxVr149a9SoUZbT6bQ7mvX+++9b9erVswICAqyaNWtaKSkp1unTp295juv9PHW5XNbo0aOtsLAwKzAw0OrSpcst+W98vVypqalXXD527Fjbcl2+VfpK0/r164s1ly/w9mQAAGAsrlEBAADGoqgAAABjUVQAAICxKCoAAMBYFBUAAGAsigoAADAWRQUAABiLogIAAIxFUQFQrBwOh5YsWWJ3DI9FR0dr5syZdscA8H8oKkAJ9Nhjj8nhcOhPf/pTkWUpKSlyOBx67LHHfLrPF154QXfddZdPtwkAFBWghIqMjNT8+fN17tw599j58+c1d+5cW1+SWRpduHDB7gjAbYuiApRQLVq0UGRkpBYtWuQeW7RokerUqaO4uLhC6zqdTj399NOqUaOGypUrp3bt2mnr1q3u5Rs2bJDD4dC6devUsmVLVahQQW3atHG/GTYtLU3jxo3Tjh075HA45HA4lJaW5v78iRMn9MADD6hChQq644479OGHH14ze3R0tF588UUlJycrJCREderUKfQm5st5Tp8+7R7LzMyUw+HQoUOH3JkqVaqkZcuWqVGjRqpQoYL69u2rs2fP6t1331V0dLQqV66sp59+WgUFBYX2f+bMGQ0YMEBBQUGqVauWZs2aVWj56dOn9cQTT6h69eoKDQ3Vvffeqx07driXXz669NZbb6lu3boqV67cNb9fAFdHUQFKsOTkZKWmprrn33nnHQ0aNKjIen/5y1/0z3/+U++++662b9+uBg0aqHv37jp58mSh9UaNGqXp06dr27Zt8vf3V3JysiSpf//+evbZZ9WsWTMdO3ZMx44dU//+/d2fGzdunB5++GF99dVX6tmzpwYOHFhk2781ffp0tWzZUl9++aX+67/+S3/+85/dxchTZ8+e1SuvvKL58+dr5cqV2rBhgx544AEtX75cy5cv13vvvafXX39dCxcuLPS5l156SbGxsfryyy81YsQIDRkyRGvWrHEv79evn7Kzs7VixQplZGSoRYsW6tKlS6Hv6cCBA/rnP/+pRYsWKTMz06vcAH7F7tc3A/C9pKQkq3fv3lZ2drYVGBhoHTp0yDp06JBVrlw566effrJ69+7tfi19Xl6eVbZsWWvOnDnuz1+4cMGKiIiwpk2bZlnW/79Cfu3ate51PvroI0uSde7cOcuyLGvs2LFWbGxskSySrL/+9a/u+by8PEuStWLFiqvmj4qKsh555BH3vMvlsmrUqGHNnj27UJ5Tp0651/nyyy8tSdbBgwcty7Ks1NRUS5J14MAB9zp//OMfrQoVKlhnzpxxj3Xv3t364x//WGjfPXr0KJSnf//+VkJCgmVZlrV582YrNDTUOn/+fKF16tevb73++uvuP4uyZcta2dnZV/0eAXjG38aOBKCYVa9eXYmJiUpLS5NlWUpMTFS1atUKrfPtt9/q4sWLatu2rXusbNmyuueee7Rnz55C68bExLi/Dg8PlyRlZ2df95qXX38uKChIoaGhys7O9vgzDodDNWvWvO5nfqtChQqqX7++ez4sLEzR0dEKDg4uNPbb7cbHxxeZv3wn0I4dO5SXl6eqVasWWufcuXP69ttv3fNRUVGqXr26V3kBFEVRAUq45ORkDR48WJKKXGvhrbJly7q/djgckiSXy+XV5y5/9nqfu9ZnypS5dNbasiz38osXL3q0jRvJ8mt5eXkKDw/Xhg0biiyrVKmS++ugoCCPtwng6igqQAnXo0cPXbhwQQ6HQ927dy+yvH79+goICNCnn36qqKgoSZd+6W/dulVDhw71eD8BAQFFLkotLpePVBw7dkyVK1eWJJ9eB/LZZ58VmW/SpImkSxcpHz9+XP7+/oqOjvbZPgFcGRfTAiWcn5+f9uzZo927d8vPz6/I8qCgIP35z3/W888/r5UrV2r37t168skndfbsWT3++OMe7yc6OloHDx5UZmamTpw4IafT6ctvo5AGDRooMjJSL7zwgvbv36+PPvpI06dP99n2P/30U02bNk379u3TrFmztGDBAg0ZMkSS1LVrV8XHx6tPnz5avXq1Dh06pH//+98aNWqUtm3b5rMMAC6hqAClQGhoqEJDQ6+6fMqUKXrooYf0hz/8QS1atNCBAwe0atUq99EKTzz00EPq0aOHOnfurOrVq2vevHm+iH5FZcuW1bx58/TNN98oJiZGU6dO1cSJE322/WeffVbbtm1TXFycJk6cqBkzZriPRjkcDi1fvlwdOnTQoEGD1LBhQ/3+97/X4cOHFRYW5rMMAC5xWL8+yQsAAGAQjqgAAABjUVQAAICxKCoAAMBYFBUAAGAsigoAADAWRQUAABiLogIAAIxFUQEAAMaiqAAAAGNRVAAAgLEoKgAAwFgUFQAAYKz/BSFdcY3alUn+AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "months= range(1,13)\n",
    "\n",
    "plt.bar(months, results['Sales'])\n",
    "plt.xticks(months)\n",
    "plt.ylabel('Sales in USD ($)')\n",
    "plt.xlabel('Month number')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "d1954d41-14ce-4cd8-8d45-313d777d5dcf",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Question 2: What city had the highest number of sales?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aaa16539-39a1-4960-b9db-fa1640a44ec9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
