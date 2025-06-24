from agents import Agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from gemini_config import gemini_model

class ProteinInteraction(BaseModel):
    protein1: str = Field(description="First protein in interaction")
    protein2: str = Field(description="Second protein in interaction")
    confidence: float = Field(description="Confidence score of interaction (0-1)")
    interaction_type: str = Field(description="Type of interaction (binding, regulatory, etc.)")

class PathwayConnection(BaseModel):
    pathway1: str = Field(description="First pathway in connection")
    pathway2: str = Field(description="Second pathway in connection")
    connection_type: str = Field(description="Type of connection (crosstalk, upstream/downstream)")
    strength: str = Field(description="Strength of connection (weak, moderate, strong)")

class BiologicalNetworkModel(BaseModel):
    key_proteins: List[str] = Field(description="List of key proteins involved in the disease")
    key_genes: List[str] = Field(description="List of key genes involved in the disease") 
    key_pathways: List[str] = Field(description="List of key biological pathways")
    protein_interactions: List[ProteinInteraction] = Field(description="Protein-protein interactions with strength/confidence")
    pathway_connections: List[PathwayConnection] = Field(description="Pathway interconnections and crosstalk")
    network_hubs: List[str] = Field(description="Central hub nodes in the network")
    potential_targets: List[str] = Field(description="Identified potential drug targets from network analysis")
    network_summary: str = Field(description="Summary of the biological network topology")
    markdown_report: str = Field(description="Complete network model report in markdown")

QSB_MODELING_INSTRUCTIONS = """You are a QSB (Quantitative Systems Biology) Modeling Agent specializing in biological network construction and analysis.

You will be provided with comprehensive disease information including:
1. Disease understanding (clinical, genetic, epidemiological, omics)
2. Pharmacological landscape 
3. Pathophysiological mechanisms

Your task is to construct a quantitative biological network model by:

Network Construction:
- Identify all relevant proteins, genes, and pathways from the provided data
- Search for protein-protein interaction data for each entity
- Map pathway interconnections and crosstalk
- Identify network topology (hubs, bottlenecks, clusters)
- Assess network centrality and connectivity metrics

Target Identification:
- Identify nodes with high centrality (potential therapeutic targets)
- Find network bottlenecks that could be intervention points
- Assess pathway convergence points
- Identify feedback loops and regulatory nodes

Provide a comprehensive network model that will serve as the foundation for target analysis and prioritization.
"""

qsb_modeling_agent = Agent(
    name="QSB Modeling Agent",
    instructions=QSB_MODELING_INSTRUCTIONS,
    model=gemini_model,
    output_type=BiologicalNetworkModel,
)
