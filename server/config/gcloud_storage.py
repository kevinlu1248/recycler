from google.cloud import storage
import os

storage_client = storage.Client()
bucket_name = os.environ.get("MAIN_BUCKET")
bucket = storage_client.bucket(bucket_name)
ext_to_mime = {
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "gif": "image/gif",
    "bmp": "image/bmp",
    "raw": "raw",
    "ico": "image/ico",
    "pdf": "application/pdf",
    "tiff": "image/tiff",
}


def list_blobs_with_prefix(prefix, delimiter=None):
    """Lists all the blobs in the bucket that begin with the prefix.

    This can be used to list all blobs in a "folder", e.g. "public/".

    The delimiter argument can be used to restrict the results to only the
    "files" in the given "folder". Without the delimiter, the entire tree under
    the prefix is returned. For example, given these blobs:

        a/1.txt
        a/b/2.txt

    If you just specify prefix = 'a', you'll get back:

        a/1.txt
        a/b/2.txt

    However, if you specify prefix='a' and delimiter='/', you'll get back:

        a/1.txt

    Additionally, the same request will return blobs.prefixes populated with:

        a/b/
    """

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(
        bucket_name, prefix=prefix, delimiter=delimiter
    )

    # print("Blobs:")
    # for blob in blobs:
    #     print(blob.name)
    #
    # if delimiter:
    #     print("Prefixes:")
    #     for prefix in blobs.prefixes:
    #         print(prefix)

    return blobs


def upload_blob_from_directory(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    blob = bucket.blob(destination_blob_name)
    print(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    file_name = os.path.basename(destination_blob_name)

    print(
        "File {} uploaded to {} and can be founded at {}/{}".format(
            source_file_name, destination_blob_name, os.environ.get("GOOGLE_CLOUD_STORAGE_BUCKET"),
            file_name
        )
    )


def upload_blob_from_string(input_blob, destination_blob_name, mime="text/plain"):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    blob = bucket.blob(destination_blob_name)
    print(destination_blob_name)
    blob.upload_from_string(input_blob)
    file_name = os.path.basename(destination_blob_name)

    print(
        "Blob string uploaded to {} and can be founded at {}/{}".format(
            destination_blob_name, os.environ.get("GOOGLE_CLOUD_STORAGE_BUCKET"),
            file_name
        )
    )


def test_image_id():
    """Getting number of items in Cloud Storage + 1."""
    return sum(1 for s in list_blobs_with_prefix("test_images/"))


def push_image_from_directory(source_file_name):
    """Pushes an image to the Cloud with extension x.ext, where x is the file id and ext is the extension."""
    # file_name = os.path.basename(source_file_name)
    _, file_extension = os.path.splitext(source_file_name)
    upload_blob_from_directory(source_file_name, "test_images/{}{}".format(test_image_id(), file_extension))


def push_blob_from_string(input_blob, ext):
    """Pushes an image to the Cloud with extension x.ext, where x is the file id and ext is the extension."""
    mime = ext_to_mime[ext.strip(".")]
    upload_blob_from_string(input_blob, "test_images/{}{}".format(test_image_id(), ext), mime)


if __name__ == '__main__':
    push_image_from_directory("../../resources/recyclables_thumb[2].jpg")
