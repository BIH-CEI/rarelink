import pytest
from rarelink.preprocessing import parse_redcap_code
from phenopacket_mapper.data_standards import CodeSystem, Coding

@pytest.fixture
def resources():
    return [
        CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED', url='https://www.snomed.org/snomed-ct'),
        CodeSystem(name='Monarch Disease Ontology', namespace_prefix='MONDO', url='https://mondo.monarchinitiative.org/'),
        CodeSystem(name='Human Phenotype Ontology', namespace_prefix='HPO', url='https://hpo.jax.org/'),
        CodeSystem(name='Online Mendelian Inheritance', namespace_prefix='OMIM', url='https://omim.org/'),
        CodeSystem(name='Orphanet', namespace_prefix='ORDO', url='https://www.orpha.net/consor/cgi-bin/index.php'),
    #    CodeSystem(name='NCBI Taxonomy', namespace_prefix='NCBITAXON', url='https://www.ncbi.nlm.nih.gov/taxonomy'),
        CodeSystem(name='Logical Observation Identifiers Names and Codes', namespace_prefix='LOINC', url='https://loinc.org/'),
        CodeSystem(name='HUGO Gene Nomenclature Committee', namespace_prefix='HGNC', url='https://www.genenames.org/'),
    #    CodeSystem(name='GENO: The Genotype Ontology', namespace_prefix='GENO', url='http://www.genoontology.org/'),
    #    CodeSystem(name='National Cancer Institute Thesaurus (NCIT)', namespace_prefix='NCIT', url='https://ncithesaurus.org/'),
    #    CodeSystem(name='Sequence Ontology (SO)', namespace_prefix='SO', url='http://www.sequenceontology.org/'),
        CodeSystem(name='International Classification of Diseases', namespace_prefix='ICD10CM', url='https://www.cdc.gov/nchs/icd/icd10cm.htm'),
    #    CodeSystem(name='ICD-11', namespace_prefix='ICD11', url='https://icd.who.int/en')
    ]

@pytest.mark.parametrize("input, expected", [
    ("snomed_410605003", Coding(system=CodeSystem(name='SNOMED CT', namespace_prefix='SNOMED', url='https://www.snomed.org/snomed-ct'), code='410605003')),
    ("mondo_0968976", Coding(system=CodeSystem(name='MONDO', namespace_prefix='MONDO', url='https://mondo.monarchinitiative.org/'), code='0968976')),
    ("hp::4000034", Coding(system=CodeSystem(name='Human Phenotype Ontology', namespace_prefix='HPO', url='https://hpo.jax.org/'), code='00000')),
    ("omim_00000", Coding(system=CodeSystem(name='OMIM', namespace_prefix='OMIM', url='https://omim.org/'), code='00000')),
    ("ordo_00000", Coding(system=CodeSystem(name='ORDO', namespace_prefix='ORDO', url='https://www.orpha.net/consor/cgi-bin/index.php'), code='00000')),
#    ("ncbitaxon_00000", Coding(system=CodeSystem(name='NCBI Taxonomy', namespace_prefix='NCBITAXON', url='https://www.ncbi.nlm.nih.gov/taxonomy'), code='00000')),
    ("loinc_00000", Coding(system=CodeSystem(name='LOINC', namespace_prefix='LOINC', url='https://loinc.org/'), code='00000')),
    ("hgnc_00000", Coding(system=CodeSystem(name='HGNC', namespace_prefix='HGNC', url='https://www.genenames.org/'), code='00000')),
#    ("geno_00000", Coding(system=CodeSystem(name='GENO: The Genotype Ontology', namespace_prefix='GENO', url='http://www.genoontology.org/'), code='00000')),
#    ("ncit_00000", Coding(system=CodeSystem(name='National Cancer Institute Thesaurus (NCIT)', namespace_prefix='NCIT', url='https://ncithesaurus.org/'), code='00000')),
#    ("so_00000", Coding(system=CodeSystem(name='Sequence Ontology (SO)', namespace_prefix='SO', url='http://www.sequenceontology.org/'), code='00000')),
    ("icd10cm_00000", Coding(system=CodeSystem(name='ICD-10-CM', namespace_prefix='ICD10CM', url='https://www.cdc.gov/nchs/icd/icd10cm.htm'), code='00000')),
#    ("icd11_00000", Coding(system=CodeSystem(name='ICD-11', namespace_prefix='ICD11', url='https://icd.who.int/en'), code='00000')),
])
def test_preprocess_redcap_code(input, resources, expected):
    assert parse_redcap_code(input, resources) == expected