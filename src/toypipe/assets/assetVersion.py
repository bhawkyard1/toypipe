from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from toypipe.assets.serializable import Serializable

class AssetVersion(Serializable):
    __tablename__ = "AssetVersion"
    id = Column(None, ForeignKey("Serializable.id"), primary_key=True)


    # Whether this asset version is approved.
    approved = Column(Boolean)

    # The files that are associated with this asset.

    def __init__(self):
        super(AssetVersion, self).__init__()

    @property
    def assetStack(self) -> "AssetStack":
        """ Returns the asset stack this sits on. """
        pass

    @property
    def approved(self) -> bool:
        pass

    @approved.setter
    def approved(self, value: bool):
        pass
