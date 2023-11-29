import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

products_df = pd.read_csv('./dashboard/products.csv')
customers_df = pd.read_csv('./dashboard/customers.csv')
sellers_df = pd.read_csv('./dashboard/sellers.csv')

st.header('Brazilian E-Commerce Public')

# PRODUCT SALES
st.subheader('Best and Worst Performing Product by Number of Sales')
col1, col2 = st.columns(2)
with col1:
    total_sales = products_df.order_count.sum()
    st.metric("Total Sales", value=total_sales)
 
with col2:
    total_products = products_df.product_id.count()
    st.metric("Total Products", value=total_products)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,6))

sns.barplot(x='order_count', y='product_id', data=products_df.head(5), ax=ax[0], palette='viridis')
ax[0].set_ylabel('ID Product')
ax[0].set_xlabel('Quantity')
ax[0].set_title('Best Performing Product', loc='center', fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)

sns.barplot(x='order_count', y='product_id', data=products_df.tail(5), ax=ax[1], palette='viridis')
ax[1].set_ylabel('ID Product')
ax[1].set_xlabel('Quantity')
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title('Worst Performing Product', loc='center', fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

st.pyplot(fig)

# PRODUCT REVIEW
st.subheader('Best and Worst Performing Product by Number of Review')
col1, col2 = st.columns(2)
with col1:
    total_review = products_df.review_count.sum()
    st.metric("Total Review", value=int(total_review))
 
with col2:
    total_products = products_df.product_id.count()
    st.metric("Total Products", value=total_products)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,6))

sns.barplot(x='review_count', y='product_id', data=products_df.head(5), ax=ax[0], palette='viridis')
ax[0].set_ylabel('ID Product')
ax[0].set_xlabel('Review Count')
ax[0].set_title('Best Performing Product', loc='center', fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)

# menampilkan review_mean di setiap bar
for i, p in enumerate(ax[0].patches):
    ax[0].annotate(f'Review Mean: {products_df["review_mean"].iloc[i]:.1f}', 
                   (p.get_width(), p.get_y() + p.get_height()/2), 
                   ha='center', va='center', fontsize=12, color='white', xytext=(-70, 0), textcoords='offset points')

sns.barplot(x='review_count', y='product_id', data=products_df.tail(5), ax=ax[1], palette='viridis')
ax[1].set_ylabel('ID Product')
ax[1].set_xlabel('Review Count')
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title('Worst Performing Product', loc='center', fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

# menampilkan review_mean di setiap bar
for i, p in enumerate(ax[1].patches):
    ax[1].annotate(f'Review Mean: {products_df["review_mean"].iloc[-(i+1)]:.1f}', 
                   (p.get_width(), p.get_y() + p.get_height()/2), 
                   ha='center', va='center', fontsize=12, color='white', xytext=(70, 0), textcoords='offset points')

st.pyplot(fig)

# CUSTOMER STATE
st.subheader('Best and Worst Performing Customer by State')
col1, col2 = st.columns(2)
with col1:
    total_state = customers_df.customer_state.value_counts().count()
    st.metric("Total State", value=int(total_state))
 
with col2:
    total_customers = customers_df.customer_id.count()
    st.metric("Total Customers", value=total_customers)

customerState = customers_df.groupby('customer_state', as_index=False).count().sort_values(by='customer_id', ascending=False)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))

ax[0].set_title('Best Performing Customer', loc='center', fontsize=15)
ax[0].pie(
  x=customerState['customer_id'].iloc[:5],
  labels=customerState['customer_state'].iloc[:5],
  autopct='%1.1f%%'
)

ax[1].set_title('Worst Performing Customer', loc='center', fontsize=15)
ax[1].pie(
  x=customerState['customer_id'].iloc[-5:],
  labels=customerState['customer_state'].iloc[-5:],
  autopct='%1.1f%%'
)

st.pyplot(fig)

# CUSTOMER RFM
st.subheader('Best Customer Based on RFM Parameters')
col1, col2, col3 = st.columns(3)
with col1:
    avg_recency = round(customers_df.recency.mean(), 1)
    st.metric("Average Recency (Days)", value=avg_recency)
 
with col2:
    avg_frequency = round(customers_df.frequency.mean(), 1)
    st.metric("Average Frequency", value=avg_frequency)
    
with col3:
    avg_monetary = round(customers_df.monetary.mean(), 1)
    st.metric("Average Monetary", value=avg_monetary)

fig, ax = plt.subplots(figsize=(10,6))

sns.barplot(x='recency', y='customer_id', data=customers_df.sort_values(by='recency').head(5), palette='viridis')
ax.set_ylabel('ID Customer')
ax.set_xlabel('Recency in Days')
ax.set_title('By Recency (Days)', loc='center', fontsize=15)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

sns.barplot(x='frequency', y='customer_id', data=customers_df.sort_values(by='frequency', ascending=False).head(5), palette='viridis')
ax.set_ylabel('ID Customer')
ax.set_xlabel('Frequency')
ax.set_title('By Frequency', loc='center', fontsize=15)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

sns.barplot(x='monetary', y='customer_id', data=customers_df.sort_values(by='monetary', ascending=False).head(5), palette='viridis')
ax.set_ylabel('ID Customer')
ax.set_xlabel('Monetary')
ax.set_title('By Monetary', loc='center', fontsize=15)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

# SELLER STATE
st.subheader('Best and Worst Performing Seller by State')
col1, col2 = st.columns(2)
with col1:
    total_state = sellers_df.seller_state.value_counts().count()
    st.metric("Total State", value=int(total_state))
 
with col2:
    total_sellers = sellers_df.seller_id.count()
    st.metric("Total Sellers", value=total_sellers)

sellerState = sellers_df.groupby('seller_state', as_index=False).count().sort_values(by='seller_id', ascending=False)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))

ax[0].set_title('Best Performing Seller', loc='center', fontsize=15)
ax[0].pie(
  x=sellerState['seller_id'].iloc[:5],
  labels=sellerState['seller_state'].iloc[:5],
  autopct='%1.1f%%'
)

ax[1].set_title('Worst Performing Seller', loc='center', fontsize=15)
ax[1].pie(
  x=sellerState['seller_id'].iloc[-5:],
  labels=sellerState['seller_state'].iloc[-5:],
  autopct='%1.1f%%'
)

st.pyplot(fig)