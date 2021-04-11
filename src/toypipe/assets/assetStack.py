from typing import Iterator
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from toypipe.assets.serializable import Serializable

class AssetStack(Serializable):
    __tablename__ = "AssetStack"
    id = Column(None, ForeignKey("Serializable.id"), primary_key=True)

    # The name asset represented by the stack.
    name = Column(String)

    def __init__(self):
        super(AssetStack, self).__init__()

    @property
    def assets(self) -> Iterator["AssetVersion"]:
        """ Gets the assets in this stack. 
            Sorted by version number.

            Returns:
                list: list of the assets in this stack.
        """
        pass

    @property
    def approvedAssets(self) -> Iterator["AssetVersion"]:
        """ Gets the approved assets in this stack. 
            Sorted by version number.

            Returns:
                list: list of the assets in this stack.
        """
        pass
    
    @property
    def latestAsset(self) -> "AssetVersion":
        """ Gets the latest asset in the stack.

            Returns:
                AssetVersion: The latest asset in the stack.
        """
        pass

    @property
    def latestApprovedAsset(self) -> "AssetVersion":
        """ Gets the latest asset in the stack, which is also approved.

            If no asset is approved, it will return latestAsset.

            Returns:
                Asset: The latest approved asset in the stack.
        """
        pass
