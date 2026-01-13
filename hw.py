import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nDataFrame Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nNames column:")
print(df["Name"])

print("\nFirst two rows:")
print(df.head(2))

df["Passed"] = df["Marks"] >= 80
print("\nAfter adding Passed column:")
print(df)

print("\nStudents with marks greater than 85:")
print(df[df["Marks"] > 85])

print("\nSorted by Marks (descending):")
print(df.sort_values(by="Marks", ascending=False))

df.loc[df["Name"] == "Bob", "Marks"] = 820000
print("\nAfter updating Bob's marks:")
print(df)

df = df.drop(columns=["Passed"])
print("\nAfter removing Passed column:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())