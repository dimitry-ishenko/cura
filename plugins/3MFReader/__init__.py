# Copyright (c) 2015 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.
from typing import Dict
import sys

from UM.Logger import Logger
try:
    from . import ThreeMFReader
except ImportError:
    Logger.log("w", "Could not import ThreeMFReader; libSavitar may be missing")

from . import ThreeMFWorkspaceReader

from UM.i18n import i18nCatalog
from UM.Platform import Platform
catalog = i18nCatalog("cura")

def getMetaData() -> Dict:
    # Workarround for osx not supporting double file extensions correctly.
    if Platform.isOSX():
        workspace_extension = "3mf"
    else:
        workspace_extension = "curaproject.3mf"

    metaData = {}
    if "3MFReader.ThreeMFReader" in sys.modules:
        metaData["mesh_reader"] = [
            {
                "extension": "3mf",
                "description": catalog.i18nc("@item:inlistbox", "3MF File")
            }
        ]
        metaData["workspace_reader"] = [
            {
                "extension": workspace_extension,
                "description": catalog.i18nc("@item:inlistbox", "3MF File")
            }
        ]
    
    return metaData


def register(app):
    if "3MFReader.ThreeMFReader" in sys.modules:
        return {"mesh_reader": ThreeMFReader.ThreeMFReader(),
                "workspace_reader": ThreeMFWorkspaceReader.ThreeMFWorkspaceReader()}
    else:
        return {}
