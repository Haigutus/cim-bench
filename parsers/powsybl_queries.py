"""PowSyBl CGMES template queries for SPARQL-native tools (issue #12).

Query text taken verbatim from powsybl-core
(cgmes/cgmes-model/src/main/resources/CIM16.sparql, query `acLineSegments`),
(c) RTE, Mozilla Public License 2.0. CIM100.sparql does not override this
query, so the same text serves CGMES 2.4 and 3.0 - only the cim namespace
differs, which is injected via PREFIX (PowSyBl binds it at runtime too).

One adaptation: the outer `{ GRAPH ?graph { ... } }` wrapper is removed.
PowSyBl loads each profile into a named graph; cim-bench adapters load all
profiles into the default graph, where the GRAPH clause would match nothing.
"""

ACLINE_SEGMENTS = """
SELECT *
WHERE {
    ?ACLineSegment
        a cim:ACLineSegment ;
        cim:ACLineSegment.r ?r ;
        cim:ACLineSegment.x ?x ;
        cim:ACLineSegment.bch ?bch ;
        cim:IdentifiedObject.name ?name .
    OPTIONAL {
        ?ACLineSegment cim:ACLineSegment.gch ?gch
    }
    ?Terminal1
        a cim:Terminal ;
        cim:Terminal.ConductingEquipment ?ACLineSegment .
    OPTIONAL { ?Terminal1 cim:ACDCTerminal.sequenceNumber ?seq1 }
    ?Terminal2
        a cim:Terminal ;
        cim:Terminal.ConductingEquipment ?ACLineSegment .
    OPTIONAL { ?Terminal2 cim:ACDCTerminal.sequenceNumber ?seq2 }
    FILTER ( bound(?seq1) && ?seq1 = "1" && bound(?seq2) && ?seq2 = "2"
        || !bound(?seq1) && !bound(?seq2) && str(?Terminal1) < str(?Terminal2) )
    OPTIONAL {
        ?ACLineSegment cim:Equipment.EquipmentContainer ?Line .
        ?Line
            a cim:Line ;
            cim:IdentifiedObject.name ?lineName
    }
}
"""


def acline_segments_query(cim_namespace: str) -> str:
    """PowSyBl's acLineSegments query with the dataset's cim namespace bound."""
    return f"PREFIX cim: <{cim_namespace}>\n{ACLINE_SEGMENTS}"
