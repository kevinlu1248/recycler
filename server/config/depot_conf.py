
# my_app/config/depot_conf.py

import os

from depot.manager import DepotManager

DepotManager.configure('default', {
    'depot.backend': 'depot.io.boto3.S3Storage',
    'depot.endpoint_url': 'https://storage.googleapis.com',
    'depot.access_key_id': os.environ.get('GOOGLE_CLOUD_STORAGE_ACCESS_KEY'),
    'depot.secret_access_key': os.environ.get('GOOGLE_CLOUD_STORAGE_SECRET_KEY'),
    'depot.bucket': os.environ.get('GOOGLE_CLOUD_STORAGE_BUCKET')
})

# def init_depots(app):
#     """Setup all configured depots"""
#
#     depot_name = 'avatar'
#     depot_config = default_config(app)
#
#     DepotManager.configure(depot_name, depot_config)
#
#
# def default_config(app):
#     """Return a default config that is used by all depots"""
#
#     if app.testing:
#         return test_config()
#     else:
#         return production_config(app)
#
#
# def test_config():
#     """Return the default test config that is used by all depots"""
#
#     return {'depot.backend': 'depot.io.memory.MemoryFileStorage'}
#
#
# def production_config(app):
#     """Return the default production config that is used by all depots"""
#
#     return {
#         'depot.backend': 'depot.io.boto3.S3Storage',
#         'depot.endpoint_url': 'https://storage.googleapis.com',
#         'depot.access_key_id': app.config.get('GOOGLE_CLOUD_STORAGE_ACCESS_KEY'),
#         'depot.secret_access_key': app.config.get('GOOGLE_CLOUD_STORAGE_SECRET_KEY'),
#         'depot.bucket': app.config.get('GOOGLE_CLOUD_STORAGE_BUCKET')
#     }