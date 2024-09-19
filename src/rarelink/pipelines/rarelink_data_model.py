from phenopacket_mapper.data_standards import DataModel, DataField
from phenopacket_mapper.data_standards.value_set import ValueSet

RARELINK_DATAMODEL_2_0 = DataModel(
    data_model_name="rarelink",
    fields=[DataField(name="temp", value_set=ValueSet())],
    resources=[]
)  # TODO @aslgrafe: replace with finished datamodel
