import polars as pl
import glob

def downsample_parquet_to_csv(parquet_glob, output_path, limit=200_000):
    files = glob.glob(parquet_glob)
    if not files:
        print(f"❌ No files matched: {parquet_glob}")
        return

    print(f"Processing {len(files)} files from {parquet_glob} → {output_path} ...")
    df = pl.read_parquet(files)  # Pass list of file paths
    if len(df) > limit:
        df = df.sample(n=limit)
    df.write_csv(output_path)
    print(f"✅ Wrote {len(df)} rows to {output_path}")

downsample_parquet_to_csv("raw_customers/*.parquet", "seeds/raw_customers.csv", limit=100_000)
downsample_parquet_to_csv("raw_orders/*.parquet", "seeds/raw_orders.csv", limit=200_000)
downsample_parquet_to_csv("raw_payments/*.parquet", "seeds/raw_payments.csv", limit=200_000)
