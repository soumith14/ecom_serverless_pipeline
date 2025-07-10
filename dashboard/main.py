from pyathena import connect
from pyathena.pandas.cursor import PandasCursor
import pandas as pd
import matplotlib.pyplot as plt

# 1) Connect to Athena, specifying your database/schema
conn = connect(
    s3_staging_dir='s3://yourprefix-athena-query-results/',  # your query-results bucket
    region_name='us-east-1',                            # your AWS region
    schema_name='ecom_db',                              # the Glue/Athena database
    work_group='primary',
    cursor_class=PandasCursor
)

# 2) Define your SQL against the Parquet table
query = """
SELECT product_id,
       SUM(total_amount) AS total_revenue
FROM parquet
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10
"""

# 3) Execute and load into a DataFrame
df = conn.cursor().execute(query).as_pandas()

# 4) Plot with matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df['product_id'], df['total_revenue'])
plt.xlabel('Product ID')
plt.ylabel('Total Revenue')
plt.title('Top 10 Products by Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
