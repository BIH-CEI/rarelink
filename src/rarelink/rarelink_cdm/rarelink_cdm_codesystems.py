from phenopacket_mapper.data_standards.code import CodeSystem
from phenopacket_mapper.data_standards.code_system import NCBITaxon, GENO, SO, ICD10CM, SNOMED, ICD11, HL7FHIR, GA4GH, ISO3166, ICF, MONDO, ORDO, OMIM, LOINC, HGVS, HGNC, HPO


class RareLink_CDM_v2_0_0_Resources:
    """
    This class is a container for the code systems used in the 
    RareLink CDM v2.0.0.

    __version__ = '2.0.0'
    """
    @property
    def NCBITaxon(self):
        return NCBITaxon.set_version("2024-07-03")
    
    def GENO(self):
        return GENO.set_version("2023-10-08")

    def SO(self):
        return SO.set_version("2.6")

    def ICD10CM(self):
        return ICD10CM.set_version("2024-09-01")

    def SNOMED(self):
        return SNOMED.set_version("2024-09-01")

    def ICD11(self):
        return ICD11.set_version("2024-09-01")

    def HL7FHIR(self):
        return HL7FHIR.set_version("v4.0.1")

    def GA4GH(self):
        return GA4GH.set_version("v2.0")

    def ISO3166(self):
        return ISO3166.set_version("2020(en)")

    def ICF(self):
        return ICF.set_version("1.0.2")

    def MONDO(self):
        return MONDO.set_version("2024-09-03")

    def ORDO(self):
        return ORDO.set_version("2024-09-12")

    def OMIM(self):
        return OMIM.set_version("2024-09-12")

    def LOINC(self):
        return LOINC.set_version("2.78")

    def HGVS(self):
        return HGVS.set_version("21.0.0")

    def HGNC(self):
        return HGNC.set_version("2024-08-23")

    def HPO(self):
        return HPO.set_version("2024-08-13")


RARELINK_CDM_V2_0_0_RESOURCES = RareLink_CDM_v2_0_0_Resources()