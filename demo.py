from HateSpeech.logger import logging
from HateSpeech.exception import CustomeException
import sys
from HateSpeech.configuration.gcloud_syncer import GCloudSync

obj=GCloudSync()
obj.sync_folder_from_gcloud("hate-speech2024","dataset.zip","download/dataset.zip")