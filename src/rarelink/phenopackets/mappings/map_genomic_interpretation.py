from rarelink.utils.processor import DataProcessor
import logging

logger = logging.getLogger(__name__)

def map_genomic_interpretation(data: dict, processor: DataProcessor) -> dict:
    """
    Maps a single genomic interpretation to the required format.

    Args:
        data (dict): Input data for genomic interpretation.
        processor (DataProcessor): Handles field processing.

    Returns:
        dict: Mapped genomic interpretation structure.
    """
    try:
        variation_descriptor = {
            "id": data.get("variation_id"),
            "geneContext": {
                "valueId": data.get("gene_context_id"),
                "symbol": data.get("gene_symbol")
            },
            "expressions": [
                {"syntax": "hgvs.c", "value": data.get("hgvs_c")},
                {"syntax": "hgvs.g", "value": data.get("hgvs_g")},
            ],
            "vcfRecord": {
                "genomeAssembly": data.get("genome_assembly"),
                "chrom": data.get("chrom"),
                "pos": data.get("pos"),
                "ref": data.get("ref"),
                "alt": data.get("alt"),
            },
            "moleculeContext": "genomic",
            "allelicState": {
                "id": data.get("allelic_state_id"),
                "label": data.get("allelic_state_label")
            },
        }

        return {
            "subjectOrBiosampleId": data.get("subject_id"),
            "interpretationStatus": data.get("interpretation_status"),
            "variantInterpretation": {"variationDescriptor": variation_descriptor},
        }
    except Exception as e:
        logger.error(f"Error mapping genomic interpretation: {e}")
        raise


def map_diagnosis(data: dict, processor: DataProcessor) -> dict:
    """
    Maps diagnosis details with multiple genomic interpretations.

    Args:
        data (dict): Input data for diagnosis.
        processor (DataProcessor): Handles field processing.

    Returns:
        dict: Mapped diagnosis structure.
    """
    try:
        disease = {
            "id": data.get("disease_id"),
            "label": data.get("disease_label"),
        }

        # Handle multiple genomic interpretations
        genomic_interpretations_data = data.get("genomic_interpretations", [])
        genomic_interpretations = [
            map_genomic_interpretation(gi_data, processor)
            for gi_data in genomic_interpretations_data
        ]

        return {
            "disease": disease,
            "genomicInterpretations": genomic_interpretations,
        }
    except Exception as e:
        logger.error(f"Error mapping diagnosis: {e}")
        raise
