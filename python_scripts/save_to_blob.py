from azure.storage.blob import BlobServiceClient

def upload_to_blob(connection_string, container_name, file_path, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    with open(file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)
    print(f"Uploaded {file_path} to {container_name}/{blob_name}")
