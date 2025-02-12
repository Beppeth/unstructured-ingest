from __future__ import annotations

import unstructured_ingest.v2.processes.connectors.fsspec  # noqa: F401
from unstructured_ingest.v2.processes.connector_registry import (
    add_destination_entry,
    add_source_entry,
)

from .airtable import CONNECTOR_TYPE as AIRTABLE_CONNECTOR_TYPE
from .airtable import airtable_source_entry
from .astradb import CONNECTOR_TYPE as ASTRA_DB_CONNECTOR_TYPE
from .astradb import astra_db_destination_entry
from .azure_cognitive_search import CONNECTOR_TYPE as AZURE_COGNTIVE_SEARCH_CONNECTOR_TYPE
from .azure_cognitive_search import azure_cognitive_search_destination_entry
from .chroma import CONNECTOR_TYPE as CHROMA_CONNECTOR_TYPE
from .chroma import chroma_destination_entry
from .couchbase import CONNECTOR_TYPE as COUCHBASE_CONNECTOR_TYPE
from .couchbase import couchbase_destination_entry, couchbase_source_entry
from .databricks_volumes import CONNECTOR_TYPE as DATABRICKS_VOLUMES_CONNECTOR_TYPE
from .databricks_volumes import databricks_volumes_destination_entry
from .elasticsearch import CONNECTOR_TYPE as ELASTICSEARCH_CONNECTOR_TYPE
from .elasticsearch import elasticsearch_destination_entry, elasticsearch_source_entry
from .google_drive import CONNECTOR_TYPE as GOOGLE_DRIVE_CONNECTOR_TYPE
from .google_drive import google_drive_source_entry
from .kdbai import CONNECTOR_TYPE as KDBAI_CONNECTOR_TYPE
from .kdbai import kdbai_destination_entry
from .local import CONNECTOR_TYPE as LOCAL_CONNECTOR_TYPE
from .local import local_destination_entry, local_source_entry
from .milvus import CONNECTOR_TYPE as MILVUS_CONNECTOR_TYPE
from .milvus import milvus_destination_entry
from .mongodb import CONNECTOR_TYPE as MONGODB_CONNECTOR_TYPE
from .mongodb import mongodb_destination_entry
from .onedrive import CONNECTOR_TYPE as ONEDRIVE_CONNECTOR_TYPE
from .onedrive import onedrive_source_entry
from .opensearch import CONNECTOR_TYPE as OPENSEARCH_CONNECTOR_TYPE
from .opensearch import opensearch_destination_entry, opensearch_source_entry
from .pinecone import CONNECTOR_TYPE as PINECONE_CONNECTOR_TYPE
from .pinecone import pinecone_destination_entry
from .salesforce import CONNECTOR_TYPE as SALESFORCE_CONNECTOR_TYPE
from .salesforce import salesforce_source_entry
from .sharepoint import CONNECTOR_TYPE as SHAREPOINT_CONNECTOR_TYPE
from .sharepoint import sharepoint_source_entry
from .singlestore import CONNECTOR_TYPE as SINGLESTORE_CONNECTOR_TYPE
from .singlestore import singlestore_destination_entry
from .sql import CONNECTOR_TYPE as SQL_CONNECTOR_TYPE
from .sql import sql_destination_entry
from .weaviate import CONNECTOR_TYPE as WEAVIATE_CONNECTOR_TYPE
from .weaviate import weaviate_destination_entry

add_destination_entry(destination_type=ASTRA_DB_CONNECTOR_TYPE, entry=astra_db_destination_entry)

add_destination_entry(destination_type=CHROMA_CONNECTOR_TYPE, entry=chroma_destination_entry)

add_source_entry(source_type=COUCHBASE_CONNECTOR_TYPE, entry=couchbase_source_entry)
add_destination_entry(destination_type=COUCHBASE_CONNECTOR_TYPE, entry=couchbase_destination_entry)

add_source_entry(source_type=ELASTICSEARCH_CONNECTOR_TYPE, entry=elasticsearch_source_entry)
add_destination_entry(
    destination_type=ELASTICSEARCH_CONNECTOR_TYPE, entry=elasticsearch_destination_entry
)

add_source_entry(source_type=GOOGLE_DRIVE_CONNECTOR_TYPE, entry=google_drive_source_entry)

add_source_entry(source_type=LOCAL_CONNECTOR_TYPE, entry=local_source_entry)
add_destination_entry(destination_type=LOCAL_CONNECTOR_TYPE, entry=local_destination_entry)

add_source_entry(source_type=ONEDRIVE_CONNECTOR_TYPE, entry=onedrive_source_entry)

add_source_entry(source_type=OPENSEARCH_CONNECTOR_TYPE, entry=opensearch_source_entry)
add_destination_entry(
    destination_type=OPENSEARCH_CONNECTOR_TYPE, entry=opensearch_destination_entry
)

add_source_entry(source_type=SALESFORCE_CONNECTOR_TYPE, entry=salesforce_source_entry)

add_destination_entry(destination_type=WEAVIATE_CONNECTOR_TYPE, entry=weaviate_destination_entry)

add_destination_entry(
    destination_type=DATABRICKS_VOLUMES_CONNECTOR_TYPE, entry=databricks_volumes_destination_entry
)

add_destination_entry(destination_type=SQL_CONNECTOR_TYPE, entry=sql_destination_entry)

add_destination_entry(destination_type=MONGODB_CONNECTOR_TYPE, entry=mongodb_destination_entry)
add_destination_entry(destination_type=PINECONE_CONNECTOR_TYPE, entry=pinecone_destination_entry)
add_source_entry(source_type=SHAREPOINT_CONNECTOR_TYPE, entry=sharepoint_source_entry)
add_destination_entry(
    destination_type=SINGLESTORE_CONNECTOR_TYPE, entry=singlestore_destination_entry
)
add_destination_entry(destination_type=MILVUS_CONNECTOR_TYPE, entry=milvus_destination_entry)
add_destination_entry(
    destination_type=AZURE_COGNTIVE_SEARCH_CONNECTOR_TYPE,
    entry=azure_cognitive_search_destination_entry,
)

add_destination_entry(destination_type=KDBAI_CONNECTOR_TYPE, entry=kdbai_destination_entry)
add_source_entry(source_type=AIRTABLE_CONNECTOR_TYPE, entry=airtable_source_entry)
