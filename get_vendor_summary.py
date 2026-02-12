import sqlite3
import pandas as pd
import logging

# ----------------------------------
# Logging configuration
# ----------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------------
# Function: Create Vendor Summary
# ----------------------------------
def create_vendor_summary(conn):
    query = """
    WITH Freight_summary AS (
        SELECT 
            VendorNumber,
            SUM(Freight) AS Freight_cost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    Purchase_summary AS (
        SELECT 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            SUM(p.Quantity) AS TotalPurchaseQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars,
            pp.volume,
            pp.price AS Actual_Price
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0    
        GROUP BY 
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.price,
            pp.volume
    ),

    Sales_Summary AS (
        SELECT 
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS Total_sales_quantity,
            SUM(SalesPrice) AS Total_Sales_Price,
            SUM(SalesDollars) AS Total_Sales_Dollars,
            SUM(ExciseTax) AS Total_Excise_tax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT 
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.Actual_Price,
        ps.volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.Total_sales_quantity,
        ss.Total_Sales_Dollars,
        ss.Total_Sales_Price,
        ss.Total_Excise_tax,
        fs.Freight_cost
    FROM Purchase_summary ps
    LEFT JOIN Sales_Summary ss
        ON ps.VendorNumber = ss.VendorNo
       AND ps.Brand = ss.Brand
    LEFT JOIN Freight_summary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC
    """

    df = pd.read_sql_query(query, conn)
    return df


# ----------------------------------
# Function: Clean & Transform Data
# ----------------------------------
def clean_data(df):
    """this function will clean the data"""

    # changing datatype to float
    df["volume"] = df["volume"].astype("float")

    # filling missing values with 0
    df.fillna(0, inplace=True)

    # removing spaces from categorical columns
    df["VendorName"] = df["VendorName"].str.strip()
    df["Description"] = df["Description"].str.strip()

    # creating new columns for better analysis
    df["GrossProfit"] = df["Total_Sales_Dollars"] - df["TotalPurchaseDollars"]

    df["ProfitMargin"] = (
        df["GrossProfit"] / df["Total_Sales_Dollars"]
    ) * 100

    df["StockTurnover"] = (
        df["Total_sales_quantity"] / df["TotalPurchaseQuantity"]
    )

    df["SalesToPurchaseRatio"] = (
        df["Total_Sales_Dollars"] / df["TotalPurchaseDollars"]
    )

    return df


# ----------------------------------
# Function: Ingest Data into SQL
# ----------------------------------
def ingest_data(df, table_name, conn):
    df.to_sql(table_name, conn, if_exists="replace", index=False)


# ----------------------------------
# Main Execution
# ----------------------------------
if __name__ == "__main__":

    # creating database connection
    conn = sqlite3.connect("inventory.db")

    logging.info("Creating Vendor Summary Table.....")
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info("Cleaning Data.....")
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info("Ingesting data.....")
    ingest_data(clean_df, "VendorSalesSummary", conn)

    logging.info("Process Completed Successfully ✅")

    conn.close()
