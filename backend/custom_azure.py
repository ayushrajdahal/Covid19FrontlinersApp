from storages.backends.azure_storage import AzureStorage
import os




class AzureMediaStorage(AzureStorage):
    account_name = os.environ.get('ACC_NAME') # Must be replaced by your <storage_account_name>
    account_key = os.environ.get('ACC_KEY') # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None