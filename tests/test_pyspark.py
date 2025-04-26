import pytest
from pyspark.sql import SparkSession
from pysparks import product_category_pairs


@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder.master("local[1]").appName("tests").getOrCreate()
    yield spark
    spark.stop()


def test_pairs_and_orphans(spark):
    products = spark.createDataFrame(
        [(1, "Book"), (2, "Phone"), (3, "Table")], ["id", "name"]
    )
    categories = spark.createDataFrame(
        [(10, "Electronics"), (11, "Furniture")], ["id", "name"]
    )
    links = spark.createDataFrame(
        [(2, 10), (3, 11)], ["product_id", "category_id"]
    )

    result = product_category_pairs(products, categories, links).collect()

    expected = {
        ("Book", None),
        ("Phone", "Electronics"),
        ("Table", "Furniture"),
    }
    assert {(row.product_name, row.category_name) for row in result} == expected
