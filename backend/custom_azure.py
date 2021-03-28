from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'dhedu' # Must be replaced by your <storage_account_name>
    account_key = 'R6GdcFQi4qV8VKZXs5PQnhmDZdiH24J3/CyMVGHWKg8oTSYRWcrIJCsar4O2HJxqdu+k84RRkrVQB441DItrpQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None