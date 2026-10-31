"""Identity guards for reusing independently verified global mining results."""
import hashlib
import json

MINED_ARTIFACTS = ('connected-patterns.json.gz', 'global-fact-dependencies.json.gz',
    'resource-binding-dependencies.json.gz', 'embedded-handoffs.json',
    'launch-definitions.json', 'archive-inventories.json')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mining_identity(data, resources):
    identity = {'algorithm_version': 1, 'evidence_manifest': sha(data / 'evidence-manifest.json'),
                'resources': sorted((r['depot'], r['binary_sha256'], r['raw_sha256'], r['family'], r['role']) for r in resources)}
    return hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
