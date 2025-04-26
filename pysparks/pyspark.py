from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def product_category_pairs(
    products_df: DataFrame,
    categories_df: DataFrame,
    prod_cat_link_df: DataFrame,
) -> DataFrame:
    return (
        products_df.alias("p")
        .join(prod_cat_link_df.alias("pc"), F.col("p.id") == F.col("pc.product_id"), "left")
        .join(categories_df.alias("c"), F.col("pc.category_id") == F.col("c.id"), "left")
        .select(F.col("p.name").alias("product_name"), F.col("c.name").alias("category_name"))
        .orderBy("product_name", "category_name")
    )