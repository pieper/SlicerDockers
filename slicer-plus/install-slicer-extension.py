
import os
extensionName = os.environ['EXTENSION_TO_INSTALL']
print(f"installing {extensionName}")
emm = slicer.app.extensionsManagerModel()
extensionMetaData = emm.retrieveExtensionMetadataByName(extensionName)
url = emm.serverUrl().toString()+'/download/item/'+extensionMetaData['item_id']
extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['md5']
slicer.util.downloadFile(url, extensionPackageFilename)
emm.installExtension(extensionPackageFilename)
exit()
