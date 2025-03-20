from rarelink.utils.processor import DataProcessor

dp = DataProcessor(mapping_config={})
print(dp.convert_date_to_iso_age("seconds: 1646092800", "2020-01-01"))
