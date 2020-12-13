import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 300)
data = {
    "Monday": ["张*", "苏*", "郝*", "董*"],
    "Tuesday": ["赵*", "李*", "耿*1", "李*"],
    "Wednesday": ["康*", "程*", "杨*", "程*2"],
    "Thursday": ["卫*", "董*2", "熊*", "何*"],
    "Friday": ["梁*", "耿*2", "赵*2", "杨*2"]
}
df = pd.DataFrame(data, columns=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
print(df)
