"""PowSyBl CGMES template queries for SPARQL-native tools (issue #12).

Query text taken verbatim from powsybl-core
(cgmes/cgmes-model/src/main/resources/CIM16.sparql, query `acLineSegments`),
(c) RTE, Mozilla Public License 2.0. CIM100.sparql does not override this
query, so the same text serves CGMES 2.4 and 3.0 - only the cim namespace
differs, which is injected via PREFIX (PowSyBl binds it at runtime too).

Two adaptations:

1. The outer `{ GRAPH ?graph { ... } }` wrapper is removed. PowSyBl loads each
   profile into a named graph; cim-bench adapters load all profiles into the
   default graph, where the GRAPH clause would match nothing.

2. The sequenceNumber comparisons are wrapped in `str()`. PowSyBl's text
   compares against the plain literal `"1"`, which relies on the loader leaving
   CGMES literals untyped - true for every tool that queries the parsed RDF
   directly. A loader that types literals from the CIM schema instead gets
   sequenceNumber as `xsd:integer`, making `?seq1 = "1"` false: the query then
   silently returns zero rows and the Terminal join goes quadratic (found with
   cimoxide, which types its literals). `str(?seq1) = "1"` is equivalent for
   untyped literals and correct for typed ones, so it cannot change any
   tool's result.
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
    FILTER ( bound(?seq1) && str(?seq1) = "1" && bound(?seq2) && str(?seq2) = "2"
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
